import re
import codecs
from window_slider import Slider
import glob, os
import pandas as pd
import numpy as np


def lista_pagine_web():
    os.chdir("F:\\themoviedb\\themoviedb\www.themoviedb.org")
    for file in glob.glob("*/*.html"):
        if not find_lang(file):
            deleter(file)


def find_lang(pagina_web):
    s = codecs.open(pagina_web, "r", "utf-8").read()
    lang_en = re.findall('<html lang="en"', s)
    if len(lang_en) == 0:
        return False
    return True

def deleter(file):
    os.remove(file)