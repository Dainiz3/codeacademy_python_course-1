import pandas as pd


df = pd.read_csv("data/credits.csv", delimiter=",")
print(df.head())
df = df[:10]

df.to_csv("data/result.csv")