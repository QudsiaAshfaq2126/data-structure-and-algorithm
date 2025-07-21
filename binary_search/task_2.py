def find_all_occurrences(numbers, target):
    result_indices = []

    for index, value in enumerate(numbers):
        if value == target:
            result_indices.append(index)

    return result_indices

numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15

indices = find_all_occurrences(numbers, number_to_find)
print(f"Indices of {number_to_find}: {indices}")
