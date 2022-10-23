
import csv
import os


with open('CSV/Projects.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        cmd = "git clone {}".format(row[0])
        print("Starting to clone {}".format(row[0]))
        proj = row[0].split('/')[-1]
        copyOver = "cp -R " + "./" + proj + " ./Projects/"
        os.system(cmd)
        os.system(copyOver)
        os.system("rm -rf " + proj)
        #os.system('mv' + cmd + 'Projects')
        print("Finished cloning {}".format(row[0]))
        print("#############################")
        print("")
    
