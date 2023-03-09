



def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    onecount, twocount, threecount = 0, 0, 0
    for i in range (0,len(answers)) :
        rest1, rest2, rest3 = i % 5, i % 8, i % 10
        if answers[i] == one[rest1]:
            onecount += 1
        if answers[i] == two[rest2]:
            twocount += 1
        if answers[i] == three[rest3]:
            threecount += 1

    score = [onecount, twocount, threecount]
    answer = []

    for i in range (1,4):
        if score[i-1] == max(score):
            answer += [i]

    return answer

print(solution([1,2,3,4,5]))