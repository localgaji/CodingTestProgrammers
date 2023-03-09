def solution(n):
    n,m = int(n.split()[0]), int(n.split()[1])
    row = '*' * n + '\n'

    return (row * m)[:-1]