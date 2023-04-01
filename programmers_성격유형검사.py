def solution(survey, choices):
    answer = ''
    first = ["R", "C", "J", "A"]
    second = ["T", "F", "M", "N"]
    count = [0, 0, 0, 0]
    for i in range(len(survey)):
        ch = survey[i][0]
        if ch in first:
            count [ first.index( ch ) ] += -1 * (choices[i] - 4)
        else: 
            count [ second.index( ch ) ] += 1 * (choices[i] - 4)
    for j in range(4):
        if count[j] >= 0:
            answer += first[j]
        else:
            answer += second[j]
    return answer

print(solution(Survey, Choices))