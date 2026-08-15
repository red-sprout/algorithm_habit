m, n = 0, 0
board = []


def init(_m, _n, sArr):
    global m, n, board

    m = _m
    n = _n
    board = [[''] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            board[i][j] = sArr[i][j]


def erase():
    visited = [[False] * n for _ in range(m)]

    for i in range(m - 1):
        for j in range(n - 1):
            c = board[i][j]

            if c == '.':
                continue

            if (c == board[i + 1][j]
                and c == board[i][j + 1]
                and c == board[i + 1][j + 1]):
                visited[i][j] = True
                visited[i + 1][j] = True
                visited[i][j + 1] = True
                visited[i + 1][j + 1] = True

    cnt = 0

    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
                board[i][j] = '.'

    return cnt


def fall():
    queues = [[] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if board[i][j] != '.':
                queues[j].append(board[i][j])

    for i in range(m - 1, -1, -1):
        for j in range(n):
            if queues[j]:
                board[i][j] = queues[j].pop()
            else:
                board[i][j] = '.'


def solution(m, n, board):
    init(m, n, board)

    answer = 0

    while True:
        cnt = erase()

        if cnt == 0:
            break

        answer += cnt
        fall()

    return answer
