from create_df import df
import pandas as pd

print(df.duplicated().sum()) #no duplicates
print(df.isnull().sum()) #11 missing postal code

#remove null postcodes
df= df.dropna(subset=["Postal Code"])
print(df.isnull().sum())

print(df.describe())

#checking date format and turning to uk format
df.loc[:, 'Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce', dayfirst=False)
df.loc[:, 'Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce', dayfirst=False)

