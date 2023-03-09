
def solution(fees, records):
    records.sort(key=lambda x:x[6:10])
    dictime = {}
    dicparkingtime = {}
    answer = []

    for r in records:
        number = r[6:10]
        if r[11:] == "OUT":
            start = dictime[number]
            end = r[:6]
            parkingtime = (int(end[:2]) - int(start[:2])) * 60 + int(end[3:]) - int(start[3:])
            if number in dicparkingtime.keys():
                dicparkingtime[number] += parkingtime
            else:
                dicparkingtime[number] = parkingtime

            dictime[number] = None
        else:
            dictime[number] = r[:5]

    for number in dictime.keys():
        if dictime[number]:
            start = dictime[number]
            end = "23:59"
            parkingtime = (int(end[:2]) - int(start[:2])) * 60 + int(end[3:]) - int(start[3:])
            if number in dicparkingtime.keys():
                dicparkingtime[number] += parkingtime
            else:
                dicparkingtime[number] = parkingtime

        import math
        money = fees[1]
        if fees[0] < dicparkingtime[number]:
            money += math.ceil((dicparkingtime[number] - fees[0]) / fees[2]) * fees[3]
        answer.append(money)

    return answer