# test_pandas_exercises.py

import pandas as pd
import pandas_ex.exercises as ex
# import solutions.solution_pandas as ex

# Fixtures
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]}) 
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [4, 5, 6, 7, 8]})
df3 = pd.read_csv('test/data.csv')

def test_create_dataframes():
    df1, df2, df3 = ex.create_dataframes()
    
    assert len(df1.columns) == 5 
    assert df1.shape == (5, 5)
    assert isinstance(df2, pd.DataFrame)
    assert isinstance(df3, pd.DataFrame)

def test_dataframe_operations():
    sorted, renamed, newcol = ex.dataframe_operations(df)
    
    assert sorted.iloc[0, 1] == 4
    assert renamed.columns[0] == 'Col1' 
    assert 'C' in newcol.columns

def test_indexing_slicing():
    subdf, colB, total = ex.indexing_slicing(df)
    
    assert subdf.shape == (3, 2)
    assert colB.name == 'B'
    assert total == 15

def test_aggregation():
    mean, max, count = ex.aggregation(df)
    
    assert mean.loc['A'] == 2
    assert max.loc['B'] == 6
    assert count.loc['A'] == 3
    