# Leetcode 643 : Maximum Average subarray

# You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose
# length is equal to k that has the maximum average value and return this value.

# Example 1:
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000


# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


def findMaxAverage(arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    maximum_windows_k_sum = sum(arr[:k])
    present_windows_k_sum = sum(arr[:k])
    for index in range(k, len(arr)):
        present_windows_k_sum = present_windows_k_sum + arr[index] - arr[index - k]
        if present_windows_k_sum > maximum_windows_k_sum:
            maximum_windows_k_sum = present_windows_k_sum
    return float(maximum_windows_k_sum)/k


arr = [1, 12, -5, - 6, 50, 3]
k = 4
print(findMaxAverage(arr, k))


########################################################################################################################
# Time Complexity  : theta(n-k)  here n is length of array and k is window size.
# Space complexity : O(1)
########################################################################################################################

