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

def generate_nodes(graph, num_seeds):
    
    seeds = []
    max_ind, cliques = clique.clique_removal(graph)
    # sort such that the largest cliques are in front
    cliques = map(list, (sorted(cliques, key = len, reverse = True)))
    # [ [(n11, deg(n11), (n12, deg(n12)), ... (n1m, deg(n1m))], [(n21, deg(n21)), ( 
    clique_degree = map(lambda clique: map(lambda node: (node, nx.degree(graph, node)), clique), cliques)
    clique_degree = map(lambda clique: sorted(clique, key = lambda (node, degree): degree, reverse = True), clique_degree)
    
    degree_rank_within_clique = 0
    while len(seeds) < num_seeds:
        clique_degree = filter(lambda cliq: len(cliq) > degree_rank_within_clique, clique_degree) 
        seeds.extend(cliq[degree_rank_within_clique][0] for cliq in clique_degree if cliq[degree_rank_within_clique][0] not in seeds)
    
    return seeds[:num_seeds]

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
    nodes = generate_nodes(graph, num_seeds)
    
    # Write the values to output file
    write_output(filename, nodes, num_seeds)