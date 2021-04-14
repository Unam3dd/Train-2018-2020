#!/usr/bin/python2
#-*- coding:utf-8 -*-

import socket
import subprocess
import os
import netifaces
import threading
import thread
from datetime import datetime
import time
import shlex
import platform
import sys
import argparse


banner = '''
 ███▄    █   ██████  ▄████▄   ▄▄▄       ███▄    █
 ██ ▀█   █ ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
▓██  ▀█ ██▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
▓██▒  ▐▌██▒  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒██░   ▓██░▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
░ ░░   ░ ▒░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
   ░   ░ ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░
         ░       ░  ░ ░            ░  ░         ░
                    ░

            \033[1;92mBy Dxvistxr
            \033[1;96mCreated For Scan Network
            \033[1;92m[\033[1:94m*\033[1;92m] Github : \033[1;96mDxvistxr\033[00m

'''

def clear_func():
    if 'Linux' not in platform.platform():
        os.system('cls')
        os.system('cls')

    elif 'Windows' not in platform.platform():
        os.system('clear')
        os.system('clear')

def try_ping(host):
    try:
        if 'Linux' not in platform.platform():
            req_ping = os.system('ping -n 1 %s > /dev/null' % (host))

            if req_ping ==0:
                get_hostname = socket.gethostbyaddr(host)
                t = datetime.now().strftime('%H:%M:%S')
                print('\033[1;92m(\033[1;96m%s\033[1;92m) \033[1;96m[\033[1;92mIP\033[1;96m] : \033[00m%s \t \033[1;92m[\033[1;96mHostname\033[1;92m] : \033[00m%s' % (t,host,get_hostname[0]))

            else:
                pass

        elif 'Windows' not in platform.platform():
            req_ping = os.system('ping -c 1 -b %s > /dev/null' % (host))

            if req_ping ==0:
                get_hostname = socket.gethostbyaddr(host)
                t = datetime.now().strftime('%H:%M:%S')
                print('\033[1;92m(\033[1;96m%s\033[1;92m) \033[1;96m[\033[1;92mIP\033[1;96m] : \033[00m%s \t \033[1;92m[\033[1;96mHostname\033[1;92m] : \033[00m%s' % (t,host,get_hostname[0]))

            else:
                pass

    except Exception as error_req_host:
        print('\033[1;91m[\033[1;94m*\033[1;91m] %s' % (error_req_host))

def start_scanner():
    gtw = netifaces.gateways()
    interface = gtw['default'][2][1]
    gtw_ip = gtw['default'][2][0]
    scanner_gtw_ip = gtw_ip[:10]
    try:
        clear_func()
        print('\033[1;92m'+banner)
        print('\t\033[1;92m[\033[1;94m*\033[1;92m] Gateway : %s' % (gtw_ip))
        print('\t\033[1;92m[\033[1;94m*\033[1;92m] Interface : %s' % (interface))
        i = 0
        while i<256:
            thread.start_new_thread(try_ping,(scanner_gtw_ip+str(i),))
            time.sleep(0.1)
            i = i+1

    except Exception as error_start_scanner:
        print(error_start_scanner)


if __name__ == '__main__':
    clear_func()
    clear_func()
    print('\033[1;92m'+banner)
    start_scanner()
