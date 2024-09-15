import pandas as pd

# Merge DataFrames
df1 = pd.DataFrame(
    {'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]} )
print(df1)
print("\n")

df2 = pd.DataFrame(
    {'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
    #index= ['val1','val2','val3'])
print(df2)
print("\n")

merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)
print("\n")
