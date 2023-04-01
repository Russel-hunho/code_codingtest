def solution(sizes):
    width, length = 0,0
    for i in range(len(sizes)):
        i_w = sizes[i][0]
        i_l = sizes[i][1]
        if max(i_w, i_l) > max(width,length):
            if width > length:
                width = max(i_w, i_l)
            else: 
                length = max(i_w, i_l)
        if min(i_w, i_l) > min(width,length):
            if width > length:
                length = min(i_w, i_l)
            else: 
                width = min(i_w, i_l)
    return width*length

print(solution(Sizes))