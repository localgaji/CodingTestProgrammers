import math as mt

def solution(n,a,b):
    answer = 0
    while a != b:
        a, b = mt.ceil(a / 2), mt.ceil(b / 2)
        answer += 1

    return answer