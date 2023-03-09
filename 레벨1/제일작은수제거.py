def solution(arr):
    arr.remove(min(arr))
    if arr == []:
        arr = [-1]
    return arr