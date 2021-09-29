import os
import ast

def create_dict():
    filename = "data/champions_dict.txt"
    if os.path.isfile(filename):
        return

    data = []
    with open("data/counterpicks.txt") as file:
        data = [line.replace('\n','').split(',') for line in file.readlines()]
        champions_names = [name[0] for name in data]
        champions_dict = {champions_names[i]: i for i in range(len(data))}

        outfile = open(filename, "w")
        outfile.write(str(champions_dict))
        outfile.close()
 
def read_dictionary(path):
    with open(path) as file:
        contents = file.read()
        return ast.literal_eval(contents)