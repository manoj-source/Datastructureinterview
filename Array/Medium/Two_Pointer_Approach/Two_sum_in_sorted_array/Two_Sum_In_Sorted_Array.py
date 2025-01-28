# Leetcode 167 :  Two Sum II - Input Array Is Sorted.

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
# that they add up to a specific target number.Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.Return the indices of the two numbers, index1 and index2, added
# by one as an integer array [index1, index2] of length 2.

# Example 1:
#            Input: numbers = [2,7,11,15], target = 9
#            Output: [1,2]
#            Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


# Example 2:

#            Input: numbers = [2,3,4], target = 6
#            Output: [1,3]
#            Explanation: The sum of 2 and 4 is 6. therefore index1 = 1, index2 = 3. We return [1, 3].


# Example 3:

#            Input: numbers = [-1,0], target = -1
#            Output: [1,2]
#            Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


def two_sum_sorted_array(arr, target):
    first_pointer = 0
    last_pointer = len(arr) - 1
    while first_pointer < last_pointer:
        sum = arr[first_pointer] + arr[last_pointer]
        if sum == target:
            return first_pointer, last_pointer
        if sum < target:
            first_pointer += 1
        else:
            last_pointer -= 1
    # If we reach here, then no two sum was found
    return -1


arr = [2, 7, 11, 15]
target = 9
print(two_sum_sorted_array(arr, target))

arr = [2, 3, 4]
target = 6
print(two_sum_sorted_array(arr, target))


arr = [-1, 0]
target = -1
print(two_sum_sorted_array(arr, target))

arr = [2, 6, 11, 15]                                # when two sum of target 9 is not found in the array
target = 9
print(two_sum_sorted_array(arr, target))


##################################################################################################################
# Time Complexity  : O(log2n)
# Space complexity : O(1)
###################################################################################################################

