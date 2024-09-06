import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Lesson-12\Video_Games_Sales_as_at_22_Dec_2016.csv")

print(df[df["User_Count"] != pd.NA])
print("\n\n\n", df.columns)
print(df.shape)

data = df.loc[1:, ["Genre", "User_Count"]].groupby("Genre")["User_Count"].sum().reset_index()

print(data)
print(df["User_Count"].sum())


plt.figure(figsize=(50, 10))


# plt.plot(data["Genre"], data["User_Count"],  marker=".")
plt.bar(data["Genre"], data["User_Count"])
plt.title("European sales")
plt.xlabel("Years")        # nhan truc X
plt.ylabel("Sales")    # nhan truc Y

plt.grid(True)  #hien thi luoi trong bang do
plt.show()






