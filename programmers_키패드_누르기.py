n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    answer = ''
    l_pos = [1,4]
    r_pos = [3,4]
    k = [[2,4],[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3]]
    for i in range(len(numbers)):
        num_pos = k[ numbers[i] ]
        if numbers[i] in [1,4,7]:
            answer += 'L'
            l_pos = num_pos
        elif numbers[i] in [3,6,9]:
            answer += 'R'
            r_pos = num_pos
        else:
            l_dis = abs(l_pos[0]-num_pos[0]) + abs(l_pos[1]-num_pos[1])
            r_dis = abs(r_pos[0]-num_pos[0]) + abs(r_pos[1]-num_pos[1])
            if (l_dis == r_dis and hand == 'right') or r_dis < l_dis:
                answer += 'R'
                r_pos = num_pos
            else:
                answer += 'L'
                l_pos = num_pos
    return answer

print(solution(n,hand))