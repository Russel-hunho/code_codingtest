n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    answer = n-len(lost)
    for i in range(len(lost)):
        if lost[i] in reserve:
            answer += 1
            reserve.remove(lost[i])
        elif lost[i]-1 in reserve:
            answer += 1
            reserve.remove(lost[i]-1)
        elif lost[i]+1 in reserve:
            if lost[i]+1 not in lost:
                answer += 1
                reserve.remove(lost[i]+1)

    return answer

print(solution(n, lost, reserve))

