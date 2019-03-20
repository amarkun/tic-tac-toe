class Player():
    def __init__(self, name, letter, size=3):
        self.name = name
        self.letter = letter
        self.choices = []
        self.choices_dict = {'row':{}, 'col':{}}
        self.size = size
        self.valid_choice = [str(value) for value in range(1,size+1)]

    def check_valid_choice(self, value, place):
        while value not in self.valid_choice:
            print('%s is not a valid %s'%(value, place))
            value = input('Please enter a valid %s (%d - %d): ' % (place, 1, self.size))
        return value

    def add_entry(self, row, col):
        '''
        row: Stirng
        col: String
        Adds the row and string to the players choices dictionary
        '''
        entry = (row, col)
        self.choices.append(entry)

        row_entry = self.choices_dict['row'].get(row, None)
        col_entry = self.choices_dict['col'].get(col, None)

        #TODO find better method for below
        if row_entry is None:
            self.choices_dict['row'][row] = 1
        else:
            self.choices_dict['row'][row] += 1
        if col_entry is None:
            self.choices_dict['col'][col] = 1
        else:
            self.choices_dict['col'][col] += 1

        #Should not happen
        if len(self.choices) > (self.size**2)/2 +1 :
            print('::: ERROR: Too many entries.')
            exit(0)

    def query(self):
        '''
        Asks users to enter coordinates of their desired entry placement
        This will be entered as 1 - board size, however they will be stored as 0 - board size minus 1
        '''
        choice = input('%s: What move would you like to make? row, column (%d - %d): '%(self.name, 1, self.size)).replace(' ','').split(',')
        while len(choice) != 2:
            print ('Please specify two values')
            choice = input('%s: What move would you like to make? row, column (%d - %d): '%(self.name, 1, self.size)).replace(' ','').split(',')
        row, col = choice
        row = self.check_valid_choice(row, 'row')
        col = self.check_valid_choice(col, 'column')

        #decrease by 1 to start from index 0
        return (int(row)-1, int(col)-1)
