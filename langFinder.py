import re
import codecs
from window_slider import Slider
import glob, os
import pandas as pd
import numpy as np

def file_finder(path):
    lista_pagine = lista_pagine_web(path)
    for i in lista_pagine:
        if find_lang(i):
            print(i)
            deleter(i)

# def lista_pagine_web(path):
#     os.chdir(path)
#     for file in glob.glob("*/*.html"):
#         if not find_lang(file):
#             deleter(file)
#

def lista_pagine_web(rootdir):
    lista_pagine = []
    for file in glob.glob(f'{rootdir}/**/*.html', recursive=True):
        if find_lang(file):
            print(file)
            deleter(file)


def find_lang(pagina_web):
    s = codecs.open(pagina_web, "r", "utf-8", errors='ignore').read()
    # s = codecs.open(pagina_web, "r", "utf-8").read()
    lang_en = re.findall('<html lang="en"', s)
    if len(lang_en) == 0:
        return False
    return True


def deleter(file):
    os.remove(file)