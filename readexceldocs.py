import openpyxl

#Getting sheets from the workbook
wb = openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames)
sheet = wb['Sheet3']
print(sheet.title)
anotherSheet = wb.active
print("Sheet that is open or active is ", anotherSheet)

#Getting cells from the sheets
sheet = wb['Sheet1']
print("Value of shee is ",sheet)

#Get a cell from the sheet
print("Getting cell from sheet",sheet['A1'])
print("Value of cell is ",sheet['A1'].value)

#Alternate method to get another cell from sheet
c = sheet['B1']
print("Reading another cell ",c.value)

#Get row, column and value from the cell
print('Row %s, Column %s is %s' % (c.row, c.column, c.value))