#!/usr/bin/python3
#-*- coding:utf-8 -*-

import hashlib
import sys
import os


def python_version():
    if sys.version[0] =="2":
        sys.exit("[!] Please Use Python 3.x")

def md5sum(filename):
    f=open(filename,"r",encoding="cp437")
    content = f.read()
    f.close()
    h = hashlib.md5()
    h.update(content.encode("cp437"))
    hex_digest = h.hexdigest()
    return hex_digest

def md5sum_bin(filename):
    f=open(filename,"rb")
    content = f.read()
    f.close()
    h = hashlib.md5()
    h.update(content)
    hex_digest = h.hexdigest()
    return hex_digest


def get_bytes(filename):
    f=open(filename,"rb")
    bytess = f.read()
    return len(bytess)


if __name__ == "__main__":
    python_version()
    if len(sys.argv) < 2:
        print("usage : %s -t <file>" % (sys.argv[0]))
    else:
        if sys.argv[1] =="-t":
            check_file = os.path.exists(sys.argv[2])
            if check_file ==True:
                hash_ = md5sum(sys.argv[2])
                print("[+] MD5 HASH : %s " % (hash_))
                print("[+] Bytes : %s" % (get_bytes(sys.argv[2])))
                print("[+] File : %s" % (sys.argv[2]))
                print("[+] Mode : RAW")
            else:
                print("[!] Error %s Found !" % (sys.argv[2]))
        
        elif sys.argv[1] =="-b":
            check_file = os.path.exists(sys.argv[2])
            if check_file ==True:
                hash_ = md5sum_bin(sys.argv[2])
                print("[+] MD5 HASH : %s " % (hash_))
                print("[+] Bytes : %s" % (get_bytes(sys.argv[2])))
                print("[+] File : %s" % (sys.argv[2]))
                print("[+] Mode : Binary")
            else:
                print("[!] Error %s Found !" % (sys.argv[2]))

        else:
            print("[!] Error Options !")