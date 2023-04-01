from collections import deque

deq = deque()

a = 10
b = 8
A = [1,2,3,4,5]
B = [21,22,23,24,25]

print(deq)

deq.append(a)
print(deq)
deq.appendleft(b)
print(deq)

deq.extend(A)
print(deq)
deq.extendleft(B)
print(deq)