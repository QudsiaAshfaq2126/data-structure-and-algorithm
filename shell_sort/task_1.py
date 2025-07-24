def shell_sort_unique(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        i = gap
        while i < len(arr):
            temp = arr[i]
            j = i
            while j >= gap:
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                elif arr[j - gap] == temp:
                    
                    arr.pop(j)
                    i -= 1  
                    break
                else:
                    break
            else:
                arr[j] = temp
            i += 1
        gap //= 2

    return arr
example_list = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
print("Original List:", example_list)

sorted_unique_list = shell_sort_unique(example_list)
print("Sorted List Without Duplicates:", sorted_unique_list)
