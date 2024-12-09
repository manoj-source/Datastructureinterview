# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same. Then return the number of
# unique elements in nums.

#   Constraints
#       1 <= nums.length <= 3 * 104
#       -100 <= nums[i] <= 100
#       nums is sorted in non-decreasing order.

def remove_duplicates_from_sorted_list(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i = i + 1
            nums[i] = nums[j]
    return nums[:i + 1]


nums = [1, 1, 2]
print(remove_duplicates_from_sorted_list(nums))


####################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################


