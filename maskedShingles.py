import numpy as np
import pandas as pd
from operator import itemgetter

def masked(url_hash_list):
    # df = esempio()
    dict = create_masked_shingles(url_hash_list)
    v_list, mv_list = split_shingle_vect(dict)
    v_list, mv_list = decrease_masked_vector(v_list, mv_list)
    v_list, mv_list = delete_under_threshold(v_list, mv_list)
    return v_list, mv_list

def delete_under_threshold(v_list, mv_list, soglia=20):
    new_v_list = []
    new_mv_list = []
    for v in v_list:
        if v[1] > soglia:
            new_v_list.append(v)

    for mv in mv_list:
        if mv[1] > soglia:
            new_mv_list.append(mv)

    new_v_list = sort_list_over_value(new_v_list)
    new_mv_list = sort_list_over_value(new_mv_list, True)
    return new_v_list, new_mv_list


def decrease_masked_vector(v_list, mv_list):
    v_list = sort_list_over_value(v_list)
    for v in v_list:
        mv_list = sort_list_over_value(mv_list, True)
        bool = False
        for mv in mv_list:
            if not bool and equal_vector(v[0], mv[0]):
                bool = True
                continue
            if bool and equal_vector(v[0], mv[0]):
                mv[1] -= 1
    sort_list_over_value(mv_list, True)
    return v_list, mv_list

def create_masked_shingles(url_hash_list):
    masked_shigle_dict = {}
    for col in url_hash_list:
        col_list = col[1]
        if tuple(col_list) in masked_shigle_dict:
            masked_shigle_dict[tuple(col_list)] += 1
        else:
            masked_shigle_dict[tuple(col_list)] = 1
        for i in range(len(col_list)):
            col_list1 = list(col_list)
            col_list1[i] = '*'
            if tuple(col_list1) in masked_shigle_dict:
                masked_shigle_dict[tuple(col_list1)] += 1
            else:
                masked_shigle_dict[tuple(col_list1)] = 1
            for j in range(i+1, len(col_list)):
                col_list2 = list(col_list1)
                col_list2[j] = '*'
                if tuple(col_list2) in masked_shigle_dict:
                    masked_shigle_dict[tuple(col_list2)] += 1
                else:
                    masked_shigle_dict[tuple(col_list2)] = 1
    return masked_shigle_dict

# def create_masked_shingles(df):
#     masked_shigle_dict = {}
#     for col in df.columns:
#         col_list = df[col]
#         if tuple(df[col]) in masked_shigle_dict:
#             masked_shigle_dict[tuple(df[col])] += 1
#         else:
#             masked_shigle_dict[tuple(df[col])] = 1
#         for i in range(len(col_list)):
#             col_list1 = list(col_list)
#             col_list1[i] = '*'
#             if tuple(col_list1) in masked_shigle_dict:
#                 masked_shigle_dict[tuple(col_list1)] += 1
#             else:
#                 masked_shigle_dict[tuple(col_list1)] = 1
#             for j in range(i+1, len(col_list)):
#                 col_list2 = list(col_list1)
#                 col_list2[j] = '*'
#                 if tuple(col_list2) in masked_shigle_dict:
#                     masked_shigle_dict[tuple(col_list2)] += 1
#                 else:
#                     masked_shigle_dict[tuple(col_list2)] = 1
#     return masked_shigle_dict


def sort_list_over_value(list_v_mv, rev=False):
    return sorted(list_v_mv, key=itemgetter(1), reverse=rev)

def split_shingle_vect(shingle_dict):
    v_list = []
    mv_list = []
    for key, value in shingle_dict.items():
        if find_wildcard(key):
            mv_list.append([key, value])
        else:
            v_list.append([key, value])
    return v_list, mv_list

def find_wildcard(tupla):
    if '*' in tupla:
        return True
    return False

def equal_vector(v1, v2):
    for i in range(len(v1)):
        if v1[i] != v2[i] and not (v1[i] == '*' or v2[i] == '*'):
            return False
    return True

def esempio():
    return pd.DataFrame({'A': [0,0,0,0,0,1,2,4], 'B': [0,0,0,0,0,1,5,3], 'C': [0,0,0,0,0,6,2,3]})

