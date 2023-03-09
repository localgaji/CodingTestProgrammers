from heapq import *

def solution(s):
    minheap, maxheap = [], []
    news = s.split(" ")
    for i in news:
        heappush(minheap, int(i))
        heappush(maxheap, (-1) * int(i))
    min, max = minheap[0], (-1) * maxheap[0]
    return str(min) + " " + str(max)