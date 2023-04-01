
import sys
Slist = list(sys.stdin.readline().rstrip())
num = 0
alplist = []
for i in Slist:
    if ord(i) in range(ord("A"),ord("Z")+1):
        alplist.append(i)
    else:
        num += int(i)
alplist.sort()
print("".join(alplist+[str(num)]))