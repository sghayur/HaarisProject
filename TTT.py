#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
in which keys will be the location(i.e : top-left,mid-right,etc.)
and initially it's values will be empty space and then after every move 
we will change the value according to player's choice of move. '''


class Board:
    def __init__ (self):
        self.totalMoves = 0
        self.board = {'7': ' ' , '8': ' ' , '9': ' ' ,
                      '4': ' ' , '5': ' ' , '6': ' ' ,
                      '1': ' ' , '2': ' ' , '3': ' ' }
    
    def print_board (self):
        B = self.board
        print(B['7'] + '|' + B['8'] + '|' + B['9'])
        print('-+-+-')
        print(B['4'] + '|' + B['5'] + '|' + B['6'])
        print('-+-+-')
        print(B['1'] + '|' + B['2'] + '|' + B['3'])

    def update_board (self, pos, turn):
        if self.is_valid_move(pos):
            self.board[pos] = turn
            self.totalMoves += 1
           
    def is_valid_move (self, pos):
         return self.board[pos] == ' '
    
    def is_game_over (self, turn):
        # We will check if player X or O has won,for every move after 5 moves. 
        B = self.board
        won = (B['7'] == B['8'] == B['9'] != ' ')  or \
              (B['4'] == B['5'] == B['6'] != ' ')  or \
              (B['1'] == B['2'] == B['3'] != ' ')  or \
              (B['1'] == B['4'] == B['7'] != ' ')  or \
              (B['2'] == B['5'] == B['8'] != ' ')  or \
              (B['3'] == B['6'] == B['9'] != ' ')  or \
              (B['7'] == B['5'] == B['3'] != ' ')  or \
              (B['1'] == B['5'] == B['9'] != ' ')         
        
        if self.totalMoves >= 5:
            if won:
                self.print_board()
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                return True
            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            elif self.totalMoves == 9:
                self.print_board()
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                return True
        return False
        
def get_valid_input (board)        :
    # Keep asking for input until a valid input is given.
    print("Move to which place?")
    while True:
        move = input()
        if move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print ("Enter one of 1 2 3 4 5 6 7 8 9")
        elif not board.is_valid_move (move):
            print("That place is already filled")
        else:
            break
    return move

def game():
    board = Board()
    turn = 'X'
    
    for i in range(10):
        board.print_board()
        print("It's your turn" + turn)
        move = get_valid_input(board)
        board.update_board(move, turn)
        if board.is_game_over(turn):
            break

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        game()

if __name__ == "__main__":
    game()