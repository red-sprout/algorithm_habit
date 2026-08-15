def findIdx(n, words):
    l = len(words)
    set_ = set()
    last = ""

    for i in range(l):
        if words[i] in set_:
            return i

        if last != "" and last[-1] != words[i][0]:
            return i

        set_.add(words[i])
        last = words[i]

    return -1


def convert(n, idx):
    if idx == -1:
        return [0, 0]

    return [
        idx % n + 1,
        idx // n + 1
    ]


def solution(n, words):
    idx = findIdx(n, words)
    return convert(n, idx)
