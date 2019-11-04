import os
import socket
from urllib.request import urlopen
from bs4 import BeautifulSoup

changed_file = open('changed.txt', 'w')
not_changed_file = open('not_changed.txt', 'w')
error_or_other_server = open('error_or_other_server.txt', 'w')

new_server = '50.28.0.27'
old_server = '69.64.88.239'

with open('urls.txt', 'r') as f:
    for line in f:
        hostname = line.strip()
        if "http" in hostname:
            no_http = hostname.replace("http://", "")
        elif "https" in hostname:
            no_http = hostname.replace("https://", "")
        else:
            no_http = hostname

        if no_http.endswith('/'):
            no_backslash = no_http.rsplit('/', 1)[0]
        else:
            no_backslash = no_http

        try:
            response = socket.gethostbyname(no_backslash)
            if '69.64.88.239' in response:
                print(f'69.64.88.239 {no_backslash}')
            elif '50.28.0.27' in response:
                try:
                    soup = BeautifulSoup(urlopen(f'http://{no_http}').read(), features="html.parser")
                except:
                    soup = BeautifulSoup(urlopen(f'https://{no_http}').read(), features="html.parser")
                if soup.title.string:
                    if 'IIS' in soup.title.string:
                        print(f'{no_backslash} is Down')
                    else:
                        print(f'DNS Changed - {no_backslash}')
            else:
                print(f'On other server {no_backslash}')
        except:
            print(f'Ops')
    # for line in f:
    #     hostname = line.strip()
    #     if "http" in hostname:
    #         no_http = hostname.replace("http://", "")
    #     elif "https" in hostname:
    #         no_http = hostname.replace("https://", "")
    #     else:
    #         no_http = hostname

    #     if no_http.endswith('/'):
    #         no_backslash = no_http.rsplit('/', 1)[0]
    #     else:
    #         no_backslash = no_http

    #     try:
    #         response = socket.gethostbyname(no_backslash)

    #         if '69.64.88.239' in response:
    #             print(f'DNS not Changed - {no_backslash}')
    #             not_changed_file.write(f'DNS not Changed - {no_backslash}\n')
    #         elif '50.28.0.27' in response:
    #             try:
    #                 soup = BeautifulSoup(
    #                     urlopen('http://'+no_http).read(), features="lxml")
    #             except:
    #                 soup = BeautifulSoup(
    #                     urlopen('https://'+no_http).read(), features="lxml")
    #             if soup.title.string:
    #                 if 'IIS' in soup.title.string:
    #                     print(f'{no_backslash} is Down')
    #                     changed_file.write(
    #                         f'On new server but down - {no_backslash}')
    #                 else:
    #                     pass
    #             print(f'DNS changed - {no_backslash}')
    #             changed_file.write(f'DNS changed - {no_backslash}\n')
    #         else:
    #             print(f'on other server - {no_backslash}')
    #             error_or_other_server.write(
    #                 f'On different server - {no_backslash}\n')

    #     except:
    #         try:
    #             soup = BeautifulSoup(
    #                 urlopen('http://'+no_backslash+'/').read(), features="lxml")
    #             print(f'Error on {no_backslash}')
    #         except:
    #             print(f'Error on {no_backslash}')
    #         error_or_other_server.write(f'Error on {no_backslash}\n')
