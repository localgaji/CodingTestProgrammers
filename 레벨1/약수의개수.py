def solution(left, right):

    answer = 0
    for number in range(left, right+1):
        if number == 1:
            submultiplecount = 1
            answer -= number
        else :
            submultiplecount = 2 #1과 자기자신
            for sub in range (2,int(number/2)+1):
                if number % sub == 0:
                    submultiplecount += 1
            if submultiplecount % 2 == 1: #홀수
                answer -= number
            else:
                answer += number
    return answer