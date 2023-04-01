import sys
input = sys.stdin.readline

class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

N = int(input())
data = dict()
for _ in range(N):
    root, left, right = input().rstrip().split()
    if left == ".":
        left = None
    if right == ".":
        right = None
    data[root] = Node(root, left, right)

#전위순회
def pre_order(root):
    print(root, end="")
    if data[root].left != None:
        pre_order(data[root].left)
    if data[root].right != None:
        pre_order(data[root].right)
#중위순회
def in_order(root):
    if data[root].left != None:
        in_order(data[root].left)
    print(root, end="")
    if data[root].right != None:
        in_order(data[root].right)
#후위순회
def post_order(root):
    if data[root].left != None:
        post_order(data[root].left)
    if data[root].right != None:
        post_order(data[root].right)
    print(root, end="")

pre_order("A")
print()
in_order("A")
print()
post_order("A")
print()