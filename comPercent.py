#!/usr/bin/python

import string
import os

files = os.listdir(".")
files.remove("comPercent.py")

totLines = 0
totComs = 0
multi = False

for fs in files:	#This loop will now go through each file and have internal loops for counting the comments in the files
	with open(fs,'r') as f:
		fLs = 0
		fCs = 0
		multi = False
		line = f.readline()
		while line: #If the string is empty, the loop will break, and we'll be at the end of the file
			totLines+=1
			fLs +=1
			#Check for comments now
			if '/*' in line:
				multi = True
				totComs +=1
				fCs+=1
				if '*/' in line:
					multi=False
				elif '//*' in line:	#Specific edge case here
					multi=False
				#print(line)
			elif multi:
				totComs+=1
				fCs+=1
				#print(line)
			elif '*/' in line:
				multi = False
				totComs +=1
				fCs+=1
				#print(line)
			elif '//' in line:
				totComs +=1
				fCs+=1
				#print(line)
				
			line = f.readline()
		ftot = (fCs/float(fLs))*100
		print("Percent comments in " + fs+ " :" + str(ftot) + '%')


print "Total lines: " + str(totLines)
print "Total lines commented: " + str(totComs)

pComs = (totComs/float(totLines))*100.0

print("Percent commented: " + str(pComs) + "%")
