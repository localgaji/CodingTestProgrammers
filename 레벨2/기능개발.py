def solution1(progresses, speeds):
    max, count = 0, 0
    answer =[]

    for progress, speed in zip(progresses, speeds):
        leftdays = (100 - progress) / speed
        if leftdays != int(leftdays):
            leftdays = int(leftdays) + 1
        else:
            leftdays = int(leftdays)

        if max == 0 :
            max = leftdays

        elif max < leftdays:
            answer.append(count)
            max = leftdays
            count = 0

        count += 1

    answer.append(count)
    return answer