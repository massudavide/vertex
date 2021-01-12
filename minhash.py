from datasketch import MinHash

def minhash_implem(df):
    list_urs_hash = []
    for col in df.columns:
        m = MinHash(num_perm=8)
        for r, row in df.iterrows():
            if df[col][r] == 1:
                m.update(r.encode('utf8'))
        list_urs_hash.append(["{0}".format(col), m.digest()])
    return list_urs_hash

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