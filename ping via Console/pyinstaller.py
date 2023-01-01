import PyInstaller.__main__

PyInstaller.__main__.run([
    r'mainC.py',
    r'-i=main.ico',
    '-F',
    '-c',
    '-n P.I.N.G. C'
])
