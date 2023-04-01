board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m = 4
n = 5

def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while True:
        dele = []
        for i in range(m-1):
            for j in range(n-1):
                k = board[i][j]
                if k != "0":
                    if board[i+1][j] == k:
                        if board[i][j+1] == k:
                            if board[i+1][j+1] == k:
                                dele.append([i,j])
        if dele == []:
            break
        #print(dele)
        for x in dele:
            board[x[0]][x[1]:x[1]+2] = ["0","0"]
            board[x[0]+1][x[1]:x[1]+2] = ["0","0"]
        #print(board)
        
        for i in range(n):
            A = []
            for j in range(m-1,-1,-1):
                if board[j][i] != "0":
                    A.append(board[j][i])
            for k in range(m-1,-1,-1):
                if A == []:
                    board[k][i] = "0"
                else:
                    board[k][i] = A[0]
                    A.pop(0)
        #print(board)
                    
        
        
    for i in range(m):
        answer += board[i].count("0")
    return answer