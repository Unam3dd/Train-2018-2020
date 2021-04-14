#!/usr/bin/python2
#-*- coding:utf-8 -*-
# Author : Unam3dd


import sys
from cryptography.fernet import Fernet


def encrypt_fernet(string):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(string)
    string_return = "[*] Key : %s\n[*] Encrypted : %s\n" % (key,encrypted)
    return string_return

def decrypt_fernet(string,key):
    f = Fernet(key)
    decrypted = f.decrypt(string)
    string_return = "[*] Key : %s\n[*] Decrypted : %s\n" % (key,decrypted)
    return string_return
    

if __name__ == '__main__':

    if sys.version[0] == "3":
        sys.exit("[!] Please Use Python2.7")

    try:

        if len(sys.argv) < 3:
            print("usage : %s -e/--encrypt <string>" % (sys.argv[0]))
            print("        %s -d/--decrypt <key> <string>" % (sys.argv[0]))
        else:
            if sys.argv[1] =="-e" or sys.argv[1] =="--encrypt":
                print(encrypt_fernet(sys.argv[2]))
        
            elif sys.argv[1] =="-d" or sys.argv[1] =="--decrypt":
                print(decrypt_fernet(sys.argv[3],sys.argv[2]))
            
            else:
                print("[!] Error Options !")
    
    except IndexError:
        print("[!] Error Index !")
