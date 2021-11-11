import javalang
import os
import sys
from collections import defaultdict

class Javadeps_parser:
    def __init__(self):
        self.allFiles = list()
        self.dependencies = defaultdict(set)
        self.valid_imports = 'patterns'

    def find_dependencies(self, source):
        ast = javalang.parse.parse(source)
        # print(ast)

        for imp in ast.imports:
            # print(imp)
            if not imp.path.startswith(self.valid_imports):
                continue
            else:
                self.dependencies[ast.package.name].add(imp.path)

            
    def parse_files(self):
        for file in self.allFiles:
            f = open(file)
            source = f.read()
            f.close()

            self.find_dependencies(source)
        print(self.dependencies)

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
    dirName = 'DesignPatterns-master/src/patterns'
    jdeps_parser = Javadeps_parser()
    listOfFiles = jdeps_parser.get_java_files(dirName)
    # print(listOfFiles)
    jdeps_parser.parse_files()
