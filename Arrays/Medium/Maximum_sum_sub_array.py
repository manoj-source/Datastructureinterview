# 53. Maximum subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


# Below is the kadan's algorithm
def maximum_sum_sub_array(arr, size):
    maximum_so_far = arr[0]
    maximum_end_here = arr[0]
    start = 0
    end = 0
    s = 0
    for i in range(1, size):
        maximum_end_here += a[i]
        if maximum_so_far < maximum_end_here:
            maximum_so_far = maximum_end_here
            start = s
            end = i
        if maximum_end_here < 0:
            maximum_end_here = 0
            s = i + 1
    return maximum_so_far, start, end


a = [1, 2, 3, 4, 20, 50]
print(maximum_sum_sub_array(a, len(a)))


########################################################################################################################
# Time complexity : O(n)
# Space complexity: 0(1)
########################################################################################################################


