"""
Split all raw_data into train, valid, test 
"""
import pandas as pd
from tqdm import tqdm

from config import *


def read_data() -> pd.DataFrame:
    df = pd.DataFrame()
    
    for code in CODES:
        tmp = pd.read_csv(
            r'trials/data/raw_data/CN_Index/{}.csv'.format(code),
            index_col=0,
        )
        tmp.columns = [[code] * len(list(tmp.columns)), list(tmp.columns)]
        
        if df.empty:
            df = tmp 
        else:
            assert len(df) == len(tmp)
            df = pd.concat([df, tmp], axis=1)
            
    return df


def split_data(
    df: pd.DataFrame, 
    split_valid: int, 
    split_test: int,
    ) -> pd.DataFrame:
    
    train = df[: len(df) - split_valid - split_test]
    valid = df[len(df) - split_valid - split_test: len(df) - split_test]
    test = df[len(df) - split_test: ]
    
    train.to_csv(
        r'/home/melonbread404/trials/trials/data/CN_Index/train_rolling_1.csv'
    )
    valid.to_csv(
        r'/home/melonbread404/trials/trials/data/CN_Index/valid_rolling_1.csv'
    )
    test.to_csv(
        r'/home/melonbread404/trials/trials/data/CN_Index/test_rolling_1.csv'
    )
    

def main():
    df = read_data()
    split_data(df, SPLIT_VALID, SPLIT_TEST)
    

if __name__ == '__main__':
    main()