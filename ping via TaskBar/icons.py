# github.com/sjsdouglas/ping
# P.I.N.G. TaskBar
# Python3.11.1
# Importações
from PIL import Image as img, ImageDraw as imgdrw


# Definições das cores dos ícones


def w():
    # Cria o fundo transparente de 33x33
    bg = img.new('RGBA', (33, 33), (0, 0, 0, 0))
    # Desenha o circulo no fundo transparente
    drw = imgdrw.Draw(bg)
    drw.ellipse((0, 0, 32, 32), fill=(
        255, 255, 255), outline=(0, 0, 0))
    return bg


def g():
    bg = img.new('RGBA', (33, 33), (0, 0, 0, 0))
    drw = imgdrw.Draw(bg)
    drw.ellipse((0, 0, 32, 32), fill=(
        0, 255, 0), outline=(0, 0, 0))
    return bg


def y():
    bg = img.new('RGBA', (33, 33), (0, 0, 0, 0))
    drw = imgdrw.Draw(bg)
    drw.ellipse((0, 0, 32, 32), fill=(
        255, 255, 0), outline=(0, 0, 0))
    return bg


def o():
    bg = img.new('RGBA', (33, 33), (0, 0, 0, 0))
    drw = imgdrw.Draw(bg)
    drw.ellipse((0, 0, 32, 32), fill=(
        255, 165, 0), outline=(0, 0, 0))
    return bg


def r():
    bg = img.new('RGBA', (33, 33), (0, 0, 0, 0))
    drw = imgdrw.Draw(bg)
    drw.ellipse((0, 0, 32, 32), fill=(
        255, 0, 0), outline=(0, 0, 0), width=1)
    return bg


def b():
    bg = img.new('RGBA', (33, 33), (0, 0, 0, 0))
    drw = imgdrw.Draw(bg)
    drw.ellipse((0, 0, 32, 32), fill=(
        0, 0, 0), outline=(0, 0, 0), width=1)
    return bg
