def solution(string, n):
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = big.lower()
    answer = ""
    for s in string :
        if s == " ":
            moved = s
        elif s in big:
            moved = big[big.index(s) + n]
        elif s in small:
            moved = small[small.index(s) + n]
        answer += moved

    return answer
