'''
CS144 Pandemaniac Project - 2016
Professor Wierman
Authors: Rushikesh Joshi and Johno Ikpeazu
'''

import sys
import json
import random

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

    # Create an empty list to store all of our nodes
    nodes = []

    # Append every node to our list "nodes"
    for key in data.keys():
        nodes.append(int(key))
    return nodes

def write_output(filename, nodes):
    # Open file to write results in for submission
    outPath = "results/" + filename + ".txt"
    output = open(outPath, 'w')

    # Generate random nodes to use for submission
    for i in range(50 * num_seeds):
        rand_val = random.randint(0, len(nodes) - 1)
        output.write(str(nodes[rand_val]) + "\n")

    output.close()

# Load the file as python argument
file_string = sys.argv[1]

# Remove the .json extension from file_string
filename = file_string[7:-5]

# Retrieve relevant (descriptive) info from graph name
num_players, num_seeds, id = parse_filename(filename)

# Retrieve list of all nodes
nodes = parse_graph(file_string)

write_output(filename, nodes)

