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

def format_nodes(data, results, trial):
	strategies = {}

	for key in trial:
		count = 0
		for iteration in trial[key]:
			strategies["trial" + str(count)] = iteration
			count += 1

	for key in results:
		count = 0
		for iteration in results[key]:
			strategies[key + str(count)] = iteration
			count += 1

	return strategies

# Load the file as python argument
graph = parse_graph(sys.argv[1])

# Load the results for corresponding graph
results = parse_graph(sys.argv[2])

# Trial method that we are testing
trial = parse_graph(sys.argv[3])

# Retrieve relevant (descriptive) info from graph name
num_players, num_seeds, id = parse_filename(filename)

# Format seed nodes in proper format for simulation
strategies = format_nodes(data, results, trial)

print strategies.keys()

'''
# Run simulation to compare scores of various strategies
sim.run(graph, strategies)
'''


