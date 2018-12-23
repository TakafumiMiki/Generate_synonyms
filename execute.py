import w2v
import mol

def main():
    words = "リストから項目を追加したり削除したりすること"
    mecab = mol.mecab()
    a,b,c,d = mecab.data(words)
    word2vec = w2v.Word_To_Vec(a,b,c,d)
    word2vec.w2v_data()

if __name__=='__main__':
    main()