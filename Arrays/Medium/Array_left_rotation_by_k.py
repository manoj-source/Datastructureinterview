# Given an integer array nums, rotate the array to the left by k steps, where k is non-negative

def reverse(first_index, last_index, array):
    while first_index < last_index:
        array[first_index], array[last_index] = array[last_index], array[first_index]
        first_index += 1
        last_index -= 1


def rotate_array_left_by_k(array, k):
    n = len(array)
    reverse(0, k - 1, array)                   # Reversing first k elements
    reverse(k, n - 1, array)                             # Reversing last k elements
    reverse(0, n - 1, array)                   # Reversing whole array


array = [1, 2, 3, 4]
rotate_array_left_by_k(array, 3)
print(array)


########################################################################################################################
# Time complexity : O(n)
# Space complexity: 0(1)
########################################################################################################################

# using python slicing -----> arr[k:]+ arr[:k]

array = [1, 2, 3, 4]
k = 3
print(array[k:] + array[:k])