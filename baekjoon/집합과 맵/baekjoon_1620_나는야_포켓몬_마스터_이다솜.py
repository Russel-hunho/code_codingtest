import sys
input = sys.stdin.readline
N,M = map(int,input().split())
pokemonlist = []
for _ in range(N):
    pokemonlist.append(input().rstrip())
for _ in range(M):
    k = input().rstrip()
    if ord(k[0]) in range(ord("0"),ord("9")+1):
        print(pokemonlist[int(k)-1])
    else:
        print(pokemonlist.index(k)+1)
        
## 시간초과 다시
## 리스트의 탐색은 시간이 O(N) -> dict를 쓰면 바로 접근하므로 Good!

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
pokemonlist = []
pokemondict = {}
for i in range(N):
    a = input().rstrip()
    pokemonlist.append(a)
    pokemondict[a] = i
for _ in range(M):
    k = input().rstrip()
    if ord(k[0]) in range(ord("0"),ord("9")+1):
        print(pokemonlist[int(k)-1])
    else:
        print(pokemondict[k]+1)