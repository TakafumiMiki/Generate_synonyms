import MeCab

class mecab():        
    # 入力された文字に対して形態素解析を行い単語別にする
    def __wakati(self,words):
        # m = MeCab.Tagger()
        m = MeCab.Tagger("-Ochasen")
        # m = MeCab.Tagger("-Owakati")
        # m = MeCab.Tagger("-Oyomi")
        word = m.parse(words).split("\n")
        return word

    def __meishi(self,word):
        meishi_data = []
        n_meishi_data = []
        # meishi_datas = [i.split() for i in word if "名詞" in i]
        for i,tango in enumerate(word):
            if "名詞" in tango:
                str1 = tango.split()
                # str1[0]はそのままの入力文字 str1[1]はカタカナで出力
                meishi_data.append(i)
                meishi_data.append(str1[0])            
            elif 'EOS' not in tango and len(tango) != 0:
                str1 = tango.split()
                # str1[0]はそのままの入力文字 str1[1]はカタカナで出力
                n_meishi_data.append(i)
                n_meishi_data.append(str1[0])
                
        return meishi_data,n_meishi_data

    def data(self,words):
        """
        入力された文字に対して形態素解析の結果と文字番号が返り値として出力されます。
        """
        m,nm = self.__meishi(self.__wakati(words))
        # 何単語目かの出力
        m_index = [m[i] for i in range(0,len(m),2)]
        nm_index = [nm[i] for i in range(0,len(nm),2)]

        #単語の出力
        m_data = [m[i] for i in range(1,len(m),2)]
        nm_data = [nm[i] for i in range(1,len(nm),2)]

        # print(m_data,nm_data)
        # print(m_index,nm_index)
        return m_data,nm_data,m_index,nm_index