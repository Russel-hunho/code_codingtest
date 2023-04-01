def solution(n, left, right):
    vec = []
    for i in range(1,n+1): # i행
        for j in range(1,n+1): #i행j열
            if j < i:
                vec.append(i)
            else:
                vec.append(j)
    return vec[left:right+1]

### 시간초과남


def solution(n, left, right):
    vec = []
    for i in range(1,n+1): # i행
        vec += [i]*i + list(range(i+1,n+1))
    return vec[left:right+1]

#여전히 시간초과 (1/4 정도는 됐음)

def solution(n, left, right):
    vec = []
    for i in range(left//n+1,right//n +2): # i행
        vec += [i]*i + list(range(i+1,n+1))
    if right%n-n+1 == 0:
        return vec[left%n:]s
    return vec[left%n : right%n-n+1]