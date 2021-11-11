import json
import os
import subprocess as sp


class Dependency_parser:

  def __init__(self, file_path):
    self.path = file_path
    self.dependency = dict()
    self.externals_modules = list()

  def get_externals(self):
    output = sp.getoutput('pydeps DataMiner --externals')
    for e in output.split('[')[1].split('\n'):
      if e and e != "]":
        e = e.split(',')[0].split('"')[1]
        self.externals_modules.append(e)

  def add_dependency(self):
    f = open(self.path,)
    data = json.load(f)

    for module in data:
      print(module)
      if module.split('.')[0] not in self.externals_modules and "imports" in data[module]:
          initial_modules = data[module]["imports"]
          final_modules = []
          for i in initial_modules:
            if i.split('.')[0] not in self.externals_modules:
              final_modules.append(i)
          if final_modules:
            self.dependency[module] = final_modules
    print(self.dependency)
    
    f.close()

if __name__ == '__main__':
  path = 'test.json'
  dp = Dependency_parser(path)
  dp.get_externals()
  dp.add_dependency()