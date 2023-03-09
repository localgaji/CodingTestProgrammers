def solution(citations):
    h = 0
    overh = 1
    while overh >= h + 1:
        h += 1
        # overh 계산
        citations = [i for i in citations if i >= h]
        overh = len(citations)
        print(h, overh)
    return h

print(solution([1,4,4,4,4,4]))