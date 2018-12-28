import w2v
import mol

def main():
    words = "今日の昼食はカレーでした"
    # positiveなら"p" negativeなら"n
    posi_or_nega = "n"
    mecab = mol.mecab()
    a,b,c,d = mecab.data(words)
    word2vec = w2v.Word_To_Vec(a,b,c,d,posi_or_nega)
    result = word2vec.w2v_data()
    print("変換前 -> " + words)
    print("変換後 -> " + result)

if __name__=='__main__':
    main()