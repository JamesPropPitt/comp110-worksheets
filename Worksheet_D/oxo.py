class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        #This command sets up the gameboard as 9 different values each beginning with 0(empty)
        self.game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        #Determines the location of a particular cell on the board using the equation y * 3 + x, so height of the co-ordinate input multiplied by 3 + the width of the co-ordinate input.
        return self.game_board[y * 3 + x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        #This algorithm accomplishes what the above two lines are asking for. The code checks get_square for the value 0 and if it is 0 returns with a mark.
        if self.get_square(x, y) == 0:
            self.game_board[y * 3 + x] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        #Once again the 2 lines above sum this up pretty well. this code goes through the length of the game_board and if any cell is empty it will return true
        for i in range(len(self.game_board)):
            if self.game_board[i] == 0:
                return False

        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
            #This determines the winner of the game by checking the co-ordinates of each possible win. Overall there are 8, 2 diagonals and 6 linear.
            #The diagonals, since they are only 2, can be done individually but instead of writing out 6 more lines of code for the linear win conditions we can use i
            #to tell the operation which number to display based on the sequence in the range of [0,1,2]
        for i in range(3):
            # Horizontal
            if self.get_square(0, i) == self.get_square(1, i) == self.get_square(2, i) != 0:
                return self.get_square(0, i)
            # Vertical
            if self.get_square(i, 0) == self.get_square(i, 1) == self.get_square(i, 2) != 0:
                return self.get_square(i, 0)
            # Diagonals
            if self.get_square(i, i) == self.get_square(i, i) == self.get_square(i, i) != 0:
                    return self.get_square(0, 0)
            if self.get_square(2, 0) == self.get_square(1, 1) == self.get_square(0, 2) != 0:
                    return self.get_square(2, 0)
        return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"