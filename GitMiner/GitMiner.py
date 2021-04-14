#!/usr/bin/python2
#-*- coding:utf-8 -*-

import json
import time
import threading
import platform
import logging
import os
import sys
import subprocess
import shlex

try:
    import requests
except ImportError:
    print('[*] Error Requests Module Not Found !')

try:
    from datetime import datetime
except ImportError:
    print('[*] Error Datetime Module Not Found !')

try:
    import readline
except ImportError:
    print('[*] Error Readline')

try:
    import wget
except ImportError:
    print('[*] Error Wget Module Not Found !')


try:
    from github import Github
except ImportError:
    print('[*] Error Import Github Module')

try:
    import glob
except ImportError:
    print('[*] Error Import Glob')


banner = '''
\033[1;96m
  ______ _____ _______ _______ _____ __   _ _______  ______
 |  ____   |      |    |  |  |   |   | \  | |______ |_____/
 |_____| __|__    |    |  |  | __|__ |  \_| |______ |    \_
                                                           
            
            [  \033[33mCreated By \033[31mUnam33d   \033[1;96m]
            [  \033[33mGithub : \033[31mUnam33d     \033[1;96m]
            [  \033[33mInstagram : \033[31m0x4eff   \033[1;96m]
\033[00m
'''

class SimpleCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            if text:
                self.matches = [s
                                for s in self.options
                                if s and s.startswith(text)]
                logging.debug('%s matches: %s', repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('(empty input) matches: %s', self.matches)

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s',repr(text), state, repr(response))
        return response


def check_internet():
    try:
        r = requests.get('https://google.com')
    except:
        sys.exit('\033[31m[!] Error : Internet Not Found \033[00m')

def gitbinpath():
    check_bin_git = os.path.exists('/usr/bin/git')
    if check_bin_git ==True:
        pass
    else:
        print('\033[31m[!] Git Not Found !')
        print('\033[32m[\033[34m*\033[32m] Installing Git Tools....')
        cmd = subprocess.Popen('apt update && apt install git -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        recheck_bin = os.path.exists('/usr/bin/git')
        if recheck_bin ==True:
            pass
        else:
            sys.exit('\033[31m[!] Git Not Found !\033[00m')


def clear_os():
    if 'Linux' not in platform.platform():
        os.system('cls')
    
    elif 'Windows' not in platform.platform():
        os.system('clear')


def commit_file_github(username,password,reponame):
    #login on github
    github_session = Github(username,password)
    repo = github_session.get_user().get_repo(reponame)
    input_files

def get_user_info(username):
    try:
        r = requests.get("https://api.github.com/users/%s" % (username))
        if r.status_code ==200:
            print('\033[32m[\033[1;94m+\033[32m] Status Code : 200 [OK]')
            print('\033[32m[\033[1;94m+\033[32m] Loading Informations....')
            content = r.text
            json_content = json.loads(content)
            username = json_content["login"]
            id_username = json_content["id"]
            node_id = json_content["node_id"]
            avatar_url = json_content["avatar_url"]
            url_profil = json_content["html_url"]
            type_profil = json_content["type"]
            name = json_content["name"]
            company = json_content["company"]
            blog = json_content["blog"]
            location = json_content["location"]
            email = json_content["email"]
            hireable = json_content["hireable"]
            bio = json_content["bio"]
            public_repos = json_content["public_repos"]
            public_gist = json_content["public_gists"]
            followers = json_content["followers"]
            following = json_content["following"]
            created_at = json_content["created_at"]
            updated_at = json_content["updated_at"]
            print("\033[32m[\033[1;94m+\033[32m] Username : %s" % (username))
            print("\033[32m[\033[1;94m+\033[32m] ID : %s" % (id_username))
            print("\033[32m[\033[1;94m+\033[32m] NODE_ID : %s" % (node_id))
            print("\033[32m[\033[1;94m+\033[32m] Avatar URL : %s" % (avatar_url))
            print("\033[32m[\033[1;94m+\033[32m] URL  : %s" % (url_profil))
            print("\033[32m[\033[1;94m+\033[32m] Type : %s" % (type_profil))
            print("\033[32m[\033[1;94m+\033[32m] Name : %s" % (name))
            print("\033[32m[\033[1;94m+\033[32m] Company : %s" % (company))
            print("\033[32m[\033[1;94m+\033[32m] Blog : %s" % (blog))
            print("\033[32m[\033[1;94m+\033[32m] Location : %s" % (location))
            print("\033[32m[\033[1;94m+\033[32m] Email : %s" % (email))
            print("\033[32m[\033[1;94m+\033[32m] Hireable : %s" % (hireable))
            print("\033[32m[\033[1;94m+\033[32m] Bio : %s" % (bio))
            print("\033[32m[\033[1;94m+\033[32m] Public Repos : %s" % (public_repos))
            print("\033[32m[\033[1;94m+\033[32m] Public Gist : %s" % (public_gist))
            print("\033[32m[\033[1;94m+\033[32m] Followers : %s" % (followers))
            print("\033[32m[\033[1;94m+\033[32m] Following : %s" % (following))
            print("\033[32m[\033[1;94m+\033[32m] Created At : %s" % (created_at))
            print("\033[32m[\033[1;94m+\033[32m] Updated At : %s" % (updated_at))

        elif r.status_code ==404:
            print('\033[31m[!] Error 404 Username %s Not Found !\033[00m' % (username))
    except:
        print('\033[31m[!] Error Sending Requests To API !\033[00m')


def search_username(username):
    try:
        r = requests.get('https://api.github.com/search/users?q=%s' % (username))
        if r.status_code ==200:
            print('\033[32m[\033[1;94m+\033[32m] Status Code : 200 [OK]')
            print('\033[32m[\033[1;94m+\033[32m] Loading Informations....')
            content = r.text
            json_content = json.loads(content)
            total_account_found = json_content["total_count"]
            print("\033[32m[\033[1;94m+\033[32m] Account Found : %d" % (total_account_found))
            i = 0
            while i<total_account_found:
                account_target = json_content["items"][i]
                username = account_target["login"]
                id_username = account_target["id"]
                avatar_url = account_target["avatar_url"]
                user_url = account_target["html_url"]
                type_account = account_target["type"]
                admin = account_target["site_admin"]
                print("\033[32m[\033[1;94m+\033[32m] Username : %s" % (username))
                print("\033[32m[\033[1;94m+\033[32m] ID : %s" % (id_username))
                print("\033[32m[\033[1;94m+\033[32m] Avatar : %s" % (avatar_url))
                print("\033[32m[\033[1;94m+\033[32m] Url Profile : %s" % (user_url))
                print("\033[32m[\033[1;94m+\033[32m] Admin : %s" % (admin))
                print("\033[32m[\033[1;94m+\033[32m] Type : %s" % (type_account))
                print("\n")
                i = i+1

        elif r.status_code ==404:
            print('\033[31m[!] Error 404 Username %s Not Found !\033[00m' % (username))

    except:
        print('\033[31m[!] Error Sending Requests To API !\033[00m')


def get_repos(username):
    try:
        r1 = requests.get("https://api.github.com/users/%s" % (username))
        r2 = requests.get('https://api.github.com/users/%s/repos' % (username))

        if r2.status_code ==200:
            if r1.status_code ==200:
                print('\033[32m[\033[1;94m+\033[32m] Status Code : 200 [OK]')
                print('\033[32m[\033[1;94m+\033[32m] Loading Informations....')
                content1 = r1.text
                content2 = r2.text
                json_content1 = json.loads(content1)
                public_repos = json_content1["public_repos"]
                json_content2 = json.loads(content2)
                i = 0
                while i<public_repos:
                    name = json_content2[i]["name"]
                    fullname = json_content2[i]["full_name"]
                    private = json_content2[i]["private"]
                    html_url = json_content2[i]["html_url"]
                    descriptions = json_content2[i]["description"]
                    language = json_content2[i]["language"]
                    watchers_count = json_content2[i]["watchers_count"]
                    stargazers_count = json_content2[i]["stargazers_count"]
                    created_at = json_content2[i]["created_at"]
                    updated_at = json_content2[i]["updated_at"]
                    pushed_at = json_content2[i]["pushed_at"]
                    ssh_url = json_content2[i]["ssh_url"]
                    clone_url = json_content2[i]["clone_url"]
                    archived = json_content2[i]["archived"]
                    forks_count = json_content2[i]["forks"]
                    branch = json_content2[i]["default_branch"]

                    print('\033[32m[\033[1;94m+\033[32m] Name : %s' % (name))
                    print('\033[32m[\033[1;94m+\033[32m] FullName : %s' % (fullname))
                    print('\033[32m[\033[1;94m+\033[32m] Descritpions : %s' % (descriptions))
                    print('\033[32m[\033[1;94m+\033[32m] Language : %s' % (language))
                    print('\033[32m[\033[1;94m+\033[32m] Watchers : %d' % (watchers_count))
                    print('\033[32m[\033[1;94m+\033[32m] Stargazer : %d' % (stargazers_count))
                    print('\033[32m[\033[1;94m+\033[32m] Private : %s' % (private))
                    print('\033[32m[\033[1;94m+\033[32m] HTML URL : %s' % (html_url))
                    print('\033[32m[\033[1;94m+\033[32m] Created Date : %s' % (created_at))
                    print('\033[32m[\033[1;94m+\033[32m] Updated Date : %s' % (updated_at))
                    print('\033[32m[\033[1;94m+\033[32m] Pushed Date : %s' % (pushed_at))
                    print('\033[32m[\033[1;94m+\033[32m] SSH URL : %s' % (ssh_url))
                    print('\033[32m[\033[1;94m+\033[32m] Clone URL : %s' % (clone_url))
                    print('\033[32m[\033[1;94m+\033[32m] Archived : %s' % (archived))
                    print('\033[32m[\033[1;94m+\033[32m] Forks : %s' % (forks_count))
                    print('\033[32m[\033[1;94m+\033[32m] Master Branch : %s' % (branch))
                    print('\n')
                    i = i+1
        
        elif r2.status_code ==404:
            print('\033[31m[!] Error 404 Username %s Not Found !\033[00m' % (username))
    
    except:
        print('\033[31m[!] Error Sending Requests To API !\033[00m')


def get_repos_max_defined(username,max_show):
    try:
        r1 = requests.get("https://api.github.com/users/%s" % (username))
        r2 = requests.get('https://api.github.com/users/%s/repos' % (username))

        if r2.status_code ==200:
            if r1.status_code ==200:
                print('\033[32m[\033[1;94m+\033[32m] Status Code : 200 [OK]')
                print('\033[32m[\033[1;94m+\033[32m] Loading Informations....')
                content1 = r1.text
                content2 = r2.text
                json_content1 = json.loads(content1)
                public_repos = json_content1["public_repos"]
                json_content2 = json.loads(content2)
                i = 0
                possibility = max_show<public_repos
                if possibility ==True:
                    while i<max_show:
                        name = json_content2[i]["name"]
                        fullname = json_content2[i]["full_name"]
                        private = json_content2[i]["private"]
                        html_url = json_content2[i]["html_url"]
                        descriptions = json_content2[i]["description"]
                        language = json_content2[i]["language"]
                        watchers_count = json_content2[i]["watchers_count"]
                        stargazers_count = json_content2[i]["stargazers_count"]
                        created_at = json_content2[i]["created_at"]
                        updated_at = json_content2[i]["updated_at"]
                        pushed_at = json_content2[i]["pushed_at"]
                        ssh_url = json_content2[i]["ssh_url"]
                        clone_url = json_content2[i]["clone_url"]
                        archived = json_content2[i]["archived"]
                        forks_count = json_content2[i]["forks"]
                        branch = json_content2[i]["default_branch"]

                        print('\033[32m[\033[1;94m+\033[32m] Name : %s' % (name))
                        print('\033[32m[\033[1;94m+\033[32m] FullName : %s' % (fullname))
                        print('\033[32m[\033[1;94m+\033[32m] Descritpions : %s' % (descriptions))
                        print('\033[32m[\033[1;94m+\033[32m] Language : %s' % (language))
                        print('\033[32m[\033[1;94m+\033[32m] Watchers : %d' % (watchers_count))
                        print('\033[32m[\033[1;94m+\033[32m] Stargazer : %d' % (stargazers_count))
                        print('\033[32m[\033[1;94m+\033[32m] Private : %s' % (private))
                        print('\033[32m[\033[1;94m+\033[32m] HTML URL : %s' % (html_url))
                        print('\033[32m[\033[1;94m+\033[32m] Created Date : %s' % (created_at))
                        print('\033[32m[\033[1;94m+\033[32m] Updated Date : %s' % (updated_at))
                        print('\033[32m[\033[1;94m+\033[32m] Pushed Date : %s' % (pushed_at))
                        print('\033[32m[\033[1;94m+\033[32m] SSH URL : %s' % (ssh_url))
                        print('\033[32m[\033[1;94m+\033[32m] Clone URL : %s' % (clone_url))
                        print('\033[32m[\033[1;94m+\033[32m] Archived : %s' % (archived))
                        print('\033[32m[\033[1;94m+\033[32m] Forks : %s' % (forks_count))
                        print('\033[32m[\033[1;94m+\033[32m] Master Branch : %s' % (branch))
                        print('\n')
                        i = i+1
                else:
                    print('\033[31m[!] Out Of Range List Repo ! %d<%d' % (max_show,public_repos))
        
        elif r2.status_code ==404:
            print('\033[31m[!] Error 404 Username %s Not Found !\033[00m' % (username))
    
    except:
        print('\033[31m[!] Error Sending Requests To API !\033[00m')



def search_repos(search_key):
    try:
        r = requests.get('https://api.github.com/search/repositories?q=%s' % (search_key))
        
        if r.status_code ==200:
            print('\033[32m[\033[1;94m+\033[32m] Status Code : 200 [OK]')
            print('\033[32m[\033[1;94m+\033[32m] Loading Informations....')
            content = r.text
            obj = json.loads(content)
            total_count = obj["total_count"]
            i = 0
            while i<total_count:
                repo = obj["items"][i]
                repo_name = repo["name"]
                fullname = repo["full_name"]
                html_url = repo["html_url"]
                descriptions = repo["description"]
                created_date = repo["created_at"]
                clone_url = repo["clone_url"]
                language = repo["language"]
                watchers_count = repo["watchers_count"]
                stargazers_count = repo["stargazers_count"]
                print("\033[32m[\033[1;94m+\033[32m] Repo Name : %s" % (repo_name))
                print("\033[32m[\033[1;94m+\033[32m] Full Name : %s" % (fullname))
                print("\033[32m[\033[1;94m+\033[32m] Html URL : %s" % (html_url))
                print("\033[32m[\033[1;94m+\033[32m] Descriptions : %s" % (descriptions))
                print("\033[32m[\033[1;94m+\033[32m] Language : %s" % (language))
                print("\033[32m[\033[1;94m+\033[32m] Created Date : %s" % (created_date))
                print("\033[32m[\033[1;94m+\033[32m] Clone URL : %s" % (clone_url))
                print("\033[32m[\033[1;94m+\033[32m] Watchers Count : %s" % (watchers_count))
                print("\033[32m[\033[1;94m+\033[32m] Stargazers Count : %s" % (stargazers_count))
                print("\n")
                i = i+1
        
        elif r.status_code ==404:
            print("\033[31m[!] Error 404")

    except:
        print('\033[31m[!] Error Sending Requests To API !\033[00m')


def console_main():
    clear_os()
    clear_os()
    print(banner)
    check_internet()
    gitbinpath()
    try:
        readline.set_completer(SimpleCompleter(['help','exit','clear','quit','userinfo','searchuser','banner','searchrepos','getrepos']).complete)
        readline.parse_and_bind('tab: complete')
        while True:
            try:
                t = datetime.now().strftime('%H:%M:%S')
                console_input = raw_input('\033[1;94m[\033[1;96m%s\033[1;94m]\033[1;92mGitMiner\033[1;96m@\033[1;94m%s\033[1;96m$ \033[00m' % (t,platform.node()))

                if console_input =="exit" or console_input =="quit":
                    print('\033[31m[!] Thanks For Using GitMiner Created By Unam33d')
                    break

                elif console_input.startswith('userinfo')==True:
                    split_input = shlex.split(console_input)
                    username = split_input[1]
                    try:
                        get_user_info(username)
                    except:
                        print('\033[31m[!] Error Get User !')
            
                elif console_input =="clear" or console_input =="cls":
                    clear_os()
            
                elif console_input.startswith('searchuser')==True:
                    split_input = shlex.split(console_input)
                    username = split_input[1]
                    try:
                        search_username(username)
                    except:
                        print('\033[31m[!] Error Search User !')
                
                elif console_input.startswith('getrepos')==True:
                    split_input = shlex.split(console_input)
                    if len(split_input) <3:
                        print('usage : getrepos <username> <max_show>')
                    else:
                        username = split_input[1]
                        max_show = int(split_input[2])
                        if max_show !="all":
                            get_repos_max_defined(username,max_show)
                        else:
                            try:
                                get_repos(username)
                            except:
                                print('\033[31m[!] Error Get Repository !')
                
                elif console_input.startswith("searchrepos")==True:
                    split_url = shlex.split(console_input)
                    if len(split_url) <2:
                        print("usage : searchrepos <repos>")
                    else:
                        keyword = split_url[1]
                        try:
                            search_repos(keyword)
                        except:
                            print("\033[31m[!] Error Search Repo")
            
                elif console_input =="banner":
                    print(banner)
            
                elif console_input =="help":
                    print('\033[34m[  Created By \033[33mUnam33d\033[34m - \033[33mGitMiner \033[31mVersion : 1.0\033[34m]\033[00m')
                    print("\033[34m[             Commands -> Descriptions        ]\033[00m")
                    print("userinfo <username> -> Get User Informations From Github")
                    print("searchuser <username> -> Search Account From Github")
                    print('getrepos <username> <max_show> -> if you get all repos enter "all" in <max_show> Get Repo List Of Username')
                    print('searchrepos <repos_name>  -> Search Repo On Github')

            
                else:
                    print('\033[31m[!] %s Command Not Found !' % (console_input))
            
            except KeyboardInterrupt:
                print('\033[31m[!] CTRL+C')
    
    except KeyboardInterrupt:
        print('\033[31m[!] CTRL+C')
    

if __name__ == '__main__':
    console_main()