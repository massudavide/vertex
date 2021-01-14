import numpy as np
import pandas as pd
import coeffs



def a(df, num_hash=8):

    lista_coeff = coeffs.get_coeffs(num_hash, len(df.index))

    df2 = pd.DataFrame()
    col_hash = []
    for i in range(num_hash):
        col_hash.append("h{0}".format(i))
        df2["h{0}".format(i)] = list(range(len(df.index)))


    count = 0
    for i in df2.columns:
        a = lista_coeff[0][count]
        b = lista_coeff[1][count]
        c = lista_coeff[2]
        df2[i] = list(map(lambda x: ((a * x) + b) % c, df2[i]))
        count += 1

    df3 = pd.DataFrame(np.full((len(col_hash), len(df.columns)), lista_coeff[2]), columns=df.columns,
                       index=col_hash)

    # for c in df.columns:
    #     for r, row in df.iterrows():
    #         if df[c][r] == 1:
    #             lista_hash = df2.T[r]
    #             lista_df3 = df3[c]
    #             df3[c] = lista_minimi_liste(lista_hash, lista_df3)
    #             print(df3[c])

    for c in df.columns:
        lista_elem_colonna = df[c]
        for r in range(len(lista_elem_colonna)):
            if lista_elem_colonna[r] == 1:
                lista_hash = df2.T[r]
                lista_df3 = df3[c]
                df3[c] = lista_minimi_liste(lista_hash, lista_df3)
    return df3


def lista_minimi_liste(list1, list2):
    lista_di_minimi = []
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            lista_di_minimi.append(list1[i])
        else:
            lista_di_minimi.append(list2[i])
    return lista_di_minimi