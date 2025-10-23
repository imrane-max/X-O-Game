from tkinter import *
import random
import time



### Window ###
window = Tk()
window.title("X O")

### Functions ###
def next_turn(row, col):
    global player
    if game_btn[row][col]['text'] == "" and check_winner() == False:
        game_btn[row][col]['text'] = player

        if check_winner() == False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        elif check_winner() == True:
            label.config(text=(player + " wins!"))
        elif check_winner() == 'tie':
            label.config(text=("Tie, No Winner!"))

def check_winner():
    # horizontal
    for row in range(3):
        if game_btn[row][0]['text'] == game_btn[row][1]['text'] == game_btn[row][2]['text'] != "":
            for i in range(3):
                game_btn[row][i].config(bg="cyan")
            return True

    # vertical
    for col in range(3):
        if game_btn[0][col]['text'] == game_btn[1][col]['text'] == game_btn[2][col]['text'] != "":
            for i in range(3):
                game_btn[i][col].config(bg="cyan")
            return True

    # diagonals
    if game_btn[0][0]['text'] == game_btn[1][1]['text'] == game_btn[2][2]['text'] != "":
        game_btn[0][0].config(bg="cyan")
        game_btn[1][1].config(bg="cyan")
        game_btn[2][2].config(bg="cyan")
        return True

    if game_btn[0][2]['text'] == game_btn[1][1]['text'] == game_btn[2][0]['text'] != "":
        game_btn[0][2].config(bg="cyan")
        game_btn[1][1].config(bg="cyan")
        game_btn[2][0].config(bg="cyan")
        return True

    # tie
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btn[row][col].config(bg="red")
        return 'tie'
    else:
        return False

def check_empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btn[row][col]['text'] != "":
                spaces -= 1
    return spaces != 0

def start_new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for col in range(3):
            game_btn[row][col].config(text="", bg="#F0F0F0")

### Players ###
players = ["X", "O"]
player = random.choice(players)

### UI ###
game_btn = [[0,0,0],[0,0,0],[0,0,0]]

label = Label(text=(player + " turn"), font=("consolas", 40))
label.pack(side="top")

restart_btn = Button(text="Restart", font=("consolas", 30), command=start_new_game)
restart_btn.pack(side="top")

btn_frame = Frame(window)
btn_frame.pack()

for row in range(3):
    for col in range(3):
        game_btn[row][col] = Button(btn_frame, text="", font=("consolas", 40), width=4, height=1,
                                    command=lambda r=row, c=col: next_turn(r, c))
        game_btn[row][col].grid(row=row, column=col)

window.mainloop()
