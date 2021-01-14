from datasketch import MinHash
import coeffs
import numpy as np
import signatureCreator
import hashlib

def minhash_implem(url_shingles_list):
    list_url_hash = []
    for url in range(len(url_shingles_list)):
        m = MinHash(num_perm=8)
        shingle_list = url_shingles_list[url][1]
        for shingle in shingle_list:
            m.update(shingle.encode('utf8'))
        list_url_hash.append(["{0}".format(url_shingles_list[url][0]), m.digest()])
    return list_url_hash

def minhash_implem2(url_shingles_list, num_hash):
    lista_shingle = all_shingle_list(url_shingles_list)
    shingle_vector_dict = dict_shingle_vector(lista_shingle, num_hash)
    list_url_hash = []
    for url in range(len(url_shingles_list)):
        lista_hash = [len(url_shingles_list)] * num_hash
        shingle_list = url_shingles_list[url][1]
        for shingle in range(len(shingle_list)):
            vect = list(shingle_vector_dict[shingle_list[shingle]])
            lista_hash = signatureCreator.lista_minimi_liste(lista_hash, vect)
            # print('vect: ',vect, '\n', 'lista_hash: ', lista_hash)
        list_url_hash.append(["{0}".format(url_shingles_list[url][0]), lista_hash])
        # print('------------------> ',url_shingles_list[url][0], lista_hash, '\n\n')
    return list_url_hash


def all_shingle_list(url_shingle_list):
    s_list = []
    for i in range(len(url_shingle_list)):
        for j in range(len(url_shingle_list[i][1])):
                s_list.append(url_shingle_list[i][1][j])
    s_list = list(dict.fromkeys(s_list))
    return s_list

def dict_shingle_vector(lista_shingle, num_hash):
    lista_coeff = coeffs.get_coeffs(num_hash, len(lista_shingle))
    shingle_vector_dict = {}
    for i in range(len(lista_shingle)):
        hash_vector = []
        shingle = int(hashlib.sha1(lista_shingle[i].encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        for count in range(num_hash):
            a = lista_coeff[0][count]
            b = lista_coeff[1][count]
            c = lista_coeff[2]
            hash = ((a * shingle) + b) % c
            # hash = ((a * i) + b) % c
            hash_vector.append(hash)
        shingle_vector_dict[lista_shingle[i]] = tuple(hash_vector)
    return shingle_vector_dict

# def minhash_implem(df):
#     list_urs_hash = []
#     for col in df.columns:
#         m = MinHash(num_perm=8)
#         for r, row in df.iterrows():
#             if df[col][r] == 1:
#                 m.update(r.encode('utf8'))
#         list_urs_hash.append(["{0}".format(col), m.digest()])
#     return list_urs_hash

# def prova_minhash():
#     data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
#             'estimating', 'the', 'similarity', 'between', 'datasets']
#     data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
#             'estimating', 'the', 'similarity', 'between', 'documents']
#
#     m1, m2 = MinHash(num_perm=8), MinHash(num_perm=8)
#     for d in data1:
#         m1.update(d.encode('utf8'))
#     for d in data2:
#         m2.update(d.encode('utf8'))
#     print(m1.digest())
#     print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))
#
#     s1 = set(data1)
#     s2 = set(data2)
#     actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
#     print("Actual Jaccard for data1 and data2 is", actual_jaccard)