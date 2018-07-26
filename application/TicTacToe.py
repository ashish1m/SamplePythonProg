def displayBoard(board):
    print("\n   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("   |   |   \n")


def ifAnybodyWon(board, mark):
    return board[0] == board[1] == board[2] == mark \
           or board[3] == board[4] == board[5] == mark \
           or board[6] == board[7] == board[8] == mark \
           or board[0] == board[3] == board[6] == mark \
           or board[1] == board[4] == board[7] == mark \
           or board[2] == board[5] == board[8] == mark \
           or board[0] == board[4] == board[8] == mark \
           or board[2] == board[4] == board[6] == mark


def setPlayerSymbol():
    marker = ""

    while marker != 'X' and marker != 'O':
        marker = input("Player 1: choose your symbol from 'X' or 'O':: ").upper()

    if marker == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return {"p1": player1, "p2": player2}


def ifPosEmpty(board, pos):
    return not (board[pos] == "X" or board[pos] == "O")


def isAllFilled(board):
    for item in board:
        if item.lower() != 'x' and item.lower() != 'o':
            return False
    return True


def startGame(playerSymbol):
    tictactoe = [" "] * 9
    isPlayer1NotDone = True
    marker = ''

    while (not (ifAnybodyWon(tictactoe, marker))) and (not isAllFilled(tictactoe)):
        displayBoard(tictactoe)
        if isPlayer1NotDone:
            player1Pos = int(input("Player 1: Choose from 1-9 pos:: ")) - 1
            if player1Pos not in range(0, 9):
                print("Please choose number between 1-9")
                continue

            if ifPosEmpty(tictactoe, player1Pos):
                tictactoe[player1Pos] = marker = playerSymbol.get("p1")
                isPlayer1NotDone = False
            else:
                print("One of you have already played here. Choose some other place.")
                continue
        else:
            player2Pos = int(input("Player 2: Choose from 1-9 pos:: ")) - 1
            if player2Pos not in range(0, 9):
                print("Please choose number between 1-9")
                continue

            if ifPosEmpty(tictactoe, player2Pos):
                tictactoe[player2Pos] = marker = playerSymbol.get("p2")
                isPlayer1NotDone = True
            else:
                print("One of you have already played here. Choose some other place.")
                continue

    displayBoard(tictactoe)
    result = ifAnybodyWon(tictactoe, marker)
    if not result:
        print("OOPS!!! It's a draw. Better luck next time.")
    else:
        if playerSymbol.get("p1") == marker:
            winner = "Player 1"
        else:
            winner = "Player 2"
        print("Congratulations {}. You won the game".format(winner))


print("Hey! Welcome to the TIC-TAC-TOE game. \nI think you already know the rules of the game. \nLets get started.")

while True:
    playerSymbol = setPlayerSymbol()
    print("Lets start the game.")
    startGame(playerSymbol)
    playAgain = input("Do you want Play again? Enter Y or N: ").upper()
    if playAgain == "Y":
        continue
    else:
        break

print("Thanks for playing.")
exit()

# tictactoe = ["X", "O", "X", "X", " ", "O", "X", " ", "O"]
