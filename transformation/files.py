def read_from(path):
    with open(path) as file:
        return  [line.replace('\n','').split(',') for line in file.readlines()]