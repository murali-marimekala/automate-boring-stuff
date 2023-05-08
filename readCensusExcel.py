# Tabulates population and number of census tracts for each country
import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet =  wb['Population by Census Tract']
countyData = {}

#Step-1 Reading the spreadsheet data

#Fill in countyData with each countys population and tracts
print("Reading rows ...")

for row in range(2, sheet.max_row + 1):
    #Each row in  the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    #print("Value of state is %s, county is %s and pop is %s" % (state, county, pop))
  
#Step-2: Populate the Data structure
    #Make sure that the key for this state exists
    #Set default will do nothing if the key already exists, you can call it on every iteration of the for loop without a problem
    countyData.setdefault(state, {})
    #Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts':0, 'pop':0})
    #Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    #increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)
    #print("Value of pop is %s" %(countyData[state][county]['pop']))

#Step-3 : Write the results to a file
#pprint.pformat() function used to write the countyData dictionary value as a massive string to a file
print('Writing the results to a file census2010.py ...')
resultFile = open('census2010.py','w')
resultFile.write('allData =' +pprint.pformat(countyData))
resultFile.close()
lsprint('Done...')