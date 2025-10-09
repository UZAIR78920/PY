import pandas as pd
import numpy as np
data = {'City': ['London', 'Paris', 'Tokyo', 'Sydney', 'New York'],
 'Population': [8.9, np.nan, 14.0, 5.3, 8.4],
 'Area': [1572, 105, 2194, np.nan, 784]}
cities_df = pd.DataFrame(data)
print("Original DataFrame:\n", cities_df)
print("\n--- Indexing and Selection ---")
print("Population column:\n", cities_df['Population'])
print("\nRow at index 2 (Tokyo):\n", cities_df.iloc[2])
print("\nRows for 'London' and 'New York':\n", cities_df.loc[[0, 4], ['City', 'Area']])
print("\n--- Handling Missing Data ---")
df_dropped = cities_df.dropna()
print("DataFrame after dropping rows with NaN:\n", df_dropped)
df_filled = cities_df.fillna(0)
print("\nDataFrame after filling NaN with 0:\n", df_filled)