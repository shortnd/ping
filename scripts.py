import os
import socket

changed_file = open('changed.txt', 'w')
not_changed_file = open('not_changed.txt', 'w')
error_or_other_server = open('error_or_other_server.txt', 'w')

# www_change_file = open('www_changed.txt', 'w')
# www_not_changed_file = open('www_not_changed.txt', 'w')
# www_error_or_other_server = open('www_error_or_other_server.txt', 'w')
# changed_on_both = open('changed_on_both.txt', 'w')
# changed_new_www_old = open('changed_new_www_old.txt', 'w')


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
        print(f'DNS not Changed - {no_backslash}')
        not_changed_file.write(f'DNS not Changed - {no_backslash}\n')
      elif '50.28.0.27' in response:
          print(f'On new server')
          changed_file.write(f'On new server - {no_backslash}\n')
      else:
          print('on other server')
          error_or_other_server.write(f'On different server - {no_backslash}\n')

    except:
      print(f'Error on {no_backslash}')
      error_or_other_server.write(f'Error on {no_backslash}\n')

    # no_www = no_backslash.replace('www.', '')

    # try:
    #   www_res = socket.gethostbyname(no_www)

    #   if new_server in response and new_server in www_res:
    #     print(f'both changed for - {no_backslash}')
    #     changed_on_both.write(f'DNS changed for both www and {no_www} - {no_backslash}\n')
    #   elif new_server in response and old_server in www_res:
    #     print('Changed on new not on old')
    #     changed_new_www_old.write(f'WWW not changed to new - {no_backslash}\n')
    #   elif '69.64.88.239' in www_res:
    #     print(f'DNS not Changed - {no_backslash}')
    #     www_not_changed_file.write(f'DNS not Changed - {no_backslash} - Current DNS {www_res}\n')
    #   elif '50.28.0.27' in www_res:
    #     print(f'On new server')
    #     www_change_file.write(f'On new server - {no_backslash}\n')
    #   else:
    #     print('on other server')
    #     www_error_or_other_server.write(f'On different server - {no_backslash} - Current DNS {www_res}\n')
    # except:
    #   print(f'WWW error on {no_backslash}')
