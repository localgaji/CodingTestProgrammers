def solution(n, words):
    correctwords = [words[0]]
    last = words[0][-1]

    for i in range(1, len(words)):
        gamer, turn = i % n + 1, i // n + 1

        if words[i][0] != last:
            return [gamer, turn]

        if words[i] in correctwords:
            return [gamer, turn]

        correctwords.append(words[i])
        last = words[i][-1]

    return [0, 0]