# To find the Maximum Element in the list

def max_element_in_list(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element


# Randomly Maximum Element
arr = [1, 34, 5, 7, 10]
print(max_element_in_list(arr))


# First element is maximum
arr = [100, 34, 5, 7, 10]
print(max_element_in_list(arr))


# Last element is maximum
arr = [100, 34, 5, 7, 1000]
print(max_element_in_list(arr))

####################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################

