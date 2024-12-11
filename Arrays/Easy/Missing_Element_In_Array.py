# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
# missing from the array.

# Constraints:
#    n == nums.length
#    1 <= n <= 104
#    0 <= nums[i] <= n
#    All the numbers of nums are unique.

##############################################################################################################

# Approach :

#    Another efficient approach is to use the XOR operation. The approach is based on the idea that XOR of a number with
#    itself is 0, and XOR of a number with 0 is the number itself. This means that if we find XOR of first N natural
#    numbers and then take XOR of each array elements with this, then the resultant will be the missing number.


def missing_number(arr):
    n = len(arr)
    xor1 = 0
    xor2 = 0

    # XOR all array elements
    for num in arr:
        xor2 ^= num

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i

    # Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2


a = [3, 0, 1]
print(missing_number(a))


####################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################





