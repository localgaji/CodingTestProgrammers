def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        ith_row_sum = []
        for j in range(0, len(arr1[i])):
            ith_row_sum += [arr1[i][j] + arr2[i][j]]
        answer += [ith_row_sum]

    return answer