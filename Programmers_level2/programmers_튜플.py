s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{20,111},{111}}"

def solution(s):
    x = list(map(str,s[2:-2].split("},{")))
    k = 0
    for i in x:
        if len(i) > k:
            k = len(i)
            A = i
    ans = list(map(int,A.split(",")))
    return ans

print(solution(s))


#### List 말고 set 써서

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{20,111},{111}}"

def solution(s):
    x = list(map(str,s[2:-2].split("},{")))
    l = len(x)
    k = [[0]]*l
    for i in x:
        A = list(map(int,i.split(",")))
        k[len(A)-1] = A
    ans = k[0]
    for i in range(1,len(k)):
        ans.append(list(set(k[i])-set(k[i-1]))[0])
    return ans

print(solution(s))


#### sort(key = len)

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{20,111},{111}}"

def solution(s):
    x = list(map(str,s[2:-2].split("},{")))
    x.sort(key = len)
    ans = [int(x[0])]
    for i in range(1,len(x)):
        i_set = set(map(int,x[i].split(",")))
        i_1_set = set(map(int,x[i-1].split(",")))
        ans.append(list(i_set - i_1_set)[0])
    return ans

print(solution(s))