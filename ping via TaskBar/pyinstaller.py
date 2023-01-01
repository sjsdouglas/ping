import PyInstaller.__main__

PyInstaller.__main__.run([
    r'mainTB.py',
    r'-i=main.ico',
    '-F',
    '-w',
    '-n P.I.N.G. TB'
])
