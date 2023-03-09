def tentotwo(n, size):

    string = ""
    maxnumber = 0

    for i in range (0, size):
        maxnumber += 2 ** i
    if maxnumber < n:
        string = "크기초과"

    while n > 1:
        rest = n % 2
        divided = n//2
        string = str(rest) + string
        n = divided

    if n == 0:
        string = string
    else :
        string = "1" + string

    while len(string) < size:
        string = "0" + string
    return string


def solution(n, arr1, arr2):

    listsum, answer = [], []

    for x,y in zip(arr1, arr2):
        sum = str(int(tentotwo(x, n)) + int(tentotwo(y, n)))
        while len(sum) != n:
            sum = '0' + sum
        listsum.append(sum)

    for string in listsum:
        code = ""
        for i in string:
            if i == '0':
                code = code + ' '
            else:
                code = code + '#'
        answer.append(code)

    return answer