import sys
input = sys.stdin.readline
N = int(input())
people = []
meet = []
rainbow = dict()
for _ in range(N):
    A,B = map(str,input().split())
    meet.append([A,B])
    people.append(A)
    people.append(B)
people = set(people)
for i in people:
    rainbow[i] = 0
for i in range(N):
    A = meet[i][0]
    B = meet[i][1]
    if "ChongChong" in [A,B]:
        rainbow[A] = 1
        rainbow[B] = 1
    elif 1 in [rainbow[A],rainbow[B]]:
        rainbow[A] = 1
        rainbow[B] = 1
print(sum(rainbow.values))