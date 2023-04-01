T = int(input())
for _ in range(T):
    X,Y,D,T = map(int,input().split())
    r = (X**2+Y**2)**0.5
    if D <= T:
        print(r)
    else:
        if r//D == 0:
            print(min( (r//D)*T+r%D, (r//D+2)*T, (r//D+1)*T+(D-r%D) ))
        else:
            print(min( (r//D)*T+r%D, (r//D+1)*T, (r//D+1)*T+(D-r%D) ))
        