def solution(strings, n):

    nstrings, answer = [], []
    for string in strings:
        string = string[n] + string
        nstrings.append(string)

    nstrings.sort()

    for string in nstrings:
        answer.append(string[1:])

    return answer
