def solution(id_list, report, k):
    #report 리스트 중복 제거
    report = list(set(report))

    # 딕서너리 피신고자 : 신고자(모두)
    accused_dict = {}

    for i in report:
        report_accused = i.split()
        reporter = report_accused[0]
        accused = report_accused[1]
        if accused in list(accused_dict.keys()):
            accused_dict[accused] += [reporter]
        else:
            accused_dict[accused] = [reporter]

    sendmail = []
    for i in range (0,len(id_list)):
        if not id_list[i] in list(accused_dict.keys()):
            accused_dict[id_list[i]] = 0
        elif len(accused_dict[id_list[i]]) >= k :
            sendmail += accused_dict[id_list[i]]

    answer = []
    for i in id_list:
        answer += [sendmail.count(i)]
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))