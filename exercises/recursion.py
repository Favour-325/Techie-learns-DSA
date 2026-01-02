# Fibonacci
from linked_lists import Node

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
       return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Reverse linked list using recursion
head = Node(0)
A = Node(2)
B = Node(4)
C = Node(6)

head.next = A
A.next = B
B.next = C

def reverse(node):
    if not node:
        return
    
    reverse(node.next)
    print(node.data)

reverse(head)