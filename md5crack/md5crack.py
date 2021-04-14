#!/usr/bin/python3
#author : Dxvistxr - LSD
#coding:utf-8

import requests
import json
import time
from datetime import datetime
import platform
import subprocess
import os
import sys
import argparse
import hashlib



class config():
        #API_LINK = https://md5decrypt.net/en/Api/
        email = 'youremail@gmail.com' #YOUR_EMAIL FROM API
        code = 'yoursecretcode' #YOUR SECRET CODE (GET BY EMAIL SEND BY API)

banner = '''
\033[1;91m███╗   ███╗██████╗ ███████╗     \033[1;97m██████╗██████╗  █████╗  ██████╗██╗  ██╗
\033[1;91m████╗ ████║██╔══██╗██╔════╝    \033[1;97m██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
\033[1;91m██╔████╔██║██║  ██║███████╗    \033[1;97m██║     ██████╔╝███████║██║     █████╔╝ 
\033[1;91m██║╚██╔╝██║██║  ██║╚════██║    \033[1;97m██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
\033[1;91m██║ ╚═╝ ██║██████╔╝███████║    \033[1;97m╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
\033[1;91m╚═╝     ╚═╝╚═════╝ ╚══════╝     \033[1;97m╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                \033[1;97mBy Dxvistxr - \033[1;91m2\033[1;97m0\033[1;91m1\033[1;97m9
                                \033[1;97mYoutube : \033[1;91mhttps://www.youtube.com/channel/UCmRpdW8WVVA4o3nhPjMG3Bg\033[1;97m
                                for show help type : python3 md5crack.py -h
'''


def sys_required():
    if 'Linux' not in platform.platform():
        sys.exit('[*] System GNU/Linux Is Required !')

