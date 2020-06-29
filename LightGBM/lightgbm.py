import pandas as pd

train_path = '/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/train_preliminary/'

ad_name = 'ad.csv'
user_name = 'user.csv'
click_name = 'click_log.csv'

df = pd.read_csv(train_path + ad_name, sep=',')
print(df.columns)
print(df.tail(5))

df = pd.read_csv(train_path + click_name, sep=',')
print(df.columns)
print(df.tail(5))

df = pd.read_csv(train_path + user_name, sep=',')
print(df.columns)
print(df.tail(5))