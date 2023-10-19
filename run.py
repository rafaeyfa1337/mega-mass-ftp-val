import sys, os
from ftplib import FTP
from colorama import Fore, Style
from platform import system
if system() == 'Linux':
    os.system('clear')
else:
    os.system('cls')
print(f"""{Fore.YELLOW}
    __  ___                 __  ___                ________________ _    __      __
   /  |/  /__  ____ _____ _/  |/  /___ ___________/ ____/_  __/ __ \ |  / /___ _/ /
  / /|_/ / _ \/ __ `/ __ `/ /|_/ / __ `/ ___/ ___/ /_    / / / /_/ / | / / __ `/ / 
 / /  / /  __/ /_/ / /_/ / /  / / /_/ (__  |__  ) __/   / / / ____/| |/ / /_/ / /  
/_/  /_/\___/\__, /\__,_/_/  /_/\__,_/____/____/_/     /_/ /_/     |___/\__,_/_/   
            /____/ {Fore.WHITE} (c) Rafaeyfa1337 | Mass FTP Validator (host|port|username|password)
""")
targetnya = input("Please give me the list: ")
def ftp_login(host, port, username, password):
    try:
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(user=username, passwd=password)
        print(f'{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] {host}|{port}|{username}|{password} -> {Fore.GREEN}OK')
        with open('result_ftp.txt', 'a') as f:
            f.write(f'{host}|{port}|{username}|{password}\n')
        ftp.quit()
    except:
        print(f'{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] {host}|{port}|{username}|{password} -> {Fore.RED}NO')
def main():
    urllist = targetnya
    with open(urllist, 'r') as f:
        urls = f.readlines()
    for url in urls:
        url = url.strip().split('|')
        host = url[0]
        port = int(url[1])
        username = url[2]
        password = url[3]
        ftp_login(host, port, username, password)
if __name__ == '__main__':
    main()
