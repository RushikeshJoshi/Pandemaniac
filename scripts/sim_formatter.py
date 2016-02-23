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

    # Create a networkx graph from our adjacency list data
    G = nx.from_dict_of_lists(data)

    return G

def generate_nodes(graph):

    values = []
    nodes = nx.degree_centrality(graph)
    for node in nodes:
        values.append((node, nodes[node]))

    values.sort(key = itemgetter(1), reverse = True)
    return values

def format_nodes(num_seeds, nodes):
	strategies = {}

# Load the file as python argument
file_string = sys.argv[1]

# Remove the .json extension from file_string
filename = file_string[7:-5]

# Retrieve relevant (descriptive) info from graph name
num_players, num_seeds, id = parse_filename(filename)

# Retrieve list of all nodes
graph = parse_graph(file_string)

# Retrieve a list sorted in descending order of node and degree centrality
nodes = generate_nodes(graph)

# Format seed nodes in proper format for simulation
strategies = format_nodes(num_seeds, nodes)

# Run simulation to compare scores of various strategies
sim.run(graph, strategies)