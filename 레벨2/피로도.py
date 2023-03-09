def solution(k, dungeons):
    import itertools

    a = itertools.permutations(range(len(dungeons)), len(dungeons))
    answers = []

    for order in a:
        answer = 0
        piro = k
        for index in order:
            dun = dungeons[index]
            if piro >= dun[0]:
                piro -= dun[1]
                answer += 1
        answers.append(answer)

    return max(answers)