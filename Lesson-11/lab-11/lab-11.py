import pandas as pd


df = pd.read_excel("Lesson-11/lab-11/provinces.xlsx")
coastlines = pd.read_excel("Lesson-11/lab-11/coastlines.xlsx")
borders_china = pd.read_excel("Lesson-11/lab-11/borders.xls", sheet_name="CHN")
borders_lao = pd.read_excel("Lesson-11/lab-11/borders.xls", sheet_name="LAO")
borders_khm = pd.read_excel("Lesson-11/lab-11/borders.xls", sheet_name="KHM")

borders = pd.concat([borders_china, borders_lao, borders_khm])

def bai1():
    df['Density'] = df['Population'] * 1000 / df['Area']
    print(df[['Name', 'Population', 'Area', 'Density']])

def bai2():
    print(f"\n\nsố tỉnh thành giáp biển ở Việt Nam: {coastlines["Name"].count()}\n\n")

    cl = []
    for i in range(len(df)):
        if df['Name'][i] in coastlines['Name'].values:
            cl.append(coastlines.loc[coastlines['Name'] == df['Name'][i], 'Coastline'].values[0])
        else:
            cl.append(0)

    df["coastlines"] = pd.Series(cl)
    print(df)

def bai3():
    borders['BorderWith'] = borders.apply(lambda row: 'CHN' if row.name in borders_china.index else ('LAO' if row.name in borders_lao.index else 'KHM'), axis=1)


    borders_grouped = borders.groupby('Tên tỉnh')['BorderWith'].agg(['count']).reset_index()
    borders_grouped.columns = ['Tên tỉnh', 'BorderCount']

    borders_pivot = borders.pivot_table(index='Tên tỉnh', values='BorderWith', aggfunc=lambda x: ', '.join(x)).reset_index()
    borders_pivot.columns = ['Tên tỉnh', 'BorderWith']

    df = pd.merge(borders_grouped, borders_pivot, on='Tên tỉnh')

    df.to_excel("borders_updated.xlsx", index=False)

    two_borders = df[df['BorderCount'] == 2]
    print(two_borders)


    print(borders)



    # # tao bang border_updated rieng
    # border_updated_df = pd.DataFrame(columns=['Name', 'BorderWith', 'BorderCount'])

    # # chay file de doc data trong tung sheet
    # border_list = (('CHN', 'China'), ('LAO', 'Laos'), ('KHM', 'Combodia'))

    # for coutry in border_list:
    #     inp_df = pd.read_excel(borders, sheet_name=coutry[0])
    
    # # chay vong lap de ghi vao file province
    # for name in inp_df['Tên tỉnh']:
    #     matching_row = border_updated_df[df['Name'] == name]
    #     if(not matching_row.empty):
    #         border_updated_df.at[matching_row.index[0], 'BorderWith'] += ", " + coutry[1]
    #         border_updated_df.at[matching_row.index[0], 'BorderCount'] += 1
    #     else:
    #         border_updated_df = pd.concat([border_updated_df, pd.DataFrame({'Name': [name], 'BorderWith': [coutry[1] + ','], 'BorderCount': [1]})], ignore_index=True)
    # # in ra bang province
    # print(border_updated_df)

    # # update du lieu cho file province
    # border_updated_df.to_excel("borders_updated.xlsx", index=False)




print("Chọn bài:")
print("1. Bài 1")
print("2. Bài 2")
print("3. Bài 3")

choice = input("Nhập số bài: ")

functions = {
    "1": bai1,
    "2": bai2,
    "3": bai3
}

if choice in functions:
    functions[choice]()
else:
    print("Số bài không hợp lệ")
