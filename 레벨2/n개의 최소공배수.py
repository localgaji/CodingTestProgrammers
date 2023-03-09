
def solution(arr):
    result = arr[0]
    for num in arr[1:]:
        x = result
        y = num
        mul = x * y
        remainder = x % y
        while remainder != 0:
            x = y
            y = remainder
            remainder = x % y
        result = mul // y
    return result


#최소공배수 : 유클리드호제법 풀이

def uclid(x,y):
    mul = x * y
    remainder = x % y
    while remainder != 0:
        x = y
        y = remainder
        remainder = x % y
    return mul // y

def solution1(arr):
    result = arr[0]

    for num in arr[1:]:
        result = uclid(result, num)
        print(num, result)

    return result

#