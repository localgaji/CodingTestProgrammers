def solution(n):
    answer = 1
    for number in range(3, n + 1):
        divisorcount = 1
        if number % 2 == 0:
            pass
        else:
            for divisor in range(2, int(number ** (0.5)) + 1):
                if number % divisor == 0:
                    divisorcount += 1
                    break
            if divisorcount == 1:
                answer += 1

    return answer