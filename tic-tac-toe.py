# Author: Ziqing Zhang
# Descrption: Tic-Tac-Toe Game

# The TicTacToe board is stored in a 3x3 multidimensional list of characters containing spaces at the start of the game (an empty board). 
# Each time a player makes a move, an 'X' or 'O' is put in the proper location in the array.
# Your "clear" function should initialize the board to store spaces
# Your "display" function should display the board, with gridlines between each position (using the characters '-' and '|', which are not stored in the array)
# Your "takeTurn" function should ask the user to enter amove, and check for errors in input. Specifically, you should check for the following 2 kinds of errors:
# Row or Column is out of range (less than 0 or greater than 2)
# Specified position is already occupied (a player can only move to an empty spot)
# If either of the above errors are found, the same player should be asked to re-enter their move until they get it right.
# Your "winner" function should examine the board and return one of the following characters:
# ' ' (a space) meaning the game is not yet over
# 'X' meaning that player X has won
# 'O' meaning that player O has won
# '?' meaning that the game is over because the board is full, but no one won.
# I recommend you write some helper functions to help with all the various pieces of this program.
# Remember you should never copy and paste code if you can avoid it.
# Write a function to perform a common, generalizable task, and call that function every time you need it.
# As always, don't use any global variables.
# Following is the beginning of the TicTacToe program and an example of how your program should behave. 
# You should copy this TicTacToe.cpp file exactly and use it as a starting point and to test your code once you've finished it. 


#    Starting point for Extra Credit
#    Tic Tac Toe game program

def clear():        # Clears the board of any char from before and starts a new game.
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


# ///////  display  ////////
# // Display the current status of the board on the
# // screen, using hyphens (-) for horizontal lines
# // and pipes (|) for vertical lines.
def display(board):       # Draws board on screen.
  for row in range(len(board)):
    for col in range(len(board)):
      print(board[row][col] + "|", end = '')
      
    if (row != len(board) - 1):
      print("\n-------")
  print("")
  
  return True

# ///////  takeTurn  ////////
# // Allow the nextPlayer to take a turn.
# // Send output to screen saying whose turn
# // it is and specifying the format for input.
# // Read user's input and verify that it is a
# // valid move.  If it's invalid, make them
# // re-enter it.  When a valid move is entered,
# // put it on the board.
def takeTurn(board, nextPlayer):        # Input Validation, and takeTurn function                                          to obtain different player choices.
  row = None
  col = None
  
  while (row is None or col is None):
    try:
      print("Its " + nextPlayer + " turn : ")
      print("Please enter your move in row and column.")
      print("So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.")
      row = int(input("Enter row: "))
      col = int(input("Enter col: "))

      if (0 <= row and  row <= 2 and 0 <= col and col <= 2):
          if board[row][col] == ' ':
              board[row][col] = nextPlayer
              break
          else:
              print("ERROR. Position is occupied.")
              row = None
              col = None
      else:
          print("Invalid entry: row and column must both be between 0 and 2 (inclusive). Please try again.")
          row = None
          col = None
          
    except:
        print("ERROR: Must be numeric values. Please try again.")
        row = None
        col = None

  if nextPlayer == 'X':
    return 'O'
  else:
    return 'X'



# ///////  winner  /////////
# // Examines the board and returns one of the following:
# // ' ' (a space) meaning the game is not yet over
# // 'X' meaning that player X has won
# // 'O' meaning that player O has won
# // '?' meaning that the game is over because the board
# //     is full, but no one won.
def winner(board):        # Checks for any winning cases to end the game.

    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board [0][0] is not ' ':
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not ' ':
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not ' ':
        return board[0][2]
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not ' ':
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not ' ':
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]and board[2][0] is not ' ':
        return board[2][0]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not ' ':
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] is not ' ':
        return board[0][2]
    for row in board:
        for cell in row:
            if cell ==' ':
              return '?'

    return '?'

# ///////  main  ////////
# // No changes needed in this function.
# // It declares the variables, initializes the game,
# // and plays until someone wins or the game becomes unwinnable.
def main():       # Calls on all functions, and makes the game happen.

  board = clear()
  nextPlayer = 'X'
  winningPlayer = ' '

  display(board)

  while winningPlayer == ' ':
      nextPlayer = takeTurn(board, nextPlayer)
      display(board)
      winningPlayer = winner(board)
      
      if winningPlayer == 'X' or winningPlayer == 'O':
        print("Congratulations, ", winningPlayer, " YOU WON!")
      else:
        winningPlayer = ' '
  return True

main()

# Test Results
# 
#  | | |
# -------
#  | | |
# -------
#  | | |
# Its X turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: q
# ERROR: Must be numeric values. Please try again.
# Its X turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: -2
# Enter col: 2
# Invalid entry: row and column must both be between 0 and 2 (inclusive). Please try again.
# Its X turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 1
# Enter col: 1
#  | | |
# -------
#  |X| |
# -------
#  | | |
# Its O turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 0
# Enter col: 2
#  | |O|
# -------
#  |X| |
# -------
#  | | |
# Its X turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 0
# Enter col: 1
#  |X|O|
# -------
#  |X| |
# -------
#  | | |
# Its O turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 1
# Enter col: 2
#  |X|O|
# -------
#  |X|O|
# -------
#  | | |
# Its X turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 0
# Enter col: 1
# ERROR. Position is occupied.
# Its X turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 0
# Enter col: 0
# X|X|O|
# -------
#  |X|O|
# -------
#  | | |
# Its O turn :
# Please enter your move in row and column.
# So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.
# Enter row: 2
# Enter col: 2
# X|X|O|
# -------
#  |X|O|
# -------
#  | |O|
# Congratulations,  O  YOU WON!
