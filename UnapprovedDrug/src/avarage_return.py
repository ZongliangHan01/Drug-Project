import pandas as pd

# df = pd.read_csv("historical_data/approved_price_difference.csv",  index_col=0)
df = pd.read_csv("historical_data/5_diff_close_price.csv")
means = df.mean()
for i in range(len(means)):
    print(means[i])
# print(df.mean())

