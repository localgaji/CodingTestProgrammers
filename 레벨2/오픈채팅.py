def solution(record):
    answer, list_record = [], []
    nick = {}
    inout = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for i in record:
        splited = i.split(" ")
        if splited[0] != "Leave":
            nick[splited[1]] = splited[2]

    for i in record:
        splited = i.split(" ")
        move, userid = splited[0], splited[1]
        if move != "Change":
            answer.append(nick[userid] + inout[move])

    return answer