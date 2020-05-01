'''
GEOG5003M Practical
Agent Based Modelling
'''

import random
#import operator
import matplotlib.pyplot
import time
import agentframework
import csv


# Calculate thedistance between agents
def distance_between(agents_row_a, agents_row_b): 
    # Check what type of object is being passed in
    # print (type(agents_row_a))
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

### Extra challenge function ###
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
        print ("{}: [{},{}]".format(i,agents[i].x, agents[i].y))
        agent_a = agents[i]
        
        # Compare the agent to other agents in the list.
        # Slice the list to start at the next agent. This is so we dont iterate 
        # over agents that have already been compared.
        # The ' + 1' is used so it is not checking the agent against itself.
        for agent_b in agents[i + 1:]:
            dist = (((agent_a.x - agent_b.x)**2) + ((agent_a.y - agent_b.y)**2))**0.5
            print ("\t{}: [{},{}] Distance: {}".format(i + 1, agent_b.x, agent_b.y, dist))
            
            distances.append(dist)
            
    end = time.perf_counter()
    print("time = " + str(end - start))
    
    return distances

### Initial parameters
# Number of initial agents 
num_of_agents = 150
# Number of times to move the agents
num_of_iterations = 100
# Set our neighbourhood area
neighbourhood = 20
# Store our agents in a list
agents = []

###


#enable command line args to be used






# Set up the Environment before adding Agents.
# Read in environment data from a text file and store it in a list
in_file = open(r'in.txt', newline='') 
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


# Add the initial number of agents rondomly generated integer between 0 and 99 
# for the x and y coordinates
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


# loop through each agent and move it a number of times
for j in range(num_of_iterations):
    # Shuffle the Agents list to equalise the wealth
    random.shuffle(agents)
    # Move each agent
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
                  
# Set up the plot area and add the environment
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
# Add each agent to a scatter plot
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# Plot the furthest east point a different colour
#max_east = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(max_east[1],max_east[0], color='red')

# Show the plot
matplotlib.pyplot.show()



'''
# Extra Challenges
# Efficiently compare ALL distances to each other and get max and min distances
distances = all_distance_between(agents)
# Get the maximum distance
print ('Maximum distance:' + str (max(distances)))
# get the minimum distance
print ('Minimum distance:' + str (min(distances)))
'''      
        
