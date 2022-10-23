# file = open('ProjectsList.sv', 'r')
# project = file.readline()
# print(project)
# # while file != '':
# #     print(project)
# #     project = file.readline()


import csv
#from git.repo.base import Repo
import os
from src import test


with open('test.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    fileCount = 0
    for row in reader_obj:
        cmd = "git clone {}".format(row[0])
        print("Starting to clone {}".format(row[0]))
        os.system(cmd)
        print("Finished cloning {}".format(row[0]))
        print("#############################")
        print("")
    
