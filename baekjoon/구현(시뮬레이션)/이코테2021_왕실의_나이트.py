## https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 47:09

# 8X8에서 나이트의 위치가 주어졌을 때
# 나이트가 이동할 수 있는 경우의 수 출력

#열: a~h
#행: 1~8
#input 예시: a1

s = list(input())
k = ["a","b","c","d","e","f","g","h"]
x = k.index(s[0])+1 #1~8
y = int(s[1]) #1~8

xylist = []
xylist.append([x+2,y+1])
xylist.append([x+2,y-1])
xylist.append([x-2,y+1])
xylist.append([x-2,y-1])
xylist.append([x+1,y+2])
xylist.append([x+1,y-2])
xylist.append([x-1,y+2])
xylist.append([x-1,y-2])
count = 0
for xy in xylist:
    if xy[0] in range(1,9) and xy[1] in range(1,9):
        count += 1
print(count)