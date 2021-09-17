from transformation.transform_counterpicks import transform_counterpicks
from transformation.champions_dict import create_dict
from extraction.counterpick import extract_counterpicks
from extraction.stats import extract_stats
from extraction.cost import extract_costs
from extraction.positions import extract_positions
from extraction.similarity import extract_similarity

extract_costs()
extract_positions()
extract_similarity()
extract_stats()
extract_counterpicks()

create_dict()

transform_counterpicks()