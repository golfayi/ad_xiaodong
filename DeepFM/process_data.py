import pandas as pd
import pdb
from sklearn.preprocessing import LabelEncoder

train_path = '/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/train_preliminary/'

ad_name = 'ad.csv'
user_name = 'user.csv'
click_name = 'click_log.csv'

def process_error_value(x):
    try:
        x = int(x)
        return x
    except:
        return -1

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
    for col in columns:
        df[col] = df[col].apply(lambda x: process_error_value(x))
        if col not in ['click_times']:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

    pdb.set_trace()
    time_num = str(1)
    click_times_num = str(1)
    creative_id_num = str(len(set(df['creative_id'].astype('str').tolist())))
    ad_id_num = str(len(set(df['ad_id'].astype('str').tolist())))
    product_id_num = str(len(set(df['product_id'].astype('str').tolist())))
    product_category_num = str(len(set(df['product_category'].astype('str').tolist())))
    advertiser_id_num = str(len(set(df['advertiser_id'].astype('str').tolist())))
    industry_num = str(len(set(df['industry'].astype('str').tolist())))
    with open('/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/sample_data/feature_sizes.txt', 'w+') as f:
        f.write(','.join([time_num, click_times_num, creative_id_num, ad_id_num, product_id_num, product_category_num, advertiser_id_num, industry_num]) + '\n')
    df = df.drop(['user_id'], axis=1)
    df.to_csv('/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/sample_data/train.txt', sep=',', index=None,
              columns=['time', 'click_times', 'creative_id', 'ad_id', 'product_id', 'product_category', 'advertiser_id', 'industry', 'gender'])
    df.to_csv('/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/sample_data/train1.txt', sep=',', index=None,
              columns=['time', 'click_times', 'creative_id', 'ad_id', 'product_id', 'product_category', 'advertiser_id', 'industry', 'age'])

if __name__ == '__main__':
    get_full_sample_data()