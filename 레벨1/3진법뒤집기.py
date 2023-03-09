def solution(n):

    string = ""
    while True: #1,2가 아닐 동안
        rest = n % 3
        n = n // 3
        string = string + str(rest)
        n = n
        if n < 3:
            if n:
                string = string + str(n)
            break

    return int(string, 3)