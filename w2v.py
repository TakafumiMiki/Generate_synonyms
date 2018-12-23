import gensim
import mol

model = gensim.models.Word2Vec.load(r'word2vec_dict\word2vec.gensim.model')

m_datas,nm_datas,m_indexes,nm_indexes = mol.data()

p_results = []
bunsyo = []
j = k = 0

for m_data in m_datas:
    p_results.append(model.most_similar(m_data,topn = 1))

# 元の文章を表現
# 同じ表現の単語(p_result)を m_datasに置き換える

# for i in range(len(m_datas + nm_datas)):
#     if i in m_indexes:
#         bunsyo.append(m_datas[j])
#         j += 1

#     elif i in nm_indexes:
#         bunsyo.append(nm_datas[k])
#         k += 1

# print(bunsyo)
