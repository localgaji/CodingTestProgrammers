def solution(n):
    answer = 0
    if n == 1:
        return 1
    for startnumber in range (1, n//2 + 1):
        sum = 0
        i = startnumber
        while sum < n:
            sum += i
            i += 1
        if sum == n:
            answer += 1
    return answer + 1

