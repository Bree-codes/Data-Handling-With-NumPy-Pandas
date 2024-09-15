import pandas as pd

# Merge DataFrames
df1 = pd.DataFrame(
    {'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]} )
print(df1)

df2 = pd.DataFrame(
    {'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]} )
print(df2)

merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)

# Join DataFrames
df3 = pd.DataFrame({'value3': [7, 8]}, index=['A', 'B'])
joined_df = df1.join(df3)
print(joined_df)