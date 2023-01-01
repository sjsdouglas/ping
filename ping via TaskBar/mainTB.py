# github.com/sjsdouglas/ping
# P.I.N.G. TaskBar
# Python3.11.1
# Importações
from icons import *
from ping3 import ping
from time import sleep
from pystray import Icon, Menu, MenuItem
from threading import Thread
from tkinter import Tk


# Janela do tkinter


jan = Tk()
jan.title("P.I.N.G.")
jan.withdraw()


# Muda o ícone de acordo com o ping


loop = True


def update_icon():
    global loop
    while loop:
        try:
            ping_output = ping("google.com", unit="ms")
            print(f'\n{ping_output:4.0f}', end='')
            if ping_output == 0:
                bg = w()
            elif 0 < ping_output <= 50:
                bg = g()
            elif 50 < ping_output <= 60:
                bg = y()
            elif 60 < ping_output < 100:
                bg = o()
            elif ping_output >= 100:
                bg = r()
            icon.icon = bg  # type: ignore
        except TypeError:
            bg = w()
        sleep(1)


# Fecha o aplicativo caso o botão Sair seja pressionado


def on_clicked(icon, item):
    global loop
    if str(item) == 'Sair':
        icon.stop()
        jan.destroy()
        loop = False


# Faz o ícone mudar corretamente
if __name__ == "__main__":
    icon = Icon("P.I.N.G.", title='P.I.N.G.', menu=Menu(
        MenuItem('Sair', on_clicked)))
    icon.icon = b()
    thread = Thread(target=update_icon)
    thread.start()
    icon.run()
    jan.mainloop()
