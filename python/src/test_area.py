# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:51:46 2020

@author: mhoyl
"""

import csv
import matplotlib.pyplot

import sys

'''
f = open(r'in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    for value in row:				# A list of value
        print(value) 				# Floats
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
'''





def main():
    print("hello world!")
    x = 50
    y = 70
    num = 300
    print (x)
    print (y)
    print (num)



if __name__ == "__main__":
    main()


# read in environment data from a text file
# format into list for matplotlib

in_file = open('in.txt', newline='') 
dataset = csv.reader(in_file, quoting=csv.QUOTE_NONNUMERIC)
# Lines here happen before any data is processed
environment = []

for row in dataset:
    # Turn each line into a list of values
    rowlist = []
    for value in row:
        rowlist.append(value)
    # Add the line to the Environment
    environment.append(rowlist)
# Close the file 
in_file.close()

print ("\npassed the main")
# Display the Evnvironment in matplotlib
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show() 