import random


def drawBoard(board):

    print("   |   |")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |")


def inputPlayerLetter():
    letter = ''
    while not(letter =='X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    if random.randint(0,1) == 0 :
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes/no)')
    return raw_input().lower().startswith('y')

def makeMove(board, letter,move):
    board[int(move)] = letter


def isWinner(b,l):
    return((b[7]== b[8] == b[9] == l) or
           (b[4] == b[5] == b[6] == l) or
           (b[1] == b[2] == b[3] == l) or
           (b[1] == b[4] == b[7] == l) or
           (b[2] == b[5] == b[8] == l) or
           (b[3] == b[6] == b[9] == l) or
           (b[7] == b[5] == b[3] == l) or
           (b[9] == b[5] == b[1] == l))
    
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '



def getPlayerMove(board):  
    move = ' ' 
    while str(move) not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not isSpaceFree(board, int(move)):
          print('What is your next move? (1:9)')
          move = input()
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
        


def getComputerMove(board,computerLetter): #AIalgorithm
    if computerLetter =='X':
        playerLetter = 'O'
    else:
        playerLetter ='X'

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move
    if isSpaceFree(board,5):
        return 5
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

#The start of the game
print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The '+turn+' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)

            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print('You Win!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie.')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print('Oops! you LOSE.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie.')
                        break
                else:
                    turn = 'player'

    if not playAgain():
            break
                



    
    
            
