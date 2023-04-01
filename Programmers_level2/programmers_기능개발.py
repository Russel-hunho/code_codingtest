from re import L


progresses = [95, 90, 99, 99, 80, 99]
speeds = 	[1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(speeds)):
        k = (99-progresses[i])//speeds[i]+1
        if temp == []:
            temp.append(k)
        elif temp[0] < k:
            answer.append(len(temp))
            temp = [k]
        else:
            temp.append(k)
    answer.append(len(temp))
    return answer


print(solution(progresses, speeds))