### STAND ALONE FUNCTION 
### FOR QUICKLY WRITING ONE OR MANY FILES TO A CSV as dataframe 
### v 1.1 NOVEMBER 2018 
### BY TGURGICK

__author__ = "Trevor Gurgick"
__copyright__ = "Copyright (c) 2018, Trevor Gurgick"

__license__ = "GPL"
__version__ = "1.1"
__status__ = "active"

import pandas as pd
import csv
import os

def writeCSV(data,filename):
	cwd = os.getcwd()
	print("Current directory: %s" %(cwd))
	path = '%s/%s.csv' %(cwd,filename)

	if type(data) != dict:
		try:
			data = pd.DataFrame(data,dtype=None)	
			data.to_csv(path)	
			print("SAVED: %s" %(path))
		except:
			pass
	elif type(data) == dict:
		try:
			data = pd.DataFrame.from_dict(data,orient='index')
			data.to_csv(path)	
			print("SAVED: %s" %(path))	
		except:
			pass	
if __name__ == '__main__':
	writeCSV(data,filename)
