#! /usr/bin/env python3
# Done by Henok_S
import pyperclip
import random
def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

def CheckWin(board):
    board_in_list = [x for x in ttt.values()]
    board_in_list_copy = board_in_list
    if board['top-l'] == board['mid-m'] == board['low-r'] != " " or board['top-r'] == board['mid-m'] == board['low-l'] != " ":
        return True
    arr = []
    arr_H = []
    for j in range (3):
        arr.append([])
        for i in range (3):
            arr[j].append(board_in_list[((j)+3*(i))])
        arr_H.append(board_in_list_copy[:3])
        board_in_list_copy = board_in_list_copy[3:]
    for a in range (3):
        if (len(set((arr[a]))) == 1 and " " not in arr[a]) or (len(set((arr_H[a]))) == 1 and " " not in arr_H[a]):
            return True
    print(arr)
    return False
    
def generate_value(board):
    board_keys = [x for x in board.keys()]
    while 1:
        a = random.randint(0,9)
        if board[board_keys[a]] == " ":
            return ['C',board_keys[a]]
    
    

 

ttt = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
       'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
       'low-l': ' ', 'low-m': ' ', 'low-r': ' '}
print(ttt)
printBoard(ttt)
counter = 0
r = open('database.txt', 'r')
text = (r.read()).split("\n\n")
w = open('database.txt', 'w')

while ' ' in ttt.values():
    counter+=1
    if counter % 2 == 0:
        b = generate_value(ttt)
        place = b[1]
        value = b[0]
        ttt[place] = value
        
        printBoard(ttt)
        if CheckWin(ttt):
            print("Player ",value," won!!")
            break
    else:
        print('Input which place to fill in')
        place = input()
        if place == '':
            printBoard(ttt)
            break
        elif ttt[place] == ' ':
            print('Input what you want to fill it with')
            value = input()
            ttt[place] = value
            printBoard(ttt)
            if CheckWin(ttt):
                print("Player ",value," won!!")
                break
        else:
            print('value already occupied try again')
    