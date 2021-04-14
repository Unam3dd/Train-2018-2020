#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os
import hashlib
import sys
import argparse
import _thread
import time
from datetime import datetime


def hashcrack(hashh,type_hash,wordlist):
    try:
        check_passlist = os.path.exists(wordlist)
        if check_passlist ==True:
            with open(wordlist,'r') as f:
                content = f.readlines()
                for password in content:
                    password = password.rstrip()

                    if type_hash =='md5':
                        encrypt_password = hashlib.md5(password.encode('utf-8')).hexdigest()
                        t_p = datetime.now().strftime('[%H:%M:%S]')
                        os.system('clear')
                        os.system('clear')
                        print('\033[1;92m[\033[1;94m+\033[1;92m] Try Password : '+str(hashh+':'+password))
                        time.sleep(0.1)

                        if hashh == encrypt_password:
                            t = datetime.now().strftime('%H:%M:%S')
                            os.system('clear')
                            os.system('clear')
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Hash Cracked ! at '+str(t))
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Hash : '+str(hashh))
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Type : MD5')
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Password : '+str(password))
                            break
                        
                        else:
                            pass
                    
                    elif type_hash =='sha1':
                        os.system('clear')
                        os.system('clear')
                        encrypt_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
                        t_p = datetime.now().strftime('[%H:%M:%S]')
                        print('\033[1;92m[\033[1;94m+\033[1;92m] Try Password : '+str(hashh+':'+password))
                        time.sleep(0.2)

                        if hashh == encrypt_password:
                            os.system('clear')
                            os.system('clear')
                            t = datetime.now().strftime('%H:%M:%S')
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Hash Cracked ! at '+str(t))
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Hash : '+str(hashh))
                            print('\033[1;92m[\033[1;94m+\033[1;92m] TYPE : SHA1')
                            print('\033[1;92m[\033[1;94m+\033[1;92m] Password : '+str(password))
                            break
                        
                        else:
                            pass
                    
                    else:
                        print('\033[1;91m[!] Type Hash Not Found !')
        else:
            print('\033[1;91m[!] Invalid Passlist Not Found !')
    
    except Exception as error1:
        print('\033[1;91m[!] Exception : '+str(error1))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('hash',help='Set Hash')
    parser.add_argument('type_hash',help='Set Type Hash Exemple md5, sha1')
    parser.add_argument('passlist',help='Set Passlist')
    args = parser.parse_args()

    if args.hash:
        if args.type_hash:
            if args.passlist:
                hashcrack(args.hash,args.type_hash,args.passlist)


if __name__ == '__main__':
    main()