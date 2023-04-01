from collections import deque

deq = deque()

a = 10
b = 8
A = [1,2,3,4,5]
B = [21,22,23,24,25]

print(deq)

print()
deq.append(a)
print(deq)
deq.appendleft(b)
print(deq)

print()
deq.extend(A)
print(deq)
deq.extendleft(B)
print(deq)

print()
deq.pop()
print(deq)
deq.popleft()
print(deq)

print()
deq.remove(10)
print(deq)

print()
deq.rotate(3)
print(deq)
deq.rotate(-2)
print(deq)