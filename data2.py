import pandas as pd

df=pd.read_csv('cleaned_Data.csv')
df=df[~((df['target'] == "Graduate") & (df['grade'] == 0))]
df=df[~((df['enrolled_units'] == 0) & (df['grade'] == 0))]

df.to_csv('cleaned_Data2.csv', index=False)
