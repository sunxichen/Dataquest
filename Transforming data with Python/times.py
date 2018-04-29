#找到提交文章最多的时间段
import read
import dateutil

def extractHour(item):
    date = dateutil.parser.parse(item)
    hour = date.hour
    return hour

if __name__ == "__main__":
    hn = read.load_file()
    hn["hour"] = hn["submission_time"].apply(extractHour)
    print(hn["hour"].value_counts())