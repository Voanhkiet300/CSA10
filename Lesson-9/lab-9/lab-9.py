from data import col_list, province_list
import pandas as pd


# series --------------------------------
# 1 cot
# series = pd.Series(province_list, index=['a', 'b', 'c'])
# data = {'a': 'abc', 'b': 'xyz', 'c': 'mno'}

# series = pd.Series(data=data, index=['a', 'b', 'c'])

# data = {"a": -1.3, "b": 11.7, "d": 2.0, "f": 10, "g": 5}
# series = pd.Series(data, index=["a", "b", "c", "d", "e", "f"])
# print(series[0:6:2])




# dataFrame -----------------------------
data = pd.DataFrame(data=province_list, columns=col_list)
# print(data.head(10))


# luu vao xls
data.to_excel("Lesson-9/lab-9/province.xlsx")
