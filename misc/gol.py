import os
import time

class Gol:
    def __init__(self):
        # initialize
        self.columns = 60
        self.rows = 30
        self.state = [[x % 2 == 2 for x in range(self.columns)] for y in range(self.rows)]
        self.state[3][3] = True
        self.state[3][4] = True
        self.state[3][5] = True
        self.state[5][3] = True
        self.state[5][4] = True
        self.state[5][5] = True
        self.state[6][3] = True
        self.state[6][4] = True
        self.state[6][5] = True
        self.state[7][5] = True
        self.state[7][3] = True
        self.state[7][4] = True
        self.state[7][5] = True
        self.state[7][7] = True
        self.state[7][8] = True
        self.state[7][9] = True
        self.state[7][4] = True
        self.state[9][3] = True
        self.state[9][4] = True
        self.state[9][7] = True
        self.state[9][8] = True
        self.state[9][9] = True
        self.state[9][10] = True
        self.state[29][3] = True
        self.state[29][4] = True
        self.state[29][5] = True
        self.state[15][3] = True
        self.state[15][4] = True
        self.state[15][5] = True
        self.state[16][13] = True
        self.state[16][14] = True
        self.state[16][15] = True
        self.state[17][15] = True
        self.state[17][13] = True
        self.state[17][14] = True
        self.state[17][15] = True
        self.state[17][17] = True
        self.state[17][18] = True
        self.state[17][19] = True
        self.state[17][14] = True
        self.state[19][13] = True
        self.state[19][14] = True
        self.state[19][17] = True
        self.state[19][18] = True
        self.state[19][19] = True
        self.state[19][10] = True

    def run(self):

        for i in range(200):
            os.system('clear')
            time.sleep(0.1)
            self.print_state()
            print('generation: ' + str(i))
            next_state = []
            for k in range(self.rows):
                row = []
                for j in range(self.columns):
                    row.append(self.will_live(j, k))
                next_state.append(row)

            self.state = next_state

    def will_live(self, c, r):
        neighbours = 0
        if self.is_alive(c+1, r):
            neighbours += 1
        if self.is_alive(c-1, r):
            neighbours += 1

        if self.is_alive(c, r+1):
            neighbours += 1
        if self.is_alive(c, r-1):
            neighbours += 1

        if self.is_alive(c+1, r+1):
            neighbours += 1
        if self.is_alive(c-1, r-1):
            neighbours += 1

        if self.is_alive(c-1, r+1):
            neighbours += 1
        if self.is_alive(c+1, r-1):
            neighbours += 1

        if neighbours == 3:
            return True
        if self.is_alive(c, r) and neighbours == 2:
            return True
        else:
            return False

    def is_alive(self, c, r):
        if c < 0 or c >= self.columns or r < 0 or r >= self.rows:
            return False
        return self.state[r][c]

    def print_state(self):
        for r in self.state:
            row = ''
            for c in r:
                row += '*' if c else ' '
            print(row)
