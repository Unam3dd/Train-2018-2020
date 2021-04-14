#!/usr/bin/python2
#-*- coding:utf-8 -*-


import platform
import time
import shlex
import sys
from datetime import datetime
from itertools import izip, cycle
import base64
import socket
import select
import string
import requests
import platform
import json

def xor_crypt_string(data, key, encode=False, decode=False):
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored

def distrib_data(sockfd, message):
    for socket in CONN_LIST:
        if socket != server_socket and socket != sock:
            try:
                data = xor_crypt_string(message,xor_key,encode=True)
                socket.send(data)
            except:
                socket.close()
                CONN_LIST.remove(socket)

CONN_LIST = []
BUFFER_SIZE = 4096

def console(host,port,key):
    if sys.version[0] =="3":
        sys.exit("[*] Python 2 Required !")

    global server_socket
    global sock
    global xor_key
    xor_key = key
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, int(port)))
    server_socket.listen(10)
    CONN_LIST.append(server_socket)
    print('[*] Key Server => %s' % (key))
    print('[*] Listening On %s:%s' % (host,port))

    while True:
        read_sockets,write_sockets,error_sockets = select.select(CONN_LIST,[],[])
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONN_LIST.append(sockfd)
                print("[%s] -> Connected On Server" % (addr[0]))
                t = datetime.now().strftime('%d %H:%M:%S')
                distrib_data(sockfd, "\033[00m[\033[1;94m%s\033[00m] has joined Server at %s\n" % (addr[0],t))
            else:
                try:
                    data = sock.recv(BUFFER_SIZE)
                    if data:
                        decode_data = xor_crypt_string(data,xor_key,decode=True)
                        ip = sock.getpeername()[0]
                        split_data = decode_data.split(':')
                        
                        if split_data[1].startswith('/exit')==True:
                            distrib_data(sock,"[%s] -> Disconnected !\033[00m\n" % (ip))
                            print("\033[31m[%s] -> Disconnected !\033[00m\n" % (ip))
                            sock.close()
                            CONN_LIST.remove(sock)
                            continue
                            
                        else:
                            t = datetime.now().strftime('%H:%M:%S')
                            distrib_data(sock,"\033[32m["+t+"|"+ip+"@\033[1;96m"+split_data[0]+"\033[32m]\033[1;96m "+split_data[1]+"\033[00m")
                            print("\033[32m[%s|\033[32m%s@\033[1;96m%s\033[32m] \033[1;96m%s\n" % (t,ip,split_data[0],split_data[1]))
                except:
                    distrib_data(sock,"[%s] -> Disconnected !\n" % (addr[0]))
                    print("\033[31m[%s] -> Disconnected !\n" % (addr[0]))
                    sock.close()
                    CONN_LIST.remove(sock)
                    continue
    
    server_socket.close()

if __name__ == '__main__':
    if 'Linux' not in platform.platform():
        sys.exit("[*] Linux Platform Required !")

    if len(sys.argv) <4:
        print('usage : %s <host> <port> <key_xor>' % (sys.argv[0],))
    else:
        console(sys.argv[1],sys.argv[2],sys.argv[3])