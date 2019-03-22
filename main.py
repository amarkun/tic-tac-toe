#!/usr/bin/python3
# main.py
# Adam Markun
import pdb
import argparse

from lib.game import Game

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-s','--size',
            help='Size n will create an nxn board',
            type=int,
            dest='size'
    )
    args = parser.parse_args()
    size = 3 if args.size is None else args.size
    play_game = True
    while play_game:
        #initialize game
        game = Game(size=size)
        game.play_game()
        play_again = input('Would you like to play again? (y/n): ').lower()
        if play_again == 'n':
            print('Thanks for playing!')
            play_game = False
        elif play_again != 'y':
            print('We\'ll take that as a no...')
            play_game = False
        #else:
        #    size = int(input('What size board do you want?'))

    #handle input with boar
    #check move

if __name__ == "__main__":
    exit(main())
