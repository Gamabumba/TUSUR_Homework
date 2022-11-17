import pandas as pd
import numpy as np

df = pd.read_csv("First_data_set.csv")
df.dropna(axis=0, how='all')

print(df.hhs_geo_region.unique())

df_filter = df['education'].isin(['Some College'])
df[df_filter]
print(df[df_filter])

max_children = df[df_filter]['household_children'].max()
mean_children = df[df_filter]['household_children'].mean()
SKO_children = np.std(df[df_filter]['household_children'])

print(max_children)
print(mean_children)
print(SKO_children)