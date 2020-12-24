#!/home/ted/advent-of-code/venv/bin/python3

# here we have a direct graph from container to contained
# *and* a number on each edge
# and then we recursively visit starting from the given node


import igraph
import re
import sys

def get_weighted_edges(line):
    container, contained_raw = re.match(
        r'^(.*) bags contain (.*)\.$', line).groups()
    contained_number_color_list = [x.strip() for x in contained_raw.split(',')]
    # print(container, contained_raw, contained_number_color_list)
    if contained_raw == 'no other bags':
        return []
    contained = [re.match(r'^([0-9]+) (.*) bags?$', x).groups()
                 for x in contained_number_color_list]
    return [(int(c[0]), container, c[1]) for c in contained]

def countem(g, start, weight):
    count = 1
    for edge in [g.es[e] for e in g.incident(start)]:
        count += countem(g, edge.target, edge['weight'])
    return count * weight

def main():
    edges = []
    for line in sys.stdin:
        line = line.rstrip()
        edges += get_weighted_edges(line)
    # weight source dest
    vertex_to_id = {}
    id = 0
    id_edges = []
    edge_weights = []
    for edge in edges:
        for vertex in edge[1:]:
            if not vertex in vertex_to_id:
                vertex_to_id[vertex] = id
                id += 1
        id_edges.append((vertex_to_id[edge[1]], vertex_to_id[edge[2]]))
        edge_weights.append(edge[0])
    g = igraph.Graph(directed=True,
                     edges=id_edges,
                     edge_attrs={'weight': edge_weights})

    print(g)
    start = vertex_to_id['shiny gold']

    result = countem(g, start, 1)
    print(result-1)
    
    
    # print('shiny gold', vertex_to_id['shiny gold'])
    

main()
