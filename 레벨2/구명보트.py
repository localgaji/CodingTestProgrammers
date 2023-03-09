from collections import deque

def solution(people, limit):
    people.sort()
    deq = deque(people)
    print(deq)
    count = 0
    while deq:
        if len(deq) == 1:
            count += 1
            break
        maxkg = deq.pop()
        minkg = deq[0]
        if maxkg == limit or maxkg + minkg > limit:
            count += 1
        else:
            deq.popleft()
            deq.append(maxkg+minkg)
        print(deq, count)
    return count