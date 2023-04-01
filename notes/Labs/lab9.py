"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    """ initializes the board list """
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    """
    checks the value of the board at the given position
    if the value is 'x' or 'o', then it has already been played, making it illegal
    so to check if it IS legal, we need to make sure the value is NOT 'x' or 'o'
    """
    return not (board[position - 1] == 'x' or board[position - 1] == 'o')


def fill_spot(board, position, character):
    """
    first make sure the character is valid. using lower() and strip() are good ways to take out an irregularities
    then check if the move is legal. if it is not legal, we do not want to do anything, so we just return
    if it's the correct character and a legal move, change the value at the position (position - 1) to the given character

    There are plenty of other ways to lay out this logic, but this captures the general idea.

    """
    if character.lower().strip() != 'x' and character.lower().strip() != 'o':
        return
    if not is_legal(board, position):
        return
    board[position - 1] = character


def winning_game(board):
    """
    The and/or logic is that for each line, the first and second items need to be equal AND the second and third items
    also need to be equal.
    If that is True for the first row OR the second OR the third...then there is a winner.
    """
    winners = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for winner in winners:
        if board[winner[0]] == board[winner[1]] and board[winner[1]] == board[winner[2]]:
            return True
    return False
    # This is a brute force way of doing it
    # return board[0] == board[1] and board[1] == board[2] or \
    #        board[3] == board[4] and board[4] == board[5] or \
    #        board[6] == board[7] and board[7] == board[8] or \
    #        board[0] == board[3] and board[3] == board[6] or \
    #        board[1] == board[4] and board[4] == board[7] or \
    #        board[2] == board[5] and board[5] == board[8] or \
    #        board[0] == board[4] and board[4] == board[8] or \
    #        board[2] == board[4] and board[4] == board[6]


def game_over(board):
    """
    first check if the game has been won,
    if not, count the number of x's and o's on the board, if there have been 9 plays, the game is over!

    There are probably many ways to check if this game is done, for example you could also check if there are any
    spaces that have not yet been played on (see example comment). Any way that works and makes sense it good!

    example:
    over = True
    for spot in board:
        if not(spot == 'x' or spot == 'o'):
            over = False
            break
    return over
    """

    if winning_game(board):
        return True
    count = 0
    for spot in board:
        if spot == 'x' or spot == 'o':
            count = count + 1
    return count == 9


def get_winner(board):
    if winning_game(board):
        xes = 0
        oes = 0
        for space in board:
            if space == 'x':
                xes = xes + 1
            elif space == 'o':
                oes = oes + 1
        if xes > oes:
            return "x"
        return "o"
    return None


def play(board):
    """
    this function keeps track of whose turn it is.
    if you do not want to do that, you can have the user enter their letter and the position, either way is fine
    - we first check the board to see if it is a game over, either by 3 in a row or no more space
    - then we print the board and get the user input for where they want to go
    - the next condition is only necessary if the game is keeping track of which player is going. if you don't do that,
    then you should only need the fill_spot() function. in this case though, we need to know which player is up so we can
    automatically fill in the correct symbol. we also need to change players so the game knows the next player is up.
    You will notice that before we change players, we check if the move was legal. We do this because, if the move is not
    legal, we want the same player to go again. we can still call fill_spot, because the move will be illegal and nothing
    will change.
    - once the game is over, we reprint the board and say game over.
    we could try to say which player one, but then we would have to differentiate between winning vs. no more moves, which
    we currently do not do. So rather than that, we just stick with a generic game over message.
    """
    player_one = 'x'
    player_two = 'o'
    player_up = 1

    while not (game_over(board)):
        print_board(board)
        position = int(input('player {0}, choose a position: '.format(player_up)))
        if player_up == 1:
            if is_legal(board, position):
                player_up = 2
            fill_spot(board, position, player_one)

        else:
            if is_legal(board, position):
                player_up = 1
            fill_spot(board, position, player_two)

    print_board(board)
    winner = get_winner(board)
    if winner == 'x':
        print("x's win!")
    elif winner == 'o':
        print("o's win!")
    else:
        print('tie')

def main():
    play_again = True
    while play_again:
        board = build_board()
        play(board)
        play_again = input('play again? ')[0].lower() == 'y'


if __name__ == '__main__':
    main()
