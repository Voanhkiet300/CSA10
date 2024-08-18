import pandas as pd
from data import province_list, col_list

data = pd.DataFrame(data=province_list, columns=col_list)
# print(data[11:21])


def bai1():
    print(f"List of provinces and cities: ", end=" ")
    for i in range(len(data)-1) :
        print(data.loc[i, "Name"], end=", ")
    print(data.loc[len(data)-1, "Name"], end=".")

def bai2():
    a = []
    for i in range(len(data)):
        if (data.loc[i, "Division"] == "Thành phố Trung ương"):
            a.append(i)
    print(data.loc[a, ["Name", "Region"]])

def bai3():
    print(f"Số vùng địa lý ở Việt Nam: {len(data['Region'].unique())}")
    print("\nSố tỉnh thành trong mỗi vùng địa lý:", data.groupby('Region')['Name'].count().to_string())

def bai4():
    max_pop = data.loc[data['Population'].idxmax()]
    min_pop = data.loc[data['Population'].idxmin()]
    print(f"Tỉnh/thành phố có dân số đông nhất:\t {max_pop['Name']}: \t{max_pop['Population']} người")
    print(f"Tỉnh/thành phố có dân số ít nhất: \t {min_pop['Name']}: \t\t\t{min_pop['Population']} người")

def bai5():
    total_area = data['Area'].sum()
    region_areas = data.groupby('Region')['Area'].sum()
    region_ratios = region_areas / total_area *100
    print("Tổng diện tích các vùng địa lý:", total_area)
    print("\nTổng diện tích của từng vùng địa lý:")
    print(region_areas.to_string())
    print("\nTỉ lệ diện tích của từng vùng địa lý:")
    print(region_ratios.to_string())


print("Chọn bài:")
print("1. Bài 1")
print("2. Bài 2")
print("3. Bài 3")
print("4. Bài 4")
print("5. Bài 5")

choice = input("Nhập số bài: ")

functions = {
    "1": bai1,
    "2": bai2,
    "3": bai3,
    "4": bai4,
    "5": bai5
}

if choice in functions:
    functions[choice]()
else:
    print("Số bài không hợp lệ")

