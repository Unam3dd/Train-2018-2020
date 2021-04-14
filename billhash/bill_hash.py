#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os
import hashlib
import sys
import argparse
import time
from datetime import datetime
import threading
import platform



def clear_os():
    if 'Linux' not in platform.platform():
        os.system('cls')
    
    elif 'Windows' not in platform.platform():
        os.system('clear')


def hashcrack(hashh,type_hash,wordlist):
    clear_os()
    try:
        check_passlist = os.path.exists(wordlist)
        if check_passlist ==True:
            with open(wordlist,'r') as f:
                content = f.readlines()
                i = 0
                for password in content:
                    password = password.rstrip()

                    
                    if type_hash =='md5':
                        encrypt_password = hashlib.md5(password.encode('utf-8')).hexdigest()
                        t_p = datetime.now().strftime('[%H:%M:%S]')
                        #sys.stdout.write('\r\033[1;96m[\033[1;93m?\033[1;96m] \033[1;96mTry Password : %s:\033[1;93m%s           ' % (hashh,password))
                        time.sleep(0.1)

                        if hashh == encrypt_password:
                            clear_os()
                            t = datetime.now().strftime('%H:%M:%S')
                            print('\n')
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Hash Cracked ! at %s' % (t))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Hash : \033[00m%s\033[1;96m' % (hashh))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Type : \033[00m%s\033[1;96m' % (type_hash))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Password : \033[1;91m%s\033[00m' % (password))
                            print('\n')
                            print('\n')
                            break
                        else:
                            sys.stdout.write('\r\033[1;96m[\033[1;93m?\033[1;96m] \033[1;96mPassword Failed : \033[1;91m%s:\033[1;91m%s           ' % (hashh,password))
                    
                    elif type_hash =='sha1':
                        encrypt_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
                        t_p = datetime.now().strftime('[%H:%M:%S]')
                        #sys.stdout.write('\r\033[1;96m[\033[1;93m?\033[1;96m] \033[1;96mTry Password : %s:\033[1;93m%s           ' % (hashh,password))
                        time.sleep(0.1)

                        if hashh == encrypt_password:
                            clear_os()
                            t = datetime.now().strftime('%H:%M:%S')
                            print('\n')
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Hash Cracked ! at %s' % (t))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Hash : \033[00m%s\033[1;96m' % (hashh))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Type : \033[00m%s\033[1;96m' % (type_hash))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Password : \033[1;91m%s\033[00m' % (password))
                            print('\n')
                            print('\n')
                            break
                        else:
                            sys.stdout.write('\r\033[1;96m[\033[1;93m?\033[1;96m] \033[1;96mPassword Failed : \033[1;91m%s:\033[1;91m%s           ' % (hashh,password))
                    
                    elif type_hash =='sha256':
                        encrypt_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                        t_p = datetime.now().strftime('[%H:%M:%S]')
                        #sys.stdout.write('\r\033[1;96m[\033[1;93m?\033[1;96m] \033[1;96mTry Password : %s:\033[1;93m%s           ' % (hashh,password))
                        time.sleep(0.1)

                        if hashh == encrypt_password:
                            clear_os()
                            t = datetime.now().strftime('%H:%M:%S')
                            print('\n')
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Hash Cracked ! at %s' % (t))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Hash : \033[00m%s\033[1;96m' % (hashh))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Type : \033[00m%s\033[1;96m' % (type_hash))
                            print('\033[1;96m[\033[1;94m+\033[1;96m] Password : \033[1;91m%s\033[00m' % (password))
                            print('\n')
                            print('\n')
                            break
                        else:
                            sys.stdout.write('\r\033[1;96m[\033[1;93m?\033[1;96m] \033[1;96mPassword Failed : \033[1;91m%s:\033[1;91m%s           ' % (hashh,password))
                    
                    else:
                        print('\033[1;91m[!] Type Hash Not Found !')
        else:
            print('\033[1;91m[!] Invalid Passlist Not Found !')
    
    except Exception as error1:
        print('\033[1;91m[!] Exception : %s' % (error1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--hash',help='Set Hash')
    parser.add_argument('type_hash',help='Set Type Hash Exemple md5, sha1')
    parser.add_argument('passlist',help='Set Passlist')
    parser.add_argument('-f','--hashlist',type=str,help='Set Hashlist')
    args = parser.parse_args()

    if args.hash:
        if args.type_hash:
            if args.passlist:
                hashcrack(args.hash,args.type_hash,args.passlist)
    
    if args.hashlist:
        with open(args.hashlist,'r') as f:
            content_hash = f.readlines()
            for hash_in_list in content_hash:
                hash_in_list = hash_in_list.rstrip()
                t = threading.Thread(target=hashcrack, args=(hash_in_list,args.type_hash,args.passlist))
                t.start()