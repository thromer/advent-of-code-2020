#!/home/ted/advent-of-code/venv/bin/python3

# seems like
# we need a directed graph (from 'contained' to 'contains')
# we need to see what is reachable from a given node
# so we tr

import igraph
import re
import sys

def get_edges(line):
    container, contained_raw = re.match(
        r'^(.*) bags contain (.*)\.$', line).groups()
    contained_number_color_list = [x.strip() for x in contained_raw.split(',')]
    # print(container, contained_raw, contained_number_color_list)
    if contained_raw == 'no other bags':
        return []
    contained = [re.match(r'^[0-9]+ (.*) bags?', x)[1]
                 for x in contained_number_color_list]
    return [(c, container) for c in contained]

def main():
    edges = []
    for line in sys.stdin:
        line = line.rstrip()
        edges += get_edges(line)
    vertex_to_id = {}
    id = 0
    id_edges = []
    for edge in edges:
        for vertex in edge:
            if not vertex in vertex_to_id:
                vertex_to_id[vertex] = id
                id += 1
        id_edges.append((vertex_to_id[edge[0]], vertex_to_id[edge[1]]))
    print(id_edges)
    g = igraph.Graph(directed=True, edges=id_edges)
    print('shiny gold', vertex_to_id['shiny gold'])
    asp = g.get_all_shortest_paths(vertex_to_id['shiny gold'])
    destinations = set()
    for p in asp:
        destinations.add(p[-1])
    print(destinations)
    print(len(destinations)-1)
        
    

main()
