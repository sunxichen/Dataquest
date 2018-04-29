#找到所有文章标题中使用最多的100个单词
import read
import string
from collections import Counter

def combine_headlines(df):
    #将所有的headline合并为一个长string,并将String中所有单词lowercase
    s = ""
    for index, row in df.iterrows():
        s += str(row["headline"])
    return s.lower()

def split_string(s):
    #将string split成单词，并处理punctuation
    #"Helo, my name is Joe! and i live!!! in a button; factory:"
    #['Helo', ',', 'my', 'name', 'is', 'Joe', '!', 'and', 'i', 'live', '!!!',
    #  'in', 'a', 'button', ';', 'factory', ':']
    words=[]
    words = [word.strip(string.punctuation) for word in s.split()]
    return words
if __name__ == "__main__":
    hn = read.load_file()
    long_string = combine_headlines(hn)
    words = split_string(long_string)
    cnt  = Counter()
    for word in words:
        cnt[word]+=1
    print(cnt.most_common(100))

