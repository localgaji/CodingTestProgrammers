def distance(a,b):
    location = {1: [1,1], 2: [1,2], 3: [1,3], 4: [2,1], 5: [2,2], 6: [2,3], 7: [3,1], 8: [3,2], 9: [3,3], '*': [4,1], 0: [4,2], '#': [4,3] }
    a_location, b_location = location.get(a), location.get(b)
    dx, dy = abs(a_location[0] - b_location[0]), abs(a_location[1] - b_location[1])
    distance = dx + dy
    return distance

def leftvsright(left,right,now,hand):
    if now in [1,4,7] :
        result = 'L'
    elif now in [3,6,9] :
        result = 'R'
    elif distance(now,left) > distance(now,right):
        result = 'R'
    elif distance(now,left) < distance(now,right):
        result = 'L'
    elif distance(now,left) == distance(now,right):
        result = hand[0]
        result = result.upper()
    return result

def solution(numbers, hand):

    # list = [0왼손위치, 1오른손위치, 2누를번호, 3무슨손?]
    list0 = ['*','#', numbers[0], leftvsright('*', '#', numbers[0], hand)]
    wholelist = [list0]
    for n in range(1, len(numbers)):
        if wholelist[n-1][-1] == "R":
            lefthand = wholelist[n-1][0]
            righthand = wholelist[n-1][2]
        else :
            lefthand = wholelist[n-1][2]
            righthand = wholelist[n-1][1]
        pressnum = numbers[n]
        whathand = leftvsright(lefthand, righthand, pressnum, hand)
        listn = [lefthand, righthand, pressnum, whathand]
        wholelist.append(listn)

    answer = ""
    for lists in wholelist:
        answer += lists[-1]
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'right'))