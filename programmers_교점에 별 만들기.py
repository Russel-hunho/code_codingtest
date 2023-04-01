line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]


def solution(line):
    answer = []
    star = []
    for i in range(len(line)):
        A,B,E = line[i][0:3]
        for j in range(i):
            C,D,F = line[j][0:3]
            if A*D-B*C == 0:
                break
            else:
                x = (B*F-E*D)/(A*D-B*C)
                y = (E*C-A*F)/(A*D-B*C)
                if x-int(x) == 0 and y-int(y)==0:
                    star.append([int(x),int(y)])
    min_x = min(list(zip(*star))[0])
    max_x = max(list(zip(*star))[0])
    min_y = min(list(zip(*star))[1])
    max_y = max(list(zip(*star))[1])

    for n in range(max_y,min_y-1, -1):
        star_inhere = [k[0] for k in star if k[1]==n]
        star_inhere.sort()
        col = ''
        for m in range(min_x,max_x+1):
            if m in star_inhere:
                col += "*"
            else:
                col += "."
        answer.append(col)
    
    return answer

print(solution(list))