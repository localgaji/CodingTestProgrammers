def solution(s):
    answer = sorted(s)
    answer.reverse()
    string = ""
    for i in answer:
        string += i

    return string