import pandas as pd

df = pd.read_excel("Lesson-10\pokemon_data.xlsx")
# print(df)

# cu phap thong thuong (slice) -----------
# 1 cot => series
# data = df.Name    # biet truoc thuoc tinh
# data = df["Name"]   # co the tuy chinh thuoc tinh
# print(data.head(10))
# print(type(data))


# 1 hang => dataFrame
# data = df[4:5]
# print(data)
# print(type(data))


# nhieu hang => dataFrame
# data = df[4:30:5]
# print(data)
# print(type(data))


# nhieu cot => dataFrame
# data = df[["Name", "HP"]]
# print(data.head(5))
# print(type(data))






# truy xuat bang "loc" ----------------
# loc: duoc goi bang label (column)
# 1 cot
# data = df.loc[:,"Name"]
# print(data.head(5))
# print(type(data))


# 1 hang
# data = df.loc[10]
# print(data)
# print(type(data))


# 1 o => phu thuoc vao kieu du lieu cua o
# data = df.loc[10, "HP"]
# print(data)
# print(type(data))


# nhieu cot => dataFrame
# data = df.loc[:, "HP": "Speed"]     # lay lien tuc

# data = df.loc[:, ["HP", "Speed"]]   # lay tung cot cu the

# print(data)


# nhieu hang => dataFrame
# data = df.loc[1:8]
# print(data)


# nhieu cot + nhieu hang => dataFrame
# data = df.loc[1:8, ["HP", "Attack"]]
# print(data)


# truy xuat bang "iloc" dem
# 1 cot
# data = df.iloc[:, 1]
# print(data.head(5))
# print(type(data))


# 1 hang
# data = df.iloc[10]
# print(data)
# print(type(data))


# 1 o => phu thuoc vao kieu du lieu cua o
# data = df.iloc[10, 3]
# print(data)
# print(type(data))


# nhieu cot => dataFrame
# data = df.iloc[:, 1: 5]     # lay lien tuc

# data = df.iloc[:, [5, 11]]   # lay tung cot cu the

# print(data)


# nhieu hang => dataFrame
# data = df.iloc[1:8]
# print(data)

# nhieu cot + nhieu hang => dataFrame
# data = df.iloc[1:8, [3, 8]]
# print(data)

# tong ket du lieu ---------------
# print(df.HP)
# print(df.describe())
print(df["Name"].describe())
# print(df["HP"].sum())
# print(df["HP"].sum())
# print("value count", df.Legendary.value_counts())

# truy xuat co dk ------------
# in ra ten cua poke co hp > 150
# filtered_df = df[df.HP > 150]
# print(filtered_df.Name)


# in ra ten cua poke co ten Chansey
# filtered_df = df[df.Name == 'Chansey']
# print(filtered_df)