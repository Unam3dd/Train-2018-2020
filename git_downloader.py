#!/usr/bin/python3
#-*- coding:utf-8 -*-

try:
    import os
    import requests
    import json
except Exception as error_import:
    print("[+] Import not found  : %s " % (error_import))

def get_repos(username, page):
    return requests.get("https://api.github.com/users/%s/repos?per_page=100&page=%d" % (username, page))

if __name__ == "__main__":
    x = 1
    count_repos = 1

    while True:
        r = get_repos("Unam3dd",x)
        json_object = json.loads(r.text)

        if len(json_object) == 0:
            break
        else:
            for obj in json_object:
                print("[+] PAGE : %d" % (x))
                print("[+] Count : %d" % (count_repos))
                print("[+] CLONE URL : %s" % (obj["clone_url"]))
                print("[+] Language : %s" % (obj["language"]))
                print("\n")
                os.system("git clone %s" % (obj["clone_url"]));
                count_repos += 1
            
            x += 1
