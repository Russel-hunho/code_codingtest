import sys
n = int(input())
ndict = dict()
for _ in range(n):
    a,b = input().rstrip().split()
    if b == "enter":
        ndict[a] = 1
    else:
        ndict[a] = 0

nlist = []
for i in ndict.keys():
    if ndict[i] == 1:
        nlist.append(i)
nlist.sort(reverse = True)
for i in nlist:
    print(i)