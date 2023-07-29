# pandas_solutions.py

import pandas as pd
import numpy as np

def create_dataframes():

    df1 = pd.DataFrame(np.random.randn(5, 5))
    
    df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    df3 = pd.read_csv('solutions/data.csv')
    
    return df1, df2, df3

def dataframe_operations(df):

    sorted_df = df.sort_values(by='B')
    
    renamed_df = df.rename(columns={'A': 'Col1'})
    
    new_df = df.assign(C=[1, 2, 3])
    
    return sorted_df, renamed_df, new_df

def indexing_slicing(df):

    subset_df = df.loc[1:3, ['A', 'B']]
    
    column = df['B']
    
    total = df['A'].sum()
    
    return subset_df, column, total

def aggregation(df):

    mean_df = df.mean()
    max_df = df.max()
    count_df = df.count()
    
    return mean_df, max_df, count_df
