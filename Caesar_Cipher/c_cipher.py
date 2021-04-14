#!/usr/bin/python2
#-*- coding:utf-8 -*-

import string
import collections
import sys

def caesar_encrypt_decrypt(rotate_string,rotate_number):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(rotate_number)
    lower.rotate(rotate_number)

    upper = "".join(list(upper))
    lower = "".join(list(lower))

    caesar_ = rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

    return caesar_

def brute_force(encrypted_cipher):
    i = 0
    while i<26:
        d = caesar_encrypt_decrypt(encrypted_cipher,i * -1)
        print("Caesar (%d) : %s" % (i,d))
        i = i+1


def python_required():
    if sys.version[0] =="3":
        sys.exit("[!] Please Use Python2.7 for This Script")

if __name__ == '__main__':
    python_required()
    if len(sys.argv) < 3:
        print("Caesar Cipher")
        print("usage : %s -e/--encrypt <string> <key>" % (sys.argv[0]))
        print("        %s -d/--decrypt <cipher> <key>" % (sys.argv[0]))
        print("        %s -b/--bruteforce <cipher>" % (sys.argv[0]))
    else:
        if sys.argv[1] == "-e" or sys.argv[1] == "--encrypt":
            d = caesar_encrypt_decrypt(sys.argv[2],int(sys.argv[3]))
            print("[*] Plain Text : %s" % (sys.argv[2]))
            print("[*] Cipher Text : %s" % (d))

        elif sys.argv[1] =="-d" or sys.argv[1] =="--decrypt":
            d = caesar_encrypt_decrypt(sys.argv[2],int(sys.argv[3]) * -1)
            print("[*] Cipher Text : %s" % (sys.argv[2]))
            print("[*] Plain Text  : %s" % (d))

        
        elif sys.argv[1] =="-b" or sys.argv[1] =="--bruteforce":
            brute_force(sys.argv[2])

        else:
            print("[!] Options Invalid !")