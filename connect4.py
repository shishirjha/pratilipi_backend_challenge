class Connect4:
    def __init__(self):
        self.no_of_rows = 6  # height
        self.no_of_columns = 7  # width
        self.board = [['' for x in range(self.no_of_columns)]
                      for i in range(self.no_of_rows)]
        self.no_of_moves = 1

    def return_board(self):
        return self.board

    def get_column(self, index):
        return [i[index] for i in self.board]

    def get_row(self, index):
        return self.board[index]

    def get_diagonals(self):
        diagonals = []
        for p in range(self.no_of_rows + self.no_of_columns - 1):
            diagonals.append([])
            for q in range(max(p - self.no_of_rows + 1, 0),
                           min(p + 1, self.no_of_rows)):
                diagonals[p].append(self.board[self.no_of_rows - p + q - 1][q])
        for p in range(self.no_of_rows + self.no_of_columns - 1):
            diagonals.append([])
            for q in range(max(p - self.no_of_rows + 1, 0),
                           min(p + 1, self.no_of_rows)):
                diagonals[p].append(self.board[p - q][q])
        return diagonals

    def make_move(self, player, col):
        if player not in ['Y', 'R']:
            return self.board, "Invalid"
        if self.no_of_moves % 2 == 0 and player == 'Y' or (self.no_of_moves % 2 != 0 and player == 'R'):
            return self.board, "Invalid"
        if '' not in self.get_column(col):
            return self.board, "Invalid"  # if no space in column return invalid
        i = self.no_of_rows - 1
        while self.board[i][col] != '':
            i -= 1
        self.board[i][col] = player
        self.no_of_moves += 1
        return self.board, "Valid"

    def check_win(self):
        for i in range(self.no_of_rows):  # check rows
            for x in range(self.no_of_columns - 3):
                if self.get_row(i)[x:x + 4] in [['0', '0',
                                                 '0', '0'], ['1', '1', '1', '1']]:
                    return self.board[i][x]
        for i in range(self.no_of_columns):  # check columns
            for x in range(self.no_of_rows - 3):
                if self.get_column(
                        i)[x:x + 4] in [['0', '0', '0', '0'], ['1', '1', '1', '1']]:
                    return self.board[x][i]
        for i in self.get_diagonals():
            for x in range(len(i)):
                if i[x:x + 4] in [['0', '0', '0', '0'], ['1', '1', '1', '1']]:
                    return i[x]

        return None


boardForConnect4 = Connect4()
board, validity = boardForConnect4.make_move('Y', 0)
board, validity = boardForConnect4.make_move('R', 0)
board, validity = boardForConnect4.make_move('Y', 0)
board, validity = boardForConnect4.make_move('R', 0)
board, validity = boardForConnect4.make_move('Y', 0)
board, validity = boardForConnect4.make_move('R', 0)
board, validity = boardForConnect4.make_move('Y', 0)

print(validity)
print(boardForConnect4.board)
# print(boardForConnect4.get_diagonals())
