# https://guccin.tistory.com/81 참고
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

L = [A[0]]
for i in range(1,N):
    # 새 수가 마지막 값보다 크다면?
    if A[i] > L[-1]:
        L.append(A[i])
        continue
    # 새 수가 마지막 값보다 작다면?
        # L의 A[i]보다 큰 가장 작은 값을, A[i]로 대체
            # -> A[i]로 끝나는, 가장 긴 부분수열이 L에 포함되어있다.
    start = 0 # 인덱스값
    end = len(L)-1 # 인덱스값
    while start <= end:
        mid = (start + end)//2 # 업데이트 할 위치 찾기
        if L[mid] >= A[i]:
            ans = mid #업데이트 할 위치
            end = mid - 1
        else:
            start = mid + 1
    L[ans] = A[i] # 업데이트
print(len(L))
    #L이 가장 긴 부분수열 자체는 아니지만, 길이는 그 긴 부분수열의 길이를 대변함!