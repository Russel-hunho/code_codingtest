import sys
N = 0.0
tot = 0.0
grade_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0}
while True:
    A = sys.stdin.readline()
    if not A:
        break
    Name,L,G = map(str,A.split())
    if G != "P":
        N += float(L)
        tot += float(L)*float(grade_dict[G])
print(tot/N)