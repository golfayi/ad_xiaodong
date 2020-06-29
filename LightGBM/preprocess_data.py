import pandas as pd
import pdb

train_path = '/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/train_preliminary/'

ad_name = 'ad.csv'
user_name = 'user.csv'
click_name = 'click_log.csv'

def get_full_sample_data():
    df_ad = pd.read_csv(train_path + ad_name, sep=',')
    print(df_ad.columns)

    df_click = pd.read_csv(train_path + click_name, sep=',')
    print(df_click.columns)

    df_user = pd.read_csv(train_path + user_name, sep=',')
    print(df_user.columns)

    df = pd.merge(df_click, df_ad, on='creative_id')
    print(df.columns)
    print(df.tail(10))
    print(df.shape)

    df = pd.merge(df, df_user, on='user_id')
    print(df.columns)
    print(df.tail(10))
    print(df.shape)
    columns = df.columns
    df.time = df.time.apply(lambda x: int(x) % 7)
    pdb.set_trace()

    df.to_csv('/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/sample_data/sample.csv', sep=',', index=None)

if __name__ == '__main__':
    get_full_sample_data()