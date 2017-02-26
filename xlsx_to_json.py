""" 
This is how one can convert data from excel files into json format

"""
import xlrd
from collections import OrderedDict
import simplejson as json

# importing xlsx file
wb = xlrd.open_workbook('excel_file.xlsx')
sh = wb.sheet_by_index(0)

# List for holding dict
x_list = []

# Iterating through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
	x = OrderedDict()
	row_values = sh.row_values(rownum)
	x['column_1'] = row_values[0]
	x['column_2'] = row_values[1]
	x['column_3'] = row_values[2]
	x['column_n'] = row_values[n]

	x_list.append(vt)

j = json.dumps(x_list)

with open('x_file.json', 'w') as f:
	f.write(j)