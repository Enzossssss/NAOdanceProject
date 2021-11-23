from aima.utils import *
from aima.planning import *
import random
import dati


def extract_dest(move):
    # return str(move).split(" ")[-1].removesuffix(")")
    string = str(move).split(" ")[-1]
    return string[:len(string)-1]


def generate_choreography(moves):
    choreography = [str(moves[0]).split("(")[1].split(",")[0]]
    for move in moves:
        #choreography.append(str(move).split(" ")[1].removesuffix(")"))
        string = str(move).split(" ")[-1]
        string = string[:len(string)-1]
        choreography.append(string)
    return choreography


solution = []

for i in range(len(dati.MANDATORY_POSITION) - 1):
    print("From " + dati.MANDATORY_POSITION[i] +
          " to " + dati.MANDATORY_POSITION[i + 1])

    """ solution_part = generate_positions(compatibilities=compatibilities,
                                           initial=positions[i],
                                           final=positions[i + 1],
                                           min_moves=min_moves) """
##################################################################################################################################
    temp_solution = []

    while True:

        temp_compatibilities = dati.randcompatibilities()

        """ solution.extend(plan_positions(used_compatibilities, initial=initial, final=final)) """
        ##################################################################################################################################
        knowledge = []

        for pos, comp_pos in temp_compatibilities.items():
            for p in comp_pos:
                knowledge.append(
                    expr("Compatible(" + str(pos) + "," + str(p) + ")"))

        knowledge.extend([expr("In(" + dati.MANDATORY_POSITION[i] + ")")])

        move = Action('Move(x, y)', precond='In(x) & Compatible(x, y)',
                      effect='In(y) & ~In(x)', domain='Position(x) & Position(y)')

        goals = "In(" + dati.MANDATORY_POSITION[i + 1] + ")"

        positions_domain = ""
        for p in dati.ALL_POSES:
            positions_domain += "Position(" + str(p) + ") & "
        positions_domain = positions_domain[:len(positions_domain) - 3]

        problem = PlanningProblem(initial=knowledge, goals=goals, actions=[
                                  move], domain=positions_domain)

        piece_solution = GraphPlan(problem).execute()

        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(piece_solution)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

        temp_solution.extend(linearize(piece_solution))

        print('\n-----------------------------------------------------------------------------------------------')
        print(temp_solution)
        print('----------------------------------------------------------------------------------------------------------\n')

        ##################################################################################################################################

        if len(temp_solution) >= dati.MIN - 1:
            break

        temp_solution.remove(temp_solution[-1])

        # if len(temp_solution) > 0:
        #     second_last = extract_dest(temp_solution[-1])
        #     temp_compatibilities.get(second_last).remove(
        #         dati.MANDATORY_POSITION[i + 1])
        #     initial = second_last
        # else:
        #     temp_compatibilities.get(dati.MANDATORY_POSITION[i]).remove(
        #         dati.MANDATORY_POSITION[i + 1])

        """ # artistic correction: remove looping moves
            if len(temp_solution) >= 4:
                for i in range(len(temp_solution) - 3):
                    if temp_solution[i] == temp_solution[i + 2] and temp_solution[i + 1] == temp_solution[i + 3]:
                        first = extract_dest(temp_solution[-1])
                        second = extract_dest(temp_solution[-2])
                        temp_solution = temp_solution[:len(temp_solution) - 2]
                        temp_compatibilities.get(first).remove(second)
                        break """
        ##################################################################################################################################
    solution.extend(temp_solution)
    if i != len(dati.ALL_POSES) - 2:
        solution = solution[:len(solution)]

    """ # assumes more ways
        choreography_part = generate_choreography(temp_solution)
        for j in range(len(choreography_part) - 2):
            dati.COMPATIBILITIES[choreography_part[j]].remove(choreography_part[j + 1])
        if (not choreography_part[1] in dati.ALL_POSES):
            dati.COMPATIBILITIES.pop(choreography_part[1], None) """
c = generate_choreography(solution)
print(c)


def generate_choreography(moves):
    choreography = [str(moves[0]).split("(")[1].split(",")[0]]
    for move in moves:
        #choreography.append(str(move).split(" ")[1].removesuffix(")"))
        string = str(move).split(" ")[-1]
        string = string[:len(string)-1]
        choreography.append(string)
    return choreography


""" def generate_choreography_file(choreography):
    f = open("choreography.txt", "w")
    for move in choreography:
        f.write(str(move)+"\n")
    f.close()
    print("Choreography exported in choreography.txt" """
