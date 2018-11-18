# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:43:02 2018

@author: ravul
"""


def gameBoard (player = 0, row = 0, column = 0, justDisplay = False):
    try:
        if not justDisplay:
            game[row][column] = player
        print('   0  1  2')
        for count,row in enumerate(game):
            print(count, row)
    except IndexError as e:
        print(e, "\nMake sure you have entered the correct indices values")
        
def winner(current_game):
    
    # Horizontal
    for horzt in game:
        if horzt.count(horzt[0]) == len(horzt) and horzt[0] != 0:
            print("Winner is player", horzt[0],'- Horizontal')
            return True
    # Diagonal
    diag1 = []
    for col,row in enumerate(reversed(range(len(game)))):
        diag1.append(game[row][col])
    if diag1.count(diag1[0]) == len(diag1) and diag1[0] != 0:
        print("Winner is player", diag1[0],'- Diagonal')
        return True
    
    diag2 = []
    for idx in range(len(game)):
        diag2.append(game[idx][idx])
    if diag2.count(diag2[0]) == len(diag2) and diag2[0] != 0:
        print("Winner is player", diag2[0],'- Diagonal')
        return True
    
    # Vertical
    for col in range(len(game)):
        column = []
        for row in game:
            column.append(row[col])
        if column.count(column[0]) == len(column) and column[0] != 0:
            print("Winner is player", column[0],'- Vertical')
            return True
    return False
            
play = True
import itertools
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    gameBoard(justDisplay = True)
    gameWon = False
    Players = itertools.cycle([1,2])
    while not gameWon:

        current_player = next(Players)
        print("Player " + str(current_player) + "'s turn")
        row_choice = int(input("What row do you want to place? \n(0,1,2):"))
        col_choice = int(input("What column do you want to place? \n(0,1,2):"))
        gameBoard(current_player, row_choice, col_choice)
        if winner(game):
            break
    if not (input("Do you want to play another game (y/n)?:") == 'y'):
        break
    