scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        if scoville[0] >= K:
            break
        elif len(scoville) == 1:
            return -1
        answer += 1
        A = scoville[0]+scoville[1]*2
        scoville.pop(0)
        scoville.pop(0)
        for i in range(len(scoville)):
            if A <= scoville[i]:
                scoville.insert(i,A)
                break
        
    return answer

print(solution(scoville, K))