def solution(s):
    answer, rotated = 0, 0
    dic = {"]": "[", ")": "(", "}": "{"}
    while rotated < len(s):
        s = s[-1] + s[:-1]
        print(s)
        news = []
        istrue = 1
        rotated += 1
        for i in s:
            if not news:
                if i in dic.values():
                    news.append(i)
                else:
                    istrue = 0
                    break
            elif i in dic.keys() and dic[i] == news[-1]:
                news.pop()
            else:
                news.append(i)
            print("i:", i, "news:", news)
        if news:
            istrue = 0
        if istrue:
            answer += 1

    return answer