from collections import deque

def solution(queue1, queue2):
    answer = 0
    sumd1, sumd2 = sum(queue1), sum(queue2)
    qsum = (sumd1 + sumd2) / 2
    d1, d2 = deque(queue1), deque(queue2)
    max = (len(d1) + len(d2)) + 3

    while sumd1 != qsum and answer <= max:
        if sumd1 > sumd2:
            pop = d1.popleft()
            d2.append(pop)
            sumd1 -= pop
            sumd2 += pop
        elif sumd1 < sumd2:
            pop = d2.popleft()
            d1.append(pop)
            sumd1 += pop
            sumd2 -= pop
        answer += 1
        print(d1,d2, sumd1, sumd2, answer, qsum)
    if answer > max:
        return -1
    return answer