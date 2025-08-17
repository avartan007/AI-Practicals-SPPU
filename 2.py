import math

def print_board(b):
    print('\n'.join(' | '.join(row) for row in b), '\n')

def check_win(b, p):
    lines = [[(r, c) for c in range(3)] for r in range(3)] + \
            [[(r, c) for r in range(3)] for c in range(3)] + \
            [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
    return any(all(b[i][j] == p for i, j in line) for line in lines)

def is_draw(b):
    return all(cell != ' ' for row in b for cell in row)

def minimax(b, is_max):
    if check_win(b, 'O'): return 1
    if check_win(b, 'X'): return -1
    if is_draw(b): return 0

    best = -math.inf if is_max else math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'O' if is_max else 'X'
                score = minimax(b, not is_max)
                b[i][j] = ' '
                best = max(best, score) if is_max else min(best, score)
    return best

def ai_move(b):
    best, move = -math.inf, None
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'O'
                score = minimax(b, False)
                b[i][j] = ' '
                if score > best:
                    best, move = score, (i, j)
    if move:
        b[move[0]][move[1]] = 'O'

def play_game():
    b = [[' '] * 3 for _ in range(3)]
    print("Tic Tac Toe - You (X) vs Bot (O)")
    print_board(b)

    while True:
        try:
            r, c = map(int, input("Enter your move (row col): ").split())
            if not (0 <= r < 3 and 0 <= c < 3) or b[r][c] != ' ':
                raise ValueError
        except:
            print("Invalid move. Try again.")
            continue

        b[r][c] = 'X'
        print_board(b)

        if check_win(b, 'X'):
            print("You win!")
            break
        if is_draw(b):
            print("Draw!")
            break

        ai_move(b)
        print("Bot played:")
        print_board(b)

        if check_win(b, 'O'):
            print("Bot wins!")
            break
        if is_draw(b):
            print("Draw!")
            break

play_game()


