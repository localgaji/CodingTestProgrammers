def solution(numbers):

    answer = []
    for i in range (0,len(numbers)):
        a = numbers[i]
        for j in range (i+1,len(numbers)):
            b = numbers[j]
            if not a+b in answer:
                answer.append(a+b)

    return sorted(answer)