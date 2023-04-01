n = 5

def solution(n):
    
    def trigonal(n):
        if n == 1:
            return [1]
        elif n == 2:
            return [[1],[2,3]]
        elif n == 3:
            return [[1],[2,6],[3,4,5]]
        else:
            m = 3*(n-1)
            A = [i for i in trigonal(n-3)]
            B = [[1],[2,3*(n-1)]] #1,2행
            for i in range(len(A)):
                C = [i+3]
                for j in A[i]:
                    C.append(j+m)
                C.append(3*(n-1)-(i+1))
                B.append(C)
            B.append([i for i in range(n,2*n)]) #마지막행
            return B
    #확인용
    K = trigonal(n)
    for i in range(len(K)):
        for j in K[i]:
            print(j,end="")
        print("")
    2차원 배열 다 풀어서 1차원 만들기
    answer = []
    for i in range(len(K)):
        for j in K[i]:
            answer.append(j)
            
    return answer

print(solution(n))


def solution(n):
    
    def trigonal(n):
        if n == 1:
            return [1]
        elif n == 2:
            return [[1],[2,3]]
        elif n == 3:
            return [[1],[2,6],[3,4,5]]
        else:
            m = 3*(n-1)
            A = [i for i in trigonal(n-3)]
            B = [[1],[2,3*(n-1)]] #1,2행
            for i in range(len(A)):
                C = [i+3]
                for j in A[i]:
                    C.append(j+m)
                C.append(3*(n-1)-(i+1))
                B.append(C)
            B.append([i for i in range(n,2*n)]) #마지막행
            return B
    #확인용
    K = trigonal(n)
    for i in range(len(K)):
        for j in K[i]:
            print(j,end="")
        print("")
    2차원 배열 다 풀어서 1차원 만들기
    answer = []
    for i in range(len(K)):
        for j in K[i]:
            answer.append(j)
            
    return answer