import heapq

A = [1, 0, -4, 2, 5, 3, 8, 12, 10]
print("A =", A)

# Time: O(n)
# Space: O(1)

heapq.heapify(A) # Build min heap
#print(A)

# Insert element
# Time: O(log n)
# Space: O(n)

heapq.heappush(A, 4)
#print(A)

# Time: O(log n)

#print(heapq.heappop(A)) # Pop the smallest item off the heap
#print(A)


def heapsort(arr):
    # Time: O(log n), Space O(n)
    # NB: O(1) Space is possible via swapping, but this is complex
    heapq.heapify(arr)
    n = len(A)
    new_line = [0] * n # This is one subtle game changer. This initializes an empty list of equal length with that of the array

    for i in range(n):
        minn = heapq.heappop(arr)
        new_line[i] = minn

    return new_line

#print(heapsort(A))

# Time: O(log n)
heapq.heappushpop(A, 99) # Push item on the heap and pop the smallest item from the list
print(A)

# To build a max heap simply negate the values before inserting so they are placed at the beginning of the list
heapq.heappush(A, -99)
print(A)

def maxheapsort(arr):
    n = len(arr)

    for i in range(n):
        arr[i] = -arr[i]

        heapq.heapify(arr)
    
    return arr