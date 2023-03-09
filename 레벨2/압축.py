#일부 런타임 에러

def solution(msg):
    answer = []
    words = ["A", "B", "C", "D", "E",
             'F', "G", 'H', "I", 'j',
             'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']
    dic = {}
    index = 1
    for w in words:
        dic[w] = index
        index += 1

    i = 0
    while i < len(msg):
        n = 1
        s = msg[i:i + n]
        while s in dic.keys() and i + n < len(msg):
            n += 1
            s = msg[i:i + n]
        print(s)
        answer.append(dic[s[:-1]])
        dic[s] = len(dic.keys()) + 1
        i += n - 1
        print(answer)

    return answer


print(solution("KAKAO"))

