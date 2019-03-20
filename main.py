# main.py
# Adam Markun
import pdb
import argparse

from lib.game import Game

#TODO currently there are three sources of entries
# 1. a dict of X and O with lists containing tuples of (row, col) numbers
# 2. a set of (row, col) tuples
# 3. a dict of 'col' and 'row' which are dicts with 1 to the size of the board for each entry_list
# 1 is used when the baord is displayed
# 2 is used to check if an entry already exists
# 3 is used to check if a user is a check_winner
# I want to keep 3 because a player class should have access to answers
# I want to keep 1 because there needs to be a dictionary containing actual x and o splits
# Possible solution:
# only the players will have a record of entries, which will be formatted (row, col)
# when the board is displayed, both players will be fed to the board, and the board will format these correctly
# for check answer the dictionary like 3 will be constructed and checked in the same function
# Note this makes it more dependent on having two players
def main():
    #initialize game
    game = Game()
    game.setup_game()
    game.play_game()


    #handle input with boar
    #check move

if __name__ == "__main__":
    main()
