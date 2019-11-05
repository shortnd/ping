import os
import socket
from urllib.request import urlopen
from bs4 import BeautifulSoup

changed_file = open('changed.txt', 'w')
not_changed_file = open('not_changed.txt', 'w')
error_or_other_server = open('error_or_other_server.txt', 'w')

new_server = '3.231.123.127'
old_server_1 = '161.47.104.26'
old_server_2 = '161.47.104.27'

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
            if old_server_1 in response:
                print(f'{old_server_1} - {no_backslash}')
                not_changed_file.write(f'DNS not Changed - {no_backslash} - {old_server_1}\n')

            elif old_server_2 in response:
                print(f'{old_server_2} - {no_backslash}')
                not_changed_file.write(f'DNS not Changed - {no_backslash} - {old_server_2}\n')

            elif new_server in response:
                try:
                    target = f'http://{no_http}'
                    soup = BeautifulSoup(urlopen(target).read(), features="html.parser")
                except:
                    target = f'https://{no_http}'
                    soup = BeautifulSoup(urlopen(target).read(), features="html.parser")
                if soup.title.string:
                    if 'IIS' in soup.title.string:
                        print(f'{target} is Down - {soup.title.string}')
                        error_or_other_server.write(f'{target} is Down - {soup.title.string}\n')
                    else:
                        print(f'DNS Changed - {target} - {soup.title.string}')
                        changed_file.write(f'DNS Changed - {target} - {soup.title.string}\n')

            else:
                print(f'On other server {no_backslash}')
                error_or_other_server.write(f'On other server {no_backslash}')

        except:
            try:
                soup = BeautifulSoup(
                    urlopen(f'http://{no_backslash}/').read(), features="html.parser"
                )
                print(f'Error on {no_backslash}')
            except:
                print(f'Error on {no_backslash}')
            error_or_other_server.write(f'Error on {no_backslash}\n')
