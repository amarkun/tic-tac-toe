class Board():
    def __init__(self, size=3):
        self.size = size
        self.board_template = ''
        print("Board set to size %s"%size)
    def create_board_template(self):
        col_template = (' %s |'*(self.size-1)) + ' %s '
        row_template = ('---+' *(self.size-1)) + '---'
        self.board_template = ('%s\n%s\n'%(col_template, row_template))*2+col_template
    def handle_input(self):
        self.num_values += 1
    def display_board(self, entries):
        '''
        entries: Dict<String: List<Tuple<Int, Int>>>
        Takes Dictionary with keys X and O, and values a list of ituples with int values like (row, col)
        Iterate through the letters and fill out final_entries with either X or O
        '''
        final_entry_list = [' ']*(self.size)**2
        for letter in entries:
            entry_list = entries[letter]
            for row, col in entry_list:
                index = self.size*row + col
                final_entry_list[index] = letter
        #TODO: get method of finding the height of the screen
        print('\n'*45 + self.board_template%tuple(final_entry_list))
