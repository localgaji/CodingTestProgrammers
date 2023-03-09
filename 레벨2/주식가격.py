def solution(prices):
    from collections import deque
    answer = []
    deq = deque(prices)
    while len(deq) > 1:
        a = deq.popleft()
        sec = 0
        for i in deq:
            sec += 1
            if i < a:
                break

        answer.append(sec)

    answer.append(0)
    return answer