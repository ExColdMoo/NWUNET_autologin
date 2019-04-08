#!/usr/bin/env python
#coding:utf-8
import requests
import json
import base64
import socket

def get_session():
    url = "http://10.16.0.12:8081/portal/api/v2/session/list"
    r = requests.get(url, headers=h)
    return json.loads(r.text)["sessions"][0]["acct_unique_id"]

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def logout(session):
    url = "http://10.16.0.12:8081/portal/api/v2/session/acctUniqueId/" + session
    r = requests.delete(url,headers=h)
    if(r.status_code == 200 ):
        return True
    return False

def login(username,password):
    IP=get_host_ip()
    d = {
        "deviceType":"PC",
        "webAuthUser": username,
        "webAuthPassword": password,
        "redirectUrl":"http://10.16.0.12:8081/?usermac=00-74-9C-80-9D-35&userip="+IP+"&origurl=http://s3.cn-northwest-1.amazonaws.com.cn/captive-portal/connection-test.html?noCache=1554724964474300353&nasip=10.0.4.14",
        "type":"login"
    }
    url = "http://10.16.0.12:8081/portal/api/v2/online"
    r =  requests.post(url, data=json.dumps(d), headers=h)
    token = json.loads(r.text)["token"]
    return token


def print_format(msg):
    msg = "[***] " + msg
    print(msg)


def main():
    global h
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    h = {
        "Host": "10.16.0.12:8081",
        "User-Agent": ua,
        "Content-type": "application/json",
    }
    print("请输入校园网账号")
    username = input()
    print("请输入校园网密码")
    password = input()
    print_format("login...")
    token = login(username,password)
    h["Authorization"] = token
    print_format("Token: " + token)
    session = get_session()
    print_format("Session: "+ session)
    # if logout(session):
    #     print_format("Logout Success")
    # else:
    #     print_format("Logout Fails")

if __name__ == '__main__':
    main()