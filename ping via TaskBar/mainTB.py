# github.com/sjsdouglas/ping
# PING_TaskBar_0.2.4.0
# Python3.11.1


# - - - - - - - - - - IMPORTS - - - - - - - - - - #


from icons import *
from ping3 import ping
from time import sleep
from pystray import Icon, Menu, MenuItem
from threading import Thread
from tkinter import Tk, ttk, Label, CENTER, Entry, Button


# - - - - - - - - - - LOG - - - - - - - - - - #


###########################################################################################
# from logging import basicConfig, DEBUG, exception, log, INFO                            #
# basicConfig(filename='.log.txt',                                                        #
#             encoding='utf-8',                                                           #
#             format=' \n ---> %(asctime)s | %(name)s | %(levelname)s | %(message)s \n ', #
#             datefmt='%H:%M:%S',                                                         #
#             level=DEBUG)                                                                #
###########################################################################################


# - - - - - - - - - - VARIABLES - - - - - - - - - - #


z = False
loop = True


# - - - - - - - - - - TKINTER - - - - - - - - - - #


# TK Config
root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("PING TaskBar - Address to be pinged")
root.wm_iconphoto(False,
                  PhotoImage(
                      file=r'C:\Users\Douglas\Documents\Python\PINGpy\ping via TaskBar\main-1.png'))
root.attributes('-topmost', 1)
posx = (root.winfo_screenwidth() / 2) - (212 / 2)
posy = (root.winfo_screenheight() / 2) - (124 / 2)
root.geometry(f'{212}x{124}+{posx:.0f}+{posy:.0f}')
root.resizable(False, False)
# TK Layout
lab_1 = Label(frm,
              text='Enter the website or IP address',
              font='Arial 10')
ent_1 = Entry(frm,
              width=30,
              justify=CENTER)
lab_2 = Label(frm,
              text=f'-',
              font='Courier 9')
btn_1 = Button(frm,
               text='OK',
               width=11,
               command=lambda: get_data())
btn_2 = Button(frm,
               text='CANCEL',
               width=11,
               command=lambda: root.destroy())
ent_1.focus_force()
# TK Grid
frm.grid()
lab_1.grid(row=0, columnspan=2)
ent_1.grid(row=1, columnspan=2, padx=4, pady=4)
lab_2.grid(row=4, columnspan=2)
btn_1.grid(row=3, column=0, padx=4, pady=4)
btn_2.grid(row=3, column=1, padx=4, pady=4)
# TK Bind
root.bind('<Return>', lambda event: get_data())
root.bind('<Escape>', lambda event: root.destroy())


# - - - - - - - - - - DEF'S - - - - - - - - - - #


def get_data():
    global ent_get
    global z
    ent_get = ent_1.get().lower()
    x = False
    if ent_get == '':
        ent_get = 'google.com'
        x = True
    elif 'https://' in ent_get:
        lab_2.config(text='Delete "https://".')
    elif 'http://' in ent_get:
        lab_2.config(text='Delete "http://".')
    elif '/' in ent_get:
        lab_2.config(text='Delete "/".')
    else:
        x = True
    if x:
        root.destroy()
        z = True
        update_icon()


def update_icon():
    global loop
    bg = None
    while loop:
        try:
            ping_output = ping(ent_get, unit="ms")
            print(f'\n{ping_output:4.0f}', end='')
            if ping_output == 0:
                bg = wi()
            elif 0 < ping_output <= 50:
                bg = g()
            elif 50 < ping_output <= 60:
                bg = y()
            elif 60 < ping_output < 100:
                bg = o()
            elif ping_output >= 100:
                bg = r()
            icon.icon = bg
        except TypeError:
            bg = wi()
        sleep(1)


def on_clicked(icon, item):
    global loop
    if str(item) == 'Exit':
        loop = False
        icon.stop()


# - - - - - - - - - - RUN - - - - - - - - - - #


if __name__ == "__main__":
    root.mainloop()
    if z:
        icon = Icon(name="PING",
                    title='PING',
                    menu=Menu(
                        MenuItem('Exit', on_clicked)))
        icon.icon = b()
        thread = Thread(target=update_icon)
        thread.start()
        icon.run()
