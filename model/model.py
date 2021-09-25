from transformation.transform_counterpicks import flatten
from transformation.files import read_from
from pymprog import *

def champion_equations(dict):
    positions_file = read_from("data/positions.txt")
    similarity_file = read_from("data/similarity.txt")
    stats_file = read_from("data/stats.txt")

    positions = [[int(p) for p in position[1:]] for position in positions_file]
    similarities = [[int(s) for s in similarity[1:]] for similarity in similarity_file]
    stats = [[int(float(s)*100) for s in stats[2:]] for stats in stats_file]

    return [positions[dict[key]] + 
           similarities[dict[key]] + 
           stats[dict[key]] for key in dict]

def execute_model(r1,r2,r3,r4,r5,o,dict):
    # data blocks

    stats_file = read_from("data/stats.txt")

    victory_rates = flatten([[int(float(s)*100) for s in stats[1:2]] for stats in stats_file])

    R = victory_rates

    champion_equation = champion_equations(dict)
    A = champion_equation

    costs_file = read_from("data/costs.txt")
    costs = flatten([[int(s) for s in costs[1:2]] for costs in costs_file])
    
    b = [1 for _ in range(155)]

    # model blocks
    begin('champion pool selection')

    verbose(True)

    champions = range(155)
    x = var('r', champions, bool)
    
    maximize(sum(R[i]*x[i] for i in champions))

    # cada conjunto de atributos por campeao >= 1
    for i in champions: 
        sum(A[i][j]*x[j] for j in range(len(champion_equation[0]))) >= b[i]

    # numero de campeoes final na solucao = 20
    sum(x[i] for i in champions) <= 20
    sum(x[i] for i in champions) >= 20

    # restricao de orcamento <= O
    sum(x[i]*costs[i] for i in champions) <= int(o)

    # restricao de champions da posicao r1 >= 8
    sum(A[i][r1]*x[i] for i in champions) >= 8

    # restricao de champions da posicao r2 >= 7
    sum(A[i][r2]*x[i] for i in champions) >= 7

    # restricao de champions da posicao r3+r4+r5 >= 3
    sum(A[i][r3]*x[i] for i in champions) >= 1
    sum(A[i][r4]*x[i] for i in champions) >= 1
    sum(A[i][r5]*x[i] for i in champions) >= 1

    solve()

    # report block
    print(f"###>Objective value: {vobj()}")
    # sensitivity()

    save(mip='_save.mip')
    end()