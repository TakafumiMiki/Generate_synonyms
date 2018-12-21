import MeCab

# 入力された文字に対して形態素解析を行い単語別にする
def wakati(words):
    # m = MeCab.Tagger()
    m = MeCab.Tagger("-Ochasen")
    # m = MeCab.Tagger("-Owakati")
    # m = MeCab.Tagger("-Oyomi")
    word = m.parse(words).split("\n")
    return word

def meishi(word):
    meishi_data = []
    # meishi_datas = [i.split() for i in word if "名詞" in i]
    for i in word:
        if "名詞" in i:
            str1 = i.split()
            # str1[0]はそのままの入力文字 str1[1]はカタカナで出力
            meishi_data.append(str1[0])
    return meishi_data 

def main():
    words = "リストから項目を追加したり削除したりすること"
    # words = input("文字を入力\n")
    s = meishi(wakati(words))
    print(s)

if __name__=='__main__':
    main() 