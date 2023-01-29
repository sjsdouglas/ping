import PyInstaller.__main__

PyInstaller.__main__.run([
    r'mainC.py',
    r'-i=main.ico',
    r'--version-file=versionfile.txt',
    '-F',
    '-c',
    '-nPING C'
])
