###시간초과
def solution(people, limit):
    people.sort(reverse = True)
    i = 0
    count = 0
    print(people)
    while True:
        if len(people) == 1:
            count += 1
            break
        elif len(people) == 0:
            break
        elif people[0]+people[-1] > limit:
            people.pop(0)
            count += 1
        else:
            people.pop(0)
            people.pop(-1)
            count += 1
    return count


###시간 더 초과
def solution(people, limit):
    peo = [j for j in people if j <= (limit - min(people))]
    peo.sort()
    i = 0
    count = len(people)-len(peo)
    #print(people)
    while True:
        if len(peo) == 1:
            count += 1
            break
        elif len(peo) == 0:
            break
        elif peo[0]+peo[-1] > limit:
            peo.pop(-1)
            count += 1
        else:
            peo.pop(0)
            peo.pop(-1)
            count += 1
    return count

###당연히 더 오래걸림
def solution(people, limit):
    i = 0
    count = 0
    while True:
        if len(people) == 1:
            count += 1
            break
        elif len(people) == 0:
            break
        elif max(people)+min(people) > limit:
            people.remove(max(people))
            count += 1
        else:
            people.remove(max(people))
            people.remove(min(people))
            count += 1
    return count


###pop도 안써야 통과됨!!
def solution(people, limit):
    people.sort(reverse=True)
    count = 0
    j,k = 0,-1
    while True:
        if j + abs(k) == len(people):
            count += 1
            break
        elif j + abs(k) == len(people) +1:
            break
        elif people[j]+people[k] > limit:
            j += 1
            count += 1
        else:
            j += 1
            k -= 1
            count += 1
    return count