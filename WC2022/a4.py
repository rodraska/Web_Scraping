import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("All.csv")

portuguese_league = df.loc[df["League"] == "Portugal"]

eighteen = df.loc[df["Age"] == 18]

trintao = df.loc[df["Age"] >= 30]

frw = df.groupby("Position").get_group("FRW")

top10leagues = df["League"].value_counts().head(10).plot.pie(autopct="%.2f")

plt.show()

print(portuguese_league)



