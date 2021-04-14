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


def connect(LHOST,LPORT):
    print('\033[1;91m[\033[00m+\033[1;91m] \033[00mListening On %s:%s' % (LHOST,LPORT))
    nc = nclib.Netcat(listen=(LHOST,LPORT))
    data = nc.recv(4096)
    nc.interact()

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
        args = parser.parse_args()
        print('\033[00m')
        connect(args.lhost,args.lport)

if __name__ == '__main__':
    main()
