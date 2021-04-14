#!/usr/bin/python2
#coding:utf-8

import socket
import subprocess
import os
import sys
import requests
import json
import thread
import platform
import time
from datetime import datetime

banner = '''
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux World  |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb  [Internet : \033[1;92mFound !]
   HZM            MMMM  [Author : \033[1;92mDxvistxr]
   FqM            MMMM  [Youtube : \033[1;92mhttps://www.youtube.com/channel/UCmRpdW8WVVA4o3nhPjMG3Bg]
 __| ".        |\dS"qML [Github : https://github.com/VnomDavistar/PortScanner\033[1;92m]
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'
     Version 1.0 - 2019
'''


def check_internet():
    try:
        r=requests.get('https://www.google.com')
    except:
        sys.exit('[*] Internet Not Found !')


def portscan(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print('\033[1;92m[\033[1;94m+\033[1;92m] \033[1;92m'+str(port)+' ~> open !\n')
    except:
        pass

def portscanwindows(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print('[+] '+str(port)+' ~> open !\n')
    except:
        pass

def mainwindows():
    target = raw_input('[+] Enter Target IP :> ')
    i = 1
    x = input('[+] Enter Max Port :> ')
    y = 1
    print('[+] Scanning : '+str(target)+' max port : '+str(x))
    while i<x:
        thread.start_new_thread(portscan,(target,y))
        time.sleep(0.1)
        i = i+1
        y = y+1
    
    print('[+] Scanner Finish !')

def main():
    target = raw_input('\033[1;92m[\033[1;94m+\033[1;92m] Enter Target IP :> ')
    i = 1
    x = input('\033[1;92m[\033[1;94m+\033[1;92m] Enter Max Port :> ')
    y = 1
    print('\033[1;92m[\033[1;94m+\033[1;92m] Scanning : '+str(target)+' max port : '+str(x))
    while i<x:
        thread.start_new_thread(portscan,(target,y))
        time.sleep(0.1)
        i = i+1
        y = y+1
    
    print('\033[1;92m[\033[1;94m+\033[1;92m] Scanner Finish !')


def runmain():
    if 'Linux' not in platform.platform():
        os.system('cls')
        os.system('cls')
        os.system('color a')
        print(banner)
        mainwindows()
    
    elif 'Windows' not in platform.platform():
        os.system('clear')
        os.system('clear')
        print('\033[1;92m'+banner)
        main()

runmain()
