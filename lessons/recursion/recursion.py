# Fibonacci
from lessons.linked_lists.linked_lists import Node
import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
       return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
       return 1
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    return memo[n]

print("Simple fibonacci")
start1 = time.time()
print(fibonacci(20))
stop1 = time.time()
print("Fibonacci Memo")
start2 = time.time()
print(fibonacci_memo(100))
stop2 = time.time()
print(f"Duration: {stop1-start1}")
print(f"Duration: {stop2-start2}")



# Reverse linked list using recursion
""" head = Node(0)
A = Node(2)
B = Node(4)
C = Node(6)

head.next = A
A.next = B
B.next = C """

def reverse(node):
    if not node:
        return
    
    reverse(node.next)
    print(node.data)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
