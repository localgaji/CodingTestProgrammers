def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()
    newlost = lost[:]

    for i in lost:
        if i in reserve:
            newlost.remove(i)
            reserve.remove(i)
    new2lost = newlost[:]


    for i in newlost:
        if i-1 in reserve:
            new2lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            new2lost.remove(i)
            reserve.remove(i+1)

    answer = n - len(new2lost)

    return answer, newlost

print(solution(3,[1,2],[2,3]))