'''
CS144 Pandemaniac Project - 2016
Professor Wierman
Authors: Rushikesh Joshi and Johno Ikpeazu

This module will create nodes and output them in the format required for 
the given simulator (sim.py)
'''

import sim
import sys
import json
import random
import networkx as nx
from operator import itemgetter, attrgetter

def parse_filename(filename):
    # Retrieve relevant information from name of graph
    info = filename.split(".")
    num_players = info[0]
    num_seeds = int(info[1])
    id = info[2]
    return num_players, num_seeds, id

def parse_graph(file_string):
    # Open the file and decode the json information
    with open(file_string, 'r') as f:
        data = json.load(f)
    return data

def format_nodes(results, trial):
	strategies = []
	
	for key in trial:
		count = 0
		strats = {}
		for iteration in trial[key]:
			strats[str(count)] = iteration
			count += 1
		strategies.append(strats)

	for key in results:
		strats = {}
		count = 0
		for iteration in results[key]:
			strats[str(count)] = iteration
			count += 1
		strategies.append(strats)

	return strategies

# Load the file as python argument
graph = parse_graph(sys.argv[1])

# Remove the .json extension from file_string
filename = sys.argv[1][7:-5]

# Retrieve relevant (descriptive) info from graph name
num_players, num_seeds, id = parse_filename(filename)
print "Number of players = ", num_players

# Load the results for corresponding graph
results = parse_graph(sys.argv[2])

# Trial method that we are testing
trial = parse_graph(sys.argv[3])

# Format seed nodes in proper format for simulation
strategies = format_nodes(results, trial)

#print strategies
# print len(strategies)
# for elem in strategies:
# 	print "NEW DICT"
# 	print elem
# nodes = {}
# count = 0
# nodes[str(count)] = strategies[count][str(0)]
# count += 1
# nodes[str(count)] = strategies[count][str(0)]
# count += 1
# nodes[str(count)] = strategies[count][str(0)]
# count += 1
# nodes[str(count)] = strategies[count][str(0)]
# count += 1
# nodes[str(count)] = strategies[count][str(0)]
# print "Nodes are: ", nodes
# print
# sim.run(graph, nodes)

# Run simulation to compare scores of various strategies
for i in range(50):
	nodes = {}
	for j in range(int(num_players) + 1):
		nodes[str(j)] = strategies[j][str(i)]
	sim.run(graph, nodes)



