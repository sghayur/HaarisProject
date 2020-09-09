# Author: Haaris Wasti
#The tic tac toe game know accomadates Two players
# They have been defined into classes 
# USer friendly features have been added to let the player make sure he inputs a valid input and the option to restart the game


# Move the existing code to a class Board and creating the object of the board in the game.

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
        # After 5 moves we will start checking for who wins becuase it is impossible to win before that
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
            # IF there is a tie it will still be announcend and you can play again
            elif self.totalMoves == 9:
                self.print_board()
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                return True
        return False
        
def get_valid_input (board)        :
    # Makes sure the input given works 
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

        # switches between player 1 and 2
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Asking if the players want to play again or not
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        game()

if __name__ == "__main__":
    game()