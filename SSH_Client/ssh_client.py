#!/usr/bin/python2
#-*- coding:utf-8 -*-

import time
from datetime import datetime
import platform
import socket
import os
import sys
import readline
import logging
from pexpect import pxssh


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

def clear_os():
    if 'Linux' not in platform.platform():
        os.system("cls")
    
    elif 'Windows' not in platform.platform():
        os.system("clear")


def check_ssh_service(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        return True
    except:
        return False


def simple_client_connect(ip,prt,username,password):
    ssh_session = pxssh.pxssh()
    try:
        ssh_session.login(ip,username,password,port=prt)
    except pxssh.ExceptionPxssh as e:
        print("[!] Failed Login %s:%s\n" % (username,password))
        print(e.message)
    
    
    readline.set_completer(SimpleCompleter(['exit','quit']).complete)
    readline.parse_and_bind('tab: complete')
    while True:
        try:
            t = datetime.now().strftime("%H:%M:%S")
            console = raw_input("[%s-%s@%s]$" % (t,username,ip))
            
            if console.startswith("exit")==True:
                ssh_session.logout()
                sys.exit()
            else:
                ssh_session.sendline(console)
                ssh_session.prompt()
                print(ssh_session.before)
        
        except KeyboardInterrupt:
            print("[!] Type 'quit' or 'exit' for Exiting Shell")



if __name__ == '__main__':
    if len(sys.argv) <5:
        print("usage : %s <ip> <port> <username> <password>" % (sys.argv[0]))
    else:
        if "Linux" not in platform.platform():
            clear_os()
            print("[*] Wait Update For Windows Client")
        
        elif "Windows" not in platform.platform():
            try:
                service = check_ssh_service(sys.argv[1],int(sys.argv[2]))
                if service ==True:
                    try:
                        simple_client_connect(sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4])
                    except Exception as get_console:
                        print(get_console.message)
                else:
                    print("\033[31m[!] %s:%s Destination Host Unreachable" % (sys.argv[1],sys.argv[2]))
            
            except Exception as error_console_ssh:
                print("\033[31m[!] %s" % (error_console_ssh.message))
