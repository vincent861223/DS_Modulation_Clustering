from graphviz import Digraph
from collections import defaultdict
import json
import argparse



def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, default="mockito")
    parser.add_argument("--type", type=str, required=True)

    return parser

g = Digraph('G', filename='cluster.gv')
dependency_dict = defaultdict(list)

def read_json(json_file):
     
    f = open(json_file)
    data = json.load(f)
    for i in data:
        dependency_dict[data[i]].append(i)
    # print(dependency_dict)
    f.close()

def draw_clusters(cluster, nodes):
    cluster_name = 'cluster_' + str(cluster)
    with g.subgraph(name=cluster_name) as c:
        c.attr(rank='same')
        c.attr(color='blue')
        c.node_attr['style'] = 'filled'
        for n in nodes:
            c.node(n)
        # c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
        c.attr(label=cluster_name)

def draw_edges(dep_file):
    f = open(dep_file)
    data = json.load(f)
    f.close()

    dependency_set = set()
    for i in data:
        if "imports" not in data[i]:
            continue
        for to in data[i]["imports"]:
            dependency_set.add((i, to))
            
    for p, q in dependency_set:
        # print(p + "  ->  " + q)
        g.edge(p, q)

if __name__ == '__main__':
    args = argparser().parse_args()
    cluster_file = "results/{}_{}.json".format(args.project, args.type)
    dep_file = "deps/{}.json".format(args.project)
    read_json(cluster_file)
    for k, v in dependency_dict.items():
        draw_clusters(k, v)
    draw_edges(dep_file)
    g.graph_attr['rankdir'] = 'LR'
    g.view()