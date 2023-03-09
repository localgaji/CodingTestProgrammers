def solution(clothes):

    dic = {}
    for i in clothes:
        key, value = i[1], i[0]
        if key in dic.keys():
            dic[key] += 1
        else:
            dic[key] = 2

    answer = 1
    for i in list(dic.values()):
        answer *= i

    return dic.values(), answer