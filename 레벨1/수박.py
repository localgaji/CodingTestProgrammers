def solution(n):
    string = ""
    for i in range(1, n + 1):
        if i % 2 == 1:
            string = string + "수"
        else:
            string = string + "박"

    return string