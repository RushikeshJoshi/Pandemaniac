'''
CS144 Pandemaniac Project - 2016
Professor Wierman
Authors: Rushikesh Joshi and Johno Ikpeazu

This algorithm will generate nodes for submission that have the greatest 
degree centrality.
'''

import sys
import json
import random
import networkx as nx
from networkx.algorithms.approximation import clique
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
    max_ind, cliques = clique.clique_removal(graph)
    cliques = sorted(cliques, key = len, reverse = True)
    clique_degree = map(lambda clique: map(lambda node: (node, nx.degree(graph, node)), clique), cliques)
    clique_degree = map(lambda clique: sorted(clique, reverse = True, key = lambda (node, degree): degree), clique_degree)
    return [cliq[0][0] for cliq in clique_degree]

def write_output(filename, nodes, num_seeds):
    # Open file to write results in for submission
    outPath = "results/" + filename + "_clique.txt"
    output = open(outPath, 'w')

    # Generate random nodes to use for submission
    for i in range(50):
        for j in range(num_seeds):
            output.write(str(nodes[j][0]) + "\n")

    output.close()

if __name__ == '__main__':
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
    
    # Write the values to output file
    write_output(filename, nodes, num_seeds)