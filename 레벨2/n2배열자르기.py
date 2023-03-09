def solution(n, left, right):
    arr = []
    for row in range(left//n, right//n + 1):
        for column in range(0, n):
            if column >= row:
                arr.append(column + 1)
            else:
                arr.append(row + 1)
    return arr[left % n : (right - left) + (left % n) + 1]