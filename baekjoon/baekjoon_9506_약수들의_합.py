while True:
    a = int(input())
    if a == -1:
        break
    alist = []
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            alist.append(i)
            if a//i != i:
                alist.append(a//i)
    #print(alist)
    if sum(alist)+1==a:
        alist.sort()
        print("{} = 1".format(a), end="")
        for i in alist:
            print(" + {}".format(i), end="")
        print("") #한줄 띄우기
    else:
        print("{} is NOT perfect.".format(a))