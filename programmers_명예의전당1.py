k = 3
score = [10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    answer = []
    board = []
    for i in score:
        board.append(i)
        board.sort()
        if len(board) > k:
            board.pop(0)
        answer.append(board[0])
    return answer
    
print(solution(k,score))

# remove 이용
k = 3
score = [10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    answer = []
    board = []
    for i in score:
        board.append(i)
        if len(board) > k:
            board.remove( min(board) )
        answer.append(min(board))
    return answer
    
print(solution(k,score))
