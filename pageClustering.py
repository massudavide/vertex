import maskedShingles
import pandas as pd
import numpy as np


def clustering_pages(lista_vectors, mv_list):
    mv_list = cluster_vectors(mv_list)
    for url in range(len(lista_vectors)):
        tupla = tuple(lista_vectors[url][1])
        for mv in mv_list:
            if maskedShingles.equal_vector(tupla, mv[0]):
                mv[2].append(lista_vectors[url][0])
                mv[3] += 1
                break
    return mv_list

# def clustering_pages(df, mv_list):
#     mv_list = cluster_vectors(mv_list)
#     for url in df.columns:
#         tupla = tuple(df[url])
#         for mv in mv_list:
#             if maskedShingles.equal_vector(tupla, mv[0]):
#                 mv[2].append(url)
#                 mv[3] += 1
#                 break
#     return mv_list
# [tupla_masked_vector, occorrenze_tuple, [lista_url], cardinalità_url]



def cluster_vectors(mv_list):
    for mv in mv_list:
        mv.append([])
        mv.append(0)
    return mv_list


