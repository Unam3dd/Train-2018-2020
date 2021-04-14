#!/usr/bin/python2
#-*- coding:utf-8 -*-

import platform
import os
import sys
import json
import time

try:
    from datetime import datetime
except ImportError:
    print("\033[32m[\033[31m!\033[32m] Datetime Not Found ! Please Install Datetime")

try:
    import requests
except ImportError:
    print("\033[32m[\033[31m!\033[32m] Requests Not Found !")



banner = '''
\033[32m
_  _ ____ ____ ____ ____ ____ _  _ 
 \/  [__  |___ |__| |__/ |    |__| 
_/\_ ___] |___ |  | |  \ |___ |  | 
                                               
            
        [Author : \033[34mUnam3dd\033[32m]
        [Github : \033[34mUnam3dd\033[32m]

\033[00m
'''

def send_file_api(apikey,filename):
    try:
        check_filename = os.path.exists(filename)
        if check_filename ==True:
            url = 'https://www.virustotal.com/vtapi/v2/file/scan'
            params = {'apikey': apikey }
            files = {'file': (filename, open(filename, 'rb'))}
            response = requests.post(url, files=files, params=params)
            content = response.text
            obj = json.loads(content)
            print("\033[32m[\033[34m+\033[32m] File : %s\033[00m" % (filename))
            link = obj["permalink"]
            resource = obj["resource"]
            scan_id = obj["scan_id"]
            verbose_msg = obj["verbose_msg"]
            print("\033[32m[\033[34m+\033[32m] Link : %s\033[00m" % (link))
            print("\033[32m[\033[34m+\033[32m] Message : %s\033[00m" % (verbose_msg))
            send_requests_api(apikey,resource)
        else:
            print("\033[31m[!] Error File Not Found !")
    except:
        print("\033[31m[!] Send File API Error !")



def send_url_api(apikey,url):
    try:
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': apikey, 'resource':url}
        response = requests.get(url,params=params)
        obj = json.loads(response.text)
        scan_date = obj["scan_date"]
        verbose_msg = obj["verbose_msg"]
        detect_av = obj["positives"]
        total_av = obj["total"]
        print("\033[32m[\033[34m*\033[32m] URL : %s" % (url))
        print("\033[32m[\033[34m*\033[32m] Scan Date : %s" % (scan_date))
        print("\033[32m[\033[34m*\033[32m] Message : %s" % (verbose_msg))
        print("\033[32m[\033[34m*\033[32m] AV Detection : %d/%d" % (detect_av,total_av))
        for av_name in obj["scans"]:
            print("\033[32m[\033[34m*\033[32m] AV Name : %s\033[00m" % (av_name))
            detected = obj["scans"][av_name]["detected"]
            results = obj["scans"][av_name]["result"]
            if detected ==True:
                print("\033[32m[\033[34m*\033[32m] Detected : \033[31m%s\033[00m" % (detected))
                print("\033[32m[\033[34m*\033[32m] Results  : \033[31m%s\033[00m" % (results))
                print("\n")
            else:
                print("\033[32m[\033[34m*\033[32m] Detected : \033[32m%s\033[00m" % (detected))
                print("\033[32m[\033[34m*\033[32m] Results  : \033[32m%s\033[00m" % (results))
                print("\n")
    
    except Exception as error_send_url_api:
        print(error_send_url_api)

