def solution(s):
    string = s
    onecount = string.count("1")
    count, removedzero = 0, 0
    while string != "1":
        onecount = string.count("1")
        removedzero += (len(string) - onecount)
        string = bin(onecount)[2:]
        count += 1

    return [count, removedzero]
