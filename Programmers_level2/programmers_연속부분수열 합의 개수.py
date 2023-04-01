elements = [7,9,1,1,4]

def solution(elements):
    sum_list = []
    n = len(elements)
    for i in range(1,n+1):
        for j in range(n):
            if j+i < n:
                sum_list.append(sum(elements[j:j+i]))
            else:
                sum_list.append(sum(elements[j:]+elements[0:j+i-n]))
    answer = len(set(sum_list))
    return answer
print(solution(elements))