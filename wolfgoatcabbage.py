from search import *

class WolfGoatCabbage(Problem):
    def __init__(self):
        super().__init__(frozenset(['F', 'G', 'W', 'C']), frozenset())
        #initialstate = frozenset({'F', 'G', 'W', 'C'})
        #goalstate = ({})
        #forbidden = frozenset({'F', 'C'}, {'F', 'W'}, {'F', 'G'})

    def goal_test(self, state):
        return state == frozenset(['F', 'G', 'W', 'C'])

    def result(self, state, action):
        new_state = self.state
        if 'F' in state:
            new_state.remove(obj) # set function / difference

        elif 'F' in action:
                new_state.add(obj) # union add another character

        return frozenset(new_state)

    def actions(self, state):
        left_bank = set(state)
        right_bank = set(['F', 'G', 'W', 'C']) - left_bank
        actions = []
        if 'F' in left_bank:
            for obj in left_bank:
                if obj != 'F':
                    actions.append(frozenset([obj]))
            if 'G' in left_bank:
                actions.append(frozenset(['G', 'F']))
            if 'C' in left_bank:
                actions.append(frozenset(['C', 'F']))
            if 'W' in left_bank and 'G' not in left_bank:
                actions.append(frozenset(['W', 'F']))
        return actions

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)