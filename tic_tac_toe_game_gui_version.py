import random
from player_gui import Human, CPU, GoodCPU

class Game:
    def __init__(self):
        self.board = ["" for i in range(9)]
        self.current_turn = "X"
        self.current_winner = None
        self.recent_move = -1
        self.player_choice = ""
        self.order = ""
        self.difficulty = ""
        self.winning_three = []

    def reset(self):
        self.board = ["" for i in range(9)]
        self.current_turn = "X"
        self.current_winner = None
        self.recent_move = -1
        self.player_choice = ""
        self.order = ""
        self.difficulty = ""
        self.winning_three.clear()
    
    def available_moves(self):
        i = 0
        available_moves = []
        for x in self.board: 
            if x == "":
                available_moves.append(i)
            i += 1
        return available_moves

    def check_win_no_result(self):
        if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != "":
            return True
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != "":
            return True
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != "":
            return True
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != "":
            return True
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != "":
            return True
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != "":
            return True
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != "":
            return True
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != "":
            return True
        else:
            return False

    def check_win(self):
        if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(0)
                self.winning_three.append(1)
                self.winning_three.append(2)
            return True
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(3)
                self.winning_three.append(4)
                self.winning_three.append(5)
            return True
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(6)
                self.winning_three.append(7)
                self.winning_three.append(8)
            return True
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(0)
                self.winning_three.append(3)
                self.winning_three.append(6)
            return True
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(1)
                self.winning_three.append(4)
                self.winning_three.append(7)
            return True
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(2)
                self.winning_three.append(5)
                self.winning_three.append(8)
            return True
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(0)
                self.winning_three.append(4)
                self.winning_three.append(8)
            return True
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != "":
            if self.winning_three:
                pass
            else:
                self.winning_three.append(2)
                self.winning_three.append(4)
                self.winning_three.append(6)
            return True
        else:
            return False
    
    def full_board(self):
        for i in self.board:
            if i == "":
                return False
        return True

    def is_empty(self):
        return "" in self.board
    
    def num_empty(self):
        return self.board.count("")

    def play_move(self, index, letter):
        self.board[index] = letter
        if self.check_win_no_result():
            self.current_winner = letter



            