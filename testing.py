import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

print(df)
print(df.columns)

df.drop