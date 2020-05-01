'''
GEOG5003M Practical
Agent Based Modelling
'''

import random
#import operator
import time
import agentframework
import csv

import requests
import bs4

# Use TkInter backend
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 


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
num_of_agents = 25
# Number of times to move the agents
num_of_iterations = 100
# Set our neighbourhood area
neighbourhood = 20
# Store our agents in a list
agents = []

###


# Set up the Environment before adding Agents.
# Read in environment data from a text file and store it in a list
in_file = open(r'in.txt', newline='') 
dataset = csv.reader(in_file, quoting=csv.QUOTE_NONNUMERIC)
# Lines here happen before any data is processed
environment = []

# Restructure the csv data into a list of values
for row in dataset:
    # Turn each line into a list of values
    rowlist = []
    for value in row:
        # Add the line to the Environment
        rowlist.append(value)
    
    environment.append(rowlist)
# Close the file 
in_file.close()


#scrape agents from an external web page
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# Check the number of available agents from the web scraping against the num_of_agents
if (len(td_ys) < num_of_agents):
    num_of_agents = len(td_ys)

# Add agents from the web scraped data. 
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    print ("[{},{}]".format(x,y))
    agents.append(agentframework.Agent(environment, agents, x, y))


''' Code before web scraping
# Add the initial number of agents rondomly generated integer between 0 and 99 
# for the x and y coordinates
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
'''


''' code before animation
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
'''


# Use the maximum length of the environment as the bounding extent for the agents and the plot.
# max_environment_y equals the amount of rows
max_environment_y = len(environment)

# max_environment_y equals the amount of records in a row. Just need to use the first row
max_environment_x = len(environment[0])



fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
matplotlib.pyplot.imshow(environment)

def update(frame_number):
    
    fig.clear()
    matplotlib.pyplot.ylim(0, max_environment_y)
    matplotlib.pyplot.xlim(0, max_environment_x)
    matplotlib.pyplot.imshow(environment)

    # loop through each agent and move it a number of times
    for j in range(num_of_iterations):
        # Shuffle the Agents list to equalise the wealth
        random.shuffle(agents)
        # Move each agent
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 
# Show the plot
matplotlib.pyplot.show()

# Test the _str_ override for an agent
if (len(agents) > 0):
    print(str(agents[0]))


############### Tkinter would not work for me ###############################
## FigureCanvasTkAgg has no 'show' was error message. and I had all correct imports.
## So I moved on
''' 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.show() 

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() 
'''   




'''
# Extra Challenges
# Efficiently compare ALL distances to each other and get max and min distances
distances = all_distance_between(agents)
# Get the maximum distance
print ('Maximum distance:' + str (max(distances)))
# get the minimum distance
print ('Minimum distance:' + str (min(distances)))
'''      
        
