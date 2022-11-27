import pandas as pd

import matplotlib.pyplot as plt

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

names = df.Name.tolist()

revs = []
for name in names:
    if "Rev." in name:
        revs.append(name)


reverends = df.loc[df["Name"].str.contains("Rev.")]

not_reverends = df.loc[~df["Name"].str.contains("Rev.")]

rev_or_mr = df.loc[(df["Name"].str.contains("Rev\.")) | (df["Name"].str.contains("Mr\."))]

rev_or_misters = df.loc[df["Name"].str.contains("Rev\.|Mr\.", regex=True)]

new_df = df.filter(["Age", "Name"])

#print(df.filter(["Name"]).Name.str.contains("Miss.").value_counts())

#print(df[df.filter(["Name"]).Name.str.contains("Miss.") == True])

#print(df[df.Name.str.contains("Miss.") == True].filter(["Name", "Age"]))

#print(df.query("Pclass == 3"))

#print(df.query("Pclass == 3 & Survived == 1 & (Age > 40 | Age < 10)"))

#print(df.groupby("Sex").get_group("male"))

#print(df.groupby("Age").get_group(22))

#print(df.groupby("Sex").count())

#print(df.groupby("Sex").sum())

#print(df.groupby("Sex").Fare.sum())

#pd.set_option('display.max_rows', 1000)

#print(df.groupby(["Sex", "Pclass", "Age"]).Fare.sum())

#df["Sex"].value_counts().plot.barh(title="Passengers on Titanic", color=["red", "green"])

#plt.show()

#df["Sex"].value_counts().plot.pie(figsize=(6, 6), labels=["Male", "Female"], autopct="%.2f")

#plt.show()

df.loc[(df.Pclass == 1), "Pclass"] = "First"
df.loc[(df.Pclass == 2), "Pclass"] = "Second"
df.loc[(df.Pclass == 3), "Pclass"] = "Third"

df["Pclass"] = df.Pclass.astype("category")

df.plot.scatter(x="Age", y="Fare", c="Pclass", cmap="viridis", figsize=(10, 5))

plt.show()