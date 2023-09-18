import tkinter as tk
from PIL import Image, ImageTk
import random
from gtts import gTTS
from playsound import playsound
import os
import time


def speak(Text):
    obj = gTTS(text=Text, lang='en', slow=False)
    obj.save("Text.mp3")
    playsound("Text.mp3")
    os.remove("Text.mp3")

def start_game():
    global im
    global b1, b2
    #Creating Button for Players
    #Player 1
    b1.place(x=800, y=550)
    #player 2
    b2.place(x=800, y=400)

    #Dice Button
    im = Image.open("images/roll_dice.png")
    im = im.resize((65, 65))
    im = ImageTk.PhotoImage(im)
    imgbutton = tk.Button(root, image=im, height= 80, width=80, bg='red', activebackground='green')
    imgbutton.place(x=870, y = 250)


    #Exit Button
    exit = tk.Button(root, text="Click Here to End Game", height= 3, width=20, fg= "black", bg= 'orange', font=('Cursive', 14,'bold'), activebackground='red',command=root.destroy) 
    exit.place(x=800, y=20)


def reset_coins():
    global player_1, player_2
    global pos1, pos2

    player_1.place(x=0, y = 655)
    player_2.place(x=0, y = 635)
    pos1 = 0
    pos2 = 0


def load_dice_images():
    global Dice
    names = [
        "1.png",
        "2.png",
        "3.png",
        "4.png",
        "5.png",
        "6.png",
    ]
    for nam in names:
        im = Image.open("images/" + nam)
        im = im.resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)



def chech_Ladder(Turn):
    global pos1, pos2
    global Ladder
    f = 0 # No Ladder
    if Turn == 1:
        if pos1 in Ladder:
            pos1 = Ladder[pos1]
            f = 1
    else:
        if pos2 in Ladder:
            pos2 = Ladder[pos2]
            f = 1
    return f



def check_snake(Turn):
    global pos1, pos2
    global Snake
 
    if Turn == 1:
        if pos1 in Snake:
            pos1 = Snake[pos1]
     
    else:
        if pos2 in Snake:
            pos2 = Snake[pos2]
      
    
def rooling_dice():
    global Dice
    global turn
    global pos1, pos2
    global b1, b2

    r = random.randint(1, 6)
    imgbutton = tk.Button(root, image=Dice[r-1], height= 80, width=80, bg='red', activebackground='green')
    imgbutton.place(x=870, y = 250)
    # time.sleep(1)
    # speak(str(r))
    Lad = 0
    if turn == 1:
        if (pos1 + r) <= 100:
            pos1 = pos1 + r
        Lad = chech_Ladder(turn)
        check_snake(turn)
        move_coin(turn, pos1)
        if r!= 1 and Lad == 0:
            turn = 2
            b1.configure(state="disabled")
            b2.configure(state="normal")

        
    else:
        if (pos2 + r) <= 100:
            pos2 = pos2 + r
        
        Lad = chech_Ladder(turn)
        check_snake(turn)
        move_coin(turn, pos2)
        if r!= 1 and Lad == 0:
            turn = 1
            b2.configure(state="disabled")
            b1.configure(state="normal")
    # speak("player - " + str(turn) + " turn ")
    is_winner()




def is_winner():
    global pos1, pos2
    if pos1 == 100:
        msg = "Player-1 is the  Winner"
        speak(msg)
        lab = tk.Label(root, text=msg, height= 3, width=20, fg= "black", bg= 'orange', font=('Cursive', 14,'bold'), activebackground='red')
        lab.place(x=800, y=150)
        reset_coins()
    elif pos2 == 100:
        msg = "Player-2 is the  Winner"
        speak(msg)
        lab = tk.Label(root, text=msg, height= 3, width=20, fg= "black", bg= 'orange', font=('Cursive', 14,'bold'), activebackground='red')
        lab.place(x=800, y=150)
        reset_coins()
    
        
    

    
def move_coin(Turn, r):
    global player_1, player_2
    global Index, pos1, pos2
    if Turn == 1:
        player_1.place(x = Index[r][0], y = Index[r][1])
        # speak("You are at" + str(pos1))
    else:
        player_2.place(x = Index[r][0], y = Index[r][1])
        # speak("You are at" + str(pos2))
def get_index():
    global player_1, player_2
    num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91,81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
           60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 
           , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            ]
    # player_1.place(x = 10, y = 30)
    # player_2.place(x = 35, y = 30)
    row = 10
    i = 0
    for x in range (1, 11):
        col = 30
        for y in range(1, 11):
            Index[num[i]] = (col, row)
            col = col + 70
            i = i+1
        
        row = row + 70
    print(Index)    
    
    

    



#to store dice images
Dice = []
#to store x & y Coordinates
Index = {}

# intial position of players
pos1 = None
pos2 = None

#Ladder Bottom to Top
Ladder = {
    4: 56,
    12: 50,
    14: 55,
    22: 58,
    41: 79,
    54: 88
}
#Snake Head to tail
Snake = {
    96: 42,
    94: 71,
    75: 32,
    47: 16,
    37: 3,
    28: 10
}

# Create the main window
root = tk.Tk()
root.geometry("1200x800")
root.title("Snake and Ladder Board")

f1 = tk.Frame(root, width= 1200, height= 680, relief='raised')
f1.place(x=0, y=0)

#set Board 
img1 = tk.PhotoImage(file= "images/Snake_and_Ladder.png")
Lab = tk.Label(f1, image=img1)
Lab.place(x=0, y=0)
#player 1 button
b1 = tk.Button(root, text="Player-1", height= 3, width=20, fg= "black", bg= 'yellow', font=('Cursive', 14,'bold'), activebackground='blue', command=rooling_dice) 
#player 2 button
b2 = tk.Button(root, text="Player-2", height= 3, width=20, fg= "red", bg= 'cyan', font=('Cursive', 14,'bold'), activebackground='blue', command=rooling_dice ) 
#player 1 coin
player_1 = tk.Canvas(root, width= 20, height= 20)
player_1.create_oval(5, 5, 20, 20, fill = 'yellow')

#player 2 coin
player_2 = tk.Canvas(root, width= 20, height= 20)
player_2.create_oval(5, 5, 20, 20, fill = 'cyan')

#whose turn first -- by default player 1
turn = 1

#keep coins in start
reset_coins()

# Get index of each number
get_index()

#load dice images
load_dice_images()



speak("Welcome to Snake and Ladder Game. Game will Start with Player 1")
#Start Button
start_game()




# Run the event loop
root.mainloop()
