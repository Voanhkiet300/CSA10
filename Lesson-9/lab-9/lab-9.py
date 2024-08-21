from data import col_list, province_list
import pandas as pd


# dataFrame -----------------------------
data = pd.DataFrame(data=province_list, columns=col_list)


num_rows, num_cols = data.shape
print(f"Số dòng: {num_rows}")
print(f"Số cột: {num_cols}")


memory_usage = data.memory_usage()
print(f"Kích thước lưu trữ của df trong bộ nhớ: {memory_usage.sum()} bytes")


print(f"Kiểu dữ liệu của từng cột trong df:\n{data.dtypes}")


# luu vao xlsx
# data.to_excel("Lesson-9/lab-9/province.xlsx")
