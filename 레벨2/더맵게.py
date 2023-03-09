
import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    count = 0
    max = len(scoville)

    while scoville and count <= max:
        print(scoville)
        first = heapq.heappop(scoville)
        if scoville and first < k:
            second = heapq.heappop(scoville)
            if first > second:
                first, second = second, first
            mixed = first + second * 2
            scoville.append(mixed)
            count += 1
        elif not scoville and first < k:
            return -1

    return count

print(solution([10,50,70,90,50,40], 10000))