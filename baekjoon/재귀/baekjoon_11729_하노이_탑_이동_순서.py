N = int(input())

def numhanoy(n):
    if n == 1:
        return 1
    else:
        return 2*numhanoy(n-1)+1

def hanoy(n,start,end):
    #n: 횟수
    #start: 시작막대
    #end: 끝 막대
    
    if n == 1:
        return [[start, end]]
    else:
        k = [i for i in [1,2,3] if i not in [start, end]][0]
        temp = []
        temp += hanoy(n-1,start,k)
        temp += [[start, end]]
        temp += hanoy(n-1,k,end)
        return temp

print(numhanoy(N))
A = hanoy(N,1,3)
for i in A:
    print("{} {}".format(i[0],i[1]))