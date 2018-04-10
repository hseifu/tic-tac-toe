#! /usr/bin/env python3

#Tic tac toe with AI
#Collaborator 1: Henok Hailu
#Collaborator 2: Leul Shiferaw

#board contains a list of characters representing
#the different values in the different entries of
#a board, where " " = empty slot and has the property
#turn represents which character goes next
class Board:
    def __init__(self, turn = "X", values = [" ", " ", " ", " ", " ", " ", " ", " ", " "], orig = None):
        self.values = values
        self.turn = turn

    def copy_constructor(self, orig):
        self.values = orig.values
        self.turn = orig.turn

    #Is Board Full
    def isFull(self):
        return not (" " in self.values)

    #overloaded [] operator
    def __getitem__(self, index):
        return self.values[index]

    #overloading the in operator
    def __contains__(self, val):
        return val in self.values

    #change turn
    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

#Print Board
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


#Checks for end
#1 for X won
#-1 for O won
#0 for not over yet
def check_terminate(A):
    x="X"
    #check win across main diagonal 
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
    #No wins
    return 0

#minimax
#will never get a full board as input
mv=0
def Minimax2(A):
    global mv
    moves=[]
    for i in range(9):
        if A.values[i] == " ":
            A.values[i] = A.turn

            #Base case
            temp=check_terminate(A)
            if temp==-1:
                mv=i
                A.values[i]=" "
                return -1
            elif temp==1:
                mv=i
                A.values[i]=" "
                return 1
            elif A.isFull():
                mv=i
                A.values[i]=" "
                return 0
            
            #Change Turn
            A.change_turn()

            moves.append([i,Minimax2(A)])

            #Reset
            A.change_turn()
            A.values[i]=" "

    if A.turn=="X":
        #Find Max
        mv=moves[0][0]
        mx_sc=moves[0][1]
        for x in moves:
            if x[1] > mx_sc:
                mv=x[0]
                mx_sc=x[1]
        return mx_sc
    else:
        #Find Min
        mv=moves[0][0]
        mi_sc=moves[0][1]
        for x in moves:
            if x[1] < mi_sc:
                mv=x[0]
                mi_sc=x[1]
        return mi_sc

def Play():
    Game_Board = Board()
    
    #Choose Player turn
    pl_tn=input("X or O: ")

    #Game Loop
    while True:
        #Display board
        print("Board: ")
        printBoard(Game_Board)

        #Display turn
        print("Turn: ", Game_Board.turn)

        #Player turn
        if Game_Board.turn==pl_tn:
            pl = int(input(": "))
            while (pl < 0 or pl > 8) or Game_Board.values[pl]!=" ":
                print("Try again")
                pl=int(input(": "))
            Game_Board.values[pl] = Game_Board.turn
        else:
            #Computer turn (X)
            Minimax2(Game_Board)
            Game_Board.values[mv] = Game_Board.turn

        #Check For Winner
        temp=check_terminate(Game_Board)
        if temp == 1:
            printBoard(Game_Board)
            print("Game over, winner is X")
            break 
        elif temp == -1:
            printBoard(Game_Board)
            print("Game over, winner is O")
            break
        elif Game_Board.isFull():
            printBoard(Game_Board)
            print("Game Over, Draw")
            break

        #Switch turn
        Game_Board.change_turn()

#Start game
Play()
