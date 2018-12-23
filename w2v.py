import gensim
import mol

words = "リストから項目を追加したり削除したりすること"
# words = input("文字を入力\n")
model = gensim.models.Word2Vec.load(r'word2vec_dict\word2vec.gensim.model')

mecab = mol.mecab()
m_datas,nm_datas,m_indexes,nm_indexes = mecab.data(words)

p_tango = []
bunsyo = []
j = k = 0

for m_data in m_datas:
    p_results = model.most_similar(m_data,topn = 1)
    for p_result in p_results:
        p_tango.append(p_result[0])

for i in range(len(m_datas + nm_datas)):
    if i in m_indexes:
        bunsyo.append(p_tango[j])
        j += 1

    elif i in nm_indexes:
        bunsyo.append(nm_datas[k])
        k += 1
p_bunsyo = ""

for bun in bunsyo:
    p_bunsyo += bun

print(p_bunsyo)

