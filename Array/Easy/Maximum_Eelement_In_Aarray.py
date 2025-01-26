# To find the Maximum Element in the list in constant time
# Input :
#        1) Input array contain positive and negative elements


def maximum_element_in_array(arr):
    max_element = float('-inf')
    max_index = -1
    for index in range(len(arr)):
        if arr[index] > max_element:
            max_element = arr[index]
            max_index = index
    return max_index, max_element


arr = [-20, 25, 50, -45, 100, -36]
print(maximum_element_in_array(arr))


arr = [-20, -25, -50, -45, -1, -36]
print(maximum_element_in_array(arr))


####################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################
