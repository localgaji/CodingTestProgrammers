def solution(n):
    answer = ''
    dic = {1:"1", 2:"2", 0:"4"}
    while n > 0:
        front = n % 3
        answer = dic[front] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
        print(front, n, answer)

    return answer