from collections import deque

def solution(priorities, location):
    dp = deque(priorities)
    di = deque([i for i in range(0,len(priorities))])
    output = []
    while dp:
        p = dp.popleft()
        i = di.popleft()
        if len(dp) == 0 or p >= max(dp):
            output.append(p)
            if i == location:
                return len(output)
        else:
            dp.append(p)
            di.append(i)
    return False