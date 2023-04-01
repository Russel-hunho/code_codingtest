import sys
input = sys.stdin.readline
N = int(input())
roadlist = list(map(int,input().split())) # N-1개
pricelist = list(map(int,input().split())) # N개

leastprice = pricelist[0]
cost = 0

for i in range(1,N):
    cost += roadlist[i-1]*leastprice
    if pricelist[i] < leastprice:
        leastprice = pricelist[i]
print(cost)