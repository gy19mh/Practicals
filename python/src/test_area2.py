import csv
import matplotlib.pyplot

# Set up the Environment before adding Agents.
# Read in environment data from a text file and store it in a list
in_file = open(r'in.txt', newline='') 
dataset = csv.reader(in_file, quoting=csv.QUOTE_NONNUMERIC)
# Lines here happen before any data is processed
environment = []


maxval = 0
maxval1 = 23

def main():
    print("Main")
    global maxval1
    maxval1 = 900
    
    
    
if __name__ == "__main__":
    main()    
    
    

import requests
import bs4


num_of_agents = 100

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


print (len(td_xs))



for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    #print ("[{},{}]".format(x,y))