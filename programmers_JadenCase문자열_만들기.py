s = "3people unFollowed me"

def solution(s):
    x = list(map(str, s.split()))
    #print(ord("A")) # 65
    #print(ord("a")) # 97
    #print(ord("z")) # 122
    #print(ord("1")) # 49
    
    for i in range(len(x)):
        for j in range(len(x[i])):
            if j == 0:
                if ord(x[i][j]) > 96:
                    x[i][j] = chr( ord(x[i][j]) - 32 )
            else:
                if ord(x[i][j]) < 97:
                    x[i][j] = chr( ord(x[i][j]) + 32 )
                    
    return 0

print(solution(s))