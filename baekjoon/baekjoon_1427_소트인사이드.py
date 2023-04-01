Nlist = list(input()) #str으로 받아서, 한글자씩을 list의 원소로 반환
A = [int(i) for i in Nlist]
A.sort(reverse = True)
for i in A:
    print(i, end="")