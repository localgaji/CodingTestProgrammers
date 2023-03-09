def solution(words):
    newwords = ""
    count = 0
    for i in words:
        if i == " ":
            count = 0
            newwords = newwords + i
        else:
            count += 1
            if count % 2 == 1:
                newwords = newwords + i.upper()
            else:
                newwords = newwords + i.lower()

    return newwords