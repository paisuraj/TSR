
import os
dir = os.path.dirname(os.path.abspath(__file__))

test_file_arr = []
#create ORIG-file
with open('ORIG-FILE.txt', 'w') as orig_file:
    for path, currentDirectory, files in os.walk(dir + "/tests"):
        #print('1')
        for file in files:
            #print('YES')
            if file.startswith("test_") and file.endswith(".py"):
                #os.system('coverage run -m pytest' + str(file))
                orig_file.write(file + '\n')
                test_file_arr.append(file)

#create data-file
import json
with open('DATA-FILE.txt', 'w') as data_file:
    for test in test_file_arr:
        #run coverage on each py test file then run coverage json
        os.system(f'coverage run -m pytest tests/{test}')
        os.system('coverage json')
        cov = open('coverage.json')
        data = json.load(cov)
        data_file_txt = str(test)

        for file_name in data['files']:
            data_file_txt = f'{data_file_txt}, {file_name}'
        data_file.write(data_file_txt)

#run reduce.py
newpath = f'{dir}/RESULTS'
if not os.path.exists(newpath):
    os.mkdir(newpath)

print(newpath)
algo = ['greedy', 'ge', 'gre', 'hgs', 'random']

for i in algo:
    command = f'py reduce.py DATA-FILE.txt ORIG-FILE.txt {i} > RESULTS/results_{i}.txt'
    print(command)
    os.system(command)