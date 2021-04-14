#!/usr/bin/python2
#-*- coding: utf-8 -*-

import os
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import argparse

def ftp_server(host,port,user,passwd,pathroot):
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, passwd, pathroot, perm="elradfmwMT")
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((host, port), handler)
    server.serve_forever()

def main():
    parser = argparse.ArgumentParser()
    print('\033[1;93m')
    print('\033[1;93m[*] By Dxvistxr')
    parser.add_argument('host',type=str, help='Set FTP Host')
    parser.add_argument('port',type=int, help='Set FTP Port')
    parser.add_argument('user',type=str,help='Set FTP USER')
    parser.add_argument('password',type=str,help='Set FTP PASSWORD')
    parser.add_argument('pathroot',type=str,help='Set FTP PATHROOT')
    args = parser.parse_args()
    print('\033[00m')
    ftp_server(args.host,args.port,args.user,args.password,args.pathroot)


if __name__ == '__main__':
    main()
