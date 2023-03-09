def solution(cacheSize, cities):

    from collections import deque

    answer = 0
    cache = deque()
    if cacheSize == 0:
        cacheSize = 1
    for i in cities:
        i = i.lower()
        if i in cache: # hit
            answer += 1
            if i != cache[-1]:
                index = cache.index(i)
                cache[index], cache[-1] = cache[-1], cache[index]
        elif len(cache) < cacheSize: # 공간 남음
            answer += 5
            cache.append(i)
        elif len(cache) == cacheSize: # full
            answer += 5
            cache.popleft()
            cache.append(i)
        print(cache, answer)

    return answer