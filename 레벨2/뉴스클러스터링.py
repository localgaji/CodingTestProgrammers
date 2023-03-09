def solution(str1, str2):
    import re
    sets = []
    for string in [str1, str2]:
        setn = []
        for i in range(0, len(string) - 1):
            a = string[i].lower() + string[i + 1].lower()
            if not re.search("[^a-z]", a):
                setn.append(a)
        sets.append(setn)
    a, b = sets[0], sets[1]

    int_i, sum_i = 0, 0
    for i in set(a):
        if i in b:
            int_i += min(a.count(i), b.count(i))
            sum_i += max(a.count(i), b.count(i))
        else:
            sum_i += 1

    for i in set(b):
        if not i in a:
            sum_i += 1

    return int_i / sum_i * 65536