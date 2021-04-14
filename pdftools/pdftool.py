#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
import time
import platform
import os
import json

try:
    from datetime import datetime
except ImportError:
    sys.exit("[*] Exception datetime Import Error")

try:
    from googlesearch import *
except ImportError:
    sys.exit("[*] Exception googlesearch Import Error")

try:
    import wget
except ImportError:
    sys.exit("[*] Exception wget Import Error")

try:
    import requests
except ImportError:
    sys.exit("[*] Exception Requests Import Error")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("[*] Exception BeautifulSoup Import Error")

try:
    import urllib.parse
except ImportError:
    sys.exit("[*] Exception URLLIB.Parse Import Error")

try:
    import pydf
except ImportError:
    sys.exit("[*] Exception PYDF Import Error")

def check_internet():
    try:
        r = requests.get('https://www.google.com')
        return True
    except:
        return False


def check_py_version():
    if sys.version[0] == "2":
        sys.exit("[*] Please Use Python3.6.0 or + for This Script")


def check_platform():
    if 'Windows' in platform.platform():
        sys.exit("[!] Linux Required !")

def simple_search_pdf(query,number,stp):
    t = datetime.now().strftime("%H:%M:%S")
    print("[%s] Start Search For %s...." % (t,query))
    print("[*] Wait Moment Please....")
    try:
        for website in search(query,num=number,stop=stp,pause=2):
            if website.endswith(".pdf")==True:
                PDF_LIST.append(website)
            else:
                pass
        
        return PDF_LIST
    
    except Exception as error_search:
        return error_search

PDF_LIST = []


banner = '''
\033[38;5;82m
 ██▓███  ▓█████▄   █████▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██░  ██▒▒██▀ ██▌▓██   ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▓██░ ██▓▒░██   █▌▒████ ░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒██▄█▓▒ ▒░▓█▄   ▌░▓█▒  ░    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒ ░  ░░▒████▓ ░▒█░         ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒▓▒░ ░  ░ ▒▒▓  ▒  ▒ ░         ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░▒ ░      ░ ▒  ▒  ░             ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░░        ░ ░  ░  ░ ░         ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
            ░                            ░ ░      ░ ░      ░  ░      ░  
          ░                                                             
                    [ Created By Unam3dd   ]
                    [ Github  : Unam3dd    ]
                    [ Version :  0.1       ]
\033[00m
'''

