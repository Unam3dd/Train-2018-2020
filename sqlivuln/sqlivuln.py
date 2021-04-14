#!/usr/bin/python2
#-*- coding:utf-8 -*-

import json
import time
import os
import subprocess
import platform
import sys


banner_ascii = '''
\033[1;91m
  ██████   █████   ██▓     ██▓    ██▒   █▓ █    ██  ██▓     ███▄    █ 
▒██    ▒ ▒██▓  ██▒▓██▒    ▓██▒   ▓██░   █▒ ██  ▓██▒▓██▒     ██ ▀█   █ 
░ ▓██▄   ▒██▒  ██░▒██░    ▒██▒    ▓██  █▒░▓██  ▒██░▒██░    ▓██  ▀█ ██▒
  ▒   ██▒░██  █▀ ░▒██░    ░██░     ▒██ █░░▓▓█  ░██░▒██░    ▓██▒  ▐▌██▒
▒██████▒▒░▒███▒█▄ ░██████▒░██░      ▒▀█░  ▒▒█████▓ ░██████▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░░▓        ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░ ▒ ░      ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░ ░░   ░ ▒░
░  ░  ░     ░   ░   ░ ░    ▒ ░        ░░   ░░░ ░ ░   ░ ░      ░   ░ ░ 
      ░      ░        ░  ░ ░           ░     ░         ░  ░         ░ 
                                      ░                               
\033[00m                                            
                        
                        [   Author : \033[1;91mUnamed\033[00m   ]
                        [   Date : \033[1;91m2019\033[00m       ]
                        [   Github : \033[1;91mDxvistxr\033[00m ]
                        [   Instagram : \033[1;91m0x4eff\033[00m]


'''

global payloads
global url_found
global sqli_url
payloads = ["You have an error in your SQL syntax"]
url_found = []
sqli_url = []

def install_requirement():
    try:
        if 'Linux' not in platform.platform():
            os.system('py -m pip install sqlmap datetime requests argparse google')
        
        elif 'Windows' not in platform.platform():
            os.system('python2 -m pip install sqlmap datetime google requests argparse && python3 -m pip install sqlmap datetime requests google argparse')
    
    except Exception as error_execute_command:
        print(error_execute_command)

try:
    from datetime import datetime
except ImportError:
    print('[!] Error Import datetime')
    install_requirement()

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('[!] Error Import bs4  !')
    install_requirement()

try:
    import argparse
except ImportError:
    print('[!] Error Import argparse')

try:
    import requests
except ImportError:
    print('[!] Error Import requests')

try:
    from googlesearch import search
except ImportError:
    print('[!] Error : Import Google Search')


def isearch(query,max_stop_website):
    check_internet()
    print('\033[1;92m[\033[1;94m*\033[1;92m] \033[00mWaiting Moment Please Search..')
    try:
        if max_stop_website ==None:
            for website in search(query, tld="co.in", num=10, stop=20, pause=2):
                t = datetime.now().strftime('%H:%M:%S')
                #print('\033[1;92m[\033[1;94m%s\033[1;92m] %s ' % (t,website))
                url_found.append(website)

            print('\033[1;92m[\033[1;94m*\033[1;92m] Search Finish At %s ' % (t))
        else:
            for website in search(query, tld="co.in", num=10, stop=max_stop_website, pause=2):
                t = datetime.now().strftime('%H:%M:%S')
                #print('\033[1;92m[\033[1;94m%s\033[1;92m] %s' % (t,website))
                url_found.append(website)

            print('\033[1;92m[\033[1;94m*\033[1;92m] Search Finish At %s ' % (t))

    except Exception as error_search:
        print(error_search)

def check_internet():
    try:
        r = requests.get('https://google.com')
    except:
        print('[*] Error Internet Not Found !')

def check_isqli(url):
    try:
        t = datetime.now().strftime('%H:%M:%S')
        r = requests.get(url+'"')
        content = r.text
        status = r.status_code
        if status ==200 or status ==301 or status ==302:
            for payload in payloads:
                #print('\033[1;92m[\033[1;96m%s\033[1;92m] \033[00mTry Payloads => \033[1;95m%s\033[00m' % (t,payload))
                if payload in content:
                    print('\033[1;92m[\033[1;94m%s\033[1;92m] \033[00m[\033[1;92mINFO\033[00m] \033[\033[1;96m%s \033[00m \033[1;95mvulnerable\033[00m' % (t,url))
                    sqli_url.append(url)
                    break
                else:
                    print('\033[1;92m[\033[1;94m%s\033[1;92m] \033[00m[\033[1;92mINFO\033[00m] \033[1;96m%s \033[1;91mnot vulnerable\033[00m' % (t,url))
        
        elif status ==500 or status ==503:
            print('\033[1;91m[!] %s Server Error !\033[00m' % (url))
        
        elif status ==404:
            print('\033[1;91m[!] %s 404 not found !\033[00m' % (url))
    
    except Exception as error_sqli:
        print('[!] Error Hostname !')


if __name__ == '__main__':
    try:
        print(banner_ascii)
        parser = argparse.ArgumentParser()
        parser.add_argument('-u','--url',type=str, help='Set URL')
        parser.add_argument('-f','--urlfile',type=str, help='Set URL FILE')
        parser.add_argument('-g','--google',type=str, help='Set Search Google')
        parser.add_argument('-m','--numbermax',type=int,help='Set Number Max Page (Default is 20)')
        args = parser.parse_args()

        if args.url:
            try:
                check_internet()
                check_isqli(args.url)
                print('+-------------------------------+')
                print('|     \033[1;91mURL FOUND VULNERABLE\033[00m      |')
                print('+-------------------------------+')
                i = 0
                for url_found in sqli_url:
                    print('[\033[1;91m%s\033[00m] \033[1;91m%s\033[00m' % (i,url_found))
                    i = i+1

            except Exception as error_check_sqli:
                print(error_check_sqli)
        
        elif args.urlfile:
            try:
                check_internet()
                check_url_file = os.path.exists(args.urlfile)
                if check_url_file ==True:
                    with open(args.urlfile,'r') as f:
                        content = f.readlines()
                        for link in content:
                            link = link.rstrip()
                            check_isqli(link)
                        
                        print('+-------------------------------+')
                        print('|     \033[1;91mURL FOUND VULNERABLE\033[00m]      |')
                        print('+-------------------------------+')
                        i = 0
                        for url_found in sqli_url:
                            print('[\033[1;91m%s\033[00m] \033[1;91m%s\033[00m' % (i,url_found))
                            i = i+1
                
                else:
                    print('[!] %s not found !' % (args.urlfile))
            
            except Exception as error_urlfile:
                print(error_urlfile)
        

        elif args.google:
            try:
                check_internet()
                isearch(args.google,args.numbermax)
                for urllink in url_found:
                    check_isqli(urllink)
                
                print('+------------------------------------------+')
                print('|           URL FOUND VULNERABLE           |')
                print('+------------------------------------------+')
                i = 0
                for url_found in sqli_url:
                    print('[\033[1;91m%s\033[00m] \033[1;91m%s\033[00m' % (i,url_found))
                    i = i+1
                
                print('\033[1;92m[\033[1;94m*\033[1;92m]\033[00m Scan finish !')

            except Exception as error_google_search_args:
                print(error_google_search_args)

        else:
            print('\033[1;91m[!] Error options ! please set -h for show options !')
    
    except Exception as error_main:
        print(error_main)