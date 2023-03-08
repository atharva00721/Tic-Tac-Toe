import random

#sets up board
def printBoard(value):
    print("\n")  
    print("\t      |      |")  
    print(f"\t  {value[0]}   |  { value[1]}   |  {value[2]}")  
    print('\t______|______|______')  
    print("\t      |      |") 
    print(f"\t  {value[3]}   |  {value[4]}   |  {value[5]}")  
    print('\t______|______|______')  
    print("\t      |      |")  
    print(f"\t  {value[6]}   |  {value[7]}   |  {value[8]}")  
    print("\t      |      |")  
    print("\n") 


#Checks if the board is filled completely
def empty(board):
    empty = 9
    for i in range(len(board)):
        if board[i] != "-":
            empty -= 1
    if empty == 0:
        return True
    
    
#Checks if the position player wants to take is already taken
def checkAvailable(board_element):
    if board_element == "-":
        return True
    else:
        return False
    

#Checks if the play won
def checkWin(board):
    winLines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ]
    for line in winLines:
        if (board[line[0]]=="X" or board[line[0]]=='O'):
            if board[line[0]] == board[line[1]] == board[line[2]]:
                return True
            

#bot
def bot(board):
    availableMoves = []
    for position in range(len(board)):
        if board[position] == "-":
            availableMoves.append(position+1)
    m = random.choice(availableMoves)
    return m


def score():
    
if __name__ == "__main__":
    turn = 1 # 1 == X, 0 == O
    print("""
    ----------------------------------
    |                                |   
    |   Welcome to Tic Tac Toe       |
    |                                |
    ----------------------------------
    """)
    mode = 1
    while True:
        print("""
        Enter 1 to play
        Enter 2 to quit""")
        mode = int(input(">> "))
        if mode == 2:
            break
        # initial empty array  
        board = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]
        printBoard(board)
        while True:
            try:
                if turn == 1:
                    move = int(input(">> "))
                    # move = 1
                    try:
                        if checkAvailable(board[move - 1]):
                            board[move - 1] = "X"
                            printBoard(board)
                            if checkWin(board):
                                print("X WON")    
                                break 
                            turn -= 1
                            print("O's Chance")
                        else:
                            print("Please select another position")
                    except ValueError:
                        print("a number between 1-9")
                    
                else:
                    bot_move = int(bot(board))
                    # bot_move = 1
                    if checkAvailable(board[bot_move-1]):
                        board[bot_move - 1] = "O"
                        printBoard(board)
                        if checkWin(board):
                            print("O WON")    
                            break   
                        turn += 1
                        print("X's Chance")
                
                
            except ValueError:
                print("fuck you use a number between 1 to 9")
                break
            if empty(board):
                print("Game Over! It's a tie")
                break
                    