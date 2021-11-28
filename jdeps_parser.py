# parsing output from "jdeps -v ./build/libs/mockito-core-4.1.1-SNAPSHOT.jar > jdeps-output.txt"
from pprint import pprint


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
                if key not in deps_set:
                    deps_set[key] = {}
                    deps_set[key]["imports"] = set()

                deps_set[key]["imports"].add(val)

        # convert set to list
        for k, v in deps_set.items():
            v["imports"] = list(v["imports"])

        return deps_set


if __name__ == '__main__':
    jdeps_parser = JdepsParser(f="./jdeps-output.txt", p_name="org.mockito")
    pprint(jdeps_parser.get())
