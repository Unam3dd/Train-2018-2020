#!/usr/bin/python2
#-*- coding:utf-8 -*-
#Created By Unamed


import hashlib
import binascii
import os
import sys
import logging

try:
    from datetime import datetime
except ImportError:
    print("\033[31m[!] Error Datetime Not Found !")

import time


banner = '''
\033[32m
 __   _ _______        _______
 | \  |    |    |      |  |  |
 |  \_|    |    |_____ |  |  |
                              
        
        NTLM Hash Brute Forcer With Wordlist
        
        \033[00m[  Github    :    \033[34mUnam3dd\033[00m]
        [  Instagram :    \033[34munam3dd\033[00m]
        [  Version :      \033[34m  0.1\033[00m  ]

'''

def required_python_version():
    if sys.version[0] =="3":
        sys.exit("[*] Python 2.7 Required !")


def start_crack(target_hash,wordlist):
    try:
        check_wordlist = os.path.exists(wordlist)
        
        if check_wordlist ==True:
            with open(wordlist) as f:
                content = f.readlines()
                for password in content:
                    password = password.rstrip()
                    hashh = hashlib.new('md4',password.encode("utf-16le")).digest()
                    password_hash = binascii.hexlify(hashh)
                    if target_hash == password_hash:
                        t = datetime.now().strftime("%H:%M:%S")
                        print("(\033[33m%s\033[00m)\033[32m[\033[34m+\033[32m] Hash Cracked => \033[33m%s:%s\033[00m" % (t,target_hash,password))
                        logname = "hash_found_%s.txt" % (target_hash)
                        logging.basicConfig(filename=logname, level=logging.DEBUG, format = '%(message)s')
                        logging.info("Hash Cracked => %s:%s" % (target_hash,password))
                        print("(\033[33m%s\033[00m)\033[32m[\033[34m+\033[32m] Password Save As \033[33m%s\033[00m" % (t,logname))
                        break
                    else:
                        t = datetime.now().strftime("%H:%M:%S")
                        print("(\033[33m%s\033[00m)\033[32m[\033[31m-\033[32m] Hash Failed => %s:%s\033[00m" % (t,target_hash,password))
        else:
            print("\033[31m[!] %s Not Found !" % (wordlist))

    except:
        print("\033[31m[!] Error Start Crack !")


if __name__ == "__main__":
    print(banner)
    required_python_version()
    if len(sys.argv) <3:
        print("usage : %s <ntlm_hash> <wordlist>" % (sys.argv[0]))
    else:
        start_crack(sys.argv[1],sys.argv[2])