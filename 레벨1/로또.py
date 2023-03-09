def solution(lottos, win_num):

    # 요소 0을 모두 제거
    while lottos.count(0):
        lottos.remove(0)

    # 확실한 매치 개수 검사
    matchcount = 0
    for i in lottos:
        if i in win_num:
            matchcount += 1
        else:
            pass

    # 최대 최소 매치 개수
    minmatch = matchcount
    maxmatch = matchcount + (6 - len(lottos))

    # 등수 계산 (0개 매치와 1개 매치는 등수가 동일, 7등은 없음)
    answer = [7 - maxmatch, 7 - minmatch]
    answer = [i-1 if i ==7 else i for i in answer]

    return answer

print(solution([1,2,3,4,5,6], [11,12,13,14,15,16]))
print(solution([0,0,0,0,0,0], [11,12,13,14,15,16]))