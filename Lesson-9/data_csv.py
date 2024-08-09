import pandas as pd
# print(pd.__version__)

# df = pd.read_csv('Lesson-9\pokemon_data.csv')
# print(df.head(3))
# print('----------------------------------')
# print(df.tail(3))

# tu tao dataframe thong qua dictionary (dict)

# df = pd.DataFrame(
#     {
#         'Name': ['Anastasia', 'Dima', 'Katherine'],
#         'Score': [12.5, 9.0, 16.5],
#         'Attemps': [1, 3, 2]
#     }
# )
# print(df)

# # xuat file csv
# df.to_csv("new_csv")



# ve du lieu len bang do (cho so - 2D)
import matplotlib.pyplot as plt
df = pd.read_csv('Lesson-9\pokemon_data.csv')

plt.figure(figsize=(10, 6))

plt.plot(df["HP"], df["Attack"], marker="o")
plt.title("HP and Attack")
plt.xlabel("HP")        # nhan truc X
plt.ylabel("Attack")    # nhan truc Y

plt.grid(True)  #hien thi luoi trong bang do
plt.show()