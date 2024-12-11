# To find the prefix sum of the given array

def prefix_sum_array(nums):
    sum = 0
    prefix_array = []
    for i in range(len(nums)):
        sum += nums[i]
        prefix_array.append(sum)
    return prefix_array


arr = [1, 2, 3, 4, 5, 6]
print(prefix_sum_array(arr))


#################################################################################################################
# Time complexity : O(n)
# Space Complexity: O(1)
##################################################################################################################

