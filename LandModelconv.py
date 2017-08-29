import csv
import xlrd

workbook = xlrd.open_workbook('C:/Users/cra987/Dropbox/PythonWork/Acre New Temp C2 NBHD 002.3.xlsx')
for sheet in workbook.sheets():
    with open('{}.csv'.format(sheet.name), 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(sheet.row_values(row) for row in range(sheet.nrows))
        
import pandas as pd
df1 = pd.read_csv("C:/Users/cra987/ACRE Model.csv")

dat=df1.iloc[17:22,2:6]
adsp=df1.iloc[17:22,12]
area=df1.iloc[17:22,8]