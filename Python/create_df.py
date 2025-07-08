import pandas as pd

def dataframe():
    df = pd.read_csv(r"C:\Users\rebec\.cache\kagglehub\datasets\rohitsahoo\sales-forecasting\versions\2\train.csv")
    return df

print(dataframe())
