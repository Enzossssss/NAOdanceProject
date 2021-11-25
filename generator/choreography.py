from aima.search import *
from time import sleep
from position import *

pos = POSITION
man_pos = MANDATORY_POSITION

""" state: (current position, number of move, time to arrive at current position, list of previous position) """


class Choreography(Problem):

    def __init__(self, initial, goal):
        self.initial = (initial[0], initial[1],
                        initial[2], tuple(initial[-1], ))
        self.goal = (goal[0], goal[1], goal[2], tuple(goal[-1]))
        Problem.__init__(self, initial, goal)

    def isValid(self, state):
        position, counter, time, moves = state
        if time < self.goal[2] and self.goal[0] not in moves:
            return True
        else:
            return False

    def actions(self, state):
        # sleep(1)
        if not self.isValid(state):
            #print('sono dentro')
            return []

        position, counter, time, moves = state

        if position == 'Sit' or position == 'SitRelax':
            return [('Sit', 'Stand')]

        result = [(position, nextPosition)
                  for nextPosition in pos.keys() if nextPosition not in moves]
        result.append((position, self.goal[0]))
        #print('RESULT OF ACTION:', result)
        return result

    def result(self, state, action):
        # sleep(1)
        #print('ACTION OF RESULT:', action)
        position, counter, time, moves = state

        nextPosition = action[-1]

        list_moves = list(moves)
        list_moves.append(nextPosition)

        if nextPosition in pos.keys():
            return (nextPosition, counter + 1, time + pos[nextPosition], tuple(list_moves))
        if nextPosition in man_pos.keys():
            return (nextPosition, counter + 1, time + man_pos[nextPosition], tuple(list_moves))

    def goal_test(self, state):
        #print('STATE OF GOAL_TEST:', state)
        position, counter, time, moves = state
        positionGoal, counterGoal, timeGoal, moves = self.goal

        return position == positionGoal and counter >= counterGoal and (time >= timeGoal-5 and time <= timeGoal)


def generate(start, end):
    return Choreography((start, 0, man_pos[start],
                         (start, )), (end, 5, 20, ()))


def main():
    pos = list(man_pos.keys())
    final = []

    print('Generating choreography...')

    for i in range(len(pos) - 1):
        final.append(pos[i])

        problem = generate(pos[i], pos[i+1])
        solution = depth_first_graph_search(problem)
        if solution != None:
            final.extend(solution.state[-1][1:-1])

    final.append(pos[-1])

    print()
    print('Choreograph: ')
    print(final)

    print()
    print('Choreograph will be start...')

    with open("../choreography.txt", "w") as file:
        for row in final:
            if row == pos[-1]:
                file.write(str(row))
            else:
                file.write(str(row) + '\n')


if __name__ == '__main__':
    main()
