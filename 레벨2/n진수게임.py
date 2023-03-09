def solution(n, t, m, p):
    answer = ''
    result = "0"
    i = 0
    num_alpha = ["A", "B", "C", "D", "E", "F"]
    while len(result) < t * m:
        decimal = i
        base_n = ""
        while decimal != 0:
            a = decimal % n
            if a >= 10:
                a = num_alpha[a % 10]
            base_n = str(a) + base_n
            decimal = decimal // n
        result += base_n
        i += 1

    for order in range(1, t * m):
        if order % m == p:
            answer += result[order - 1]

    return answer