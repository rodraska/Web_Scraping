import pandas as pd

df = pd.read_csv("titanic.csv")

cols = df.columns.tolist()

head = df.head(10)

lista = df.iloc[20:25]

stats = df.describe()

women = df.loc[df["Sex"] == "female"]

women_stats = women.describe()

women_rich = df.loc[(df["Sex"] == "female") & (df["Pclass"] == 1)]

women_rich_stats = women_rich.describe()

women_rich_dead = df.loc[(df["Sex"] == "female") & (df["Pclass"] == 1) & (df["Survived"] == 0)]

not_rich = df.loc[df["Pclass"] != 1]

women_or_rich = df.loc[(df["Pclass"] == 1) | (df["Sex"] == "female")]

women_and_sexy = df.loc[(df["Sex"] == "female") & (df["Age"] > 18.0) & (df["Age"] < 30.0)]

#print(df.sort_values(["Age", "Pclass", "Sex"], ascending=[1,1,0]))

#print(df.drop(columns=["Parch", "Ticket"]))

#print(df.dropna())

df2 = pd.read_csv("titanic.csv")

df2 = df2[df2["Age"].notna()]

df2.Age = df2.Age.astype(int)

print(df2)
