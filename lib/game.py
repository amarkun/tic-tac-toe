from lib.player import Player
from lib.board import Board

class Game():
    def __init__(self, size=3):
        self.size = size
        self.comb_entries_dict = {'X':[],'O':[]}
        self.board = Board(size)
        self.board.create_board_template()

    def setup_game(self):
        player1_letter = input("What letter would Player 1 like to user? (X or O)?: ").upper()
        if player1_letter not in ['X', 'O']:
            print('Invalid input! Automatically selecting X for Player 1 and O for Player 2')
            player1_letter = 'X'
            player2_letter = 'O'
        else:
            print('Assigned %s to Player 1'%player1_letter)
            player2_letter = 'O' if player1_letter == 'X' else 'X'
            print('Assigned %s to Player 2'%player2_letter)
        self.p1 = Player('Player 1', player1_letter, self.size)
        self.p2 = Player('Player 2', player2_letter, self.size)
    def update_entries(self, player, row, col):
        '''
        row: String
        col: String
        converts a row and col stirng to entries to be used in the board display
        '''
        #update entries for the player, should this be done here?
        # maybe player should be a subclass of Game?
        player.add_entry('row', row)
        player.add_entry('col', col)
        #convert string to actual index, subtract 1 for math reasons
        row_index = int(row)-1
        col_index = int(col)-1
        entry = (row_index, col_index)
        #used to check if entries have been made before
        self.comb_entries.add((row,col))
        #uses the
        self.comb_entries_dict[player.letter].append(entry)

    def check_winner(self, player):

        choices_dict = player.choices_dict
        diag = 0
        for loc_dict in choices_dict.values():
            for entry in loc_dict.values():
                if entry == self.size:
                    return True

        #TODO figure out a better way to do this
        left_diag_list = [(num,num) for num in range(self.size)]
        right_diag_list = [(num,(self.size-num-1)) for num in range(self.size)]
        lDiag = 0
        rDiag = 0
        for choice in player.choices:
            if choice in left_diag_list:
                lDiag += 1
            if choice in right_diag_list:
                rDiag += 1
        if lDiag == self.size or rDiag == self.size:
            return True
        return False
    @property
    def num_entries(self):
        '''
        Returns the number of total entries
        '''
        return (len(self.p1.choices) + len(self.p2.choices))
    @property
    def combined_entries(self):
        '''
        Returns a list of combined entries
        '''
        return self.p1.choices + self.p2.choices

    def play_game(self):
        winner = False
        print('Game Start!')
        while winner is False:
            self.board.display_board(self.p1, self.p2)
            current_player = self.p1 if self.num_entries % 2 == 0 else self.p2
            #note these are strings
            row, col = current_player.query()
            while (row,col) in self.combined_entries:
                print('That location is already filled. Please pick a new locatoin.')
                row, col = current_player.query()
            current_player.add_entry(row, col)
            winner = self.check_winner(current_player)
            if winner is True:
                self.board.display_board(self.p1, self.p2)
                print('%s is the winner!!!'%current_player.name)
            elif self.num_entries == self.size**2:
                self.board.display_board(self.p1, self.p2)
                print('Tie Game!')
                winner = True
            #self.check_finished(p1.choice, p2.choice)
            #check for winner
