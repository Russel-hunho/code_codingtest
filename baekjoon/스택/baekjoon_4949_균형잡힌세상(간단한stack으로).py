import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == ".":
        break
    S = list(S)
    isbalancestack = []
    state = 1
    while True:
        if len(S) == 0:
            break
        A = S.pop()
        if A in ["[","]","(",")"]:
            if A in ["]",")"]:
                isbalancestack.append(A)
            elif A == "(":
                if isbalancestack == []:
                    state = 0
                    break
                elif isbalancestack[-1] == ")":
                    isbalancestack.pop()
                else:
                    state = 0
                    break
            elif A == "[":
                if isbalancestack == []:
                    state = 0
                    break
                elif isbalancestack[-1] == "]":
                    isbalancestack.pop()
                else:
                    state = 0
                    break
    if len(isbalancestack) != 0 or state == 0:
        print("no")
    else:
        print("yes")