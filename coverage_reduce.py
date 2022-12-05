import json
import os

dir = os.path.dirname(os.path.abspath(__file__))
print(f'dir is {dir}')

if not os.path.exists(f'{dir}/workspace'):
    os.mkdir(f'{dir}/workspace')
if not os.path.exists(f'{dir}/workspace/COVERAGE'):
    os.mkdir(f'{dir}/workspace/COVERAGE')

data_file_path = f'{dir}/workspace/DATA-FILE.txt'
orig_file_path = f'{dir}/workspace/ORIG-FILE.txt'
stats_file_path = f'{dir}/workspace/STATS.txt'

num_tests_coverage_worked = 0
num_tests_skipped = 0
tests_coverage_worked = []
tests_skipped = []
data_file_dict = {}

if os.path.exists(data_file_path):
    os.remove(data_file_path)
data_file = open(data_file_path, 'a')

if os.path.exists(orig_file_path):
    os.remove(orig_file_path)
orig_file = open(orig_file_path, 'a')

if os.path.exists(stats_file_path):
    os.remove(stats_file_path)
stats_file = open(stats_file_path, 'a')

for path, currentDirectory, files in os.walk(dir + "/tests"):
    for file in files:
        if file.startswith("test_") and file.endswith(".py"):
            print(f'Running coverage on {path}/{file}')
            test_file_name = file.split('.')[0]
            print(f'Test file name is {test_file_name}')
            os.system(f"coverage run --omit 'env/*' -m pytest {path}/{file}")
            os.system(
                f"coverage json -i -o workspace/COVERAGE/coverage-{test_file_name}.json --show-contexts")

            # if coverage run is successful
            if os.stat(f'workspace/COVERAGE/coverage-{test_file_name}.json').st_size != 0:
                num_tests_coverage_worked += 1
                tests_coverage_worked.append(
                    [file, os.stat(f'workspace/COVERAGE/coverage-{test_file_name}.json').st_size])

                # open coverage file to create DATA-FILE
                cov = open(
                    f'workspace/COVERAGE/coverage-{test_file_name}.json')
                data = json.load(cov)

                # create dictionary of tests to entities by looking at the contexts of each file in coverage
                for file_name in data['files']:
                    #print(f"{data['files'][file_name]['contexts']} is type: {type(data['files'][file_name]['contexts'])}")
                    for line_num, tests in data['files'][file_name]['contexts'].items():
                        for test in tests:
                            if test != '':
                                if test not in data_file_dict.keys():
                                    data_file_dict[test] = [file_name]
                                if file_name not in data_file_dict[test]:
                                    data_file_dict[test].append(file_name)
                cov.close()
            # coverage run unsuccessful
            else:
                num_tests_skipped += 1
                tests_skipped.append(file)
# add to ORIG file
for test in data_file_dict.keys():
    orig_file.write(f'{test}\n')
# write data_file_dict to DATA-FILE
for test, entities_list in data_file_dict.items():
    data_file.write(f'{test}')
    for entity in entities_list:
        data_file.write(f', {entity}')
    data_file.write('\n')

# write stats_file
stats_file.write(
    f"Tests coverage was successful: ({num_tests_coverage_worked})\n")
for file_size in tests_coverage_worked:
    stats_file.write(f'{file_size[0]}\t{file_size[1]}\n')
stats_file.write(f'Tests coverage was unsuccessful: ({num_tests_skipped})\n')
for file in tests_skipped:
    stats_file.write(f'{file}\n')

stats_file.close()
orig_file.close()
data_file.close()

# run reduce.py
if not os.path.exists(f'{dir}/workspace/RESULTS'):
    os.mkdir(f'{dir}/workspace/RESULTS')

algo = ['greedy', 'ge', 'gre', 'hgs', 'random']

for i in algo:
    command = f'py reduce.py {dir}/workspace/DATA-FILE.txt {dir}/workspace/ORIG-FILE.txt {i} > {dir}/workspace/RESULTS/results_{i}.txt'
    print(f'Running reduction with {i} algorithm')
    os.system(command)
