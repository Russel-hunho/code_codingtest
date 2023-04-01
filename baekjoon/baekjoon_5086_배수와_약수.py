while True:
    A = input()
    if A == "0 0":
        break
    I,J = map(int,A.split())
    if J%I == 0:
        print("factor")
    elif I%J == 0:
        print("multiple")
    else:
        print("neither")