# To find the Minimum Element in the list

def min_element_in_list(arr):
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element


# Randomly Maximum Element
arr = [10, 34, 5, 7, 100]
print(min_element_in_list(arr))


# First element is maximum
arr = [1, 34, 5, 7, 10]
print(min_element_in_list(arr))


# Last element is maximum
arr = [100, 34, 5, 7, 3]
print(min_element_in_list(arr))


####################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################

