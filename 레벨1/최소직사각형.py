def solution(sizes):
    short, long = [], []

    for size in sizes:
        size.sort()
        short += [size[0]]
        long += [size[1]]

    answer = max(short) * max(long)
    return answer