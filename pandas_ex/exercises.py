# pandas_exercises.py

import pandas as pd


def create_dataframes():
    """
    Create sample Pandas DataFrames for manipulating.
    
    Returns
    -------
    df1: DataFrame of shape (5, 5)
        DataFrame with random normal values
    df2: DataFrame
        DataFrame created from dict of lists
    df3: DataFrame
        DataFrame read from CSV file
    """
    
    # TODO: Create random normal DataFrame
    df1 = None
    
    # TODO: Create DataFrame from dict of dicts
    df2 = None 
    
    # TODO: Read DataFrame from CSV
    df3 = None
    
    return df1, df2, df3


def dataframe_operations(df):

    """
    Perform operations like sorting, renaming, adding columns.
    
    Parameters
    ----------
    df : DataFrame
        Input DataFrame
        
    Returns
    -------
    sorted_df : DataFrame
        Original DataFrame sorted by column 'B'
    renamed_df : DataFrame
        DataFrame with column 'A' renamed to 'Col1'
    new_df : DataFrame
        Original DataFrame with new column 'C'
        
    TODO: Sort DataFrame by column 'B'
    TODO: Rename column 'A' to 'Col1'
    TODO: Add new column 'C' with values [1, 2, 3]
    """
    
    sorted_df = None
    renamed_df = None
    new_df = None
    
    return sorted_df, renamed_df, new_df


def indexing_slicing(df):
    """
    Exercises for indexing and slicing DataFrame.
    
    Parameters
    ----------
    df : DataFrame 
        Input DataFrame
        
    Returns
    -------
    subset_df : DataFrame
        DataFrame sliced to rows 1-3 and columns 'A' and 'B' 
    column : Series
        Series containing column 'B'
    total : float
        Total of column 'A'
    
    TODO: Slice df to rows 1-3 and cols 'A' and 'B'
    TODO: Select column 'B'
    TODO: Get total of column 'A'
    """
    
    subset_df = None
    column = None
    total = None
    
    return subset_df, column, total


def aggregation(df):
    """
    Apply aggregate functions to DataFrame.
    
    Parameters
    ----------
    df : DataFrame
        Input DataFrame
        
    Returns
    -------
    mean_df : Series
        Mean of each column
    max_df : Series
        Max of each column
    count_df : Series
        Count of each column
        
    TODO: Get mean of each column
    TODO: Get max of each column
    TODO: Get count of each column
    """
    
    mean_df = None
    max_df = None
    count_df = None
    
    return mean_df, max_df, count_df

