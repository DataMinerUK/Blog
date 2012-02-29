import csv                             #allows me to work with csv files
from datetime import date, timedelta   #allows me to deal with dates
from dateutil import parser            #great library for dealing with dates

#Opening the data sheet and moving down past the headings row
f = open("Famine in Somalia%3A how did the world respond%3F DATA - Aid flows.csv", "rU")
table = csv.reader( f )
table.next()

dataDict = {}

#Making a dictionary of donors to list of dates they donated i.e. {donor1: [date1, date2, date3], donor2: [date1, date2], ...}
for row in table:
#	print row
	donor = row[0]
	donation_date = parser.parse(row[4]).strftime('%Y-%m-%d')
	if donor in dataDict.keys():
		dataDict[donor].append(donation_date)
	else:
		dataDict[donor] = [donation_date]

print dataDict

donorsByDate = {}

# Restructuring dataDict to a new dictionary donorsByDate = {date1: [donor1, donor2], date2: [donor3], ...}
for donor, donation_dates in dataDict.iteritems():
	donation_dates.sort()                             #sorting the list of date values
	donation_date = donation_dates[0]                 #getting the earliest date
	lst = donorsByDate.get( donation_date, [] )       #putting earliest date as the key and filling in a list of donors
	lst.append( donor )
	donorsByDate[ donation_date ] = lst
	
print donorsByDate

#Making a date range so that every day has a value
d1 = date(2010,07,21)
d2 = date(2012,02,15)

delta = d2 - d1

#Adding the missing dates to the dictionary with an empty list as the values
for i in range(delta.days + 1):
	date = d1 + timedelta(days = i)
	date = date.strftime("%Y-%m-%d")
	if date not in donorsByDate:
		donorsByDate[date] = []
		
print donorsByDate

#Making a new csv for the output
out = csv.writer(open("CountOfUniqueDonorsByDate.csv", "w"))
out.writerow(["Date", "Number of Unique Donors"])              #Headers

#Writing out the date and the number of donors i.e. the length of the list, sorted by date
for d in sorted(donorsByDate):
	out.writerow([d, len(donorsByDate[key])])
