# https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

## 이 문제는 O(n^2) 정렬로는 안됨

# 0. 기본 sort함수는 nlogn이다!
# input 속도는 높여야 통과됨
'''
import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    k = int(sys.stdin.readline())
    A.append(k)
A.sort()
for i in A:
    print(i)
'''

## O(nlogn)인 것엔 아래 3가지가 있다
## 병합정렬, 힙정렬, 퀵정렬(퀵정렬은 최악에는 n^2..)

# 힙정렬을 이용해보자!
import sys
N = int(sys.stdin.readline())
A = [None] # head에서 index 0은 사용 X

for _ in range(N):
    k = int(sys.stdin.readline())
    A.append(k)
A.sort()
for i in A:
    print(i)
