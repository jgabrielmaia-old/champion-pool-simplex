def extract_output(path,dictionary):
    with open(path) as file:
        lines = [[int(line.split()[0]), line.split()[3]] for line in file.readlines()[175:330]]
        new_dict = dict([(value, key) for key, value in dictionary.items()])
        
        champions = []
        for l in lines:
            if int(l[1]) == 1:
                champions += [new_dict[l[0]]]
        
        outfile = open("output.txt", "w")
        outfile.write(','.join(champions))
        outfile.close()  