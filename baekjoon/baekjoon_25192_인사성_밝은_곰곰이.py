'''
import sys
input = sys.stdin.readline
N = int(input())
input()
gom = []
count = 0
for _ in range(1,N):
    s = input().rstrip()
    if s == "ENTER":
        gom = [] #초기화
    elif s not in gom:
        gom.append(s)
        count += 1
'''

#시간초과

import sys
input = sys.stdin.readline
N = int(input())
input()
gom = []
count = 0
for _ in range(1,N):
    s = input().rstrip()
    if s == "ENTER":
        count += len(set(gom))
        gom = [] #초기화
    else:
        gom.append(s)
if gom != []:
    count += len(set(gom))
print(count)