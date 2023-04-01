clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    type_dict = {x : 0 for x in [i[1] for i in clothes]}
    for j in clothes:
        type_dict[j[1]] += 1
    
    for k in type_dict:
        answer *= (type_dict[k]+1)
    return answer -1

print(solution(clothes))