import os
import sys
import time

path=sys.argv[0][:-7]+'\\servers\\'

def StartServer(count):
    for nodePath in os.listdir(path):
        os.system('cd '+'\"'+path+nodePath+'\\'+'\"'+' && '+'NorthstarLauncher.exe -dedicated -multiple -softwared3d11')
    WatchDog(count)

def WatchDog(count):
    while True:
        time.sleep(60)
        for i in range(count):
            if(os.popen("netstat -a -n | find "+'\"'+str(8000+i)+'\"').read()==''):
                print('Node'+str(i)+" offline, restart.")
                os.system('cd '+'\"'+path+'\\node'+str(i)+'\"'+' && '+'NorthstarLauncher.exe -dedicated -multiple -softwared3d11')
            else:
                print('Node'+str(i)+" online.")