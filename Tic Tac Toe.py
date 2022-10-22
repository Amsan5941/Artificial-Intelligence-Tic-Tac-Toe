#Amsan Naheswaran Tic Tac Toe Game

board=[' ' for x in range (0,10)]

def placementLetter(letter,pos):
    board[pos]=letter

def freeSpaces(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def winner(gameboard,letter):
    return (gameboard[7]==letter and gameboard[8]==letter and gameboard[9]==letter) or (gameboard[4]==letter and gameboard[5]==letter and gameboard[6]==letter) or(gameboard[1]==letter and gameboard[2]==letter and gameboard[3]==letter) or(gameboard[1]==letter and gameboard[4]==letter and gameboard[7]==letter) or(gameboard[2]==letter and gameboard[5]==letter and gameboard[8]==letter) or(gameboard[3]==letter and gameboard[6]==letter and gameboard[9]==letter) or(gameboard[1]==letter and gameboard[5]==letter and gameboard[9]==letter) or(gameboard[3]==letter and gameboard[5]==letter and gameboard[7]==letter)
    
def playerMove():
    run=True
    while run:
        move=input("Please choose where you would like to place an 'X' (1-9): ")
        try:
            move=int(move)
            if move>0 and move<10:
                if freeSpaces(move):
                    run=False
                    placementLetter("X",move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("The move is not in the range from 1-9!")     
        except:
            print("Please type a number!")
            
def compMove():
    possibleMoves=[x for x, letter in enumerate(board) if letter==" " and x!=0]
    move=0

    for let in ["O","X"]:
        for i in possibleMoves:
            boardCopy=board[:]
            boardCopy[i]=let
            if winner(boardCopy,let):
                move=i
                return move

    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen)>0:
        move=selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move=5
        return move

    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)

    return move

    
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def Boardfull(board):
    if board.count(" ")>1:
        return False
    else:
        return True
    
def main():
    print("Welcome to the Tic Tac Toe! Where you will be versuing my program! Good Luck!")
    printBoard(board)

    while not(Boardfull(board)):
        if not (winner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("The program has won this time!")
            break
        if not (winner(board,"X")):
            move=compMove()
            if move==0:
                print("Tie Game!")
            else:
                placementLetter("O",move)
                print("Computer has placed an 'O' in postion",move,":")
                printBoard(board)
        else:
            print("You have won this time!")
            break
        
        
        
    if Boardfull(board):
        print("Tie Game!")
main()
