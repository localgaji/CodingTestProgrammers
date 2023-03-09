def solution(n, m):
    maxdivisor = 1
    divisor = 2
    while divisor <= min(n,m):
        if n % divisor == 0 and m % divisor == 0:
            maxdivisor *= divisor
            n, m = n//divisor, m//divisor
            divisor = 2
        else :
            divisor += 1

    return [maxdivisor, maxdivisor*n*m]