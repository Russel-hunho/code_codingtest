arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

def solution(arr1, arr2):
    answer = []
    for j in range(len(arr1)):
        B = []
        for k in range(len(arr2[0])):
            A = 0
            for i in range(len(arr1[0])):
                A += arr1[j][i]*arr2[i][k]
            B.append(A)
        answer.append(B)    
    return answer

print(solution(arr1, arr2))