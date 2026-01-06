def binary_search_recursive(arr, target, L, R):
    N = len(arr)

    if L > R:
        return -1
    
    mid = (L + R) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, R)

    else:
        return binary_search_recursive(arr, target, L, mid - 1)
    

def main():
    a = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    print("Sorted Array:", a)
    target = int(input("Target value: "))

    index = binary_search_recursive(a, target, 0, len(a) - 1)

    print("Target found at:", index)


if __name__ == "__main__":
    main()