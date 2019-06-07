# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:10:02 2018

CM4043 Python Project

@author: Group 2 
Nguyen Linh Lan (U1640632C)
Suyash Pandey (U1441062G)
Pang Jingyi (U1640115K)
Ying Ying Ma (N1804580C)
"""

import numpy as np
np.set_printoptions(threshold=np.inf) # Ensures large boards aren't truncated in the console
import random

class Game:
    turn = 0 #this determines whether it is player 1 or CPU/player 2 playing
    wins = 0 #this represents the number of connected discs required to win
    game_over = False #initialise game
    rows = 0 # this represents the number of rows of the board
    cols = 0 # this represents the number of columns of the board
    mat = None # this represents the board matrix
    

     
def choose_opponent(): # Lets you choose whether to play against the CPU or Player 2
    '''Returns 1 when playing against CPU, returns 2 when against player 2'''
    while True: # while loop is used to keep prompting the user for an valid input
        try:
            choose_opponent = int(input("Who would you like to play against? \n 1. CPU\n 2. Player 2\n"))
            if choose_opponent == 1: # Option 1 is chosen 
                print("Playing against CPU.")
                return (choose_opponent)
                break
            elif choose_opponent == 2: #Option 2 is chosen 
                print("Playing against Player 2.")
                return (choose_opponent)
                break
            else:
                print("Invalid input! Please input option 1 or 2.")
        except (ValueError, NameError): #prompts user to input again because previous input is invalid
            print("Invalid input! Please input option 1 or 2.")
            continue


def boardsize(): # Lets you choose whether to use the default board size or to customize your own
    '''Returns tuple (6,7) when user chooses the default board, calls customization_row_col() when user chooses to customise'''
    while True:
        try:
            board_size = int(input("Would you like to:\n 1. Use the default board size?\n 2. Customize your own?\n"))
            if board_size==1: #default option
                print(np.zeros((6,7))) #prints board matrix
                return(6,7)
                break
            elif board_size==2: #customised option 
                return customization_row_col()
                break
            else:
                print("Invalid option! Please input option 1 or 2.")
        except (ValueError, NameError): #prompts user to input again because previous input is invalid
            print("Invalid input! Please enter an acceptable integer.")
            continue


def customization_row_col(): # Lets you customize the number of rows and columns of the board
   '''Returns dimensions of customised board as a tuple'''
   row = int(input("Please input a number greater than 4 for the no. of rows:\n"))
   col = int(input("Please input a number greater than 4 for the no. of columns:\n"))
   if row <= 4 or col <= 4: # check for the cases when a number smaller than 4 is inputted. 
       print("Both number of rows and columns must be greater than 4.")
       return customization_row_col()
   else: 
       print(np.zeros((row,col)))
       return (row,col) #return a tuple 


def connect_n(game): # Lets you set the winning condition
    '''Returns integer 4 if default is chosen, else returns user-inputted integer'''
    while True:
        try:
            connect_option = int(input("Would you like to:\n 1. Use default winning condition (i.e. 4 connected discs)?\n 2. Choose another winning condition?\n"))
            if connect_option == 1: #default option
                print("4 discs will have to be connected to win.")
                return 4
                break
            elif connect_option == 2:
                while True:
                    try:
                        connect_n = int(input("Enter an integer less than or equal to the number of rows or columns.\n The number of discs cannot exceed the smallest dimension of your board.\n E.g. If your board is a 10x12 board, the maximum integer allowed is 10.\n"))
                        if connect_n > game.rows or connect_n > game.cols: #check if the input is within the dimension of the board 
                            print("Invalid input! Please choose again.")
                        else:
                            print(connect_n, "discs will have to be connected to win.")
                            return (connect_n)
                    except (ValueError, NameError): #prompts user to input again because previous input is invalid
                        print("Invalid input! Please key in an integer.")
                        continue
            else:
                print("Invalid input! Please input option 1 or 2.")
        except (ValueError, NameError): #prompts user to input again because previous input is invalid
            print("Invalid input! Please input option 1 or 2.")
            continue


def check_victory(game):
    '''Returns 1 when player 1 wins, returns 2 when player 2 or CPU wins, returns 3 when draw game'''
    
    #Empty lists are created for each winning condition for both the player 1 and player/CPU
    #List is appended when there is a consecutive piece in line
    #Victory occurs when there is game.wins-1 consecutive pieces
    rowwin1=[] 
    rowwin2=[]
    colwin1=[]
    colwin2=[]
    dwin1=[]
    dwin2=[]
    ndwin1=[]
    ndwin2=[]
    
    #Check rows for wins

    for r in range(game.rows): 
        for c in range(game.cols-1):
            if game.mat[r][c] == game.mat[r][c+1] == 1: 
                rowwin1.append(1) #append 1 into the empty list if the two consecutive elements of row r are similar for player 1
                if len(rowwin1) >= game.wins-1: #return 1 if there are more than n numbers of consecutive similar dics in a row
                    return 1 
            elif game.mat[r][c] == game.mat[r][c+1] == 2:#append 1 into the empty list if the two consecutive elements of row r are similar for player 2 and CPU 
                rowwin2.append(2)
                if len(rowwin2) >= game.wins-1:
                    return 2
            else: #if the two consecutive elements are different, the list is cleared 
                rowwin1.clear() 
                rowwin2.clear()
       # if len(rowwin1) >= my_game.wins-1 or len(rowwin2) >= my_game.wins-1: #minus 1 because every pair of identical adjacent piece is 1 entry


    #Check columns for wins
    for c in range(game.cols): 
        for r in range(game.rows-1):
            if game.mat[r][c] == game.mat[r+1][c] == 1: #append 1 into the empty list if the two consecutive elements of column c are similar for player 1
                colwin1.append(1)
                if len(colwin1) >= game.wins-1:#return 1 if there are more than n numbers of consecutive similar dics in a column
                    return 1
            elif game.mat[r][c] == game.mat[r+1][c] == 2: #append 1 into the empty list if the two consecutive elements of column c are similar for player 2
                colwin2.append(2)
                if len(colwin2) >= game.wins-1:
                    return 2
            else: #if the two consecutive elements are different, the list is cleared 
                colwin1.clear()
                colwin2.clear()

    #Check positive diagonals for wins
    for r in range(game.rows-1,-1,-1):
        for c in range(game.cols):
            for k in range(1,game.wins):
                if r-k < 0 or c+k > game.cols-1:
                    continue
                
                else:
                    if game.mat[r][c] == game.mat[r-k][c+k] == 1:
                        dwin1.append(1)
                        if len(dwin1) >= game.wins-1:
                            return 1
                    
                    elif game.mat[r][c] == game.mat[r-k][c+k] == 2:
                        dwin2.append(2)
                        if len(dwin2) >= game.wins-1:
                            return 2
            dwin1.clear()
            dwin2.clear()
            
    #Check negative diagonals for wins
    for r in range(game.rows):
        for c in range(game.cols):
            for k in range(1,game.wins):
                if r+k > game.rows-1 or c+k > game.cols-1:
                    continue
                
                else:
                    if game.mat[r][c] == game.mat[r+k][c+k] == 1:
                        ndwin1.append(1)
                        if len(ndwin1) >= game.wins-1:
                            return 1
                    
                    elif game.mat[r][c] == game.mat[r+k][c+k] == 2:
                        ndwin2.append(2)
                        if len(ndwin2) >= game.wins-1:
                            return 2
            ndwin1.clear()
            ndwin2.clear()
            
    # this function also checks for the draw condition when all the top rows are filled.
    output = 3   
    for i in range(game.cols):
        if game.mat[0,i] == 0: #when there is one component that is 0, the board is not filled. 
            output = 0 
        else: 
            continue
    return output #return 3 if it is filled, return 0 if it is not filled (i.e. game still in progress). 
    
    
def apply_move(game, col, pop): 
    '''If user chooses to drop a piece, pop==False. If user chooses to pop, pop==True'''
    if pop == False: # if drop option is chosen
        if game.mat[0][col] == 0: #Checks if column is filled
            f=[] 
        for r in range(game.rows):
            if game.mat[r][col] == 0:
                f.append(r)
        game.mat[max(f)][col] = game.turn+1 #drops piece on the lowest available row in the column
        return game.mat
    
    if pop == True:# if pop option is chosen 
        specific_column = game.mat[:,col]
        popped_out = np.roll(specific_column, 1) 
        popped_out[0] = 0 
        game.mat[:,col] = popped_out
        return game.mat 

# - This function gets called to handle both disc drops and pop-outs.    
# - This function first receives a boolean value check (pop), and then a col number, and from 
# the boolean value it decides to either pop-out from or add a piece to that particular column.
# - If pop == False, the function drops a disc.        
# - If it drops a disc, it takes into account other input like the my_game.rows (derived from my_game.mat) 
# , the column the disc is being dropped in, and the my_game.mat
# - Currently, this function also checks whether the move is valid before it's executed.
#        
# - If pop == True, the function then executes a pop-out based on the column number that
# was inputted. 
# - The pop-out works by isolating the column where the pop-out is being executed, moving all 
# values in that column down by 1 spot, and then replacing the value at the top of that column 
# with 0. Finally, it re-assigns this modified column into the my_game.mat in place of
# the old one.


def check_move(game, col, pop): 
    if pop == False:
        if game.mat[0][col] == 0:
            return True
        else:
            return False
    elif pop == True:
        if game.mat[game.rows-1][col] == game.turn+1:
            return True
        else:
            return False
# - Function is called to check for whether a disc drop or pop-out is valid.
# - The apply_move function is only later called if a "True" boolean value is returned from this.
# - Function first receives Boolean value that tells it whether the player is attempting a disc
# drop or a pop-out.
# - Disallows disc drop if the column is already filled.
# - Disallows pop-outs if the player's piece isn't at the bottom of that column.


def computer_move(game,level=1):
    if level == 1:
        while True:
            move = random.randint(0, game.cols) 
            if move == game.cols:
                pop = True 
                specific_row = game.mat[game.rows-1,:] # bottom row of board is isolated
                searchval = 2 
                eligible_columns = np.where(specific_row == searchval)[0] # indexes are acquired where the CPU's pieces are at the bottom row.
                try:
                    col = random.choice(eligible_columns) # CPU makes random choice from one of these valid columns
                    return col, pop
                except (IndexError):
                    continue
            else: 
                pop = False
                col = move
                return col, pop


# - Function receives 1) my_game.mat and, 2) level of CPU as input.
# - Since my_game.mat is defined as my_game.mat = np.zeros((my_game.rows, my_game.cols)),
# the function can acquire the column count right from the inputted my_game.mat.
# - Since level = 1, a random integer roll between 0 and column count then takes place.
# - Integer rolls between 0 and my_game.cols-1 correspond to piece positions to drop on the board.
# - An Integer roll of my_game.cols returns True pop value, and the function then attempts to look
# for valid columns to pop-out from. Then it makes a random choice from one of those columns.
# - As a result, the bigger the board, the more it chooses to drop a piece rather than pop out.
# - This is our way to avoid the issue of the CPU using pop-out excessively.
# - If the CPU first rolls a pop = True but has no valid pieces to pop out, the code uses
#  a "while True" loop to keep forcing a re-roll until it chooses to drop a piece instead.
# - In either event, both a col and boolean pop value are returned, which determine the CPU's
# move.


def display_board(game): # Displays the board after every action
    print(game.mat)


def menu():
    print('Hello! Welcome to Connect-N developed by group 2!') #Welcoming message and instructions
    print('You can choose your own board size and number of consecutive discs to win.\n'
          'However, the board size has to be bigger than 4x4.\n'
          'The number of consecutive discs to win has to be smaller or equal to the dimensions of the board size.\n'
          'Keep in mind the column numbers begin with 1 (so the leftmost column corresponds to an input number of 1 and the column to its right is 2, etc.).\n'
          'Simply follow our prompts. HAVE FUN!\n')
    OPPONENT = choose_opponent()
    DIM_MATRICES = boardsize() #The output is the dimension of the game board (rows x column)
    print("The dimensions of the board (rows, columns) are:")
    print (DIM_MATRICES)
    
    
    my_game = Game()
    my_game.cols=DIM_MATRICES[0]
    my_game.rows=DIM_MATRICES[1]
    board_game = np.zeros((my_game.rows,my_game.cols))
    my_game.mat=board_game
    my_game.wins=connect_n(my_game)    
    
    LEVEL = 1
    while not my_game.game_over:
        if my_game.turn == 0:
            try:
                action = int(input("Player 1, choose an action: \n 1. Drop \n 2. Pop-out\n 3. End game\n"))
                if action == 1:
                    pop = False #when player chooses to drop piece
                    try:
                        while True:
                            col = int(input("Player 1, make your selection:\n"))
                            if col <= my_game.cols and col > 0: #to check if the values input is within the board size
                                col = col-1
                                break
                            else: 
                                print("Invalid input! Please choose again.") #prompts user to choose a valid column again
                                continue
                    except (ValueError, NameError):# if the input is invalid 
                        print("Invalid input! Please choose again.") #prompts user to input valid action
                        continue
                    if check_move(my_game, col, pop): #check if move is valid
                        apply_move(my_game, col, pop) 
                        print("Player 1 has dropped a piece into column", col+1, ".")
                        display_board(my_game)
                        if check_victory(my_game) == 1: #check for victory, draw 
                            print("Player 1 has won!!")
                            my_game.game_over = True
                        elif check_victory(my_game) == 2:
                            print("Player 2 has won!!")
                            my_game.game_over = True
                        elif check_victory(my_game) == 3: #if the whole board is filled, the game is over
                            my_game.game_over = True
                            print("It is a draw! The board is filled and neither player has connected enough discs!")
                        elif check_victory(my_game) == 0:
                            my_game.game_over = False                            
                    else:
                        print("Invalid input! That column is filled. Please choose again.")
                        continue
                elif action == 2:
                    pop = True #player 1 chooses to pop piece
                    try:
                        while True:                    
                            col = int(input("Which column do you want to pop out from?\n"))       
                            if col <= my_game.cols and col > 0: #to check if the values input is within the board size
                                col = col-1
                                break
                            else: 
                                print("Invalid number! Please choose again.")
                                continue
                    except (ValueError, NameError):
                        print("Invalid input! Please choose again.")
                        continue
                    if check_move(my_game, col, pop): # check and apply move 
                        apply_move(my_game, col, pop)
                        print("Player 1 has popped out from column", col+1, ".")
                        display_board(my_game)
                        if check_victory(my_game) == 1: #check victory and draw
                            print("Player 1 has won!!")
                            my_game.game_over = True
                        elif check_victory(my_game) == 2:
                            print("Player 1 has engaged in self-sabotage. Player 2 has won!!")
                            my_game.game_over = True
                        elif check_victory(my_game) == 3:
                            my_game.game_over = True
                            print ("It is a draw! The board is filled and neither player has connected enough discs!")
                        elif check_victory(my_game) == 0:
                            my_game.game_over = False
                    else:
                        print("Invalid input! Pop-out cannot be executed in that column. Please choose again.")
                        continue
                elif action == 3: # when player wants to end the game 
                    print("You have ended the game.")
                    break
                else:
                    print("Invalid input! Please select option 1, 2 or 3.") #error message when user inputs a integer that is not 1,2 or 3
                    continue
            except (ValueError, NameError): 
                print("Invalid input! Please select option 1, 2 or 3 again.") #error message when input is invalid 
                continue
        else:
            if OPPONENT == 1: # CPU 
                col, pop = computer_move(my_game,LEVEL) # col and pop values returned from computer_move function are used to make its move.
                if pop == True: #CPU drops piece
                    try:
                        if check_move(my_game, col, pop): # check_move used to determine if CPU's move is possible.
                            my_game.mat=apply_move(my_game, col, pop) # apply_move used to apply CPU's decision to the board if it was a valid move.
                            print("CPU has popped out from column ", col+1, ".")
                            display_board(my_game)
                            if check_victory(my_game) == 1:#check victory and draw
                                print("CPU has sabotaged itself. Player 1 has won!")
                                my_game.game_over = True
                            elif check_victory(my_game) == 2:
                                print("CPU has won!!")
                                my_game.game_over = True
                            elif check_victory(my_game) == 3:
                                my_game.game_over = True
                                print ("It is a draw! The board is filled and neither player has connected enough discs!")
                            elif check_victory(my_game) == 0:
                                my_game.game_over = False
                        else:
                            continue
                    except (IndexError):
                        continue
                elif pop == False: #CPU pops piece
                    if check_move(my_game, col, pop):
                        my_game.mat=apply_move(my_game, col, pop) #CPU's move is checked, and applied if valid using these check_move and apply_move.
                        print("CPU has dropped a piece into column ", col+1, ".")
                        display_board(my_game)
                        if check_victory(my_game) == 1: #check victory and draw
                            print("Player 1 has won!!")
                            my_game.game_over = True
                        elif check_victory(my_game) == 2:
                            print("CPU has won!!")
                            my_game.game_over = True
                        elif check_victory(my_game) == 3:
                            my_game.game_over = True
                            print ("It is a draw! The board is filled and neither player has connected enough discs!")
                        elif check_victory(my_game) == 0:
                            my_game.game_over = False
                    else:
                        continue
                             
            else: #human player 2
                try:
                    action = int(input("Player 2, choose an action: \n 1. Drop \n 2. Pop-out\n 3. End game\n"))
                    if action == 1: #Player 2 drops piece 
                        pop = False
                        try:
                            col = int(input("Player 2, make your selection:\n"))
                            if col <= my_game.cols: #to check if the values input is within the board size
                                col= col-1
                            else: 
                                print("Invalid input! Please choose again.")
                                col = int(input("Player 2, make your selection:\n"))
                                col = col-1
                        except (ValueError, NameError): #to check if the input is valid
                            print("Invalid input! Please choose again.")
                            continue
                        if check_move(my_game, col, pop): #check whether the move is valid
                            apply_move(my_game, col, pop)
                            print("Player 2 has dropped a piece into column ", col+1, ".")
                            display_board(my_game)
                            if check_victory(my_game) == 1: #check victory and draw
                                print("Player 1 has won!!")
                                my_game.game_over = True
                            elif check_victory(my_game) == 2:
                                print("Player 2 has won!!")
                                my_game.game_over = True
                            elif check_victory(my_game) == 3:
                                my_game.game_over = True
                                print ("It is a draw! The board is filled and neither player has connected enough discs!")
                            elif check_victory(my_game) == 0:
                                my_game.game_over = False
                        else: 
                            print("Invalid input! That column is filled. Please choose again.")
                            continue
                    elif action == 2: #player 2 pops piece
                        pop = True
                        try:
                            while True:                    
                                col = int(input("Which column do you want to pop out from?\n"))       
                                if col <= my_game.cols and col > 0: #to check if the values input is within the board size
                                    col = col-1
                                    break
                                else: 
                                    print("Invalid number! Please choose again.")
                                    continue
                        except (ValueError, NameError, IndexError):
                            print("Invalid input! Please choose again.")
                            continue              
                        if check_move(my_game, col, pop): # check whether the pop is valid
                            apply_move(my_game, col, pop)
                            print("Player 2 has popped out from column ",col+1, ".")
                            display_board(my_game)
                            if check_victory(my_game) == 1: # check victory and draw
                                print("Player 2 has engaged in self-sabotage. Player 1 has won!!")
                                my_game.game_over = True
                            elif check_victory(my_game) == 2:
                                print("Player 2 has won!!")
                                my_game.game_over = True
                            elif check_victory(my_game) == 3:
                                my_game.game_over = True
                                print ("It is a draw! The board is filled and neither player has connected enough discs!")
                            elif check_victory(my_game) == 0:
                                my_game.game_over = False
                        else:
                            print("Invalid input! Pop-out cannot be executed in that column.")
                            continue
                    elif action == 3: #Player 2 ends the game 
                        print("You have ended the game!")
                        break
                    else:
                        print("Invalid input! Please select option 1, 2 or 3.")
                        continue
                except (ValueError, NameError): 
                    print("Invalid input! Please choose again.")
                    continue
                     
        my_game.turn += 1 # these two following lines create new round
        my_game.turn = my_game.turn % 2
        
        if my_game.game_over: #Ask the users whether they want to continue playing another set. 
            playagain = int(input("Would you like to play the game again? \n 1. Yes \n 2. No"))
            if playagain == 1:
                return menu()
            else:
                print("Thank you for playing our game! Hope you have fun!")
                break

menu() #initialises the whole game