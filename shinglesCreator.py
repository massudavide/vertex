import re
import codecs
from window_slider import Slider
import glob, os
import pandas as pd
import numpy as np


def creazione_matrice_caratteristica(rootdir):
    df_shingles = creazione_matrice_caratteristica_aux(rootdir)
    # df_shingles = df_shingles.reset_index()
    # del[df_shingles['index']]
    return df_shingles

def creazione_matrice_caratteristica_aux(rootdir):
    shingles_df = pd.DataFrame([], [])
    pagine_list = lista_pagine_web(rootdir)
    for i in pagine_list:
        shingles_df = concat_df(i, shingles_df)
    shingles_df = shingles_df.fillna(0)
    return shingles_df

def concat_df(pagina_web, df):
    shingle_list = shingle_set(pagina_web)
    if len(shingle_list) == 0:
        return df
    df2 = pd.DataFrame(np.ones(len(shingle_list), dtype=int), columns=[pagina_web], index=shingle_list)
    df = pd.concat([df, df2], axis=1, join="outer")
    return df


def lista_pagine_web(rootdir):
    lista_pagine = []
    for file in glob.glob(f'{rootdir}/**/*.html', recursive=True):
        lista_pagine.append(file)
    # print(lista_pagine)
    return lista_pagine


def shingle_set(pagina_web):
    tag_list = regex(pagina_web)
    window_tag = tag_slider(tag_list)
    lista_shingles = list_of_shingle(window_tag)
    lista_shingles = list(dict.fromkeys(lista_shingles))
    return lista_shingles

def list_of_shingle(sequence_of_tag):
    lista_shingles = []
    for i in sequence_of_tag:
        lista_shingles.append(' '.join([str(elem) for elem in i]))
    return lista_shingles


def tag_slider(tag_list, bucket_size=10, overlap_count=9):
    window_tag = []
    tag_array = np.array(tag_list)
    if len(tag_array) < bucket_size:
        return [tag_array]
    slider = Slider(bucket_size, overlap_count)
    slider.fit(tag_array)
    while True:
        window_data = slider.slide()
        window_tag.append(window_data)
        if slider.reached_end_of_list(): return window_tag

def clean_tag(string):
    return string.split(" ")[0].replace('<', '').replace('>', '').replace('!--', '')

def remove_empty_tag(string):
    return string!="" and not string.startswith('!')

def regex(pagina_web):
    try:
        s = codecs.open(pagina_web, "r", "utf-8", errors='ignore').read()
    except:
        return []
    # s = codecs.open(pagina_web, "r", "utf-8", errors='ignore').read()
    all_tag = re.findall('<.*?>', s)

    words_list = list(map(clean_tag, all_tag))
    # print(words_list)
    words_list = list(filter(remove_empty_tag, words_list))
    return words_list