## https://www.youtube.com/watch?v=94RC-DsGMLo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=5&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98

# 순차탐색: 리스트 안에 있는 특정 데이터를 찾기 위해, 앞에서부터 찾아나가는 것

# 이진탐색: 정렬된 리스트에서, 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 시작점, 끝점, 중간점을 이용하여 탐색 범위 설정
# 단계마다 탐색 범위를 2로 나누므로, O(log N)을 보장한다


# input 예시
'''
10 7
1 3 5 7 9 11 13 15 17 19
4
'''


def binary_search(array, target, start, end):
        # array가 오름차순 정렬 되어있다고 가정!
    if start > end:
        return None
    mid = (start+end)//2 #중간점
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 target 값이 작다면: 왼쪽만 탐색
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else: # 오른쪽만 탐색
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))
target = int(input())

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)