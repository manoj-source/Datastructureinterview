# 283 Move Zeros

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.


#    Constraints:
#      1 <= nums.length <= 104
#      -231 <= nums[i] <= 231 - 1




def move_zeros_end_of_array(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


nums = [0, 2, 0, 0, 1, 2, 3, 0, 9]
move_zeros_end_of_array(nums)
print(nums)


####################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################
