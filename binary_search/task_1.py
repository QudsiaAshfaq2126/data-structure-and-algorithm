def binary_search(numbers, target):
    # Step 1: Sort the list
    indexed_numbers = list(enumerate(numbers))
    indexed_numbers.sort(key=lambda x: x[1])

    # Step 2: Initialize pointers
    low = 0
    high = len(numbers) - 1
    
    # Step 3: Binary Search
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid  # Index of the found number
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # Step 4: Number not found
    return -1

# Example usage
numbers = [1, 4, 6, 9, 10, 5, 7]
target = 5
index = binary_search(numbers, target)
print("Index of target:", index)
