def solution(arr_a, arr_b):
    answer = []
    row = []
    i, j, x, y, mul = 0, 0, 0, 0, 0
    while i < len(arr_a) :
        print(i+1, j+1, x+1, y+1)
        mul += arr_a[i][j] * arr_b[x][y]
        j += 1
        x += 1
        print("mul:", mul)
        if x == len(arr_b):
            j = 0
            x = 0
            y += 1
            row.append(mul)
            mul = 0
        if y == len(arr_b[0]):
            y = 0
            i += 1
            answer.append(row)
            row = []
    return answer