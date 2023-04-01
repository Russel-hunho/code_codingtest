array = [1, 2, 3, 3, 3, 4]

def solution(array):
    A = list(set(array))
    k = []
    for i in A:
        k.append(array.count(i))
    B = [j for j in k]
    if max(k) in B.remove(max(k)):
        return -1
    return array[k.index(max(k))]


##안됨...