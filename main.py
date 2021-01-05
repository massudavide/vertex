import requests
from lxml import html
import sys
import re
import urllib
import codecs
from window_slider import Slider
import numpy



def main():
    creazione_shingles()


def creazione_shingles():
    tag_list = regex()
    window_tag = tag_slider(tag_list)
    lista_shingles = list_of_shingles(window_tag)
    lista_shingles = list(dict.fromkeys(lista_shingles))
    print(lista_shingles)

def list_of_shingles(sequence_of_tag):
    lista_shingles = []
    for i in sequence_of_tag:
        lista_shingles.append(' '.join([str(elem) for elem in i]))
    return lista_shingles


def tag_slider(tag_list, bucket_size=10, overlap_count=9):
    window_tag = []
    tag_array = numpy.array(tag_list)
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

def regex():
    s = codecs.open("about.html", "r", "utf-8").read()
    all_tag = re.findall('<.*?>', s)

    words_list = list(map(clean_tag, all_tag))
    # print(words_list)
    words_list = list(filter(remove_empty_tag, words_list))
    return words_list


if __name__ == "__main__":
    main()
