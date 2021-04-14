#!/usr/bin/python3
#coding:utf-8

from googlesearch import search
import time
from datetime import datetime
import argparse
import os
import requests



banner = '''
             \033[1;96m dP""b8 \033[1;91m dP"Yb  \033[1;93m dP"Yb  \033[1;96m dP""b8 \033[1;92m88     \033[1;91m888888\033[00m
             \033[1;96mdP   `" \033[1;91mdP   Yb \033[1;93mdP   Yb \033[1;96mdP   `" \033[1;92m88     \033[1;91m88__\033[00m
             \033[1;96mYb  "88 \033[1;91mYb   dP \033[1;93mYb   dP \033[1;96mYb  "88 \033[1;92m88  .o \033[1;91m88""\033[00m
             \033[1;96m YboodP \033[1;91m YbodP  \033[1;93m YbodP  \033[1;96m YboodP \033[1;92m88ood8 \033[1;91m888888\033[00m
             
                    By Dxvistxr - Simple Google Search With Python 3
                                               2019
'''


def check_internet():
    try:
        r = requests.get('https://www.google.com')
    except:
        print('\033[1;91m[!] Error Internet Not Found !')

def isearch(query,max_stop_website):
    check_internet()
    print('\033[1;93m[*] Waiting Moment Please Search..')
    try:
        if max_stop_website ==None:
            for website in search(query, tld="co.in", num=10, stop=20, pause=2):
                t = datetime.now().strftime('%H:%M:%S')
                print('\033[1;92m[\033[1;94m%s\033[1;92m] %s ' % (t,website))

            print('\n')
            print('\033[1;92m[\033[1;94m*\033[1;92m] Search Finish At %s ' % (t))
            print('\n')
            print('\n')
        else:
            for website in search(query, tld="co.in", num=10, stop=max_stop_website, pause=2):
                t = datetime.now().strftime('%H:%M:%S')
                print('\033[1;92m[\033[1;94m%s\033[1;92m] %s' % (t,website))

            print('\n')
            print('\033[1;92m[\033[1;94m*\033[1;92m] Search Finish At %s ' % (t))
            print('\n')
            print('\n')

    except Exception as error_search:
        print(error_search)

def main():
    try:
        print(banner)
        parser = argparse.ArgumentParser()
        parser.add_argument('searchquery',type=str, help='Set Query')
        parser.add_argument('maxpage',type=int, help='Set MaxPage')
        args = parser.parse_args()
        isearch(args.searchquery,args.maxpage)

    except Exception as error_main:
        print(error_main)


if __name__ == '__main__':
    main()
