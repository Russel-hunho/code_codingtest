import sys
input = sys.stdin.readline
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

#l1: y = a1*x + b1
#l2: y = a2*x + b2
if x2 == x1: # 수직선
    a1 = None
    b1 = x1 # x = b1
else:
    a1 = (y2-y1)/(x2-x1)
    b1 = y1 - x1*a1
if x4 == x3: # 수직선
    a2 = None
    b2 = x3 # x = b2
else:
    a2 = (y4-y3)/(x4-x3)
    b2 = y3 - x3*a2

if a1 == a2: #기울기가 같다면
    if b1 != b2: #평행; 수직선이든 아니든 다 성립
        print(0)
    else:
        if a1 != 0:
            y5,y6 = max(y1,y2),min(y1,y2)
            y7,y8 = max(y3,y4),min(y3,y4)
            if y8 > y5 or y7 < y6:
                print(0) # 안만남
            elif y5 == y8 or y7 == y6: #한점에서 만남 = 한점이 동일하게 주어짐
                print(1)
                if y5 == y8:
                    if a1 == None:
                        print(x1,y5)
                    elif a1 > 0:
                        print(max(x1,x2),y5)
                    else:
                        print(min(x1,x2),y5)
                else: #y6
                    if a1 == None:
                        print(x1,y6)
                    elif a1 > 0:
                        print(min(x1,x2),y6)
                    else:
                        print(max(x1,x2),y6)
            else:
                print(1) # 무한히 겹침

        else: #수평선, y 값들이 다 같음
            x5,x6 = max(x1,x2),min(x1,x2)
            x7,x8 = max(x3,x4),min(x3,x4)
            if x8 > x5 or x7 < x6:
                print(0) # 안만남
            elif x5 == x8 or x7 == x6: #한점에서 만남 = 한점이 동일하게 주어짐
                print(1)
                if x5 == x8:
                    print(x5,y1)
                else: #x6
                    print(x6,y1)
            else:
                print(1) # 무한히 겹침

else:
    if a1 != None and a2 != None: #둘중에 수직선이 없는 경우
        #x = (-1)*(b2-b1)/(a2-a1)
        x = (-1)*((y3*(x4-x3)*(x2-x1) - x3*((y4-y3)*(x2-x1))) - (y1*(x4-x3)*(x2-x1) - x1*((y2-y1)*(x4-x3))))/(((y4-y3)*(x2-x1))-((y2-y1)*(x4-x3))) # 오차 줄이기
        #y = a1*x+b1
        y = (y2-y1) * ( (-1)*((y3*(x4-x3)*(x2-x1) - x3*((y4-y3)*(x2-x1))) - (y1*(x4-x3)*(x2-x1) - x1*((y2-y1)*(x4-x3)))) / (((y4-y3)*(x2-x1))-((y2-y1)*(x4-x3))) - x1 ) /(x2-x1) + y1
    elif a1 == None:
        x = x1
        #y = a2*x+b2
        y = (x1-x3)*(y4-y3)/(x4-x3)  + y3
    else:
        x = x3
        #y = a1*x+b1
        y = (x3-x1)*(y2-y1)/(x2-x1) + y1
    if (y-y1)*(y-y2) <= 0 and (y-y3)*(y-y4) <= 0 and (x-x1)*(x-x2) <= 0 and (x-x3)*(x-x4) <= 0:
        print(1)
        print(x,y)
    else:
        print(0)
'''
    a1 = (y2-y1)/(x2-x1)
    b1 = y1 - x1*a1

    a2 = (y4-y3)/(x4-x3)
    b2 = y3 - x3*a2
'''