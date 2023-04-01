'''한 선수는 제일 왼쪽에 있는 음식부터 오른쪽으로,
다른 선수는 제일 오른쪽에 있는 음식부터 왼쪽으로 순서대로 먹는 방식으로 진행됩니다.
중앙에는 물을 배치하고, 물을 먼저 먹는 선수가 승리하게 됩니다.'''

food = [1, 3, 4, 6]
# 준비한 음식의 양을 칼로리가 적은 순서대로
# food[0] = 항상 1 (물)


def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        for j in range(int(food[i]/2)):
            answer += str(i)
    ans_list = list(answer)
    ans_list.reverse()
    answer += "0" + ''.join(ans_list)
    return answer

# 대회를 위한 음식의 배치를 나타내는 문자열
print(solution(food))