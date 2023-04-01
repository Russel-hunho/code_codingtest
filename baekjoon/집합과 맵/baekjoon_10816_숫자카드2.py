import sys
input = sys.stdin.readline

N = int(input())
sang = list(map(int,input().split()))
M = int(input())
numlist = list(map(int,input().split()))
for i in numlist:
    print(sang.count(i), end=" ")
    
## count 함수 때문에 시간초과난듯

import sys
input = sys.stdin.readline

N = int(input())
sang = list(map(int,input().split()))
sangdict = {}
for i in sang:
    if i in sangdict.keys():
        sangdict[i] += 1
    else:
        sangdict[i] = 1
M = int(input())
numlist = list(map(int,input().split()))
for i in numlist:
    if i in sangdict.keys():
        print(sangdict[i], end=" ")
    else:
        print(0, end = " ")