def main():
        sys_required()
        os.system('clear')
        os.system('clear')
        print(banner)
        parser = argparse.ArgumentParser()
        parser.add_argument('-a','--hash',help='Decrypt md5')
        parser.add_argument('-l','--filehash',help='Decrypt MD5LIST')
        parser.add_argument('-j','--johncrack',help='Select Wordlist and Crack With John')
        parser.add_argument('-c','--crack',help='Crack With Wordlist, enter hash')
        parser.add_argument('-w','--wordlist',help='Select Wordlist For Cracking')
        parser.add_argument('-e','--encrypt',help='Encrypt String to md5')
        parser.add_argument('-f','--encryptfile',help='Encrypt wordlist to md5')
        parser.add_argument('-d','--download',help='Select Path For Download Wordlist')
        parser.add_argument('-s','--showinfo',help='Show Informations Of MD5 Crack, email, code, all')
        parser.add_argument('-v','--version',help='Version Command, show, update')
        args = parser.parse_args()
        
        if args.johncrack:
                check_john = os.path.exists('/etc/john')
                if check_john ==True:
                        print('\033[1;92m[*] John Found !')
                        os.system('john --wordlist='+str(args.wordlist)+' --format=raw-md5 '+str(args.john))
                else:
                        install_john = str(input('\033[1;92m[*] Do You Want Install John (yes/no) > '))
                        if install_john =='yes':
                                print('\033[1;92m[1] Install John With APT')
                                print('\033[1;92m[2] Install John With Wget')
                                choice_install_john = int(input('\033[1;92m[*] Select Choice > '))
                                
                                if choice_install_john ==1:
                                        os.system('apt update && apt upgrade -y && apt install john')
                                
                                elif choice_install_john ==2:
                                        check_wget = os.path.exists('/usr/bin/wget')
                                        if check_wget ==True:
                                                print('\033[1;92m[*] Wget Found !')
                                                print('\033[1;92m[*] Downloading John')
                                                os.system('wget https://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz')
                                                check_tar = os.path.exists('/bin/tar')
                                                if check_tar ==True:
                                                        print('\033[1;92m[*] Tar Found !')
                                                        os.system('mv john-1.8.0-jumbo-1.tar.gz john-1.8.0-jumbo.tar.gz')
                                                        os.system('tar zxvf john-1.8.0-jumbo.tar.gz')
                                                        os.system('cd john-1.8.0-jumbo-1/src && pwd && make && make clean generic')
                                                        os.system('cd john-1.8.0-jumbo-1/run/ && ./john --test')
                                                        os.system('cp -r john-1.8.0-jumbo-1 /usr/share/')
                                                        os.system('echo "./usr/share/john/run/john" > john && cp john /usr/bin')
                                                
                                                else:
                                                        print('\033[1;91m[*] Tar Not Installed !')
                                                        os.system('apt update && apt upgrade -y && apt install tar -y')

                                        
                                        else:
                                                print('\033[1;91m[*] Wget Not Installed !')
                                                os.system('apt update && apt upgrade -y && apt install wget -y')


        if args.encrypt:
                time_str = datetime.now().strftime('%H:%M:%S')
                output = hashlib.md5(args.encrypt.encode('utf-8')).hexdigest()
                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => '+str(output)+' = '+str(args.encrypt))
                print('\033[1;92m[*] String Encrypted ! At '+str(time_str))
        
        

        if args.download:
                check_wget = os.path.exists('/usr/bin/wget')
                if check_wget ==True:
                        print('\033[1;92m[*] Wget Found !')
                        print('\033[1;93m[$] Downloading Wordlist MD5...Wait')
                        os.system('wget http://md5decrypt.net/Telecharger-wordlist/Md5decrypt-awesome-wordlist.7z && mv Md5decrypt-awesome-wordlist.7z '+str(args.download))
                        print('\033[1;92m[*] Wordlist Downloaded !!!!')
                else:
                        print('\033[1;91m[*] Wget Not Found !')
                        print('\033[1;92m[*] Wait Moment Please Installing Wget...')
                        os.system('sudo apt update && apt upgrade -y && apt install wget -y')
                        print('\033[1;93m[$] Downloading Wordlist MD5...Wait')
                        os.system('wget http://md5decrypt.net/Telecharger-wordlist/Md5decrypt-awesome-wordlist.7z && mv Md5decrypt-awesome-wordlist.7z '+str(args.download))
                        print('\033[1;92m[$] Wordlist Downloaded !!!!')

        if args.hash:
                print('\033[1;92m[\033[1;93m*\033[1;92m] Wait Moment Please Cracking MD5....')
                payload = 'https://md5decrypt.net/en/Api/api.php?hash='+str(args.hash)+'&hash_type=md5&email='+str(config.email)+'&code='+str(config.code)
                try:
                        r = requests.get(payload)
                        pw = r.text

                        if pw == '':
                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+'\033[1;92m:\033[1;91mUnknow')
                        
                        elif pw =='ERROR CODE : 005':
                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+':\033[1;91mThe hash you provide doesn t seem to match with the type of hash you set.')
                        
                        elif pw =='ERROR CODE : 001':
                                print('\033[1;91m[!] You exceeded the 400 allowed request per day')
                        
                        elif pw =='ERROR CODE : 006':
                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+':\033[1;91mYou didn t provide all the arguments, or you mispell one of them.')
                        
                        else:
                                t = datetime.now().strftime('%H:%M:%S')
                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+'\033[1;92m:\033[1;93m'+str(pw))
                                print('\033[1;93m[*] Found AT => \033[1;93m'+str(t))
                except:
                        print('\033[1;91m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+':\033[1;91mException Error')
        
        if args.filehash:
                print('\033[1;92m[\033[1;93m*\033[1;92m] Wait Moment Please Cracking MD5....')
                print('\n')
                with open(args.filehash,'r') as f:
                        content = f.readlines()
                        for md5hash in content:
                                md5hash = md5hash.rstrip()
                                payload = 'https://md5decrypt.net/en/Api/api.php?hash='+str(md5hash)+'&hash_type=md5&email='+str(config.email)+'&code='+str(config.code)
                                try:
                                        r = requests.get(payload)
                                        pw = r.text
                                        t = datetime.now().strftime('%H:%M:%S')
                                        if pw =='':
                                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+'\033[1;92m:\033[1;91mUnknow')
                                        
                                        elif pw =='ERROR CODE : 005':
                                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+':\033[1;91mThe hash you provide doesn t seem to match with the type of hash you set.')
                                        
                                        elif pw =='ERROR CODE : 001':
                                                print('\033[1;91m[!] You exceeded the 400 allowed request per day')
                                        
                                        elif pw =='ERROR CODE : 006':
                                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(args.hash)+':\033[1;91mYou didn t provide all the arguments, or you mispell one of them.')

                                        else:
                                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(md5hash)+'\033[1;92m:\033[1;93m'+str(pw))
                                                print('\033[1;92m[*] Found At => \033[1;93m'+str(t))
                                except:
                                        t = datetime.now().strftime('%H:%M:%S')
                                        print('\033[1;91m[\033[1;93m*\033[1;92m] HASH (MD5) => \033[1;93m'+str(md5hash)+':\033[1;91mException')
        
        if args.encryptfile:
                with open(args.encryptfile,'r') as f:
                        content = f.readlines()
                        f.close()
                        for word in content:
                                word = word.rstrip()
                                time_str = datetime.now().strftime('%H:%M:%S')
                                output = hashlib.md5(word.encode('utf-8')).hexdigest()
                                print('\033[1;92m[\033[1;93m*\033[1;92m] HASH (MD5) => '+str(output)+' = '+str(word)+' save as '+str(args.encryptfile+'_encrypted.txt'))
                                f = open(str(args.encryptfile+'_encrypted.txt','w'))
                                f.write(output+'\n')
                                f.close()
                        
                        print('\033[1;92m[*] Wordlist MD5 generated At '+str(time_str)+' save as '+str(args.encryptfile))
        
        if args.showinfo =='email':
                print('\033[1;92m[*] Your Email => \033[1;93m'+str(config.email))
        
        if args.showinfo =='code' or args.showinfo =='secretcode':
                print('\033[1;92m[*] Your Secret Code => \033[1;93m'+str(config.code))
        
        if args.showinfo =='all':
                print('\033[1;92m[*] Your Email => \033[1;93m'+str(config.email)+'\n\033[1;92m[*] Your Secret Code => \033[1;93m'+str(config.code))
        
        if args.version =='show':
                print('\033[1;92m[*] MD5CRACK By Dxvistxr Version : 1.0 - 1/02/2019 BY LSD')
        
        if args.version =='update':
                check_git = os.path.exists('/usr/bin/git')

                if check_git ==True:
                        print('\033[1;92m[*] Git Found !')
                        print('\033[1;92m[*] Send Request On Github => https://github.com/VnomDavistar/md5crack')
                        os.system('cd ../ && rm -r md5crack && git clone https://github.com/VnomDavistar/md5crack')
                        print('\033[1;92m[*] MD5CRACK UPDATED ! '+os.system('date'))
                else:
                        choice_install_git = str(input('\033[1;92m[*] Do You Want Install GIT (yes/no) > '))
                        if choice_install_git =='yes':
                                os.system('apt update && apt upgrade -y && apt install git -y')
                                print('\033[1;92m[*] Git Found !')
                                install_update = str(input('\033[1;92m[*] Do You Want Install Update (yes/no) > '))
                                if install_update =='yes':
                                        print('\033[1;92m[*] Send Request On Github => https://github.com/VnomDavistar/md5crack')
                                        os.system('cd ../ && rm -r md5crack && git clone https://github.com/VnomDavistar/md5crack')
                                        print('\033[1;92m[*] MD5CRACK UPDATED ! '+os.system('date'))
                                
                                elif install_update =='no':
                                        sys.exit()
                        
                        elif choice_install_git =='no':
                                sys.exit('\033[1;91m[*] Git Not Installed !')
        
        if args.crack:
                hashs = args.crack
                wordlist = str(input('\033[1;92m[*] Select Wordlist => '))
                print('\033[1;92m[*] Hash => '+str(hashs))
                print('\033[1;92m[*] Wordlist => '+str(wordlist))
                choice_crack = str(input('\033[1;92m[\033[1;93m*\033[1;92m] Do You Want Crack '+str(hashs)+' with '+str(wordlist)+' (yes/no) => '))

                if choice_crack =='yes':
                        with open(wordlist,'r') as f:
                                content = f.readlines()
                                f.close()
                                for passwd in content:
                                        passwd = passwd.rstrip()
                                        hashing = hashlib.md5(passwd.encode('utf-8')).hexdigest()
                                        print('\033[1;92m[\033[1;93m*\033[1;92m] Trying => '+str(hashs+':'+passwd))
                                                
                                        if hashs == hashing:
                                                os.system('clear')
                                                os.system('clear')
                                                print(banner)
                                                print('\n')
                                                print('\033[1;92m[\033[1;94m*\033[1;92m] Hash Cracked !')
                                                time_str = datetime.now().strftime('%H:%M:%S')
                                                print('\033[1;92m[\033[1;94m*\033[1;92m] Hash : '+str(hashs+':\033[1;93m'+passwd+'\n[*] Hash Cracked At '+time_str))
                                                break
                                        
                
                elif choice_crack =='no':
                        sys.exit('\033[1;91m[*] Exiting By Dxvistxr')
                
                
                else:
                        print('\033[1;91m[*] Invalid Options')


main()
