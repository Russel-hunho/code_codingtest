lines = [[0, 1], [2, 5], [3, 9]]

def solution(lines):

    l1 = list(range(lines[0][0],lines[0][1]))
    l2 = list(range(lines[1][0],lines[1][1]))
    l3 = list(range(lines[2][0],lines[2][1]))
    l1_2_3 = [i for i in l1 if i in l2 or i in l3]
    l2_3 = [i for i in l2 if i in l3]
    tot = list(set(l1_2_3 + l2_3))

    return len(tot)

print(solution(lines))


#더 깔끔하게
lines = [[0, 1], [2, 5], [3, 9]]

def solution(lines):

    l1 = set(range(lines[0][0],lines[0][1]))
    l2 = set(range(lines[1][0],lines[1][1]))
    l3 = set(range(lines[2][0],lines[2][1]))
    return len( (l1 & l2) | (l2&l3) | (l3&l1) )

print(solution(lines))

#더 짧게
lines = [[0, 1], [2, 5], [3, 9]]

def solution(lines):

    s = [ set( range(min(l), max(l) ) ) for l in lines ]
    return len( (s[0] & s[1]) | (s[1]&s[2]) | (s[2]&s[0]) )

print(solution(lines))