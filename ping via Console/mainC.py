# github.com/sjsdouglas/ping
# PING_Console_0.2.3.0
# Python_3.11.1

# Importações
from time import sleep
from ping3 import ping
from os import system

# URL ou IP para pingar
print('Enter the website or IP address you want to ping.')
url_A = str(input(': '))
system('cls')
print(f'Pinging {url_A}...')

# Programa
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
