def solution(n):
    if n == 2:
        return 1
    x = list(range(3,n+n%2,2))
    for i in range(3, int(n**0.5)+int(n**0.5)%2 , 2):
        if i in x:
            for k in range(2,(max(x)//i)+1):
                if i*k in x:
                    x.remove(i*k)

    return len(x)+1


n = 5

def solution(n):
    if n == 2:
        return 1
    x = list(range(3,n+n%2,2))
    i = 3
    j = 0
    while True:
        x = list( set(x) - set(list(range(2*i, max(x)//i*i+1 ,i))) )
        x.sort()
        if j+1 >= len(x):
            break
        j += 1
        i = x[j]
        if i**2 > n:
            break

    return len(x)+1

print(solution(n))



## 간단하게

n = 5

def solution(n):
    x = list(range(2,n+1))
    i = 2
    j = 0
    while True:
        x = list( set(x) - set(list(range(2*i, n+1 ,i))) )
        x.sort()
        if j+1 >= len(x):
            break
        j += 1
        i = x[j]
        if i**2 > n:
            break

    return len(x)+1

print(solution(n))

l = 0
r = 0
l==r