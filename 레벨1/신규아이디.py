# 양끝 마침표 제거
def stardenddot(newid):
    if newid == ['.']:
        newid = []
    else:
        while newid[-1] == '.':
            newid = newid[:-1]
        while newid[0] == '.':
            newid = newid[1:]
    return newid


def idsolution (newid):

    # 대문자를 소문자로, 문자열을 리스트로
    newid = list(newid.lower())

    # 유효하지 않은 특수문자를 모두 제거하기
    invalidspecial = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']
    new_newid = []
    for j in newid:
        if j not in invalidspecial:
            new_newid.append(j)
    newid = new_newid

    # 마침표가 두번 이상 반복되면 한개만
    new_newid = []
    if len(newid) != 0 and len(newid) != 1 :
        for i in range (0,len(newid)-1):
            if newid[i] == '.' and newid[i+1] == '.':
                pass
            else :
                new_newid.append(newid[i])
    new_newid.append(newid[-1])
    newid = new_newid

    # 양끝 마침표 제거
    newid = stardenddot(newid)

    # 빈 문자열일 경우 a를 대입
    if newid == []:
        newid = ['a','a','a']

    # 최대 글자수
    if len(newid) > 15:
        newid = newid[:15]
        newid = stardenddot(newid)
        # 마침표가 15번째에 있는 경우 여기서 제거 필요, 마침표가 1번째에 있는 경우는 앞에서 제거 필요

    # 최소 글자수
    while len(newid) < 3:
        newid += newid[-1]

    # 문자열로 변경하여 반환
    newidstring = ''
    for character in newid:
        newidstring += character
    return newidstring

print(idsolution("...!@BaT#*..y.abcdefghijklm"))
print(idsolution("z-+.^."))
print(idsolution("=.="))
print(idsolution("123_.def"))
print(idsolution("abcdefghijklmn.p"))
