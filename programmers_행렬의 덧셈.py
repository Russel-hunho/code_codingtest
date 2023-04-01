def solution(arr1, arr2):
    
    for i in range(len(arr1)):  # 행의 수
        for j in range(len(arr1[1])): # 열의 수
            arr1[i][j] += arr2[i][j]
    
    return arr1