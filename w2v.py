import gensim
from statistics import mode

class Word_To_Vec():
    """
    word2vec.w2v_data()のみ外部から参照可能
    """
    model = gensim.models.Word2Vec.load(r'w2v_model\wiki.model')
    
    def __init__(self,m_datas,nm_datas,m_indexes,nm_indexes,p_or_n):
        self.m_datas = m_datas
        self.nm_datas = nm_datas
        self.m_indexes = m_indexes
        self.nm_indexes = nm_indexes
        self.pn = p_or_n

    def __synonym_gene(self):
        result_tango = []
        for m_data in self.m_datas:
            result_tango.append(self.counter(m_data))
            
        return result_tango

    # ここではlistの中で一番多い単語を同義語、少ないものを対義語として出力させる
    def counter(self,words):
        tango_list = self.simulation(words)
        if self.pn == "n":
            negative_list = sorted([x for x in set(tango_list) if tango_list.count(x) == 1], key=tango_list.index)
            try:
                return negative_list[0]
            except:
                return tango_list[-1]
        # 一番多いものを選択(１つもかぶりがないときに元の単語に一番近いものを出力させる)
        else:
            try:
                return mode(tango_list)
            except:
                return tango_list[0]

    # 生成された単語を3回程度繰り返す
    # ここで生成された単語が入力された単語と同じ場合は除外するようにしている
    def simulation(self,words):
        positive = []
        words1 = self.generate_synonym(words)
        for result in words1:
            words2 = self.generate_synonym(result[0])
            if result[0] != words:
                positive.append(result[0])    
            
            for result1 in words2:
                words3 = self.generate_synonym(result1[0])
                if result1[0] != words:
                    positive.append(result1[0])  
            
                for result2 in words3:
                    if result2[0] != words:
                        positive.append(result2[0])

        return positive
                
    # 似ている単語の生成
    def generate_synonym(self,words):
        word = self.model.wv.most_similar(positive = words,topn = 2)
        return word

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

