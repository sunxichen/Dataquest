#读取数据
import pandas as pd

def load_file():
    hn = pd.read_csv("hn_stories.csv",names=["submission_time", "upvotes", "url", "headline"] )
    return hn

if __name__ == "__main__":
    hn = load_file()
    print(hn.head())