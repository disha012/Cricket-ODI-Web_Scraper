
# This file scrapes the pages of the individual players and makes a CSV file for each of them saving the years, the corressponding runs and the sum total till that year. These CSV files are used by combine.py for combining all these files.

from urllib.request import urlopen
import csv
import re
from bs4 import BeautifulSoup
quote_page = 'http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID='

for i in range(2, 9999):
	a = '{0:04}'.format(i)
	page = urlopen(quote_page+a)
	soup = BeautifulSoup(page, 'html.parser')
	name_box = soup.find_all('td', attrs={'class':'Banner2'})
	if not name_box:
		continue
	name_and_coun=''
	for i in name_box:
		name_and_coun += i.text.strip()
	abc = re.split("\((.*?)\)", name_and_coun)
	name = abc[0]
	coun = abc[1]
	summ = 0 
	name_box = soup.find('table', attrs={'class':'TableLined'})
	rows = name_box.find_all('tr')
	with open(a + '.csv', 'w', encoding="ISO-8859-1", newline='') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name, coun])
		writer.writerow(["Year", "Runs", "Accumulative-sum"])
		for i, row in enumerate(rows):
			if i>0:
        			for j, td in enumerate(row.children):
        				if j==1:
        					if td.a:
        						year111 = (td.a.text.strip())
        					else:
        						year111 = (td.text.strip())
        						run111 = summ
        						break
        				if j==17:
        					run111 = (td.text.strip())
        					summ += int(run111)
        			writer.writerow([year111, run111, summ])

