def solution(s):
    s = s[2:-2]
    allsets = s.split("},{")
    answer = []
    for set in allsets:
        listset = set.split(",")
        answer.append(listset)
    answer.sort(key=len)

    result = []
    for set in answer:
        for i in set:
            if not int(i) in result:
                result.append(int(i))
    return result