'''
GEOG5003M Practical
Agent Based Modelling
'''

import random
import operator
import matplotlib.pyplot

# number of initial agents 
num_of_agents = 10 

# store our agents in a list
agents = []


# add the initial number of agents rondomly generated integer between 0 and 99 
# for the x and y coordinates
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


#loop throug each agent and move it twice
num_of_iterations = 100

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # Change agent y based on a random number.
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        # Change agent x based on a random number.
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            
        

# set up the plot area
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# add each agent to a scatter plot
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# plot the furthest east point a different colour
max_east = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(max_east[1],max_east[0], color='red')

# show the plot
matplotlib.pyplot.show()


'''
print(agents[1][0], agents[1][1]) 

# Work out the distance between the two sets of y and xs.
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer) 
print()

#get max y (first element in list)
print (max(agents))
#get max x (second element in list)
print (max(agents, key=operator.itemgetter(1)))


'''