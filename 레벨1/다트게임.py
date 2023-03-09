def solution(dartResult):
    dartlist = list(dartResult.replace("10", "z"))
    dartlist = ["10" if i == 'z' else i for i in dartlist]

    calcul = []

    for i in range(1, len(dartlist)):
        if dartlist[i] == 'D':
            calcul.append(int(dartlist[i-1]) ** 2)
        elif dartlist[i] == 'T':
            calcul.append(int(dartlist[i - 1]) ** 3)
        elif dartlist[i] == 'S':
            calcul.append(int(dartlist[i - 1]))
        elif dartlist[i] == '#':
            calcul[-1] = - calcul[-1]
        elif dartlist[i] == '*':
            calcul[-1] = calcul[-1] * 2
            if len(calcul) >= 2:
                calcul[-2] = calcul[-2] * 2



    return sum(calcul)