# parsing output from "jdeps -v ./build/libs/mockito-core-4.1.1-SNAPSHOT.jar > jdeps-output.txt"
from pprint import pprint
import argparse
import json

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, default="mockito")

    return parser


if __name__ == '__main__':
    args = argparser().parse_args()
    input_file = "deps/{}.json".format(args.project)
    output_file = "results/{}_org.json".format(args.project)
     
    with open(input_file, 'r') as f:
        dep_graph = json.load(f)
    
    cluster = {}
    for node in dep_graph.keys():
        cluster[node] = '.'.join(node.split('.')[:-1])

    with open(output_file, 'w') as f:
        json.dump(cluster, f, sort_keys=True, indent=4)