if __name__ == '__main__':
    check_platform()
    check_py_version()
    print(banner)
    if len(sys.argv) < 2:
        print("usage : %s --help /-h show Help" % (sys.argv[0]))
    else:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("\n")
            print("usage : %s       | Version 0.1 By Unam3dd" % (sys.argv[0]))
            print("                         |")
            print("Basic Usage Search PDF   |")
            print("           -s <query>    | Make Simple Search PDF On Google and Download")
            print("           -num <number> | Number Of Results per page")
            print("           -stp <number> | Stop at Last Result To Retrieve")
            print("                         |")
            print("Convert WebPage To PDF   |")
            print("           -c <link>     | Get WebPage To PDF Format")
            print("                         |")
            print("                         |")
            print("Just Download PDF        |")
            print("           -d <pdflink>  | Download PDF With Dirrect Link")

        
        elif sys.argv[1] =="-s":
            query = sys.argv[2]
            if sys.argv[3] =="-num":
                number_per_page = sys.argv[4]
                if sys.argv[5] =="-stp":
                    stop_page = sys.argv[6]
                    s_search = simple_search_pdf(query+" filetype:pdf",int(number_per_page),int(stop_page))
                    #print(s_search)
                    PDF_COUNT = len(PDF_LIST)
                    print("[*] %d PDF Found ! for %s" % (PDF_COUNT,query))
                    print("\n")
                    for i,website in enumerate(PDF_LIST):
                        dec = urllib.parse.unquote_to_bytes(website)
                        t = datetime.now().strftime('%H:%M:%S')
                        print("[%d][%s] URL : %s" % (i,t,dec.decode()))
                        print("\n")

                    input_download = str(input("[*] Do You Want Download PDF ? (yes/no) >> "))
                    if input_download =="yes" or input_download.startswith("y")==True:
                        download_number = str(input("[*] Enter Number or enter ALL for download ALL PDF >> "))
                        download_pdf_count = PDF_COUNT - 1
                        if download_number =="ALL":
                            pdf = 0
                            max_pdf = download_pdf_count
                            while pdf<=max_pdf:
                                new_url = PDF_LIST[pdf]
                                dec = urllib.parse.unquote_to_bytes(new_url)
                                print("[*] Downloading ....%s" % (dec.decode()))
                                try:
                                    downloaded = wget.download(dec.decode(),out="./pdf/")
                                    if downloaded == "-1 / unknown":
                                        print("[!] Error Downloading !")
                                        pdf = pdf+1
                                    else:
                                        print("\n[*] %s Downloaded" % (downloaded))
                                        pdf = pdf+1
                                except:
                                    pdf = pdf+1
                                    pass

                            sys.exit("[*] Thanks For Using PDFTools By Unam3dd")
                        else:
                            try:
                                download_n = int(download_number)
                                new_url = PDF_LIST[download_n]
                                dec = urllib.parse.unquote_to_bytes(new_url)
                                download_url = dec.decode()
                                print("[*] Downloading .... Wait Moment Please")
                                downloaded = wget.download(download_url,out="./pdf/")
                                if downloaded == "-1 / unknown":
                                    print("[!] Error Downloaded !")
                                    sys.exit("[*] Thanks For Using PDFTools By Unam3dd")
                                else:
                                    rename_input = str(input("\n[*] Do You Want Rename File ? (yes/no) >> "))
                                    if rename_input =="yes" or rename_input.startswith("y")==True:
                                        new_filename = str(input("[*] Enter New Name : "))
                                        os.rename(downloaded,new_filename)
                                        print("[*] New Filename : %s" % (new_filename))
                                        sys.exit("[*] Thanks For Using PDFTools By Unam3dd")
                            
                                    elif rename_input =="no":
                                        sys.exit("[*] Thanks For Using PDFTools By Unam3dd")
                                
                                    else:
                                        sys.exit("[*] Invalid Options !")
                            
                            except Exception as error_download:
                                print("[!] Error %s\n" % (error_download))
                   
                    elif input_download =="no" or input_download =="n":
                        sys.exit("[*] Thanks For Using PDFTools By Unam3dd")
                    
                    else:
                        sys.exit("[!] Options is Invalid")
        

        elif sys.argv[1] =="-c":
            link=sys.argv[2]
            print("[*] Wait Moment Converting To PDF....")
            r = requests.get(link)
            if r.status_code ==200:
                print("[*] Status Code : %d" % (r.status_code))
                filename = str(input("[*] Enter Name For File >> "))
                check_filename_exists = os.path.exists(filename)
                if check_filename_exists ==False:
                    pdfwrite = pydf.generate_pdf(r.text)
                    with open(filename,"wb") as f:
                        f.write(pdfwrite)
                    
                    f.close()
                    check_output = os.path.exists(filename)
                    if check_output ==True:
                        print("[*] File Created Save As %s" % (filename))
                    else:
                        print("[*] File Error !")
                else:
                    sys.exit("[*] This File Already Exists Please Choose Other Name")

            else:
                print("[!] Error Status Code : %d" % (r.status_code))
        
        elif sys.argv[1] =="-d":
            link=sys.argv[2]
            print("[*] Wait Moment Downloading....")
            downloaded = wget.download(link,out="./pdf/")
            if downloaded == "-1 / unknown":
                print("[!] Error Download Link")
            else:
                print("[*] Downloaded !")

        else:
            print("[!] Options is Invalid")
            print("[!] Type %s -h for show help" % (sys.argv[0]))
