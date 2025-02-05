# Leetcode 53 : Maximum Sum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
#        Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#        Output: 6
#        Explanation: The subarray[4, -1, 2, 1] has the largest sum 6.


# Example 2:
#        Input: nums = [1]
#        Output: 1
#        Explanation: The subarray[1] has the largest sum 1.


# Example 3:
#        Input: nums = [5, 4, -1, 7, 8]
#        Output: 23
# Explanation: The subarray[5, 4, -1, 7, 8] has the largest sum 23.

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

def maximum_sum_subarray(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = 0
    end = 0
    s = 0
    for index in range(1, len(arr)):
        max_ending_here += arr[index]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = index
        if max_ending_here < 0:
            max_ending_here = 0
            s = index + 1
    return (start, end), max_so_far


print(maximum_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maximum_sum_subarray([5, 4, -1, 7, 8]))


########################################################################################################################
# Time Complexity  : O(n)
# Space complexity : O(1)
########################################################################################################################

