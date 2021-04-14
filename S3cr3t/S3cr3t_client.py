#!/usr/bin/python2
#-*- coding:utf-8 -*-

import os
import time
import platform
import socket
import sys
import select
import logging
import readline

banner = '''
\033[1;96m
  ██████ ▓█████  ▄████▄   ██▀███  ▓█████▄▄▄█████▓
▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒
░ ▓██▄   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░
  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░ 
▒██████▒▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▒██▒ ░ 
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░   
░ ░▒  ░ ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░ ░ ░  ░   ░    
░  ░  ░     ░   ░          ░░   ░    ░    ░      
      ░     ░  ░░ ░         ░        ░  ░        
                ░                                


            [     Created By Unamed    ]
            [     Github : \033[31mUnam3dd\033[00m     ]
            [     Insta : \033[31m0x4eff\033[00m       ]

               Encrypted Message Live With XOR
\033[00m
'''

try:
    from datetime import datetime
except ImportError:
    print('\033[31m[!] Error Datetime Install Datetime !')

try:
    from itertools import izip, cycle
    import base64
except ImportError:
    print('\033[31m[!] Error IterTools, Base64')

def xor_crypt_string(data, key, encode=False, decode=False):
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored

class SimpleCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            if text:
                self.matches = [s
                                for s in self.options
                                if s and s.startswith(text)]
                logging.debug('%s matches: %s', repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('(empty input) matches: %s', self.matches)

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s',repr(text), state, repr(response))
        return response

def input_console(username):
    t = datetime.now().strftime('%H:%M:%S')
    sys.stdout.write('[\033[1;94m%s\033[00m] \033[32m%s$ ' % (t,username))
    sys.stdout.flush()

def run_client(host,port,xor_key,username):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host,int(port)))
    except:
        print('\033[31m[!] Error Unable Connect %s:%s' % (host,port))
        sys.exit()
    
    input_console(username)
    while True:
        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
        for sock in read_sockets:
            if sock ==s:
                data = s.recv(4096)
                if not data:
                    print('\n[!] (503) Server Error !')
                else:
                    decode_data = xor_crypt_string(data,xor_key,decode=True)
                    sys.stdout.write('\n\033[31m'+decode_data+'\033[00m')
                    input_console(username)
            else:
                msg = sys.stdin.readline()
                
                if msg.startswith('/exit')==True:
                    data_encode = xor_crypt_string(msg,xor_key,encode=True)
                    s.send(data_encode)
                    sys.exit()

                elif msg.startswith('/clear')==True:
                    clear_os()
                    string = username+":\033[1;96m%s has clear console\033[00m\n" % (username)
                    data_encode = xor_crypt_string(string,xor_key,encode=True)
                    s.send(data_encode)
                    input_console(username)

                else:
                    string = username+":"+msg
                    data_encode = xor_crypt_string(string,xor_key,encode=True)
                    s.send(data_encode)
                    print('\033[32m[\033[34m+\033[32m] Message Sent !')
                    input_console(username)

def clear_os():
    if 'Linux' not in platform.platform():
        os.system('cls')
    
    elif 'Windows' not in platform.platform():
        os.system('clear')


if __name__ == '__main__':
    if 'Linux' not in platform.platform():
        sys.exit("[*] Linux Platform Required !")

    print(banner)
    if len(sys.argv) <5:
        print('usage : %s <host> <port> <key_xor> <username>' % (sys.argv[0]))
    else:
        clear_os()
        print(banner)
        run_client(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])