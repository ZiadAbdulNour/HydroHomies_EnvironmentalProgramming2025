# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 09:21:37 2025

@author: lenovo
"""

filename = r'C:\Users\lenovo\Downloads\Leuven\Courses\Python\P_June2019.asc'
f = open (filename, 'r')

cols = f.readline().split() # To split \n: make ncols and the 30 into a list then i select what i want
rows = f.readline ().split()

ncols = int (cols[1])
nrows = int (rows[1])

for i in range (3):
    f.readline()

nodata = f.readline().split()
no_data = int (nodata[1])

DATA = f.readlines()

# Method 1 my try
i = 0
Array = []
while i < nrows:
    DATAROW = DATA[i].split()
    print (DATAROW)
    Array.append(DATAROW) # To store in the values
    i+=1

m = 0
n = 0
FloatArray = [] # PROBLEM HERE SOMEWHERE
row = []
while n < nrows:
    while m < ncols:
        row.append(float (Array[n][m]))
        m+=1
    FloatArray.append(row)
    m = 0
    n+=1
    
# I JUST NEED TO TRANSFROM ROW INTO FLOAT
p = 0
total = 0
for l in row:
    if row[l] != no_data:
        total = total + row[l] 
        p = p+1
Average = Total / p
print (Average)
        
# Method 2 Professor solution (see 2 tries of her in pics)

# Method 3 using loops (EASY)
i=0
j=0
a=0
count = 0
Total = 0
while a==0:
    if i < ncols:
        if j < nrows:
            if DATA [i][j] != no_data:
                Total = Total + DATA [i][j]
                count = count + 1
                i+=1
        else:
            a = 1
    else:
        j = j+1
        i = 0

Average = Total/count

print (Average)

# Method 4 using array (HARD)?
rainfall_rows = []

for line in arrayrows:
    parts = line.split()
    arrayrows = [] # Thats how i create an empty list
    
    for p in parts:
        try:
            values = float (p) 
        except:
            p = -9999
        continue

rainfall_rows.append (arrayrows)
    
a=0
b=0
for b < nrows:
    while a < ncols:
        array = list [
        a = a+1
print (array)
