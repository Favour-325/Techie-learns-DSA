from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

def pre_order(node):
    if not node:
        return None
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

#pre_order(A)

def in_order(node):
    if not node:
        return None
    
    in_order(node.left)
    print(node)
    in_order(node.right)

#in_order(A)

def post_order(node):
    if not node:
        return None
    
    post_order(node.left)
    post_order(node.right)
    print(node)

#post_order(A)

def pre_order_iterative(node):
    stack = [node]

    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        print(node)

def level_order_traversal(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
            
#level_order_traversal(A)


def search(node, target):
    if not node:
        return False
    
    if node.value == target:
        return True
    
    return search(node.left, target) or search(node.right, target)


def search_bst(node, target):
    if not node:
        return False
    
    if node.value == target:
        return True
    
    if target < node.value: return search_bst(node.right, target)
    else: return search_bst(node.left, target)

A1 = TreeNode(5)
B1 = TreeNode(1)
C1 = TreeNode(8)
D1 = TreeNode(-1)
E1 = TreeNode(3)
F1 = TreeNode(7)
G1 = TreeNode(9)

A1.left, A1.right = B1, C1
B1.left, B1.right = D1, E1
C1.left, C1.right = F1, G1

print(search(A1, 5))