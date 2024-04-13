import pandas as pd

df=pd.read_csv('final_data.csv')
df=df[~((df['enrolled_units'] == 0) & (df['grade'] == 0))]
df=df[~((df['grade'] == 0))]
df.to_csv('cleaned_Data2.csv', index=False)
