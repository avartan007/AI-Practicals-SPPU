def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row, board, n):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(row + 1, board, n)

def print_board(solution):
    for row in solution:
        print(" ".join("Q" if i == row else "." for i in range(len(solution))))
    print()

n = int(input("Enter N: "))
solutions = []
solve(0, [0]*n, n)
print(f"\nFound {len(solutions)} solution(s):\n")
for sol in solutions:
    print_board(sol)
