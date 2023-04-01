### 한번에 replace하면 반례 있음... Stack 순으로 해야됨..!
def solution(ingredient):
    answer = 0
    A = "".join([str(j) for j in ingredient])
    while True:
        B = A
        A = A.replace("1231","")
        if B == A:
            break
        answer += len(B)-len(A)
    return answer

### 한번에 한번만 replace 하면 시간초과됨.. 
def solution(ingredient):
    answer = 0
    A = "".join([str(j) for j in ingredient])
    while True:
        B = A
        A = A.replace("1231","",1)
        if B == A:
            break
        answer += 1
    return answer

##### 이게 더느림...
def solution(ingredient):
    answer = 0
    A = "".join([str(j) for j in ingredient])
    while True:
        B = A
        A = A.replace("1231","",1)
        if len(B) == len(A):
            break
        q = B.index("1231") #첫 1231의 맨앞1의 index 반환
        p = B.index("1") 
        if p == q:
            A = A[q:]
        else:
            A = A[p:]
        answer += 1
    return answer

##### 이건 시간초과는 안걸림. 근데 틀림..?
def solution(ingredient):
    answer = 0
    A = []
    for i in range(len(ingredient)):
        if A == []:
            if ingredient[i] == 1:
                A = [1]
        elif A[-1] - ingredient[i] == -1:
            A.append(ingredient[i])
        elif A[-1] == 3 and ingredient[i] == 1:
            A.pop(-1)
            A.pop(-1)
            A.pop(-1)
                #A = A[:-3] 이건 시간 오래걸림...
            answer += 1
            print(i,A)
        elif ingredient[i] == 1:
            A.append(1)
    return answer
    ### 1,2,2,3,1 같은 중도 결과를 못거름


### 정답
def solution(ingredient):
    answer = 0
    A = []
    for i in range(len(ingredient)):
        if A == []:
            if ingredient[i] == 1:
                A = [1]
        else:
            A.append(ingredient[i])
            if A[-4:]==[1,2,3,1]:
                A.pop(-1)
                A.pop(-1)
                A.pop(-1)
                A.pop(-1)
                answer += 1
    return answer
