import pandas as pd 
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value1': [1, 2, 3, 4]}) 
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value2': [5, 6, 7, 8]}) 
print("--- Combining Datasets ---") 
merged_df = pd.merge(df1, df2, on='key', how='inner') 
print("Inner merge of df1 and df2:\n", merged_df) 
print("\n--- Grouping and Aggregation ---") 
data = {'Category': ['A', 'B', 'A', 'B', 'A'], 'Value': [10, 20, 15, 25, 30]} 
df_group = pd.DataFrame(data) 
grouped_data = df_group.groupby('Category').mean() 
print("Grouped data by category, showing mean:\n", grouped_data) 