a = (1+5**0.5)/2
def G(n):
    if n == 3:
        return 2 - a*1
    else:
        return -1/a*G(n-1)
def F(n):
    if n == 2:
        return 1
    elif n ==3:
        return 2
    else:
        return G(n)+a*F(n-1)


def solution(n):
    return round(F(n),0)%1234567

######

def F(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else: return F(n-1)+F(n-2)


def solution(n):
    return F(n)

for i in range(31,36):
    print(solution(i))


###########



def solution(n):
    a = (1+5**0.5)/2
    def F(n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        G = (-1/a)**(n-1)
        return (a*F(n-1) + G)%1234567
            
    return F(n)%1234567



##############



def solution(n):
    def F(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 3
        elif n == 5:
            return 5
        #return (F(n//2+1) * F(n-n//2) + F(n//2) * F(n-(n//2+1))) % 1234567
        k = n//4
        if n%4 == 0:
            return ( F(k)*(F(k+1)+F(k-1)) * (F(k+1)**2 + 2*F(k)**2 + F(k-1)**2) )%1234567
        elif n%4 == 1:
            return ( (F(k+1)**2+F(k)**2)**2 + ( F(k)*(F(k+1)+F(k-1)) )**2   )%1234567
        elif n%4 == 2:
            return ( (F(k+1)**2+F(k)**2) * ( F(k)*(F(k+1)+F(k-1)) + F(k+1)*(F(k+2)+F(k)) ) )%1234567
        elif n%4 == 3:
            return ( ( F(k+1)*(F(k+2)+F(k)) )**2 + ( F(k+1)**2+F(k)**2 )**2 )%1234567
            
        
            
    return F(n)%1234567


############




