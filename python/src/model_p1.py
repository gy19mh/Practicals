'''
GEOG5003M Practical
Agent Based Modelling
'''

import random

# Make first set of x and y variable using a random int between 0 and 99
y0 = random.randint(0,99)
x0 = random.randint(0,99)


# Change y0 based on a random number.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
# Change x0 based on a random number.
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
print(y0, x0) 


# Change y0 based on a random number.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
# Change x0 based on a random number.
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
print(y0, x0) 


# Change y0 based on a random number.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
# Change x0 based on a random number.
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
print(y0, x0) 


# Make a second set of y and xs, and make these change randomly as well.
# using a random int between 0 and 99 as the starting point
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Change y1 based on a random number.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
# Change x1 based on a random number.
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1) 

# Change y1 based on a random number.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
# Change x1 based on a random number.
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1) 

# Change y1 based on a random number.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
# Change x1 based on a random number.
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1) 
# Work out the distance between the two sets of y and xs.

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer) 
