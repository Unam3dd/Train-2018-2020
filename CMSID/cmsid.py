#!/usr/bin/python3
#-*- coding:utf-8 -*-

import time
from datetime import datetime
import requests
import json
import argparse
import sys
import platform
import shutil
import os
import random


banner_font = '''

     Author : Dxvistxr
     CMS Identificator With API => \033[1;96mhttps://whatcms.org\033[00m
     2019

 '''

def check_platform():
    if 'Linux' not in platform.platform():
        sys.exit('[*] Linux Required !')

def check_python_version():
    version_py = sys.version[0]
    if '3' not in version_py:
        print(banner_font)
        sys.exit('\033[1;91m[*] Please Run cmsid.py with python3')

def check_internet():
    try:
        print('[*] Checking Internet Connection...')
        check_internet = requests.get('https://www.google.com')
        print('[*] Internet : \033[1;92mFound !')

    except Exception as error_internet:
        print('[*] Internet Not \033[1;91mFound !')
        sys.exit('\033[1;91m[!] Exiting')


def send_requests(key,target):
    try:
        check_internet()
        r = requests.get('https://whatcms.org/APIEndpoint/Detect?key=%s&url=%s' % (key,target))
        content_requests = r.text
        obj = json.loads(content_requests)
        req = obj['request']
        req_web = obj['request_web']
        code = obj['result']['code']
        msg = obj['result']['msg']
        id = obj['result']['id']
        name = obj['result']['name']
        confidence = obj['result']['confidence']
        cms_url = obj['result']['cms_url']
        t = datetime.now().strftime('%H:%M:%S')
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;96m Requests Sent At \033[1;92m%s\033[00m' % (t))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;93mRequests SuccessFull !\033[00m')
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mRequest : \033[1;96m%s' % (req))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mRequests Web : \033[1;96m%s' % (req_web))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mStatus Code : \033[1;96m%s' % (code))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mCMS Status : \033[1;96m%s' % (msg))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mID Status : \033[1;96m%s' % (id))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mCMS Name : \033[1;96m%s' % (name))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mConfidence : \033[1;96m%s' % (confidence))
        print('\033[1;92m[\033[1;94m*\033[1;92m] \033[1;92mCMS URL : \033[1;96m%s\033[00m' % (cms_url))

    except Exception as error_send_requests:
        print(error_send_requests)


def banner_show():
    try:
        check_cowsay = shutil.which('cowsay')
        if check_cowsay ==None:
            print('\033[1;91m[!] Cowsay Not Found !')
            os.system('apt update && apt install cowsay -y')
            os.system('cowsay CMS ID V1.0 By Dxvistxr')
        else:
            theme1 = 'cowsay CMS ID v1.0'
            theme2 = 'cowsay -f eyes CMS ID v1.0'
            theme3 = 'cowsay -f tux CMS ID v1.0'
            theme4 = 'cowsay -f bud-frogs CMS ID v1.0'
            choice_banner = [theme1,theme2,theme3,theme4]
            random_choice_banner = random.choice(choice_banner)
            if random_choice_banner ==theme1:
                os.system(random_choice_banner)
                print(banner_font)

            elif random_choice_banner ==theme2:
                os.system(random_choice_banner)
                print(banner_font)

            elif random_choice_banner ==theme3:
                os.system(random_choice_banner)
                print(banner_font)

            elif random_choice_banner ==theme4:
                os.system(random_choice_banner)
                print(banner_font)

    except Exception as error_banner:
        print(error_banner)


def main():
    check_platform()
    check_python_version()
    banner_show()
    parser = argparse.ArgumentParser()
    parser.add_argument('key',type=str,help='Set API Key')
    parser.add_argument('url',type=str,help='Set Target Url')
    args = parser.parse_args()
    send_requests(args.key,args.url)


if __name__ == '__main__':
    main()
