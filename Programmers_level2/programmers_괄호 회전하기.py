def solution(s):
    count = [0]*6
    lis = ["[", "]", "{", "}", "(", ")"]
    lis_start = ["[", "{", "("]
    lis_end = ["]","}",")"]
    
    #절대 안되는 가장 쉬운경우들 제거
    if len(s)%2 == 1:
        return 0
    for i in s:
        count[lis.index(i)] += 1
    if (count[0]!=count[1]) or (count[2]!=count[3]) or (count[4]!=count[5]): 
        return 0
    
    ans = 0
    k = 0
    while True:
        count_se = [0]*3
        order = []
        for j in s:
            if j in lis_start:
                count_se[lis_start.index(j)] += 1
            else:
                count_se[lis_end.index(j)] -= 1
                
            if -1 in count_se:
                break
        if count_se == [0,0,0]:
            ans += 1
        #print(k,ans)
        k += 1
        if k == len(s):
            break
        #print(s)
        s = s[-1]+s[0:-1]
        
    return ans

######## 잘못된 case 있음



def solution(s):
    count = [0]*6
    lis = ["[", "]", "{", "}", "(", ")"]
    lis_start = ["[", "{", "("]
    lis_end = ["]","}",")"]
    
    #절대 안되는 가장 쉬운경우들 제거
    if len(s)%2 == 1:
        return 0
    for i in s:
        count[lis.index(i)] += 1
    if (count[0]!=count[1]) or (count[2]!=count[3]) or (count[4]!=count[5]): 
        return 0
    
    ans = 0
    k = 0
    while True:
        count_stack = [] #index num이 저장
        suc = 1
        for j in s:
            if j in lis_start:
                count_stack.append(lis_start.index(j))
            else:
                if count_stack == []:
                    suc = 0
                    break
                elif count_stack[-1] == lis_end.index(j):
                    count_stack.pop()
                else:
                    suc = 0
                    break
        if suc == 1:
            ans += 1
        #print(k,ans)
        k += 1
        if k == len(s):
            break
        #print(s)
        s = s[-1]+s[0:-1]
        
    return ans