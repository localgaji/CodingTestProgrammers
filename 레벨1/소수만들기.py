def solution(nums):
    randomlist = []
    sumlist = []
    primecount = 0

    for i in range(0,len(nums)):
        for j in range (0,len(nums)):
            if nums[j] == nums[i] : break
            for k in range(0, len(nums)):
                if nums[k] == nums[j] or nums[k] == nums[i]: break
                random = [nums[i], nums[j], nums[k]]
                random.sort()
                if not random in randomlist:
                    randomlist.append(random)
                    sumlist.append(sum(random))

    for i in sumlist:
        divisorcount = 0
        for n in range (2, int(i/2)+1):
            if i % n == 0 :
                divisorcount += 1
                break
        if divisorcount == 0:
            primecount += 1

    return primecount

print (solution([1,2,7,6,4]))