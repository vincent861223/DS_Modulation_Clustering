# parsing output from "jdeps -v ./build/libs/mockito-core-4.1.1-SNAPSHOT.jar > jdeps-output.txt"
from pprint import pprint
import argparse
import json

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest='input_file', type=str, default="jdeps-output.txt")
    parser.add_argument("-o", dest='output_file', type=str, default="dep.json")

    return parser


class JdepsParser:
    def __init__(self, f, p_name):
        self.file = f
        self.package_name = p_name

    def get(self):
        deps_set = dict()

        with open(self.file) as f:
            for line in f:
                elements = line.split()
                if len(elements) < 3 or \
                        self.package_name not in elements[0] or \
                        self.package_name not in elements[2]:
                    continue
                key = elements[0]
                val = elements[2]
                if 'internal' in key: continue
                if key not in deps_set:
                    deps_set[key] = {}
                    deps_set[key]["imports"] = set()

                if 'internal' in val: continue
                deps_set[key]["imports"].add(val)

                if val not in deps_set:
                    deps_set[val] = {}
                    deps_set[val]["imports"] = set()

        # convert set to list
        for k, v in deps_set.items():
            v["imports"] = list(v["imports"])

        return deps_set


if __name__ == '__main__':
    args = argparser().parse_args()
    jdeps_parser = JdepsParser(f=args.input_file, p_name="org.mockito")
    # pprint(jdeps_parser.get())
    with open(args.output_file, 'w') as f:
        json.dump(jdeps_parser.get(), f, sort_keys=True, indent=4)
