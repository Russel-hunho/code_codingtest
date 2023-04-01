arr = [2,6,8,14]

def solution(arr):
    for i in range(len(arr)-1):
        A,B = max(arr[i],arr[i+1]),min(arr[i],arr[i+1]) 
        while True:
            if B == 0:
                break
            A,B = B, A%B
        arr[i+1] = arr[i]*arr[i+1]//A
    return arr[-1]

print(solution(arr))