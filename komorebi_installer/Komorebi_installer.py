#coding:utf-8

import os
import subprocess
import sys
import time
import platform

class required_tools():
    cowsay = '/usr/games/cowsay'
    git = '/usr/bin/git'


def not_windows():
    if 'Linux' not in platform.platform():
        sys.exit('[*] Linux System Required !')

def check_tools(path):
    check = os.path.exists(path)
    if check ==True:
        os.system('clear')
    else:
        print('\033[1;92m[*] Install Requirements !!!')
        print('\033[1;92m[*] Run Command : ')
        print('\033[1;92m\n')
        print('\033[1;92m[*] Debian/Ubuntu/Kali/Parrot => apt update && apt install git cowsay lolcat -y')
        print('\033[1;92m[*] ArchLinux/Manjaro => pacman -Syu && pacman -S cowsay git lolcat')
        sys.exit()

def main():
    not_windows()
    check_tools(required_tools.cowsay)
    check_tools(required_tools.git)
    while True:
        os.system('clear')
        os.system('clear')
        os.system('cowsay Live Wallpaper Installer By Dxvistxr Komorebi')
        print('\n')
        print('\033[1;96m[1] Debian/Ubuntu/Parrot/Kali Installer')
        print('\n')
        print('\033[1;96m[2] ArchLinux/Manjaro Installer')
        print('\n')
        print('\033[1;91m[3] Exiting')
        print('\n')
        choice_installer = int(input('\033[1;92m[*] Choice Installer ~> '))
        
        if choice_installer ==1:
            print('\033[1;92m[*] Updating Package...')
            subprocess.Popen('apt update', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(1)
            print('\033[1;92m[*] Installing Dependence...')
            subprocess.Popen('apt update && apt install git -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            time.sleep(1)
            print('\033[1;92m[*] Installing Requirements...')
            subprocess.Popen('apt update && apt install libgtop2-dev libgtk-3-dev gtk+-3.0 libgtop-2.0 glib-2.0 gee-0.8 libwnck-3.0 clutter-gtk-1.0 clutter-1.0 clutter-gst-3.0 cmake valac -y', shell=True, stdout=subprocess, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            time.sleep(1)
            print('\033[1;92m[*] GET Reposterie')
            subprocess.Popen('git clone https://github.com/iabem97/komorebi.git')
            time.sleep(1)
            os.system('cd komorebi && mkdir build')
            os.system('cd komorebi && cd build && cmake .. && sudo make install')
            os.system('cd /System/Applications/ && cp komorebi /usr/bin/ && cp komorebi-wallpaper-creator')
            check_final = os.path.exists('/usr/bin/komorebi')
            if check_final ==True:
                print('\033[1;92m[*] Setup Finish !!!!! SuccesFully')
            else:
                print('\033[1;91m[*] Setup Finish !!!! Not komorebi Moved in /usr/bin/ type locate komorebi for locate komorebi')
        
        elif choice_installer ==2:
            print('\033[1;92m[*] Updating Package...')
            subprocess.Popen('pacman -Syu', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(1)
            print('\033[1;92m[*] Installing Dependence...')
            subprocess.Popen('pacman -S git -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            time.sleep(1)
            print('\033[1;92m[*] Installing Requirements...')
            subprocess.Popen('pacman -S libgtop2-dev libgtk-3-dev gtk+-3.0 libgtop-2.0 glib-2.0 gee-0.8 libwnck-3.0 clutter-gtk-1.0 clutter-1.0 clutter-gst-3.0 cmake valac -y', shell=True, stdout=subprocess, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            time.sleep(1)
            print('\033[1;92m[*] GET Reposterie')
            subprocess.Popen('git clone https://github.com/iabem97/komorebi.git')
            time.sleep(1)
            os.system('cd komorebi && mkdir build')
            os.system('cd komorebi && cd build && cmake .. && sudo make install')
            os.system('cd /System/Applications/ && cp komorebi /usr/bin/ && cp komorebi-wallpaper-creator')
            check_final = os.path.exists('/usr/bin/komorebi')
            if check_final ==True:
                print('\033[1;92m[*] Setup Finish !!!!! SuccesFully')
            else:
                print('\033[1;91m[*] Setup Finish !!!! Not komorebi Moved in /usr/bin/ type locate komorebi for locate komorebi')
        
        elif choice_installer ==3:
            sys.exit('\033[1;91m[*] Exiting Installer !!!')

main()
