#! /usr/bin/env python3
# Done by Henok_S
import pyperclip
import random



#Win Check function 
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
    return False

#Random value generator
#Takes a board as parameter
#Returns a value to be filled and the keys 
def generate_value(board):
    board_keys = [x for x in board.keys()]
    while 1:
        a = random.randint(0,8)
        if board[board_keys[a]] == " ":
            return ['C',board_keys[a]]


if __name__ == "__main__":
    for i in range (100):
        ttt = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}
        counter = 0
        w = open('database.txt', 'a')
        r = open('database.txt', 'r')
        text = r.read().split('\n\n')
        string = ""
        while ' ' in ttt.values():
            counter+=1
            if counter % 2 == 0:
                b = generate_value(ttt)
                place = b[1]
                value = b[0]
                ttt[place] = value
                string += place + ' ' + value + '\n'
                if CheckWin(ttt):
                    string += "C WON\n"
                    break
            else:
                b = generate_value(ttt)
                place = b[1]
                value = chr(ord(b[0])+1)#Print D instead of C
                ttt[place] = value
                string += place + ' ' + value + '\n'#to register the move
                if CheckWin(ttt):
                    string += "D WON\n"
                    break
        if string not in text:
            w.write(string)
        w.write('\n')
        w.close()
    if len(set(text)) == (text):
        print("ITS WORKING!!")
