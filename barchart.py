import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 21): #Create some data in column A
    sheet['A' + str(i)] = i

refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=20)

seriesObj = openpyxl.chart.Series(refObj, title='Lengthy Series')

#chartObj = openpyxl.chart.BarChart()
chartObj = openpyxl.chart.LineChart()
chartObj.title = 'Murali Chart'
chartObj.append(seriesObj)

sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')