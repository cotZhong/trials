# import sys
# print(sys.path)
"""
Duplicated, because the data is not complete between the time horizen

"""
from tq_data_client import DBServer
client = DBServer(host='192.168.1.114', port='30300')

import pandas as pd
from tqdm import tqdm

from config import *

trading_dates = client.get_trading_dates(START_DATE, END_DATE)


def get_code_df(code: str) -> pd.DataFrame:
    df = pd.DataFrame()
    for date in trading_dates:
        url = f'{client.url_root}/dwd_tq_daily/dwd_index_1d_mkt/'
        params = {
            'start_date': START_DATE,
            'end_date': END_DATE,
            'trading_date': date,
            'wind_code': code
        }
        tmp = client.get_data(params=params, url=url)
        
        if df.empty:
            df = tmp
        else:
            df = pd.concat(
                [df, tmp],
                axis=0,
            )
    
    return df


def save_all():
    for code in tqdm(CODES):
        df = get_code_df(code)
        df.to_csv(
            r'trials/data/raw_data/CN_Index/{}.csv'.format(code),
            )
        

if __name__ == '__main__':
    save_all()