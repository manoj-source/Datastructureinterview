# To find the maximum sum of the "K" Consecutive elements in the array
# Above approach can be achieved using sliding window technique.


# Note : Assume Array has positive numbers.

def maximum_sum_k_consecutive(k, nums):
    present_window_sum = sum(nums[:k])
    maximum_sum = sum(nums[:k])  # sum of elements of window of size "k"
    for i in range(len(nums)-k):
        present_window_sum = present_window_sum - nums[i] + nums[i + k]
        if present_window_sum > maximum_sum:
            maximum_sum = present_window_sum
    return maximum_sum


nums = [1, 2, 3, -4, 5, 6, 1, -4, 2]
print(maximum_sum_k_consecutive(5,nums))


#################################################################################################################
# Time complexity : O(n)
# Space Complexity: O(1)
##################################################################################################################

