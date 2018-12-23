import w2v
import mol

def main():
    words = "与えられた文章に対して似た意味と反対の意味を持つ文章を返す"
    posi_or_nega = "p"
    mecab = mol.mecab()
    a,b,c,d = mecab.data(words)
    word2vec = w2v.Word_To_Vec(a,b,c,d,posi_or_nega)
    result = word2vec.w2v_data()
    print("変換前 -> " + words)
    print("変換後 -> " + result)

if __name__=='__main__':
    main()