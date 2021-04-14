#!/usr/bin/python2
#-*- coding:utf-8 -*-

import sys
import time
import platform
import os
import json

try:
    import requests
except ImportError:
    sys.exit("\033[31m[!] Error Import Requests Module")

try:
    from datetime import datetime
except ImportError:
    sys.exit("\033[31m[!] Error Import Datetime Module")


banner = '''
\033[32m
     :::    ::: :::::::::  :::::::::: ::::::::   ::::::::  ::::    ::: 
    :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+:+:   :+:  
   +:+    +:+ +:+    +:+ +:+       +:+        +:+    +:+ :+:+:+  +:+   
  +#+    +:+ +#++:++#:  +#++:++#  +#+        +#+    +:+ +#+ +:+ +#+    
 +#+    +#+ +#+    +#+ +#+       +#+        +#+    +#+ +#+  +#+#+#     
#+#    #+# #+#    #+# #+#       #+#    #+# #+#    #+# #+#   #+#+#      
########  ###    ### ########## ########   ########  ###    ####       


                    [         \033[96mCreated By Unam3dd\033[32m        ]
                    [         Github : Unam3dd          ]

                        Username Recon\033[00m
                        \033[1;96mVersion 1.0\033[00m
'''

GLOBAL_SAVE_OUTPUT_LIST = []

def python_version():
    if sys.version[0] =="3":
        sys.exit("[*] Python2.7 Required For This Script !")


def check_internet():
    try:
        r = requests.get("https://www.google.com")
        return True
    except:
        return False


def payload_status_code(url):
    try:
        r = requests.get(url)
        if r.status_code ==200:
            return True
        else:
            return False
    except:
        return False

def payload_read_response(url,error_message):
    try:
        r = requests.get(url)
        if r.status_code ==200:
            if error_message in r.text:
                return False
            else:
                return True
        else:
            return True
    except:
        print("\033[31m[!] Error Read Data !")


def check_data_json(data_file):
    check_data_file = os.path.exists(data_file)
    if check_data_file ==True:
        return True
    else:
        return False

def search_username(username):
    with open('data.json','r') as f:
        content = f.read()
        f.close()
        obj = json.loads(content)
        i = 0
        for site in obj:
            i = i+1
        
        print("\033[32m[\033[33m!\033[32m] %d Website Loadeds in Data !" % (i))
        for site_name in obj:
            link = obj[site_name]["url"]
            try:
                error_message = obj[site_name]["errorMsg"].encode('utf-8')
                link_username = link.format(username)
                send_payload_error_message = payload_read_response(link_username,error_message)
                if send_payload_error_message ==True:
                    print("\033[32m[\033[34m+\033[32m] %s \033[34mFound !\033[00m" % (link_username))
                    GLOBAL_SAVE_OUTPUT_LIST.append(link_username)
                else:
                    print("\033[32m[\033[31m-\033[32m] %s \033[31mNot Found !\033[00m" % (link_username))
            except KeyError:
                link_username = link.format(username)
                send_payload = payload_status_code(link_username)
                if send_payload ==True:
                    print("\033[32m[\033[34m+\033[32m] %s \033[34mFound !\033[00m" % (link_username))
                    GLOBAL_SAVE_OUTPUT_LIST.append(link_username)
                else:
                    print("\033[32m[\033[31m-\033[32m] %s \033[31mNot Found !\033[00m" % (link_username))
        
        f=open('output_%s.txt' % (username),'w')
        print("\n")
        print("\n")
        print("\033[32m[\033[34m+\033[32m] ---==== Account Found ====---\033[00m")
        for LINK_SAVE in GLOBAL_SAVE_OUTPUT_LIST:
            print("\033[32m[\033[34m+\033[32m] Account : %s Found !\033[00m" % (LINK_SAVE))
            f.write(LINK_SAVE+"\n")
        
        f.close()
        check_output = os.path.exists('output_%s.txt' % (username))
        if check_output ==True:
            print("\033[32m[\033[34m+\033[32m] Output Save As output_%s.txt" % (username))
        else:
            print("\033[31m[!] Error Output Not Created !")


if __name__ == '__main__':
    python_version()
    print(banner)
    if len(sys.argv) < 2:
        print("                 usage : %s <username>\n\n                 update : %s -u\n\n" % (sys.argv[0],sys.argv[0]))
    else:
        if sys.argv[1] =="-u":
            print("\033[32m[\033[33m+\033[32m] Updating Data...")
            try:
                r = requests.get("https://raw.githubusercontent.com/Unam3dd/URecon/master/data.json")
                if r.status_code ==200:
                    check_if_data = os.path.exists("data.json")
                    if check_if_data ==True:
                        f=open('data.json','r')
                        content = f.read()
                        f.close()
                        replace_content = content.replace(content,r.text)
                        f=open('data.json','w')
                        f.write(replace_content)
                        f.close()
                        t = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
                        print("\033[32m[\033[34m+\033[32m] Data Website List Updated SuccessFully At %s" % (t))
                        f=open('data.json','r')
                        content = f.read()
                        f.close()
                        load_json_website = json.loads(content)
                        number_website = 0
                        for website_count in load_json_website:
                            number_website = number_website+1
                        print("\033[32m[\033[34m+\033[32m] %d Website Loadeds In Data !" % (number_website))
                    else:
                        f=open('data.json','w')
                        f.write(r.text)
                        f.close()
                        t = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
                        print("\033[32m[\033[34m+\033[32m] Data Website List Updated SuccessFully At %s" % (t))
                        f=open('data.json','r')
                        content = f.read()
                        f.close()
                        load_json_website = json.loads(content)
                        number_website = 0
                        for website_count in load_json_website:
                            number_website = number_website+1
                        print("\033[32m[\033[34m+\033[32m] %d Website Loadeds In Data !" % (number_website))
                else:
                    print("\033[32m[\033[31m-\033[32m] Error 404 ! Update Failed !")
            
            except:
                print("\033[32m[\033[31m-\033[32m] Exception in Update Function !")

        elif check_internet()  and check_data_json("data.json")==True:
            print("\033[32m[\033[34m+\033[32m] Internet Found !")
            t = datetime.now().strftime('%H:%M:%S')
            print("\033[32m[\033[33m?\033[32m] Search Starting At \033[33m%s\033[32m For \033[33m%s\033[00m" % (t,sys.argv[0]))
            search_username(sys.argv[1])
        else:
            sys.exit("\033[31m[!] Error Internet Not Found ! or Data Not Found !")