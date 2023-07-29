#%%
# Pandas Introduction

import pandas as pd

# Creating DataFrames

# DataFrames are like tables in SQL
data = {'Apples': [30], 'Bananas': [21]}  
df = pd.DataFrame(data)
print(df)

#%%
# Can provide column names
data = [['John', 24], ['Mary', 28], ['Peter', 31], ['Tracy', 19]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

#%%
# Reading CSV is like SELECT * FROM table in SQL 
df = pd.read_csv('data.csv')
print(df.head())

#%%
# DataFrame attributes 

print(df.shape) # Number of rows and columns
print(df.dtypes) # Column types (like SQL data types)

#%%
# Selecting columns - Similar to SELECT col1, col2 FROM table

print(df['Name'])  
print(df.Name)

#%%
# Selecting rows - Similar to WHERE clause

print(df.loc[0])  
print(df.loc[[0, 1]]) 

#%%
# Filtering - Similar to WHERE

filter1 = df.Age > 20  
filter2 = df.Age < 25
filtered_df = df[filter1 & filter2] 
print(filtered_df)

#%%
# Grouping and aggregation - Similar to GROUP BY and aggregate funcs in SQL

grouped = df.groupby('Name') 
aggregated = grouped['Age'].agg([min, max, len]) 
print(aggregated)
#%%
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(1000000, 5), columns=list('ABCDE'))

# Apply
start = time.time()
df.apply(np.mean) 
end = time.time()
print(f'Time taken for apply: {end - start}')

# For loop
start = time.time()
for col in df.columns:
    df[col].mean()
end = time.time()
print(f'Time taken for for loop: {end - start}')
# %%
