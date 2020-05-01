'''
GEOG5003M Practical
Agent Based Modelling
'''

import random
import operator
import matplotlib.pyplot

#store our agents in a list
agents = []

# Add the first agent using a random int between 0 and 99 for the x and y coord
agents.append([random.randint(0,99),random.randint(0,99)]) 

# Change agents based on a random number.
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
# Change agents based on a random number.
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
print(agents[0][0], agents[0][1]) 


# Change y0 based on a random number.
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
# Change agents based on a random number.
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
print(agents[0][0], agents[0][1]) 


# Change agents based on a random number.
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
# Change agents based on a random number.
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
print(agents[0][0], agents[0][1]) 


# Make a second set of y and xs, and make these change randomly as well.
# Add the second agent using a random int between 0 and 99 for the x and y coord
agents.append([random.randint(0,99),random.randint(0,99)]) 

# Change agent based on a random number.
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
# Change agent based on a random number.
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

print(agents[1][0], agents[1][1]) 

# Change agent based on a random number.
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
# Change agent based on a random number.
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

print(agents[1][0], agents[1][1]) 

# Change agent based on a random number.
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
# Change agent based on a random number.
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

print(agents[1][0], agents[1][1]) 

# Work out the distance between the two sets of y and xs.
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer) 
print()

#get max y (first element in list)
print (max(agents))
#get max x (second element in list)
print (max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# plot the furthest east point a different colour
max_east = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(max_east[1],max_east[0], color='red')

matplotlib.pyplot.show()