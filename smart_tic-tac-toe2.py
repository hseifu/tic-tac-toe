#! /usr/bin/env python3
import copy
import sys
import threading

threading.stack_size(67108864) 
sys.setrecursionlimit(1000)
count = 0
final_move = 0
#board contains a list of characters representing
#the different values in the different entries of
#a board, where " " = empty slot and has the property
#turn represents which character goes next
class Board:
    def __init__(self, values = [" ", " ", " ", " ", " ", " ", " ", " ", " "], turn = "O", orig = None):
        self.values = values
        self.turn = turn
    def copy_constructor(self, orig):
        self.values = orig.values
        self.turn = orig.turn
    #Function for checking if we have a space left
    def isFull(self):
        if " " in self.values:
            return False
        else:
            return True
    #method to fill the index with the character: turn
    #turn also changed
    def fill(self, index):
        if self.values[index] == " ":
            self.values[index] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    #method for removing an element at index(1 indexed)
    def remove(self, index):
        self.values[index] = " "
    #method to fetch the index of a char from the board
    #with index starting at 1
    def index(self,ch):
        return self.values.index(ch)+1
    #overloaded [] operator to fetch values with 
    #counting index of 1
    def __getitem__(self, index):
        return self.values[index]
    #overloading the in operator
    def __contains__(self, val):
        return val in self.values

    def changeval(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
#Function for printing values in a board
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

    

#takes a board and a character and returns 0  
#if draw or incomplete board, returns 1 if 
#character x wins and -1 if character x loses
def check_terminate(A):
    #check win across main diagonal 
    x="X"
    if A[0] == A[4] == A[8] != " ":
        if A[0] == x:
            return 1
        else:
            return -1
    #check win across left diagonal
    if A[2] == A[4] == A[6] != " ":
        if A[2] == x:
            return 1
        else:
            return -1
    #check win across top row
    if A[0] == A[1] == A[2] != " ":
        if A[1] == x:
            return 1
        else:
            return -1
    #check win accross middle row
    if A[3] == A[4] == A[5] != " ":
        if A[3] == x:
            return 1
        else:
            return -1
    #check win accross last row
    if A[6] == A[7] == A[8] != " ":
        if A[7] == x:
            return 1
        else:
            return -1
    #check win accross first column
    if A[0] == A[3] == A[6] != " ":
        if A[0] == x:
            return 1
        else:
            return -1
    #check win accross second column
    if A[1] == A[4] == A[7] != " ":
        if A[1] == x:
            return 1
        else:
            return -1
    #check win accross last column
    if A[2] == A[5] == A[8] != " ":
        if A[2] == x:
            return 1
        else:
            return -1
    else:
        return 0


#redefined minimax
def Minimax2(A):
    #base case
    #printBoard(A)
    global final_move
    global count
    count += 1
    term = check_terminate(A)
    if term != 0 or (term == 0 and A.isFull()):
        return term
    #list to hold moves and scores
    moves = scores = []
    #iterate through entire game 
    for i in range(9):
        if A.values[i] == " ":
            A.values[i] = A.turn
            A.changeval()
            try:
                (scores.append(Minimax2(A)))
            except RecursionError as re:
                print("You have reached the maximum level of recursion which is ", count)
                sys.exit()

            moves.append(i)
            A.changeval()
            A.values[i] = " "

    if A.turn == "X":
        max_score_index = scores.index(max(scores))

        final_move = moves[max_score_index]
        return scores[max_score_index]
    else:
        min_score_index = scores.index(min(scores))
        
        final_move = moves[min_score_index]
        return scores[min_score_index]


def Play():
    Game_Board = Board()
    print(Game_Board.isFull())
    while not Game_Board.isFull():
        if check_terminate(Game_Board) == 1:
            print("Game over, winner is X")
            return 
        elif check_terminate(Game_Board) == -1:
            print("Game over, winner is O")
            return
        print("Current board is")
        printBoard(Game_Board)
        print("It is now ", Game_Board.turn, "'s turn")
        print("Where do you wanna put the value")
        pl = int(input())
        Game_Board.values[pl] = Game_Board.turn
        Game_Board.changeval()
        printBoard(Game_Board)
        print("It is now ", Game_Board.turn, "'s turn")
        Board_copy = copy.deepcopy(Game_Board)
        Minimax2(Board_copy)

        Game_Board.values[final_move] = "X"
        Game_Board.changeval()
        print("I have now filled in the place of ", final_move)
        print("The current board is")
        printBoard(Game_Board)
    print("Game has ended ")


Play()
