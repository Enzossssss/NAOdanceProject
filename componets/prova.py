from aima.utils import *
from aima.planning import *
import random
import dati

c = 0


def counter():
    global c
    c += 1
    return c


solution = []

for i in range(len(dati.MANDATORY_POSITION) - 1):
    print("From " + dati.MANDATORY_POSITION[i] +
          " to " + dati.MANDATORY_POSITION[i + 1])
##################################################################################################################################
    temp_solution = []

    temp_compatibilities = dati.COMPATIBILITIES
    ##################################################################################################################################
    knowledge = []

    for pos, comp_pos in temp_compatibilities.items():
        for p in comp_pos:
            knowledge.append(
                expr("Compatible(" + str(pos) + "," + str(p) + ")"))

    for i in range(0, 7):
        knowledge.append(
            expr("NextNumber(" + str(i) + "," + str(i+1) + ")"))

    knowledge.extend([expr("In(" + dati.MANDATORY_POSITION[i] + ")")])
    knowledge.extend([expr("C(0)")])

    move = Action('Move(x, y) & Increment(z, k)', precond='In(x) & Compatible(x, y) & Number(z) & NextNumber(z, k)',
                  effect="In(y) & ~In(x) & C(k) & ~C(z)", domain='Position(x) & Position(y) & Number(z) & Number(k)')

    goals = "In(" + dati.MANDATORY_POSITION[i + 1] + ") & C(6)"

    positions_domain = ""
    for p in dati.ALL_POSES:
        positions_domain += "Position(" + str(p) + ") & "
    for i in range(0, 7):
        positions_domain += "Number(" + str(i) + ") & "
    positions_domain = positions_domain[:len(positions_domain) - 3]

    problem = PlanningProblem(initial=knowledge, goals=goals, actions=[
        move], domain=positions_domain)
    # print('ok')
    # solution_c = SATPlan(problem, 5)
    # print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(solution_c)
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@++++++++\n')

    piece_solution = GraphPlan(problem).execute()

    temp_solution.extend(linearize(piece_solution))

    print('\n-----------------------------------------------------------------------------------------------')
    print(temp_solution)
    print('----------------------------------------------------------------------------------------------------------\n')

    solution.extend(temp_solution)

print(solution)
