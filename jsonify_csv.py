import pandas as pd


df = pd.read_csv ("train.csv")
df.to_json ("train.json", orient="records")
