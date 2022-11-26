import pandas as pd

names_dict = {"names":
        [
            "Tom",
            "Mary",
            "Jeff",
            "Rose",
            "Stephanie",
            "Rodger"
        ]}

#print(names_dict["names"])

df = pd.DataFrame(names_dict)

df.to_csv("names.csv")

df2 = pd.read_csv("names.csv")

df.to_csv("names_no_index.csv", index=False)

df3 = pd.read_csv("names_no_index.csv")

df3.to_json("names.json")

df4 = pd.read_json("names.json")

df4["ages"] = [20, 26, 20, 18, 52, 40]

names = df4.names

ages = df4.ages

ages_list = df4.ages.tolist()

row1 = df4.iloc[1]

print(row1)