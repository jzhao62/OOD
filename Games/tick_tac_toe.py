class TicTacToe:
    def __init__(self):
        self.game_end = None
        self.board = [[0] * 3] * 3
        self.current_player_mark = None

    def initialize(self):
        self.game_end = False
        self.current_player_mark = 'X'

        for i in range(3):
            for j in range(3):
                self.board[i][j] = '-'

    def get_current_player(self):
        return self.current_player_mark

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-': return False;

        self.game_end = False;
        return True

    def change_player(self):
        if self.current_player_mark == 'X':
            self.current_player_mark = 'O'
        else:
            self.current_player_mark = 'X'

    # 游戏的核心部分
    def move(self, row, col):
        if self.is_board_full():
            raise GameEndException

        if self.board[row][col] != '-':
            raise AlreadyTakenException

        self.board[row][col] = self.current_player_mark

        # ----
        win = True
        for i in range(len(self.board)):
            if self.board[row][i] != self.current_player_mark:
                win = False
                break;

        if win:
            self.game_end = True;
            return win

        # ----

        win = True
        for i in range(len(self.board)):
            if self.board[i][col] != self.current_player_mark:
                win = False;
                break;
        if win:
            self.game_end = True
            return win

        # ----

        win = True
        for i in range(len(self.board)):
            if self.board[i][i] != self.current_player_mark:
                win = False;
                break
        if win:
            self.game_end = True;
            return win

        win = True

        for i in range(len(self.board)):
            if self.board[i][len(self.board) - i - 1] != self.current_player_mark:
                win = False
                break;

        if win:
            self.game_end = True
            return win


class GameEndException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__('Game has been ended, cannot make any moves')













class AlreadyTakenException(Exception):
    def __init__(self):
        super().__init__('This place is taken')


game = TicTacToe()
game.initialize()

game.move(0, 0)
game.change_player()
game.move(1,0)