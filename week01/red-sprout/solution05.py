n = 0
pillar = []
beam = []

dx = [-1, 0, 1, 0, -1, 1, -1, 1, 0]
dy = [0, -1, 0, 1, 1, -1, -1, 1, 0]


def init(_n):
    global n, pillar, beam

    n = _n
    pillar = [[False] * (n + 1) for _ in range(n + 1)]
    beam = [[False] * (n + 1) for _ in range(n + 1)]


def pillarCheck(x, y):
    return (
        y == 0
        or beam[x][y]
        or (x > 0 and beam[x - 1][y])
        or (y > 0 and pillar[x][y - 1])
    )


def beamCheck(x, y):
    return (
        (y > 0 and pillar[x][y - 1])
        or (x < n and y > 0 and pillar[x + 1][y - 1])
        or (
            (x > 0 and beam[x - 1][y])
            and (x < n and beam[x + 1][y])
        )
    )


def create(x, y, a):
    if a == 0:
        if pillarCheck(x, y):
            pillar[x][y] = True
    else:
        if beamCheck(x, y):
            beam[x][y] = True


def delete(x, y, a):
    if a == 0:
        if not pillar[x][y]:
            return

        flag = False
        pillar[x][y] = False

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n and 0 <= ny <= n:
                if pillar[nx][ny] and not pillarCheck(nx, ny):
                    flag = True
                    break

                if beam[nx][ny] and not beamCheck(nx, ny):
                    flag = True
                    break

        pillar[x][y] = flag

    else:
        if not beam[x][y]:
            return

        flag = False
        beam[x][y] = False

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n and 0 <= ny <= n:
                if pillar[nx][ny] and not pillarCheck(nx, ny):
                    flag = True
                    break

                if beam[nx][ny] and not beamCheck(nx, ny):
                    flag = True
                    break

        beam[x][y] = flag


def getStructure():
    answer = []

    for x in range(n + 1):
        for y in range(n + 1):
            if pillar[x][y]:
                answer.append([x, y, 0])
            if beam[x][y]:
                answer.append([x, y, 1])

    return answer


def solution(n, build_frame):
    init(n)

    for build in build_frame:
        if build[3] == 1:
            create(build[0], build[1], build[2])
        else:
            delete(build[0], build[1], build[2])

    return getStructure()
