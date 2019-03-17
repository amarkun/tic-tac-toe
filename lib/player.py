class Player():
    def __init__(self, name, letter, size=3):
        self.name = name
        self.letter = letter
        self.choices = {'row':{}, 'col':{}}
        self.size = size
        self.valid_choice = [str(value) for value in range(1,size+1)]

    def check_valid_choice(self, value, place):
        while value not in self.valid_choice:
            print('%s is not a valid %s'%(value, place))
            value = input('Please enter a valid %s (%d - %d): ' % (place, 1, self.size))
        return value

    def add_entry(self, key, value):
        '''
        row: Stirng
        col: String
        Adds the row and string to the players choices dictionary
        '''
        current_entry = self.choices[key].get(value, None)
        if current_entry is None:
            self.choices[key][value] = 1
        else:
            self.choices[key][value] += 1

        if self.choices[key][value] > self.size:
            print('::: ERROR: Too many entries.')
            exit(0)

    def query(self):
        choice = input('%s: What move would you like to make? row, column (%d - %d): '%(self.name, 1, self.size)).replace(' ','').split(',')
        while len(choice) != 2:
            print ('Please specify two values')
            choice = input('%s: What move would you like to make? row, column (%d - %d): '%(self.name, 1, self.size)).replace(' ','').split(',')
        row, col = choice
        row = self.check_valid_choice(row, 'row')
        col = self.check_valid_choice(col, 'column')

        return (row, col)
