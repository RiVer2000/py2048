import random
import time
import copy
import os
import keyboard

def Display(board):
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
                
    space = len(str(largest))
    
    for row in board:
        nu = " "
        for element in row:
            nu += (" " *(space- len(str(element)))) + str(element) + str(" ")
        print(nu)
    print('\n')
    

def Left(row):
    for i in range(size-1):
        for j in range(size-1,0,-1):
            if row[j-1] == 0:
                row[j-1] = row[j]
                row[j] = 0
                
    for i in range(size-1):
        if row[i] == row[i+1]:
            row[i] *=2
            row[i+1] = 0
            
    for i in range(size-1):
        for i in range(size-1,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    return row
    
    
def Right(row):
    for i in range(size-1):
        for j in range(0,size-1):
            if row[j+1] == 0:
                row[j+1] = row[j]
                row[j] = 0
                
    for i in range(size-1,0,-1):
        if row[i] == row[i-1]:
            row[i] *=2
            row[i-1] = 0
            
    for i in range(size-1):
        for j in range(0,size-1):
            if row[j+1] == 0:
                row[j+1] = row[j]
                row[j] = 0
    return row
    
def Swipe_Left(board):
    for i in range(size):
        board[i] = Left(board[i])
    return board


def Swipe_Right(board):
    for i in range(size):
        board[i] = Right(board[i])
    return board
    

def Transpose(board):
    for i in range(size):
        for j in range(i,size):
            if not j == i:
                temp = board[i][j]
                board[i][j] = board[j][i]
                board[j][i] = temp
    return board
    
    
def Swipe_Up(board):
    board = Transpose(board)
    board = Swipe_Left(board)
    board = Transpose(board)
    return board
    
    
def Swipe_Down(board):
    board = Transpose(board)
    board = Swipe_Right(board)
    board = Transpose(board)
    return board

def Wipes():
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')    
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')

print("\t\t\t\tWelcome to the 76th Hunger games")
time.sleep(1)
print("\t\t\t\t  May the odds be ever in your Favor")
time.sleep(1)
print("\t\t\t\t    Kidding!!! Just a basic 2048 game")

print("The rules are pretty staight-forward you need to move tiles by sliding them using the keys w, a, s, d ")
print("to get to the Winning Number. By pressing x you can quit mid game")


size = 5
win = 2048

ans1 = input("Do you want to enter the Size and Winning Number(Y/N): ")
if ans1=='Y':
    size = int(input("Size : "))
    temp = int(input("\nWinning Number : "))
    a=2**(size*size)
    if temp > a:
        print('Sorry invalid winning number\n')
        win=2**(size*size)
        print('Your new winning number is: '+str(win))
        print()
    else:
        win = temp

board = [[0 for i in range(size)] for j in range(size)]

def Random():
    a = random.randint(0,size-1)
    b = random.randint(0,size-1)
    if board[a][b]== 0:
        board[a][b] = 2
    else:
        Random()
        
Random()
Display(board)


def Winning():
    for row in board:
        if win in row:
            return True
    return False


def Lose():
    temp1 = copy.deepcopy(board)
    temp2 = copy.deepcopy(board)
    temp1 = Swipe_Down(temp1)
    if temp1 == temp2:
        temp1 = Swipe_Up(temp1)
        if temp1 == temp2:
            temp1 = Swipe_Right(temp1)
            if temp1 == temp2:
                temp1 = Swipe_Left(temp1)
                if temp1 == temp2:
                    return True
    return False

game_over = False

while not game_over:
    print("Which way you want to move : " )
    valid_input  = True
    
    temp = copy.deepcopy(board)
    
    if keyboard.read_key() == "w":
        time.sleep(0.25)
        board = Swipe_Up(board)
    elif keyboard.read_key() == "s":
        time.sleep(0.25)
        board = Swipe_Down(board)
    elif keyboard.read_key() == "a":
        time.sleep(0.25)
        board = Swipe_Left(board)
    elif keyboard.read_key() == "d":
        time.sleep(0.25)
        board = Swipe_Right(board)
    elif keyboard.read_key() == "x":
        time.sleep(0.25)
        game_over = True
    else:
        valid_input = False
        
    if not valid_input:
        print("Invalid Input")
    else:
        if Winning():
            Wipes()
            Display(board)
            print("Congratulations You Won!!!!")
            game_over = True
        elif board == temp:
            print("Invalid Input")
        else:
            if Winning():
                Wipes()
                Display(board)
                print("Congratulations You Won!!!!")
                game_over = True
            else:
                Wipes()
                Random()
                Display(board)
                if Lose():
                    print("Sorry, no moves possible, You have lost")
                    game_over = True
    
    
    
    