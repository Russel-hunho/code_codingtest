## https://www.youtube.com/watch?v=i5yHkP1jQmo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=12&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 9:20
# 트리의 순회

#입력 예시:
'''
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
'''
# 7개의 Node가 있고,
# A는 자식으로 B,C를 갖고
# B는 자식으로 ....

# 전위순회, 중위순회, 후위순회를 다 구현해보자!

# Node 자료형 구현
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
    
#전위순회 구현 (Preorder Traversal)
def pre_order(node):
    print(node.data, end = " ")
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

#중위순회 구현 (Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node != None:
        in_order(tree[node.right_node])

#후위순회 구현 (Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")
        
n = int(input())
tree = {} #딕셔너리

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])