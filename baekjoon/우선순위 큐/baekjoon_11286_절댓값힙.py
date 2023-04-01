import sys
import heapq
input = sys.stdin.readline

h1 = [] # 양수만, 최소힙
h2 = [] # 음수만, 최대힙
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(h1)+len(h2) == 0 :
            print(0)
        elif len(h1) == 0: # 양수가 안남은 경우
            print((-1)*heapq.heappop(h2))
        elif len(h2) == 0: # 음수가 안남은 경우
            print(heapq.heappop(h1))
        else: #양수, 음수 둘 다 있는 경우
            a = heapq.heappop(h1)
            b = heapq.heappop(h2)
            if a >= b: #음수의 절대값이 더 작다면; 절대값이 같으면 음수 추출
                print(-b)
                heapq.heappush(h1,a)
            else:
                print(a)
                heapq.heappush(h2,b)    
    elif x > 0:
        heapq.heappush(h1,x)
    else: #x < 0:
        heapq.heappush(h2,-x)