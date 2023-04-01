board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

def solution(board):
    n = len(board)
    matrix = [[0 for i in range(n)] for j in range(n)] # 다 0인 matrix
    k = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                k += 1
                try:
                    matrix[i-1][j-1] += 1
                except:
                    pass
                try:
                    matrix[i-1][j] += 1
                except:
                    pass
                try:
                    matrix[i-1][j+1] += 1
                except:
                    pass
                try:
                    matrix[i][j-1] += 1
                except:
                    pass
                try:
                    matrix[i][j] += 1
                except:
                    pass
                try:
                    matrix[i][j+1] += 1
                except:
                    pass
                try:
                    matrix[i+1][j-1] += 1
                except:
                    pass
                try:
                    matrix[i+1][j] += 1
                except:
                    pass
                try:
                    matrix[i+1][j+1] += 1
                except:
                    pass
    ans = 0
    for j in range(n):
        ans += matrix[j].count(0)
    return ans

print(solution(board))


### index -1에서 잘 작동해버림..


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

def solution(board):
    n = len(board)
    matrix = [[0 for i in range(n)] for j in range(n)] # 다 0인 matrix
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i != 0:
                    if j != 0:
                        matrix[i-1][j-1] += 1
                    matrix[i-1][j] += 1
                    if j+1 != n:
                        matrix[i-1][j+1] += 1
                if j != 0:
                    matrix[i][j-1] += 1
                matrix[i][j] += 1
                if j+1 != n:
                    matrix[i][j+1] += 1
                if i+1 != n:
                    if j != 0:
                        matrix[i+1][j-1] += 1
                    matrix[i+1][j] += 1
                    if j+1 != n:
                        matrix[i+1][j+1] += 1
    ans = 0
    for j in range(n):
        ans += matrix[j].count(0)
    return ans

print(solution(board))