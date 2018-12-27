import gensim

class Word_To_Vec():
    """
    word2vec.w2v_data()のみ外部から参照可能
    """
    def __init__(self,m_datas,nm_datas,m_indexes,nm_indexes,p_or_n):
        self.m_datas = m_datas
        self.nm_datas = nm_datas
        self.m_indexes = m_indexes
        self.nm_indexes = nm_indexes
        self.pn = p_or_n
    def __synonym_gene(self):        
        # 同義語の生成と同じ単語が被った時に次に似ている意味の単語を出力
        p_tango = []
        model = gensim.models.Word2Vec.load(r'w2v_model\wiki.model')
        
        for m_data in self.m_datas:
            if self.pn == "p":
                p_results = model.wv.most_similar(positive = m_data,topn = 2)
            elif self.pn == "n":
                p_results = model.wv.most_similar(negative = m_data,topn = 2)
            print(m_data)
            print(p_results)
            for p_result in p_results:
                if p_result[0] == m_data:
                    continue
                else:
                    p_tango.append(p_result[0])
                    break
        return p_tango

    def __tango_link(self,p_tango):
        # 単語と接続語を連結し、文章の作成
        bunsyo = []
        j = k = 0
        p_bunsyo = ""

        for i in range(len(self.m_datas + self.nm_datas)):
            if i in self.m_indexes:
                bunsyo.append(p_tango[j])
                j += 1

            elif i in self.nm_indexes:
                bunsyo.append(self.nm_datas[k])
                k += 1

        for bun in bunsyo:
            p_bunsyo += bun

        return p_bunsyo
    
    def w2v_data(self):
        """
        単語に対して同義語を用意し、文字番号を従って連結された文章を返す
        """
        return self.__tango_link(self.__synonym_gene())

