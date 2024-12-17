# 724. Find Pivot Index (To find the equilibrium point in the array)

# 1) Given an array of integers nums, calculate the pivot index of this array.
# 2) The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the
#    sum of all the numbers strictly to the index's right.
# 3) If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
#    This also applies to the right edge of the array.
#    Return the leftmost pivot index. If no such index exists, return -1.

def pivot_index(arr):
    right_sum, left_sum = sum(arr[:])-arr[0], 0
    for i in range(0, len(arr)):
        print(left_sum, right_sum)
        if right_sum == left_sum:
            return i
        if i == len(arr)-1:
            right_sum = 0
        else:
            right_sum -= arr[i+1]
        left_sum += arr[i]
    return -1


arr = [-1,-1,0,1,1,0]
print(pivot_index(arr))

########################################################################################################################
# Time complexity : O(n)
# Space complexity: 0(1)
########################################################################################################################



