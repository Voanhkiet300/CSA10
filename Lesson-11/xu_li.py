import pandas as pd

# tao data
df = pd.DataFrame({
   "Name": ['Nguyen Van A', "Tran Thi B", "Lam Van C", "Nguyen Thi D", "Chau Van E"],
   "Point": [4, 2.5, 6.3, 9.0, 2.4],
    "Qualify": [True, False, False, False, True]
})

# thay đổi giá trị trong df:
# thay the tung o
# df.loc[1, "Point"] = 6.8
# df.iloc[0, 1] = 5.2
# print(df)


# at (label)
# value = df.at[3, "Qualify"]
# print(value)

# iat (index)
# df.iat[4, 0] = "Truong Thi F"
# value = df.iat[4, 0]
# print(df)


# replace(to_replace, value, [inplace=bool])
# inplace = True: Thay doi (ghi de) len df cu
# inplace = False: tao df moi + chen du lieu thay doi
# df2 = df.replace([True, False], ['Yes', 'No'], inplace=False)
# print(df2)


# thay đổi giá trị của cột & dòng:
# them cot
# df["Gender"] = pd.Series(["Nam", "Nu", "Nam", "Nu", "Nu"])
# df["Gender"] = ["Nam", "Nu", "Nam", "Nu", "Nu"]
# print(df)


# xoa cot(drop(column= ..., [inplace=bool]))
# inplace mac dinh: False
# df.drop(columns="Name", inplace=False)
# print(df)

# them dong append(series/ dict, ignore_index = True)-------------------

# df2 = df.append({'Name': "Tran Van F", "Point": 10.0, "Qualify": False}, ignore_index=True)
# print(df)

df2 = pd.concat([df, pd.DataFrame({'Name': ["Tran Van F"], "Point": [10.0], "Qualify": [False]})], ignore_index=True)
print(df2)
