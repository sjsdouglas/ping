# Prjct P.I.N.G. - github.com/sjsdouglas/ping
# Python3.11.0
from time import sleep
from ping3 import ping

# - - - - - - - Configure your script - - - - - - - #
host = 'google.com'  # Choose the host.
g = 50   # Value equal to or less than for green
y = 60   # Value equal to or less than for yellow
o = 100  # Value equal to or less than for orange
r = 100  # Value greater than for red
# - - - - - - - - - - - - - - - - - - - - - - - - - #

while True:
    try:
        p_out = ping(host, unit='ms')
        if p_out == 0:
            print(f'\n{"offline"}\n', end='')
        elif p_out >= 999:  # red
            print(f'{"999+":4}', end='')
            print(f'\033[38;2;255;0;0m ● \033[m\n')
        else:
            print(f'\n{p_out:4.0f}', end='')
            if p_out <= g:
                print(f'\033[38;2;0;255;0m ● \033[m')
            elif p_out <= y:
                print(f'\033[38;2;255;255;0m ● \033[m')
            elif p_out <= o:
                print(f'\033[38;2;255;165;0m ● \033[m')
            elif p_out >= r:
                print(f'\033[38;2;255;0;0m ● \033[m')
    except TypeError:
        print(f'\n{"time out"}\n', end='')
    sleep(1)
