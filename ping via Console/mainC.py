# github.com/sjsdouglas/ping
# PING_Console_0.2.3.0
# Python_3.11.1

# Importações
from time import sleep
from ping3 import ping
from os import system

# Programa
print('Enter the website or IP address you want to ping.')

while True:
    url_A = str(input(': ').lower())
    if 'https://' in url_A:
        print('Delete "https://".')
    elif 'http://' in url_A:
        print('Delete "http://".')
    elif '/' in url_A:
        print('Delete "/".')
    else:
        break

if url_A == '':
    url_A = 'google.com'

system('cls')
print(f'Pinging {url_A}...')

while True:
    try:
        p_out = ping(url_A, unit='ms')
        if p_out == 0:
            print(f'{"offline"}')
        elif p_out >= 999:
            print(f'{"999+":4}')
            print(f'\033[38;2;255;0;0m ● \033[m')
        else:
            print(f'{p_out:4.0f}', end='')
            if p_out <= 50:
                print(f'\033[38;2;0;255;0m ● \033[m')
            elif p_out <= 60:
                print(f'\033[38;2;255;255;0m ● \033[m')
            elif p_out <= 100:
                print(f'\033[38;2;255;165;0m ● \033[m')
            elif p_out >= 100:
                print(f'\033[38;2;255;0;0m ● \033[m')
    except TypeError:
        print(f'{"time out"}')
    sleep(1)
