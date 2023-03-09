def solution(n):
    x = 1
    y = 1
    count = 0
    while count < n - 2:
        newx = y
        newy = x + y
        x, y = newx, newy
        count += 1

    return y % 1234567