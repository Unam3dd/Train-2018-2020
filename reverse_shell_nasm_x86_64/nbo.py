#!/usr/bin/python2
#-*- coding:utf-8 -*-

import socket
import struct
import sys
import shlex
import codecs


def python2_required():
    if sys.version[0] == "3":
        sys.exit("[!] Python 2.7 Required !")

def convert_addr(addr_str):
    return hex(struct.unpack('<L', socket.inet_aton(addr_str))[0])

def convert_port(port):
    return hex(socket.htons(int(port)))

def convert_string(string):
    c = codecs.encode(codecs.decode(string.encode("hex"), 'hex')[::-1], 'hex').decode()
    return "0x"+c

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : %s -a <string_address> | Convert String Address in Network Byte Order" % (sys.argv[0]))
        print("        %s -p <int_port>       | Convert Port int in Network Byte Order" % (sys.argv[0]))
        print("        %s -s <string>         | Convert String In Little Endian" % (sys.argv[0]))
    else:
        options = sys.argv[1]
        inp = sys.argv[2]
        
        if options =="-a":
            print("[+] Address in Network Byte Order : %s" % (convert_addr(inp)))
        
        elif options =="-p":
            print("[+] Port in network byte order : %s" % (convert_port(int(inp))))
        
        elif options =="-s":
            print("[+] String in Little Endian : %s" % (convert_string(inp)))

        else:
            print("[!] Error Options !")