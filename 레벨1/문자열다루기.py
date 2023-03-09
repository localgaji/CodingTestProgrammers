def solution(s):
    a = s.lower()
    A = s.upper()
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    if A != a:
        answer = False

    return answer