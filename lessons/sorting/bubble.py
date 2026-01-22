# Time: O(n^2)
# Space: O(1)

A = [-3, 4, 2, 1, 5, 3, -6, 7, 0]

def bubble_sort(arr):
    n = len(arr)
    flag = True     # The flag acts as a signal that stops the loop when the condition is not True. In other words, it's like saying "we're not done yet" (True).

    while flag:
        flag = False    

        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

    return arr

print(bubble_sort(A))