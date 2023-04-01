import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        # "최소힙구조"에 맞게 삽입된다
    # 힙에 삽입된 모든 원소를 차례로 꺼내 담기
    for i in range(len(h)):
        result.append( heapq.heappop(h) )
    
    # 힙정렬 결과 return
    return result 

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])