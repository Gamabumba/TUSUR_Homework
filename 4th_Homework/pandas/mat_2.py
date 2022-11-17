import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Olympics 2018.xlsx", sheet_name="Olympics")

df_filter_country = df['Country'].isin(['Soviet Union']) & df['Medal'].isin(['GOLD'])

print(df[df_filter_country])

df.groupby('Year').Age.mean().plot()
plt.show()

df.drop(columns=['City'])
df_filter_season = df['Season'].isin(['Summer'])


df['Born_Year'] = df['Year'] - df['Age']
print(df[df_filter_season])

df[df_filter_season].to_csv('final_base.csv')



