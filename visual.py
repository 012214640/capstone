import pandas as pd
import seaborn as sb
from scipy.stats import pearsonr
import matplotlib.pyplot as plt


df = pd.read_csv("global_sports_footwear_sales_2018_2026_test.csv")

#sb.scatterplot(x="base_price_usd", y="units_sold", data=df)
#plt.show()

corr, p_value = pearsonr(df["base_price_usd"], df["units_sold"])

print("Correlation:", corr)
print("P-value:", p_value)