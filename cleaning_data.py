import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data_cleaned.csv')
df['enrolled_units'] = df['C1E'] + df['C2E']
df['units_evaluations'] = df['C1EV'] + df['C2EV']
df['aproved_units'] = df['C1A'] + df['C2A']
df['Grade'] = (df['C1G'] + df['C2G'])/2

del df['C1E']
del df['C2E']
del df['C1EV']
del df['C2EV']
del df['C1A']
del df['C2A']
del df['C1G']
del df['C2G']


# Save the modified DataFrame back to a CSV file
df.to_csv('cleaned_Data.csv', index=False)