def send_requests_api(apikey,hashfile):
    r = requests.get("https://www.virustotal.com/vtapi/v2/file/report?apikey=%s&resource=%s&allinfo=true" % (apikey,hashfile))
        
    if r.status_code ==200:
        content = r.text
        obj = json.loads(content)
        scan_id = obj["scan_id"]
        sha1_hash = obj["sha1"]
        resource = obj["resource"]
        response_code = obj["response_code"]
        scan_date = obj["scan_date"]
        scan_link = obj["permalink"]
        scan_finish = obj["verbose_msg"]
        sha256_hash = obj["sha256"]
        detect_av = obj["positives"]
        total_av = obj["total"]
        md5_hash = obj["md5"]

        print("\033[32m[\033[34m+\033[32m] Scan ID   : %s\033[00m" % (scan_id))
        print("\033[32m[\033[34m+\033[32m] SHA1 HASH : %s\033[00m" % (sha1_hash))
        print("\033[32m[\033[34m+\033[32m] Resource  : %s\033[00m" % (resource))
        print("\033[32m[\033[34m+\033[32m] Code      : %s\033[00m" % (response_code))
        print("\033[32m[\033[34m+\033[32m] Scan Date : %s\033[00m" % (scan_date))
        print("\033[32m[\033[34m+\033[32m] Link      : %s\033[00m" % (scan_link))
        print("\033[32m[\033[34m+\033[32m] SHA256 HASH : %s\033[00m" % (sha256_hash))
        print("\033[32m[\033[34m+\033[32m] Detected AV : %d/%d\033[00m" % (detect_av,total_av))
        print("\033[32m[\033[34m+\033[32m] md5 HASH    : %s\033[00m" % (md5_hash))

        for av_name in obj["scans"]:
            t = datetime.now().strftime("%H:%M:%S")
            print("\033[32m[\033[34m%s\033[32m] AV - NAME : \033[34m%s\033[00m" % (t,av_name))
            av_detect = obj["scans"][av_name]["detected"]
            av_version = obj["scans"][av_name]["version"]
            av_results = obj["scans"][av_name]["result"]
            av_update = obj["scans"][av_name]["update"]
            if av_detect ==True:
                print("\033[32m[\033[34m%s\033[32m] Detected  : \033[31m%s\033[00m" % (t,av_detect))
                print("\033[32m[\033[34m%s\033[32m] Version   : \033[33m%s\033[00m" % (t,av_version))
                print("\033[32m[\033[34m%s\033[32m] Results   : \033[31m%s\033[00m" % (t,av_results))
                print("\033[32m[\033[34m%s\033[32m] AV-Update : \033[31m%s\033[00m" % (t,av_update))
                print("\n")
            else:
                print("\033[32m[\033[34m%s\033[32m] Detected  : \033[32m%s\033[00m" % (t,av_detect))
                print("\033[32m[\033[34m%s\033[32m] Version   : \033[33m%s\033[00m" % (t,av_version))
                if av_results ==None:
                    print("\033[32m[\033[34m%s\033[32m] Results   : no malicious charge for %s\033[00m" % (t,av_name))
                else:
                    print("\033[32m[\033[34m%s\033[32m] Results : %s\033[00m" % (t,av_name))
                
                print("\033[32m[\033[34m%s\033[32m] AV-Update : \033[33m%s\033[00m" % (t,av_update))
                print("\n")
        
        print("\033[32m[\033[34m*\033[32m] Scan ID : %s" % (scan_finish))
    else:
        print("\033[31m[!] 404 Error HashFile Not Found : %s" % (hashfile))

def clear_os():
    if 'Linux' not in platform.platform():
        os.system('cls')
    
    elif 'Windows' not in platform.platform():
        os.system('clear')

if __name__ == '__main__':
    print(banner)
    if len(sys.argv) < 4:
        print("\033[32musage : %s <api_key> -f <filename> \033[00m" % (sys.argv[0]))
        print("\033[32musage : %s <api_key> -h <hash> \033[00m" % (sys.argv[0]))
        print("\033[32musage : %s <api_key> -hh <hash_list> \033[00m" % (sys.argv[0]))
        print("\033[32musage : %s <api_key> -u  <url> \033[00m" % (sys.argv[0]))
        print("\033[32musage : %s <api_key> -uu <url_list> \033[00m" % (sys.argv[0]))

    else:
        clear_os()
        print(banner)
        
        if sys.argv[2] == "-f":
            t = datetime.now().strftime("%H:%M:%S")
            print("\033[32m[\033[34m%s\033[32m] Starting Scan..." % (t))
            send_file_api(sys.argv[1],sys.argv[3])

            
        elif sys.argv[2] == "-h":
            t = datetime.now().strftime("%H:%M:%S")
            print("\033[32m[\033[34m%s\033[32m] Starting Scan..." % (t))
            send_requests_api(sys.argv[1],sys.argv[3])
        
        elif sys.argv[2] == "-hh":
            t = datetime.now().strftime("%H:%M:%S")
            print("\033[32m[\033[34m%s\033[32m] Starting Scan...." % (t))
            check_file = os.path.exists(sys.argv[3])
            if check_file ==True:
                f = open(sys.argv[3],'r')
                content = f.readlines()
                for line in content:
                    line = line.rstrip()
                    send_requests_api(sys.argv[1],line)
                f.close()
            
        elif sys.argv[2] == "-u":
            t = datetime.now().strftime("%H:%M:%S")
            print("\033[32m[\033[34m%s\033[32m] Starting Scan...." % (t))
            send_url_api(sys.argv[1],sys.argv[3])
            
        elif sys.argv[2] == "-uu":
            t = datetime.now().strftime("%H:%M:%S")
            print("\033[32m[\033[34m%s\033[32m] Starting Scan...." % (t))
            check_file = os.path.exists(sys.argv[3])
            if check_file ==True:
                f=open(sys.argv[3],"r")
                content = f.readlines()
                for line in content:
                    line = line.rstrip()
                    send_url_api(sys.argv[1],sys.argv[3])
            else:
                print("\033[31m[!] %s Not Found !" % (sys.argv[3]))
        else:
            print("\033[31m[!] Index Error !")
