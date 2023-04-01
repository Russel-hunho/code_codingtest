k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

def solution(k, tangerine):
    tang_dict = {x : 0 for x in tangerine}
    for i in tangerine:
        tang_dict[i] += 1
    tang_list = list(set(tangerine))
    tang_num = []
    for i in tang_list:
        tang_num.append(tang_dict[i])
    tang_num.sort(reverse = True)
    
    answer = 0
    j = 0
    while True:
        k -= tang_num[j]
        j += 1
        answer += 1
        if k <= 0:
            break
    return answer

print(solution(k,tangerine))