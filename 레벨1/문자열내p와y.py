def solution(s):
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')

    if y != p:
        answer = False
    else:
        answer = True

    return answer