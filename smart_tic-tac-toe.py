#! /usr/bin/env python3

#board contains a list of characters representing
#the different values in the different entries of
#a board, where " " = empty slot and has the property
#turn represents which character goes next
class Board:
    def __init__(self, values = [], turn = "O", orig = None):
        self.values = values
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
        self.values[index - 1] = turn
        if turn == "X":
            turn = "O"
        else turn = "X"
    #method for removing an element at index(1 indexed)
    def remove(self, index):
        self.values[index - 1] = " "
    #method to fetch the index of a char from the board
    #with index starting at 1
    def index(self,ch):
        return self.values.index(ch)+1
    #overloaded [] operator to fetch values with 
    #counting index of 1
    def __getitem__(self, index):
        return self.values[index-1]
    #overloading the in operator
    def __contains__(self, val):
        return val in self.values
        
#Function for printing values in a board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

    


#takes a board and a character and returns 0  
#if draw or incomplete board, returns 1 if 
#character x wins and -1 if character x loses
def check_terminate(A, x = A.turn):
    #check win across main diagonal 
    if A[1] == A[5] == A[9] != " ":
        if A[1] == x:
            return 1
        else:
            return -1
    #check win across left diagonal
    if A[3] == A[5] == A[7] != " ":
        if A[3] == x:
            return 1
        else:
            return -1
    #check win across top row
    if A[1] == A[2] == A[3] != " ":
        if A[1] == x:
            return 1
        else:
            return -1
    #check win accross middle row
    if A[4] == A[5] == A[6] != " ":
        if A[4] == x:
            return 1
        else:
            return -1
    #check win accross last row
    if A[7] == A[8] == A[9] != " ":
        if A[7] == x:
            return 1
        else:
            return -1
    #check win accross first column
    if A[1] == A[4] == A[7] != " ":
        if A[4] == x:
            return 1
        else:
            return -1
    #check win accross second column
    if A[2] == A[5] == A[8] != " ":
        if A[2] == x:
            return 1
        else:
            return -1
    #check win accross last column
    if A[3] == A[6] == A[9] != " ":
        if A[3] == x:
            return 1
        else:
            return -1
    else:
        return 0

#maxboard finder
def maxboard(A):
    boards = vals = []
    for i in A:
        A_copy = Board(A)
        if i == " ":
            A_copy.fill(A_copy.index(i))
            val = check_terminate(A_copy,A.turn)
    #now that we have filled it in and the turns have changed
    #we check if we can win. The parameter above is A.turn because
    #we want to know if our initial character wins
            if val == 1:
                return A_copy
            else:
                boards.append(A_copy)
                vals.append(val)
    return boards[vals.index(max(val))]

def minboard(A):
    boards = vals = []
    for i in A:
        A_copy = Board(A)
        if i == " ":
            A_copy.fill(A_copy.index(i))
            val = check_terminate(A_copy,A.turn)
    #now that we have filled it in and the turns have changed
    #we check if we can win. The parameter above is A.turn because
    #we want to know if our initial character wins
            if val == -1:
                return A_copy
            else:
                boards.append(A_copy)
                vals.append(val)
    return boards[vals.index(min(val))]
     





#Minimax algorithm that takes a board, how many times it has run,
#list of places, list of scores and which element to maximize for
def Minimax(A, i, place, score, max_for, k):
    term = check_terminate(A, max_for)
    if term == 1:
        if i == 1:
            print("Already won")
        place.append(k)
        score.append(term)
        return
    if term == -1:
        if i == 1:
            print("Already lost")
        place.append(k)
        score.append(term)
        return
    elif term == 0 and A.isFull:
        if i == 1:
            print("Already draw")
        place.append(k)
        score.append(term)
        return
    else:
        for j in range(9):
            if A.values[j] == " ":
                A.fill(j+1)
                k = j+1
                i += 1
                Minimax(A, i, place, score, max_for, k)
                A.remove(j+1)
    

def Play():
    Game_Board = Board()
    while not Game_Board.isFull():
        print("Current board is")
        printBoard(Game_Board)
        print("It is now ", Game_Board.turn, "'s turn")
        print("Where do you wanna put the value")
        pl = input()
        Game_Board.fill(pl)
        printBoard(Game_Board)
        print("It is now ", Game_Board.turn, "'s turn")
        places = scores = []
        Minimax(Game_Board, 1, places, scores, "X", 1)
        Game_Board.fill(places[scores.index(min(scores))])
        print("I have now filled in the place of ", places[scores.index(min(scores))])
        print("The current board is")
        printBoard(Game_Board)



