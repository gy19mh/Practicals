'''
GEOG5003M Practical
Agent Based Modelling
'''

import random
import operator
import matplotlib.pyplot
import time


# Calculate thedistance between agents
def distance_between(agents_row_a, agents_row_b): 
    #check what type of object is being passed in
    #print (type(agents_row_a))
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

#Extra challenges
# Get the distances of all agent compared to each other
# Optimised so it doent repeat pairs that have been used already
# Includes Print statements and a timer to help with debugging
def all_distance_between(agents):
    # Time how long it takes
    start = time.perf_counter()
    
    #create and the return a list of distances.
    distances = []
    
    # loop through each agent. Use an index loop here. The index is used later
    # so we dont re-iterate over the same agents
    for i in range(len(agents)):
        print(str(i) + ": " + str(agents[i]))
        agent_a = agents[i]
        
        # Compare the agent to other agents in the list.
        # Slice the list to start at the next agent. This is so we dont iterate 
        # over agents that have already been compared.
        # The ' + 1' is used so it is not checking the agent against itself.
        for agent_b in agents[i + 1:]:
            dist = (((agent_a[0] - agent_b[0])**2) + ((agent_a[1] - agent_b[1])**2))**0.5
            print ("\t" + str(i + 1) + ": " + str(agent_b) + " Distance: " + str(dist))
            
            distances.append(dist)
            
    end = time.perf_counter()
    print("time = " + str(end - start))
    
    return distances



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

#distance = distance_between(agents[0], agents[1])
#print(distance) 

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 


# Extra Challenges
# Compare ALL distances to each other
distances = all_distance_between(agents)
# Get the maximum distance
print ('Maximum distance:' + str (max(distances)))
# get the minimum distance
print ('Minimum distance:' + str (min(distances)))
        
        
        
'''

#get max y (first element in list)
print (max(agents))
#get max x (second element in list)
print (max(agents, key=operator.itemgetter(1)))


'''