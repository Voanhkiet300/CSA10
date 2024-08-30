import pandas as pd


df = pd.read_excel("Lesson-11/lab-11/provinces.xlsx")
coastlines = pd.read_excel("Lesson-11/lab-11/coastlines.xlsx")
borders_china = pd.read_excel("Lesson-11/lab-11/borders.xls", sheet_name="CHN")
borders_lao = pd.read_excel("Lesson-11/lab-11/borders.xls", sheet_name="LAO")
borders_khm = pd.read_excel("Lesson-11/lab-11/borders.xls", sheet_name="KHM")

borders = pd.concat([borders_china, borders_lao, borders_khm])

# bai 1: Mật Độ Dân Số
# df['Density'] = df['Population'] * 1000 / df['Area']
# print(df[['Name', 'Population', 'Area', 'Density']])

# bai 2: Bờ Biển
# print(f"\n\nsố tỉnh thành giáp biển ở Việt Nam: {coastlines["Name"].count()}\n\n")

# cl = []
# for i in range(len(df)):
#     if df['Name'][i] in coastlines['Name'].values:
#         cl.append(coastlines.loc[coastlines['Name'] == df['Name'][i], 'Coastline'].values[0])
#     else:
#         cl.append(0)

# df["coastlines"] = pd.Series(cl)
# print(df)

# bai 3: Biên Giới

borders['BorderWith'] = borders.apply(lambda row: 'CHN' if row.name in borders_china.index else ('LAO' if row.name in borders_lao.index else 'KHM'), axis=1)


# Create a new column 'BorderWith' and fill it with the country name
borders['BorderWith'] = borders.apply(lambda row: 'CHN' if row.name in borders_china.index else ('LAO' if row.name in borders_lao.index else 'KHM'), axis=1)

# Group the data by 'Name' and count the number of borders for each province
borders_grouped = borders.groupby('Tên tỉnh')['BorderWith'].agg(['count']).reset_index()
borders_grouped.columns = ['Tên tỉnh', 'BorderCount']

borders_pivot = borders.pivot_table(index='Tên tỉnh', values='BorderWith', aggfunc=lambda x: ', '.join(x)).reset_index()
borders_pivot.columns = ['Tên tỉnh', 'BorderWith']

df = pd.merge(borders_grouped, borders_pivot, on='Tên tỉnh')

df.to_excel("borders_updated.xlsx", index=False)

two_borders = df[df['BorderCount'] == 2]
print(two_borders)


print(borders)

