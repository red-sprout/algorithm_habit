zeros = 0


def binary(num):
    s = ""
    while num > 0:
        s = str(num & 1) + s
        num = num >> 1
    return s


def convert(s):
    global zeros

    l = len(s)
    cnt = 0

    for i in range(l):
        c = s[i]
        if c == '1':
            cnt += 1
        else:
            zeros += 1

    return binary(cnt)


def loop(s):
    cnt = 0

    while s != "1":
        s = convert(s)
        cnt += 1

    return [cnt, zeros]


def solution(s):
    global zeros
    zeros = 0
    return loop(s)
