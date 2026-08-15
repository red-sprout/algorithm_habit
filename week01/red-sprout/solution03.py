maxSize = 0
cache = {}


def getOld():
    val = 1_000_000_007
    old = ""

    for key in cache:
        if val > cache[key]:
            val = cache[key]
            old = key

    return old


def update(city, idx):
    global maxSize, cache

    if maxSize == 0:
        return 5

    key = city.lower()
    t = 1 if key in cache else 5

    if key in cache or len(cache) < maxSize:
        cache[key] = idx
    else:
        del cache[getOld()]
        cache[key] = idx

    return t


def solution(cacheSize, cities):
    global maxSize, cache

    t = 0
    l = len(cities)

    maxSize = cacheSize
    cache = {}

    for i in range(l):
        t += update(cities[i], i)

    return t
