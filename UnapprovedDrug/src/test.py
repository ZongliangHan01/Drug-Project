import pandas as pd

df = pd.read_csv("historical_data/approved_price_difference.csv",  index_col=0)
df.to_excel("historical_data/approved_price_difference.xlsx")