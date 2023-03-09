def solution(participant, completion):

    dic = dict.fromkeys(participant,0)
    answer = []

    for i in participant:
        dic[i] += 1

    for j in completion:
        dic[j] -= 1

    for key, value in dic.items():
        if value != 0:
            answer.append(key)

    return answer[0]