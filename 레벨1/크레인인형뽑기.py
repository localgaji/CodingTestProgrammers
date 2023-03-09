


def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        for row in board:
            if row[(i-1)] != 0:
                doll = row[i-1]
                row[(i-1)] = 0
                basket.append(doll)
                try :
                    if basket[-1] == basket[-2]:
                        basket = basket[:-2]
                        answer += 2
                except IndexError :
                    pass
                print(basket)
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

