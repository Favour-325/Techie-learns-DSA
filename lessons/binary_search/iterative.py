# Traditional Binary Search - Looking up if number is in array
# Time = O(log n)
# Space = O(1), since we're just storing L, R and M

def binary_search(arr, target):
    N = len(arr)
    L, R = 0, N-1

    while L <= R:
        M = L + ((R-L) // 2) # To avoid integer overflow

        if arr[M] == target:
            return True
        
        elif arr[M] < target:
            L = M + 1

        else:
            R = M - 1

    return False

a = [-3, -2, -1, 0, 1, 2, 3]

# Condition based search
b = [False, False, False, False, True, True, True]

def bs_condition(arr):
    N = len(arr)
    L = 0
    R = N-1

    while L < R:
        M = (L + R) // 2

        if arr[M]:
            R = M
        else:
            L = M + 1

    return L