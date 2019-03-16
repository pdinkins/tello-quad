__package__ = "tello-quad"
__version__ = "0.1.20"

import os
import threading 
import socket
import sys
import time
import platform  




def download_repos():
    os.chdir("/downloads/")
    # dji sdk tello python 
    gitclone("https://github.com/dji-sdk/Tello-Python.git")
    # micro linux 
    gitclone("https://github.com/microlinux/tello.git")
    # jabrils tellotv 
    gitclone("https://github.com/Jabrils/TelloTV.git")
    # hanyazou tellopy 
    gitclone("https://github.com/hanyazou/TelloPy.git")
    # parakhm95 tello position controller 
    gitclone("https://github.com/parakhm95/Ryze-Tello-Position-Controller.git")
    # damia fuentes dji tello py
    gitclone("https://github.com/damiafuentes/DJITelloPy.git")


def gitclone(repo):
    # download the git repo into the downloads folder
    cmd = "git clone " + str(repo)
    os.system(cmd) 

def dr():
    download_repos()

if __name__ == "__main__":
    host = ''
    port = 9000
    locaddr = (host,port) 

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = ('192.168.10.1', 8889)
    sock.bind(locaddr)
    print ('\r\n\r\nTello Python3 Demo.\r\n')
    print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')
    print ('end -- quit demo.\r\n')

    def recv():
        count = 0
        while True: 
            try:
                data, server = sock.recvfrom(1518)
                print(data.decode(encoding="utf-8"))
            except Exception:
                print ('\nExit . . .\n')
                break
    #recvThread create
    recvThread = threading.Thread(target=recv)
    recvThread.start()


    while True: 
        try:
            python_version = str(platform.python_version())
            version_init_num = int(python_version.partition('.')[0]) 
        # print (version_init_num)
            if version_init_num == 3:
                msg = input("")
            elif version_init_num == 2:
                msg = raw_input("")
            
            if not msg:
                break  

            if 'end' in msg:
                print ('...')
                sock.close()  
                break

            # Send data
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            sock.close()  
            break