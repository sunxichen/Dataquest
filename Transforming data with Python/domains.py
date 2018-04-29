#找到100个文章提交最多的domain.
import read
import pandas
from collections import Counter

def rmSubdomains(item):
    #covert blog.iweb.com to iweb.com
    #main_domain = []
    item = '.'.join(str(item).split('.')[-2:])
    return item

if __name__ == "__main__":
    hn = read.load_file()
    domains = hn["url"].apply(rmSubdomains).tolist()
    #print(domains)
    cnt = Counter(domains)
    print(cnt.most_common(100))