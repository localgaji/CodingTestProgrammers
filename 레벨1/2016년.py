def solution(month, day):
    weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    endday = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    totalday = 0

    for i in range(1,month):
        totalday += endday[i]
    totalday += day

    answer = weekday[totalday % 7]

    return answer