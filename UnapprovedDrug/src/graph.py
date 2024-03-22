import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("historical_data/approved_price_difference.csv",  index_col=0)
data = df['14B']
data = data.reset_index(drop=True)
plt.boxplot(data)
# plt.scatter(data.index, data, marker='o')
plt.grid(True)
# Customize the plot
# plt.title('Line Chart with 1 SD Error Bars')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.legend()
# plt.grid(True)

# Show the plot
plt.show()
