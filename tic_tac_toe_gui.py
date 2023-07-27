import random
from tkinter import *
from tic_tac_toe_game_gui_version import Game
from player_gui import Human, CPU, GoodCPU, MediumCPU
from center import center_win


def start_game():
    def play(button, index):
        button['text'] = game.current_turn
        button.configure(state='disabled')
        game.board[index] = game.current_turn
        if game.check_win():

            buttons[game.winning_three[0]].configure(highlightbackground='#ff0000')
            buttons[game.winning_three[1]].configure(highlightbackground='#ff0000')
            buttons[game.winning_three[2]].configure(highlightbackground='#ff0000')
            for button in buttons:
                button.configure(state='disabled')
            result_message['text'] = game.current_turn + " wins!"
            game.current_winner = game.current_turn
        elif game.full_board():
            result_message['text'] = "It's a tie!"
        else:
            result_message['text'] = ""
        game.current_turn = "O" if button['text'] == "X" else "X"

    game = Game()

    def order_choice(choice, b1, b2, b3):
        game.order = choice
        window.destroy()

    def difficulty(choice, b1, b2, b3):
        game.difficulty = choice 
        prompt_message['text'] = "Choose an order"
        b1.destroy()
        b2.destroy()
        b3.destroy()
        first = Button(window, text="First", command=lambda: order_choice(1, first, second, random_choice))
        first.grid(column=1, row=0)
        second = Button(window, text="Second", command=lambda: order_choice(2, first, second, random_choice))
        second.grid(column=2, row=0)
        random_choice = Button(window, text="Random", command=lambda: order_choice(random.randint(0,2), first, second, random_choice))
        random_choice.grid(column=3, row=0)


    def player(choice):
        game.player_choice = choice 
        if choice == "CPU":
            prompt_message['text'] = "Choose a bot difficutly."
            cpu.destroy()
            human.destroy()
            easy = Button(window, text="Easy", command=lambda: difficulty("easy", easy, medium, hard))
            easy.grid(column=1, row=0)
            medium = Button(window, text="Medium", command=lambda: difficulty("medium", easy, medium, hard))
            medium.grid(column=2, row=0)
            hard = Button(window, text="Hard", command=lambda: difficulty("hard", easy, medium, hard))
            hard.grid(column=3, row=0)
        else:
            window.destroy()

    global window
    window = Tk()
    window.title("Tic Tac Toe")
    center_win(window)
    window.geometry('500x50')
    prompt_message = Label(window, text = "Choose to play against a CPU or HUMAN")
    prompt_message.grid(column=0, row=0)
    cpu = Button(window, text = "CPU", command=lambda: player("CPU"))
    cpu.grid(column=1, row=0)
    human = Button(window, text = "HUMAN", command=lambda: player("HUMAN"))
    human.grid(column=2, row=0)
    window.mainloop()
        
    if game.player_choice == "HUMAN":
        player1 = Human("X")
        player2 = Human("O")
    else:
        if game.order == 1:
            player1 = Human("X")
            if game.difficulty == "easy":
                player2 = CPU("O")
            elif game.difficulty == "medium":
                player2 = MediumCPU("O")
            else:
                player2 = GoodCPU("O")
        else:
            player2 = Human("O")
            if game.difficulty == "easy":
                player1 = CPU("X")
            elif game.difficulty == "medium":
                player1 = MediumCPU("X")
            else:
                player1 = GoodCPU("X")

    players = {
        "X":player1,
        "O":player2
    }

    window = Tk()
    window.title("Tic Tac Toe")
    result_message = Label(window, text = "")
    result_message.grid(column=0, row=3)
    # window.after(0, play)
    rest = Button(window, text = "restart", command=lambda: refresh())
    rest.grid(column=2, row=3)
    b1 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(0), disabledforeground='White')
    orig_color = b1.cget("highlightbackground")
    b1.grid(column=0, row=0)
    b2 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(1), disabledforeground='White')
    b2.grid(column=1, row=0)
    b3 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(2), disabledforeground='White')
    b3.grid(column=2, row=0)
    b4 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(3), disabledforeground='White')
    b4.grid(column=0, row=1)
    b5 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(4), disabledforeground='White')
    b5.grid(column=1, row=1)
    b6 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(5), disabledforeground='White')
    b6.grid(column=2, row=1)
    b7 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(6), disabledforeground='White')
    b7.grid(column=0, row=2)
    b8 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(7), disabledforeground='White')
    b8.grid(column=1, row=2)
    b9 = Button(window, text = " ", width=5, height=5, command=lambda: clicked(8), disabledforeground='White')
    b9.grid(column=2, row=2)
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    move_choice = players[game.current_turn].move_choice(game)
    if move_choice == -1:
        pass
    else:
        button = buttons[move_choice]
        play(button, move_choice)

    def clicked(index):
        button = buttons[index]
        button['text'] = game.current_turn
        button.configure(state='disabled')
        game.board[index] = game.current_turn
        if game.check_win():
            buttons[game.winning_three[0]].configure(highlightbackground='#ff0000')
            buttons[game.winning_three[1]].configure(highlightbackground='#ff0000')
            buttons[game.winning_three[2]].configure(highlightbackground='#ff0000')
            for button in buttons:
                button.configure(state='disabled')
            result_message['text'] = game.current_turn + " wins!"
            game.current_winner = game.current_turn
            return None
        elif game.full_board():
            result_message['text'] = "It's a tie!"
            return None
        else:
            result_message['text'] = ""
        game.current_turn = "O" if button['text'] == "X" else "X"
        if game.player_choice == "CPU":
            move_choice = players[game.current_turn].move_choice(game)
            button = buttons[move_choice]
            play(button, move_choice)
    center_win(window)
    window.mainloop()

if __name__ == '__main__':
    def refresh():
        window.destroy()
        start_game()
    
    start_game()


