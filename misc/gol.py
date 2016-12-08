

class Gol:
    def __init__(self):
        pass

    def run(self):
        # initialize
        state = [[x % 2 == 0 for x in range(30)] for y in range(10)]

        self.print_state(state)

    def print_state(self, state):
        for r in state:
            row = ''
            for c in r:
                row += '*' if c else ' '
            print(row)