# Leetcode : 15
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
#  and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1, -1, 2],[-1, 0, 1]]

# Example :
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example :
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def triplets_sum_zero(arr):
    triplets = []
    sum = 0
    n = len(arr)
    for index in range(n-2):
        first_pointer = index + 1
        last_pointer = n - 1
        require_sum = sum-arr[index]
        while first_pointer < last_pointer:
            if arr[first_pointer] + arr[last_pointer] == require_sum:
                if [arr[index], arr[first_pointer], arr[last_pointer]] not in triplets:
                    triplets.append([arr[index], arr[first_pointer], arr[last_pointer]])
            if arr[first_pointer] + arr[last_pointer] < require_sum:
                first_pointer += 1
            else:
                last_pointer -= 1
    if len(triplets) == 0:
        return []
    else:
        return triplets


nums = [-4, -1, -1, 0, 1, 2]
print(triplets_sum_zero(nums))

nums = [0, 1, 1]
print(triplets_sum_zero(nums))

nums = [0, 0, 0]
print(triplets_sum_zero(nums))

########################################################################################################################
# Time Complexity  : O(n2)
# Space complexity : O(1)
########################################################################################################################

