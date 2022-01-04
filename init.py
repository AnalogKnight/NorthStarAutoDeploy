import os
import sys
import yaml
import time

def InitServer(gamePath,count):
    path=sys.argv[0][:-7]
    os.system('mkdir '+path+'servers')
    configFile=yaml.safe_load(open('./config.yaml','r',encoding='utf-8').read())
    serverName=configFile['serverName']
    serverDescribe=configFile['describe']
    hostName=configFile['hostName']
    gameFiles=os.listdir(gamePath)
    for i in range(count):
        nodePath=path+'servers\\'+'node'+str(i)+'\\'
        os.system('mkdir '+nodePath)
        for file in gameFiles:
            if file != 'r2' and file!='vpk':
                if os.path.isdir(gamePath+'\\'+file):
                    os.system('echo d | xcopy '+'\"'+gamePath+'\\'+str(file)+'\"'+' '+'\"'+nodePath+file +'\"'+' /e /y /q')
                else:
                    os.system('echo f | xcopy '+'\"'+gamePath+'\\'+str(file)+'\"'+' '+'\"'+nodePath+file +'\"'+' /e /y /q')
        os.system('mklink /j '+'\"'+nodePath+'\\r2'+'\"'+' '+'\"'+gamePath+'\\r2'+'\"')
        os.system('mklink /j '+'\"'+nodePath+'\\vpk'+'\"'+' '+'\"'+gamePath+'\\vpk'+'\"')
        time.sleep(1)
        serverConfig=open(nodePath+'\\R2Northstar\\mods\\Northstar.CustomServers\\mod\\cfg\\autoexec_ns_server.cfg','w')
        serverConfig.write(
            "ns_server_name "+'\"'+serverName+' - node'+str(i)+'\"'+'\n' +
            "ns_server_desc "+'\"'+serverDescribe+'\"'+'\n' +
            "ns_masterserver_hostname "+'\"'+hostName+'\"'+'\n'+
            "ns_player_auth_port "+str(8000+i)+'\n'+
            '''
ns_server_password ""
ns_report_server_to_masterserver 1
ns_report_sp_server_to_masterserver 0

ns_auth_allow_insecure 0
ns_erase_auth_info 1
everything_unlocked 1

ns_should_return_to_lobby 1

net_chan_limit_msec_per_sec 100
sv_querylimit_per_sec 15
base_tickinterval_mp 0.016666667
sv_updaterate_mp 20
sv_minupdaterate 20
sv_max_snapshots_multiplayer 300
net_data_block_enabled 0
host_skip_client_dll_crc  1
'''
        )