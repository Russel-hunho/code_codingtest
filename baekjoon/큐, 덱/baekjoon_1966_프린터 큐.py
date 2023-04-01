import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    importancy_queue = deque(map(int,input().split()))
    index_queue = deque(range(N)) #0부터 N-1까지
    count = 0
    for i in range(9,0,-1): #9부터1까지 순회, 높은 값이 중요도가 높은것!
        l = len(index_queue) # 순회는 길이만큼만 한다.
        while l > 0:
            a = importancy_queue.popleft()
            b = index_queue.popleft()
            l -= 1
            if a == i:
                count += 1
                l = len(index_queue) #순회 초기화
                if b == M:
                    print(count)
                    break
            else:
                importancy_queue.append(a)
                index_queue.append(b)
