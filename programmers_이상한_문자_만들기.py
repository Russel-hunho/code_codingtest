def solution(s):
    count = 0
    ans = []
    for i in range(len(s)):
        if s[i] == " ":
            count = 0
            ans.append(" ")
        elif count%2 == 0:
            if s[i].islower():
                ans.append( chr( ord(s[i]) + ord("A") - ord("a") ) )
            else:
                ans.append( s[i] )
            count += 1
        else:
            if s[i].isupper():
                ans.append( chr( ord(s[i]) + ord("a") - ord("A") ) )
            else:
                ans.append( s[i] )
            count += 1
    return ''.join(ans)


def solution(s):
    X = s.split(" ")
    return ''.join(ans)
