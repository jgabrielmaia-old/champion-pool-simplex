import os
from transformation.champions_dict import read_dictionary

def transform_counterpicks():
    filename = "data/nullifiers.txt"
    if os.path.isfile(filename):
        return
    
    champion_dict = read_dictionary("data/champions_dict.txt")
    nullifiers =  find_nullifiers("data/counterpicks.txt", champion_dict)
    
    content = ''
    for nullifier in nullifiers:
        content += ','.join(nullifier) + '\n'

    outfile = open(filename, "w")
    outfile.write(content)
    outfile.close()

def find_nullifiers(path, champion_dict):
    with open(path) as counterpicks_file:
        champion_counterpicks = [line.replace('\n','').split(',') for line in counterpicks_file.readlines()]

        nullifiers = []
        for counter_list in champion_counterpicks:
            champion = counter_list[0]
            champion_counters = counter_list[1:]
             
            counters_nullifiers = [champion_counterpicks[champion_dict[champion_counter]] for champion_counter in champion_counters]
            
            champion_nullifiers = list(set(flatten(counters_nullifiers)))
            champion_nullifiers.insert(0,champion)
            nullifiers += [champion_nullifiers]
        
        return nullifiers

def flatten(t):
    return [item for sublist in t for item in sublist]