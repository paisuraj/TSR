# this file is meant to create the virtual environment
import os

os.system('py -m venv env')
os.system('.\env\Scripts\activate')

os.system('pip install coverage pytest mutmut')
os.system('pip install -r requirements.txt')
