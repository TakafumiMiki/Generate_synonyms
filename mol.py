import MeCab

# 入力された文字に対して形態素解析を行い単語別にする
words = input("文字を入力")
m = MeCab.Tagger("-Owakati")
word = m.parse(words).split()
print(word)