import sys
T = int(input())

def isPalindrome(s):
    return recursion(s,0,len(s)-1,0)

def recursion(s,l,r,k):
    k += 1
    if l>=r:
        return [1,k] # 맞으면 1
    elif s[l] != s[r]:
        return [0,k] # 다르면 0, 종료
    else:
        return recursion(s,l+1,r-1,k)

for _ in range(T):
    s = input()
    print("{} {}".format(isPalindrome(s)[0],isPalindrome(s)[1]+1))