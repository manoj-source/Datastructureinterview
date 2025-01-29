# Given an array arr[] of size n and an integer sum, the task is to check if there is a triplet in the array which sums
# up to the given target sum.

# Example1:
#             input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
#             Output: true
#             Explanation: The triplet [1, 4, 8] sums up to 13
def triplet_sum_in_array(arr, target):
    n = len(arr)
    for index in range(n-2):
        first_pointer = index +1
        last_pointer = n-1
        required_sum = target - arr[index]
        while first_pointer < last_pointer:
            if required_sum == arr[first_pointer] + arr[last_pointer]:
                return index, first_pointer, last_pointer
            if required_sum < arr[first_pointer] + arr[last_pointer]:
                last_pointer -= 1
            else:
                first_pointer += 1
    # If we reach here, then no two sum was found
    return -1


arr = [1, 4, 5, 6, 8, 52]
target = 15
print(triplet_sum_in_array(arr, target))


arr = [1, 1, 2, 1, 10, 8]
target = 3
print(triplet_sum_in_array(arr, target))

arr = [1, 1, 2, 5, 10, 8]
target = 3
print(triplet_sum_in_array(arr, target))

arr = [-2, -1, 0, 1, 5, 8, 10]
target = -3
print(triplet_sum_in_array(arr, target))

########################################################################################################################
# Time Complexity  : O(n2)
# Space complexity : O(1)
########################################################################################################################

