#-*- coding:utf-8 -*-

import hashlib

def md5sum(filename):
    f=open(filename,"r",encoding="cp437")
    content = f.read()
    f.close()
    h = hashlib.md5()
    h.update(content.encode("cp437"))
    hex_digest = h.hexdigest()
    return hex_digest

def md5sum_bin(filename):
    f=open(filename,"rb")
    content = f.read()
    f.close()
    h = hashlib.md5()
    h.update(content)
    hex_digest = h.hexdigest()
    return hex_digest