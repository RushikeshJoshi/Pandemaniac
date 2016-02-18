import sys
import json

def parse_graph(filename):
    # TODO
    return

def generate_seeds(num_seeds, graph):
    # TODO
    return
    
    
if __name__ == '__main__':
    filename = sys.argv[1]
    graph = load_graph(filename)
    num_players, num_seeds, unique_id = filename.split('.')
    
    seeds = generate_seeds(num_seeds, graph)
    for seed in seeds:
        sys.stdout.write(seed)
        sys.stdout.write('\n')