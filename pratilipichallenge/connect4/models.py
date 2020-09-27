from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Game(models.Model):
    YELLOW = 'Y'
    RED = 'R'
    PLAYER_CHOICES = [
        (YELLOW, 'First Player'),
        (RED, 'Second Player'),
    ]
    VALIDITY_CHOICES = [
        ('Valid', 'Valid'),
        ('Incalid', 'Invalid'),
    ]
    no_of_rows = models.IntegerField(default=6, editable=False)
    no_of_columns = models.IntegerField(default=7, editable=False)
    column = models.IntegerField()
    validity = models.CharField(
        max_length=255,
        choices=VALIDITY_CHOICES, null=True, blank=True)
    board = ArrayField(
        ArrayField(
            models.CharField(
                max_length=1,
                choices=PLAYER_CHOICES,
                default='X',
                blank=True,
                null=True
                
            ),
            size=7,
            null=True
        ),
        size=6,
        null=True
    )
    no_of_moves = models.IntegerField(default=1)
    player = models.CharField(max_length=255,
                              choices=PLAYER_CHOICES, null=True, blank=True)

    @property
    def return_board(self):
        return self.board

    @property
    def get_column(self, index):
        return [i[index] for i in self.board]

    @property
    def get_row(self, index):
        return self.board[index]

    @property
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

    @property
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

    @property
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


