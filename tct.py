#! /usr/bin/env python3
import copy
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

#minimax
def Minimax2(A):
    #base case
    moves=[]
    for i in range(9):
        if A.values[i] == " ":
            A.values[i] = A.turn
            A.changeval()

            temp=check_terminate(A)
            if temp==-1:
                A.changeval()
                A.values[i]=" "
                return [i,-1]
            elif temp==1:
                A.changeval()
                A.values[i]=" "
                return [i,1]
            elif A.isFull():
                A.changeval()
                A.values[i]=" "
                return [i,0]

            moves.append(Minimax2(A))

            A.changeval()
            A.values[i]=" "

    if A.turn=="X":
        #Find Max
        mx_mv=moves[0][0]
        mx_sc=moves[0][1]
        for x in moves:
            if x[1] > mx_sc:
                mx_sc=x[1]
                mx_mv=x[0]
        return [mx_mv, mx_sc]
    else:
        #Find Min
        mi_mv=moves[0][0]
        mi_sc=moves[0][1]
        for x in moves:
            if x[1] < mi_sc:
                mi_sc=x[1]
                mi_mv=x[0]
        return [mi_mv, mi_sc]

def Play():
    Game_Board = Board()

    #Game Loop
    while True:
        #Display board
        print("Board: ")
        printBoard(Game_Board)

        #Display turn
        print("Turn: ", Game_Board.turn)

        #Player turn
        pl = int(input(": "))
        while (pl < 0 or pl > 8) or Game_Board.values[pl]!=" ":
            print("Try again")
            pl=int(input(": "))

        Game_Board.values[pl] = Game_Board.turn

        #Check For Winner
        temp=check_terminate(Game_Board)
        if temp == 1:
            print("Game over, winner is X")
            break 
        elif temp == -1:
            print("Game over, winner is O")
            break
        elif Game_Board.isFull():
            print("Game Over, Draw")
            break

        #Switch turn
        Game_Board.changeval()

        #Print Board
        printBoard(Game_Board)

        #Computer turn (X)
        mv = Minimax2(Game_Board)
        Game_Board.values[mv[0]] = Game_Board.turn

        #Check For Winner
        temp=check_terminate(Game_Board)
        if temp == 1:
            print("Game over, winner is X")
            break 
        elif temp == -1:
            print("Game over, winner is O")
            break
        elif Game_Board.isFull():
            print("Game Over, Draw")
            break

        #Switch turn
        Game_Board.changeval()

    printBoard(Game_Board)
    print("Game has ended ")

#Start game
Play()
