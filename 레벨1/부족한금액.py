def solution(numbers):
    zerotonine = [0,1,2,3,4,5,6,7,8,9]

    for i in numbers :
        if i in zerotonine:
            zerotonine.remove(i)
    answer = 0
    for i in zerotonine:
        answer += i
    return answer
