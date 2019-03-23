#!/usr/bin/python3
# main.py
# Adam Markun
import pdb
import argparse

from lib.game import Game

def getArgs():
    '''
    Handles command line input and returns the parser object
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-s','--size',
            help='Size n will create an nxn board',
            type=int,
            dest='size'
    )
    return parser.parse_args()


def main():
    args = getArgs()
    #check args
    size = 3 if args.size is None else args.size
    if size <3 or size >10:
        print('Please enter a size in the range 3-10')
        return 0
    #enter game loop
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
