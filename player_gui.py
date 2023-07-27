import random
import math
import time
from zoneinfo import available_timezones

class Player:
    def __init__(self, symbol):
        self.symbol = symbol 

class CPU(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def move_choice(self, game):
        move_choice = random.choice(game.available_moves())
        index = game.available_moves().index(move_choice)
        del game.available_moves()[index]
        return move_choice

class MediumCPU(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.move_number = 0
    
    def move_choice(self, game):
        if len(game.available_moves()) == 9:
            move_choice = random.choice(game.available_moves())
            self.move_number += 1
            return move_choice
        else:
            if random.randint(0,2) == 1:
                move_choice = random.choice(game.available_moves())
                index = game.available_moves().index(move_choice)
                del game.available_moves()[index]
                return move_choice
            else:
                move_choice = self.minimax(game, self.symbol)["position"]
                return move_choice
    
    def minimax(self, game, player_letter):
        max_player = self.symbol
        other_player = "O" if player_letter == "X" else "X"
        
        if game.current_winner == other_player:
            return {"position" : None,
                    "score" : 1 * (game.num_empty() + 1) if other_player == max_player else -1 * (game.num_empty() + 1)
                    }
        elif not game.is_empty():
            return {"position" : None, "score" : 0}

        if player_letter == max_player:
            best = {"position" : None, "score" : -math.inf}
        else:
            best = {"position" : None, "score" : math.inf}
        
        for possible_move in game.available_moves():
            game.play_move(possible_move, player_letter)
            sim_score = self.minimax(game, other_player)
            game.board[possible_move] = ""
            game.current_winner = None
            sim_score["position"] = possible_move
            if player_letter == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best




class GoodCPU(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def move_choice(self, game):
        if len(game.available_moves()) == 9:
            move_choice = random.choice(game.available_moves())
            return move_choice
        else:
            move_choice = self.minimax(game, self.symbol)["position"]
            return move_choice

    def minimax(self, game, player_letter):
        max_player = self.symbol
        other_player = "O" if player_letter == "X" else "X"
        
        if game.current_winner == other_player:
            return {"position" : None,
                    "score" : 1 * (game.num_empty() + 1) if other_player == max_player else -1 * (game.num_empty() + 1)
                    }
        elif not game.is_empty():
            return {"position" : None, "score" : 0}

        if player_letter == max_player:
            best = {"position" : None, "score" : -math.inf}
        else:
            best = {"position" : None, "score" : math.inf}
        
        for possible_move in game.available_moves():
            game.play_move(possible_move, player_letter)
            sim_score = self.minimax(game, other_player)
            game.board[possible_move] = ""
            game.current_winner = None
            sim_score["position"] = possible_move
            if player_letter == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best


class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def move_choice(self, game):
        return -1
    