numbers = [1, 2, 4, 7, 8, 9, 10, 1, 4, 15, 18, 20, 21]
target = 4


def binary_search_algorithm(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == numbers[mid]:
            return True
        elif target < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(binary_search_algorithm(numbers, target))
