# Bryan Morris
# 11/11/19
# Tic Tac Toe

# Global Constants
X = "X"
O = "O"
EMPTY = " "
NUM_SQUARES = 9
TIE = "TIE"


#working
def intro():
    """ display game instructions """
    print (
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 1 - 9.  The number
    will correspond to the board position as illustrated:

                                 1  |  2  |  3
                                ------------
                                 4 |  5  |  6
                                ------------
                                 7 |  8  |  9

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
    )

#working
def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


#working
def display_board(board):
    """Display game board on screen."""
    print(str.format ("""
                                 {0}  |  {1}  |  {2}
                                ------------
                                 {3}  |  {4}  |  {5}
                                ------------
                                 {6}  |  {7}  |  {8}
                                 """,board [0] ,board[1], board[2],
                                       board [3] , board[4],
                                       board[5] , board[6],
                                       board[7] ,board[8]))


#working
def ask_yes_no(question):
    """Ask a yes or no question. and give a one letter response back"""
    response = None
    while response not in ("y","n","yes","no"):
        response  = input(question).lower()
    x = response[0]
    return x

#working
def ask_number(question, low, high):
    response = None
    while response not in range(low,high):
        try:
            response  = int(input(question))
        except:
            print("not a number")
    return response


#working
def assign_piece():
    "See who is going first"
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        comp = O
        player = X
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        player = O
        comp = X
    return player, comp


#working
def switch_turns(turn):
    if turn == X:
        return O
    else:
        return X

#working
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


#working
def player_turn(board,player):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (1 - 9):",1,10) -1
        if move not in legal:
            print("You are a stupid. Choose a different square.")
    print("Fine...")
    return move


#working
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            the_winner = board[row[0]]
            return the_winner
    if EMPTY not in board:
        return TIE
    
    return None


#working
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")

def comp_turn(board, comp, player):
    copy_board = board[:]
    BEST_MOVES1 = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    BEST_MOVES2 = (0, 8, 2, 6, 4, 7, 5, 3, 1)
    print("I shall take square number", end=" ")
    if comp == O:
        BEST_MOVES = BEST_MOVES1
    else:
        BEST_MOVES = BEST_MOVES2
    for move in legal_moves(board):
        copy_board[move] = comp
        if winner(copy_board) == comp:
            print(move +1)
            return move
        copy_board[move] = EMPTY
        
    for move in legal_moves(board):
        copy_board[move] = player
        if winner(copy_board) == player:
            print(move +1)
            return move
        copy_board[move] = EMPTY
        
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move +1)
            return move

def game():
    turn = X
    intro()
    board = new_board()
    display_board(board)
    player, comp = assign_piece()
    while not winner(board):
        if turn == player:
            move = player_turn(board,player)
            board[move]=player
        else:
            move = comp_turn(board, comp, player)
            board[move] = comp
        display_board(board)
        turn = switch_turns(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, comp, player)


game()


