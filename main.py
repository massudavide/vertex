import shinglesCreator
import langFinder as lf
import pageClustering
import coeffs
import maskedShingles
import signatureCreator
import numpy as np
import pandas as pd
import time
import minhash
import re



def main():

    rootdir = 'webPages/theMovieDB.org'
    # lf.lista_pagine_web(rootdir)
    mv_list = clusterizz_pagine(rootdir)
    valutazione(mv_list)

def valutazione(mv_list):
    for i in range(len(mv_list)):
        if mv_list[i][3] > 0:
            print('-----', mv_list[i][0], '-----')
            dict_value_cluster = {}
            for j in range(len(mv_list[i][2])):
                word = mv_list[i][2][j].split("\\")
                if word[1] in dict_value_cluster:
                    dict_value_cluster[word[1]] += 1
                else:
                    dict_value_cluster[word[1]] = 1
            print(dict_value_cluster)


def clusterizz_pagine(rootdir):
    t0 = time.clock()
    # df = shinglesCreator.creazione_matrice_caratteristica(rootdir)
    url_shingles = shinglesCreator.creazione_matrice_caratteristica(rootdir)
    t2 = time.clock() - t0
    print("creazione_matrice_caratteristica ---- Time elapsed: ", t2)
    t2 = time.clock()

    # df_shingles.to_csv('dfShingles_person.csv', index=False)

    # df = pd.read_csv('dfShingles_person.csv')
    # print(df.shape)
    # lista_vectors = minhash.minhash_implem(url_shingles)
    lista_vectors = minhash.minhash_implem2(url_shingles, 8)

    # df1 = signatureCreator.a(df)
    t3 = time.clock() -t2
    print("minhash.minhash_implem ---- Time elapsed: ", t3)
    t3 = time.clock()
    # df1.to_csv('prova.csv', index=False)

    # df1 = pd.read_csv('prova.csv')
    v_list, mv_list = maskedShingles.masked(lista_vectors)
    t4 = time.clock() - t3
    print("maskedShingles.masked ---- Time elapsed: ", t4)
    t4 = time.clock()

    mv_list = pageClustering.clustering_pages(lista_vectors, mv_list)
    t5 = time.clock() - t4
    print("pageClustering.clustering_pages ---- Time elapsed: ", t5)
    t5 = time.clock()

    t1 = time.clock() - t0
    print("Time elapsed: ", t1)

    # for i in range(len(mv_list)):
    #     if mv_list[i][3] > 0:
    #         print(mv_list[i][0], '\n', mv_list[i][1], '\n', mv_list[i][3], '\n', mv_list[i][2] ,'\n\n')
    return mv_list

if __name__ == "__main__":
    main()
