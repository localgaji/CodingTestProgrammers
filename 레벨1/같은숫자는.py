def solution(arr):

    newarr = [arr[0]]
    for i in arr:
        if i != newarr[-1] :
            newarr.append(i)
    return newarr