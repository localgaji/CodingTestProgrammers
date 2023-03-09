def solution (s):
    dic = {'zero': '0','one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}

    eng = list(dic.keys())
    for word in eng:
        if word in s:
            number = dic.get(word)
            s = s.replace(word, number)
    result = int(s)
    return result


