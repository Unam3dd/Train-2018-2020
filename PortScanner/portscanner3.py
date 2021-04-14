#!/usr/bin/python3
#-*- coding:utf-8 -*-

import socket
import time
import requests
from datetime import datetime
import sys
import colorama
import argparse
import _thread

TRUE = '\033[1;92m[\033[1;94m+\033[1;92m]'
FAIL = '\033[1;91m[!]'



def checking_internet():
    try:
        r = requests.get('https://www.google.com')
    except:
        sys.exit(FAIL+' Internet Not Found ! Please Try Again')

def connect_host(target,port):
    try:
        set_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        set_client.connect((target,port))
        print(TRUE+' Port %s => open ' % (port))
    except:
        pass

def connect_host_verbose(target,port):
    try:
        set_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        set_client.connect((target,port))
        print(TRUE+' Port %s => open ' % (port))
    except:
        print(FAIL+' Port %s => closed ' % (port))

def run_scanner(addr,max_port: int):
    try:
        y = 1
        i = 1
        t = datetime.now().strftime('[%d.%m.%y.%H_%M_%S]')
        print(TRUE+' Scanner Started At %s => %s' % (t,addr))
        while i<max_port:
            try:
                _thread.start_new_thread(connect_host,(addr,y))
                y = y+1
                i = i+1
            
            except Exception as error:
                print(FAIL+' Exception Error Connect')
                print(error)
    
    except Exception as error_run:
        print(error_run)



def run_scanner_verbose(addr,max_port: int):
    try:
        y = 1
        i = 1
        t = datetime.now().strftime('[%d.%m.%y_%H_%M_%S]')
        print(TRUE+' Scanner Started At %s => %s' % (t,addr))
        while i<max_port:
            try:
                _thread.start_new_thread(connect_host_verbose,(addr,y))
                y = y+1
                i = i+1
            
            except:
                print(FAIL+' Exception Error Connect')
    
    except:
        print(FAIL+' Exception Start RunScanner')


def main():
    print('Author : Dxvistxr - 2019')
    parser = argparse.ArgumentParser()
    parser.add_argument('ip',help='Set Target IP')
    parser.add_argument('max_port',type=int,help='Set Max Port For Stop Scanner')
    parser.add_argument('-v','--verbose',help='If Verbose is True : print port closed')
    args = parser.parse_args()
    
    if args.ip:
        if args.max_port:
            if args.verbose:
                checking_internet()
                run_scanner_verbose(args.ip,args.max_port)
            else:
                checking_internet()
                run_scanner(args.ip,args.max_port)


if __name__ == '__main__':
    main()