def solution(array, commands):
    answer = []

    for i in commands:
        new = sorted(array[i[0]-1:i[1]])
        answer.append(new[i[2]-1])

    return answer