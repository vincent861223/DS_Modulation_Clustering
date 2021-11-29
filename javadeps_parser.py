import javalang
import json
import os
import sys
from collections import defaultdict

class Javadeps_parser:
    def __init__(self):
        self.allFiles = list()
        self.dependencies = defaultdict(set)
        self.valid_imports = 'org.mockito'

    def find_dependencies(self, fname, source):
        ast = javalang.parse.parse(source)
        # print(ast)
        output = dict()
        for imp in ast.imports:
            # print(imp)
            if not imp.path.startswith(self.valid_imports):
                continue
            else:
                self.dependencies[fname].add(imp.path)

            #     self.dependencies[ast.package.name].add(imp.path)
            # for i in list(self.dependencies):
            #     output[i] = {'imports': list(self.dependencies[i])}
            # with open('java_dep.json', 'w') as f:
            #     json.dump(output, f, indent=4)

    def parse_files(self):
        for file in self.allFiles:
            filename = file.replace('/', '.')
            fname = 'org.' + filename[:-5]

            f = open(file)
            source = f.read()
            f.close()

            self.find_dependencies(fname, source)
        print(self.dependencies)
        # with open('dep.json', 'w') as f:
        #     json.dump(self.dependencies, f, sort_keys=True, indent=4)

    def get_java_files(self, dirName):
        # create a list of file and sub directories
        # names in the given directory
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles = allFiles + self.get_java_files(fullPath)
            else:
                if fullPath.endswith(".java"):
                    allFiles.append(fullPath)

        self.allFiles = allFiles
        return allFiles

if __name__ == '__main__':
    dirName = 'mockito/src/main/java/org/mockito'
    jdeps_parser = Javadeps_parser()
    listOfFiles = jdeps_parser.get_java_files(dirName)
    # print(listOfFiles)
    jdeps_parser.parse_files()
