# %%
import os
import pickle

import pandas as pd


# Kaggle上と別環境でpathを切り替え
pwd = os.getcwd()
if 'working' not in pwd:
    pwd = f'{pwd}/working'
    os.chdir(pwd)
    print(f'current_dir -> {pwd}')
print(f'current_dir -> {pwd}')


# コンペによってココだけ書き換える
data_sets = {
    'train': '../input/titanic/train.csv',
    'test': '../input/titanic/test.csv',
    'gender_submission': '../input/titanic/gender_submission.csv'
}

for name, path in data_sets.items():
    df = pd.read_csv(path)
    with open(f'{name}.pickle', 'wb') as f:
        pickle.dump(df, f)
