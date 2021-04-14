#!/usr/bin/python2
#-*- coding:utf-8 -*-

import os
import base64
import argparse


def encode_string(string):
    encoded = base64.b64encode(string.encode('UTF-16LE'))
    print(encoded)


def decode_string(encoded_string):
    decoded = base64.b64decode(encoded_string.encode('UTF-16LE'))
    print(decoded)



def encode_file(encoded_file):
    check_path = os.path.exists(encoded_file)
    if check_path ==True:
        f=open(encoded_file,'r')
        content = f.read()
        f.close()
        encoded = base64.b64encode(content.encode('UTF-16LE'))
        print(encoded)
    else:
        print('(-) %s Not Found !' % (encoded_file))


def decode_file(decode_file):
    check_path = os.path.exists(decode_file)
    if check_path ==True:
        f=open(decode_file,'r')
        content = f.read()
        f.close()
        decode = base64.b64encode(content.encode('UTF-16LE'))
        print(decode)
    else:
        print('(-) %s Not Found !' % (decode_file))


def console_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-es','--encode_string',type=str, help='Encode String To Powershell/Base64')
    parser.add_argument('-ds','--decode_string',type=str, help='Decode String Powershell/Base64 To Raw Text')
    parser.add_argument('-ef','--encode_file',type=str,help='Encode File Raw To Powershell/Base64')
    parser.add_argument('-df','--decode_file',type=str,help='Decode File Powershell/Base64 To Raw String')
    args = parser.parse_args()

    if args.encode_string:
        encode_string(args.encode_string)
    
    if args.decode_string:
        decode_string(args.decode_string)
    
    if args.encode_file:
        encode_file(args.encode_file)
    
    if args.decode_file:
        decode_file(args.decode_file)


if __name__ == '__main__':
    console_main()