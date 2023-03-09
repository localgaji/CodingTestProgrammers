def solution(nums):

    noduplicate = []
    for i in nums:
        if not i in noduplicate:
            noduplicate.append(i)

    if float(len(noduplicate)) >= len(nums)/2 :
        answer = int(len(nums)/2)
    elif float(len(noduplicate)) < len(nums)/2:
        answer = len(noduplicate)

    return answer