from extraction.output import extract_output
from transformation.files import read_from
from transformation.transform_counterpicks import transform_counterpicks
from transformation.champions_dict import create_dict, read_dictionary
from extraction.counterpick import extract_counterpicks
from extraction.stats import extract_stats
from extraction.cost import extract_costs
from extraction.positions import extract_positions
from extraction.similarity import extract_similarity
from model.model import execute_model

extract_costs()
extract_positions()
extract_similarity()
extract_stats()
extract_counterpicks()

create_dict()

transform_counterpicks()

values = read_from("input.txt")

r1,r2,r3,r4,r5,o = [int(v[0]) for v in values]

dict = read_dictionary("data/champions_dict.txt")

execute_model(r1,r2,r3,r4,r5,o,dict)

extract_output("_save.mip",dict)