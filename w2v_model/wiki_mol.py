import MeCab
import re


m = MeCab.Tagger("-Ochasen")
file_path = r"jawiki.txt"
temp_file_path = r"wikidata.txt"
# file_path = r"f.txt"
# temp_file_path = r"result.txt"

start = re.compile(r"^<doc(\s.*)?>$")
end = re.compile(r"^</doc>$")
eng = re.compile(r"[a-zA-z]+")
symbol = re.compile(r"[!-/:-@[-`{-~]+")

def wiki_read_file():
    get_token = []
    with open(file_path, "r",encoding = "UTF-8") as f:
        for s_line in f:
            # htmlヘッダの認識
            if re.search(start,s_line) or re.search(end,s_line):
                pass
            # 英語と記号を除去したものを形態素解析する
            else:
                s_line = re.sub(eng,"",s_line)
                s_line = re.sub(symbol,"",s_line)
                get_token.extend(tokenize(s_line))    
    return get_token

def tokenize(line):
    token = []
    word = m.parse(line)
    w = word.split("\n")
    for wd in w:
        wd1 = wd.split()
        # EOSと []を除く 
        if len(wd1) > 1:
            if "名詞" in wd1[3] or "動詞" in wd1[3]: 
                token.append(wd1[0])
    return token

def main():   
    w = wiki_read_file()
    with open(temp_file_path, "w", encoding = "utf-8") as f:
        for i in w:
            f.write(str(i + " "))

main()