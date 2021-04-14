#!/usr/bin/python3
#coding:utf-8

import os
import subprocess
import hashlib
import platform
import sys
import time


banner = '''
                                                     
      _/_/_/              _/                         
   _/          _/_/    _/_/_/_/  _/    _/  _/_/_/    
    _/_/    _/_/_/_/    _/      _/    _/  _/    _/   
       _/  _/          _/      _/    _/  _/    _/    
_/_/_/      _/_/_/      _/_/    _/_/_/  _/_/_/       
                                       _/            
                                      _/
                By Dxvistxr
'''

class tools_path():
   gcc = '/usr/bin/gcc'
   python27 = '/usr/bin/python2'
   python3 = '/usr/bin/python3'
   wine = '/usr/bin/wine'
   tdm_gcc = '/root/.wine/drive_c/TDM-GCC-64'
   python27_wine = '/root/.wine/drive_c/Python27'
   base64 = '/usr/bin/base64'



def sys_required():
   if 'Linux' not in platform.platform():
      sys.exit('[*] Linux System Required !')


def debian():
   sys_required()
   os.system('clear')
   os.system('clear')
   print('\033[1;96m'+banner)
   print('\n')
   print('\033[1;96m[*] \033[1;92m Updating Package....')
   subprocess.Popen('apt update', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
   print('\033[1;96m[*] \033[1;92m Upgrading Package....')
   subprocess.Popen('apt upgrade -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
   print('\033[1;96m[*] \033[1;92m Autoremoving Package....')
   subprocess.Popen('apt autoremove -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
   print('\033[1;96m[*] \033[1;92m[*] Checking Tools.....')
   time.sleep(0.5)
   print('\033[1;96m[*] \033[1;92m[*] Check GCC')
   check_gcc = os.path.exists(tools_path.gcc)
   if check_gcc ==True:
      print('\033[1;92m[*] GCC FOUND !')
   else:
      print('\033[1;91m[*] GCC NOT FOUND !')
      install_gcc = str(input('\033[1;92m[*] Do You Want Install (yes/no) > '))
      if install_gcc =='yes':
         os.system('apt update && apt upgrade -y && apt install gcc -y')
      
      elif install_gcc =='no':
         sys.exit('\033[1;91m[*] GCC NOT INSTALLED EXITING...')
   
   checkpython27 = os.path.exists(tools_path.python27)
   if checkpython27 ==True:
      print('\033[1;92m[*] PYTHON2.7 FOUND !')
   else:
      print('\033[1;91m[*] PYTHON27 NOT FOUND !')
      install_python27 = str(input('\033[1;92m[*] Do You Want Install (yes/no) > '))
      if install_python27 =='yes':
         os.system('apt update && apt upgrade -y && apt install python2 -y')

      elif install_python27 =='no':
         sys.exit('\033[1;91m[*] PYTHON27 NOT INSTALLED EXITING')
   
   checkpython3 = os.path.exists(tools_path.python3)
   if checkpython3 ==True:
      print('\033[1;92m[*] PYTHON3 FOUND !')
   else:
      print('\033[1;91m[*] PYTHON3 NOT FOUND !')
      install_python3 = str(input('\033[1;92m[*] Do You Want Install (yes/no) > '))
      if install_python3 =='yes':
         print('\033[1;92m[*] Installing Python3....')
         os.system('apt update && apt upgrade -y && apt install python3 -y')
      
      elif install_python3 =='no':
         sys.exit('\033[1;91m[*] PYTHON3 NOT FOUND !')
   
   check_wine = os.path.exists(tools_path.wine)
   if check_wine ==True:
      print('\033[1;92m[*] WINE FOUND !')
   else:
      print('\033[1;91m[*] WINE NOT FOUND !')
      installing_wine = str(input('\033[1;92m[*] Do You Want Install wine (yes/no) > '))
      if installing_wine =='yes':
         print('\033[1;92m[\033[1;93m1\033[1;92m] Install Wine With APT')
         print('\033[1;92m[\033[1;93m2\033[1;92m] Install Wine With WGET (DEBIAN)')
         print('\033[1;92m[\033[1;93m3\033[1;92m] Install Wine With WGET (UBUNTU & LINUX MINT)')
         print('\033[1;92m[\033[1;93m4\033[1;92m] Exiting Setup')
         choice_install_wine = int(input('\033[1;92m[*] Select Installation Method For Wine : '))
         
         if choice_install_wine ==1:
            print('\033[1;92m[*] Installing Wine...')
            os.system('apt update && apt upgrade -y && apt install wine wine-stable -y')
         
         elif choice_install_wine ==2:
            os.system('apt update && apt upgrade -y && wget -nc https://dl.winehq.org/wine-builds/winehq.key')
            os.system('sudo apt-key add winehq.key')
            print('\033[1;92m[\033[1;93m1\033[1;92m] Debian8 (Jessie)')
            print('\033[1;92m[\033[1;93m2\033[1;92m] Debian9 (Stretch)')
            print('\033[1;92m[\033[1;93m3\033[1;92m] Debian10 (Currently Testing) (Buster)')
            print('\n')
            choice_install_packet_wine = int(input('\033[1;92m[*] Choice Wine Packet : '))
            
            if choice_install_packet_wine ==1:
               print('\033[1;92m[*] Creating winehq.list....')
               print('\033[1;92m[*] Writing => \033[1;91mdeb \033[1;93mhttps://dl.winehq.org/wine-builds/debian/ \033[1;95mjessie \033[1;91mmain')
               print('\033[1;92m[*] Wait Moment Please...')
               check_apt = os.path.exists('/etc/apt/sources.list.d')
               if check_apt ==True:
                  f=open('/etc/apt/sources.list.d/winehq.list','w')
                  f.write('deb https://dl.winehq.org/wine-builds/debian/ jessie main')
                  f.close()
                  print('\033[1;92m[*] Updating Packet....')
                  os.system('apt update')
                  os.system('apt install --install-recommends winehq-stable')
               else:
                  print('\033[1;91m[*] ETC/APT/SOURCES.LIST.D NOT FOUND !')
                  sys.exit()
            
            elif choice_install_packet_wine ==2:
               print('\033[1;92m[*] Creating winehq.list....')
               print('\033[1;92m[*] Writing => \033[1;91mdeb \033[1;93mhttps://dl.winehq.org/wine-builds/debian/ \033[1;95mstretch \033[1;91mmain')
               print('\033[1;92m[*] Wait Moment Please....')
               check_apt = os.path.exists('/etc/apt/sources.list.d')
               if check_apt ==True:
                  f=open('/etc/apt/sources.list.d/winehq.list','w')
                  f.write('deb https://dl.winehq.org/wine-builds/debian/ stretch main')
                  f.close()
                  print('\033[1;92m[*] Updating Packet.....')
                  os.system('apt update')
                  os.system('apt install --install-recommends winehq-stable -y')
            
            elif choice_install_packet_wine ==3:
               print('\033[1;92m[*] Creating winehq.list....')
               print('\033[1;92m[*] Writing => deb https://dl.winehq.org/wine-builds/debian/ buster main')
               check_apt = os.path.exists('/etc/apt/sources.list.d')
               if check_apt ==True:
                  f=open('/etc/apt/sources.list.d/winehq.list','w')
                  f.write('deb https://dl.winehq.org/wine-builds/debian/ buster main')
                  f.close()
                  print('\033[1;92m[*] Updating Packet....')
                  os.system('apt update')
                  os.system('apt install --install-recommends winehq-stable -y')
            
            elif choice_install_packet_wine ==4:
               print('\033[1;92m[*] exiting....')
               sys.exit()
         
         elif choice_install_wine ==3:
            os.system('apt update && apt upgrade -y && apt install wget -y && wget -nc https://dl.winehq.org/wine-builds/winehq.key')
            os.system('sudo apt-key add winehq.key')
            print('\033[1;92m[\033[1;93m1\033[1;92m] Ubuntu 18.10')
            print('\033[1;92m[\033[1;93m2\033[1;92m] Ubuntu 18.04 & Linux Mint 19.x')
            print('\033[1;92m[\033[1;93m3\033[1;92m] Ubuntu 16.04 & Linux Mint 18.x')
            print('\033[1;92m[\033[1;93m4\033[1;92m] Ubuntu 14.04 & Linux Mint 17.x')
            choice_ubuntu_install_wine = int(input('\033[1;92m[*] Choice Packet Wine => '))
            if choice_ubuntu_install_wine ==1:
               print('\033[1;92m[*] Installing Wine Sources List..')
               os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ cosmic main'")
               os.system('apt update && sudo apt install --install-recommends winehq-stable')
            
            elif choice_ubuntu_install_wine ==2:
               print('\033[1;92m[*] Installing Wine Sources List...')
               os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'")
               os.system('apt update && sudo apt install --install-recommends winehq-stable')
            
            elif choice_ubuntu_install_wine ==3:
               print('\033[1;92m[*] Installing Wine Sources List....')
               os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main'")
               os.system('apt update && sudo apt install --install-recommends winehq-stable')
            
            elif choice_ubuntu_install_wine ==4:
               print('\033[1;92m[*] Installing Wine Sources List...')
               os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ trusty main'")
               os.system('apt update && sudo apt install --install-recommends winehq-stable')
   
   check_tdm_gcc = os.path.exists(tools_path.tdm_gcc)
   if check_tdm_gcc ==True:
      print('\033[1;92m[*] TDM-GCC FOUND !!!')
   else:
      print('\033[1;91m[*] TDM GCC NOT FOUND !!!')
      install_gcc_wine = str(input('\033[1;92m[*] Do You Want Install TDM-GCC (yes/no) > '))
      if install_gcc_wine =='yes':
         os.system('apt update && apt install wget -y && wget http://download1645.mediafire.com/mzwfmpmvxfdg/dnhcpavttyy5xwt/tdm.exe')
         os.system('wine tdm.exe')
      
      elif install_gcc_wine =='no':
         sys.exit('\033[1;91m[*] TDM GCC NOT FOUND !')
   
   check_python27_wine = os.path.exists(tools_path.python27_wine)
   if check_python27_wine ==True:
      print('\033[1;92m[*] PYTHON27 WINE FOUND !')
   else:
      print('\033[1;91m[*] PYTHON27 NOT FOUND !')
      install_python27 = str(input('\033[1;92m[\033[1;93m*\033[1;92m] Do You Want Install Python2.7 Wine (yes/no) > '))
      if install_python27 =='yes':
         os.system('apt update && apt install wget -y && wget https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi && mv python-2.7.15.msi python27.msi && wine /i msiexec python27.msi')
      
      elif install_python27 =='no':
         sys.exit('\033[1;96m[*] Python27 Not Found ! wine')
   
   check_base64 = os.path.exists(tools_path.base64)
   if check_base64 ==True:
      print('\033[1;92m[*] Base64 Found !')
   else:
      print('\033[1;91m[*] Base64 Not Found !')
      install_coreutils = str(input('\033[1;92m[*] Do You Want Install Coreutils/Base64 (yes/no) > '))
      if install_coreutils =='yes':
         os.system('apt update && apt upgrade -y && apt install coreutils -y')
      
      elif install_coreutils =='no':
         sys.exit()

sys_required()
debian()