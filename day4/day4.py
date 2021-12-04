filename = "input.txt"
numbers = []
boards_list = []
won_boards = []

with open(filename, "r") as file:
    current = []
    for line in file:
        if len(numbers) == 0:
            numbers = list(map(int, line.rstrip().split(",")))
        else:
            board_line = line.rstrip().split()
            if board_line:
                current.append(list(map(int, board_line)))
                if len(current) == 5:
                    boards_list.append(current)
                    current = []


def mark_board(board, n):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                board[i][j] = -1


def check_marked_boards_rc(board):
    for i in range(len(board)):
        marked_rows = marked_columns = True
        for j in range(len(board[i])):
            if board[i][j] != -1:
                marked_rows = False
            if board[j][i] != -1:
                marked_columns = False
            if not marked_rows and not marked_columns:
                break
        if marked_rows or marked_columns:
            return True
    return False


def check_marked_boards(boards, winning):
    for i in range(len(boards)):
        if i in winning:
            continue
        if check_marked_boards_rc(boards[i]):
            return i
    return -1


def compute_score(b, n):
    score = 0
    for i in range(len(b)):
        for j in range(len(b[i])):
            value = b[i][j]
            if value != -1:
                score += value
    return score * n


def find_winner():
    score = 0
    for n in numbers:
        for i in range(len(boards_list)):
            if i not in won_boards:
                mark_board(boards_list[i], n)
        winner = 0
        while winner != -1:
            winner = check_marked_boards(boards_list, won_boards)
            if winner != -1 and winner not in won_boards:
                won_boards.append(winner)
                score = compute_score(boards_list[winner], n)
                if len(won_boards) == 1:
                    print("Part 1 solution, first winner score:", score)
    return score


print("Part 2 solution, last winner score:", find_winner())
