"""
GEOG5003M Practical

Agent framework
"""

import random

# Agent Class
class Agent:
    # initialise the agent with random x and y coordinates limiting the range to 100
    def __init__(self, environment, agents, x=None, y=None):
        self.environment = environment
        # Use the maximum length of the environment as the bounding extent for the agents and the plot.
        # max_environment_y equals the amount of rows
        self.max_environment_y = len(self.environment)
        # max_environment_x equals the amount of records in a row. Just need to use the first row
        self.max_environment_x = len(self.environment[0])
        
        self.store = 0 #
        self.agents = agents
        if (x == None):
            self._x = random.randint(0,self.max_environment_x)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,self.max_environment_y)
        else: 
            self._y = y
    
    # override the str function to give a meaningful desricption
    def __str__(self):
        return "x: {} y: {} Store: {}".format(self._x,
                                             self._y,
                                             self.store)
    
    
    #read only property attribute for x coordinate
    @property
    def x(self):
        return self._x
    
    #read only property attribute for y coordinate
    @property
    def y(self):
        return self._y
    
    # Getter method for x coordinate
    def get_x(self):
        return self._x

    # Setter method for x coordinate
    def set_x(self, value):
        self._x = value
        
    # Getter method for Y coordinate
    def get_y(self):
        return self._y

    #Setter method for y coordinate
    def set_y(self, value):
        self._y = value

    # Change the agent x and y value using a random number
    def move(self):
        
        
        # Change agent y based on a random number.
        # use the max_environment size for the number range
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.max_environment_y
        else:
            self._y = (self._y - 1) % self.max_environment_y
            
        # Change agent x based on a random number.
        if random.random() < 0.5:
            self._x = (self._x + 1) % self.max_environment_x
        else:
            self._x = (self._x - 1) % self.max_environment_x
    
    # can you make it eat what is left?
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
    # Check if other agents are nearby and share store values
    def share_with_neighbours(self, neighbourhood): 
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if (distance <= neighbourhood):
                # Sum self.store and agent.store .
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                avg = sum / 2
                self.store = avg
                agent.store = avg
                
                #print("sharing " + str(distance) + " " + str(avg))
            
    # Check the distance between this agent and another agent    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
