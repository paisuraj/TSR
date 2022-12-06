#this file is meant to create the virtual environment
import os



os.system('py -m venv env')
os.system('.\env\Scripts\activate')


os.system('pip install coverage')
os.system('pip install mutmut')
os.system('pip install pytest')
os.system('pip install -r requirements.txt')
