from os import listdir
from sys import path
import yaml
from init import *
from start import *

configFile=yaml.safe_load(open('./config.yaml','r',encoding='utf-8').read())
gamePath=configFile['gamePath']
count=configFile['count']

operation=int(input('''
[0]Start server
[1]Initialize server
Please choose the operation:
'''))
if operation==0:
    StartServer(count)
elif operation==1:
    InitServer(gamePath,count)
