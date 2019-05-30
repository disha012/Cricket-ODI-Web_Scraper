
# This file combines all the individual CSV files made in the cricket.py file and puts them into a single CSV file (combine.csv).

import csv
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
from os import listdir

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


with open('combine.csv', 'w', encoding="ISO-8859-1", newline='') as final:
	writer = csv.writer(final)
	li = ['Name', 'Country']
	for i in range(1970, 2020):
		li.append(str(i))
	li.append('total')
	writer.writerow(li)
	filenames = find_csv_filenames(dir_path+"/cricketer2/")
	
	for name in filenames:
		print(name)
		with open(name, 'r', encoding="ISO-8859-1", newline='') as csv_file:
			reader = csv.reader(csv_file)
			lii = []
			j = 1970
			myli = []
			for i, line in enumerate(reader):
				myli.append(line)
				count=i
			i = 0
			lii.append(myli[0][0])
			lii.append(myli[0][1])
			while i < len(myli)-1:
				if i == 1 or i == 0:
					pass
				else:
					if(j == 1970):
						if(myli[i][0] != str(j)):
							lii.append('0')
							i = i - 1
					else:
					
						if(myli[i][0] == str(j)):
							lii.append(myli[i][2])
						else: 
							a = lii[-1]
							lii.append(a)
							i = i - 1
					j = j + 1
				i = i + 1
			while len(lii) < len(li):
				lii.append(lii[-1])

			writer.writerow(lii)
							
			
