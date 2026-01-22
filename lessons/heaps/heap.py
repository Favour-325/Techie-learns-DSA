# Building the heap from scratch
# Time: O(n log n)

import heapq

def heap_scratch():
    A = [1, 0, -4, 2, 5, 3, 8, 12, 10]

    heap = []

    for i in A:
        heapq.heappush(heap, i)
        
    print(heap)


# Build tuples on heaps
def tuples_heap():
    D = [4, 4, 3, 5, 3, 3, 4, 5, 5, 3]

    from collections import Counter

    counter = Counter(D)

    tuple_heap = []

    for k, v in counter.items():
        heapq.heappush(tuple_heap, (v, k))

    print(tuple_heap)

tuples_heap()