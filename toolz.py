import requests
from typing import List

def open_usernames(fileName) -> List[str]:
    with open(fileName, 'r', encoding='UTF-8') as f:
        file_contents = [line.strip('\n') for line in f]
    return file_contents

def open_proxys(proxyName) -> List[str]:
    with open(proxyName, 'r', encoding='UTF-8') as f:
        file_contents = [line.strip('\n') for line in f]
    return file_contents

def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')

def request(username, proxy):
    url = 'https://www.tiktok.com/@' + username
    edited_proxy = {"http":proxy}
    r = requests.get(url, proxies=edited_proxy, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'})
    if 'alternateName' in r.text:
        print("[TAKEN] " + username + " | " + proxy)
    elif 'window.TTGCaptcha.render' in r.text:
        print("[RATE LIMIT / BAD PROXY] "+username + " | " + proxy)
    else:
        print("[AVAILABLE] "+username + " | " + proxy)
        write_file(username)

def intro():
    print(" _   _ _    _        _      _              _     ")
    print("| | (_) |  | |      | |    | |            | |    ")
    print("| |_ _| | _| |_ ___ | | __ | |_ ___   ___ | |____")
    print("| __| | |/ / __/ _ \| |/ / | __/ _ \ / _ \| |_  /")
    print("| |_| |   <| || (_) |   <  | || (_) | (_) | |/ / ")
    print(" \__|_|_|\_\\__\___/|_|\_\  \__\___/ \___/|_/___|")
    print("by qais#0001")
    print(" ")
    print("[+] 1. Tiktok Username checker (Proxy)")
    print("[+] 2. Tiktok AutoClaimer (Proxy)")
    print("[+] 3. Tiktok AutoClaimer (Proxyless)")
    option = input("Pick a tool ")
    if option == '1':
       usernames_txt = input("Enter Name of USERNAME list ")
       proxy_txt = input("Enter Name of PROXY list ")
       oun =  open_usernames(usernames_txt)
       opx =  open_proxys(proxy_txt)
       for x in oun:
        request(x,opx[oun.index(x)])
intro()