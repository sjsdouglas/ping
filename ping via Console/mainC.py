# github.com/sjsdouglas/ping
# P.I.N.G. Console
# Python3.11.1
# Importações
from time import sleep
from ping3 import ping

# Raiz
while True:
    try:
        p_out = ping('google.com', unit='ms')
        if p_out == 0:
            print(f'\n{"offline"}\n', end='')
        elif p_out >= 999:
            print(f'{"999+":4}', end='')
            print(f'\033[38;2;255;0;0m ● \033[m\n')
        else:
            print(f'\n{p_out:4.0f}', end='')
            if p_out <= 50:
                print(f'\033[38;2;0;255;0m ● \033[m')
            elif p_out <= 60:
                print(f'\033[38;2;255;255;0m ● \033[m')
            elif p_out <= 100:
                print(f'\033[38;2;255;165;0m ● \033[m')
            elif p_out >= 100:
                print(f'\033[38;2;255;0;0m ● \033[m')
    except TypeError:
        print(f'\n{"time out"}\n', end='')
    sleep(1)
