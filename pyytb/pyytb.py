#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import time
import os

try:
    from pytube import YouTube
except ImportError:
    print("[*] Error Pytube Not Found !")


banner = '''
\033[32m
    ___  _   _ ___ ___  
   |__]  \_/   |  |__] 
   |      |    |  |__] 
                    
    [ Github : \033[31mUnam3dd\033[32m ]
    [ Author : \033[31mUnam3dd\033[32m ]

\033[00m
'''

def get_youtube_mp4(link):
    print("\033[32m[\033[34m+\033[32m] Video : %s" % (link))
    yt = YouTube(link)
    title = yt.title
    author = yt.author
    descriptions = yt.description
    stream = yt.streams.filter(file_extension='mp4').all()[0]
    print("\033[32m[\033[34m+\033[32m] Title : %s" % (title))
    print("\033[32m[\033[34m+\033[32m] Author : %s" % (author))
    print("\033[32m[\033[34m+\033[32m] Descriptions : %s\n" % (descriptions))
    print("\033[32m[\033[34m+\033[32m] Downloading %s\n" % (title))
    downloaded = stream.download()
    print("\033[32m[\033[34m+\033[32m] Save As %s " % (downloaded))

def get_youtube_mp3(link):
    print("\033[32m[\033[34m+\033[32m] Video : %s" % (link))
    yt = YouTube(link)
    title = yt.title
    author = yt.author
    descriptions = yt.description
    stream = yt.streams.filter(only_audio=True).all()[0]
    print("\033[32m[\033[34m+\033[32m] Title : %s" % (title))
    print("\033[32m[\033[34m+\033[32m] Author : %s" % (author))
    print("\033[32m[\033[34m+\033[32m] Descriptions : %s\n" % (descriptions))
    print("\033[32m[\033[34m+\033[32m] Downloading %s\n" % (title))
    downloaded = stream.download()
    split_downloaded = downloaded.split(".mp4")[0]
    split_downloaded = split_downloaded+".mp3"
    os.rename(downloaded,split_downloaded)
    print("\033[32m[\033[34m+\033[32m] Save As %s " % (split_downloaded))


if __name__ == '__main__':
    print(banner)
    if len(sys.argv) < 3:
        print("usage : %s <youtube_link> <video/audio>\n\n" % (sys.argv[0]))
    else:
        if sys.argv[2] =="video":
            get_youtube_mp4(sys.argv[1])
        
        elif sys.argv[2] =="audio":
            get_youtube_mp3(sys.argv[1])
        
        else:
            print("[Error Format !]")