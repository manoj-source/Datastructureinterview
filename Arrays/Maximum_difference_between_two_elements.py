# Leetcode problem : 2016. Maximum Difference Between Increasing Elements

# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j]
# (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

# Constraints:
#       n == nums.length
#       2 <= n <= 1000
#       1 <= nums[i] <= 109

def max_diff_between_two_elements_in_list(arr):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff


arr = [7, 1, 5, 4]
print(max_diff_between_two_elements_in_list(arr))

##################################################################################################################
# Time complexity : O(n)
# Space Complexity: O(1)
##################################################################################################################


# Another approach is using kadane's algorithm
