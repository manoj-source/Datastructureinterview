# To find the Minimum Element in the list in constant time
# Input :
#        1) Input array contain positive and negative elements


def minimum_element_in_array(arr):
    minimum_element = float('inf')
    min_index = -1
    for index in range(len(arr)):
        if arr[index] < minimum_element:
            minimum_element = arr[index]
            min_index = index
    return min_index, minimum_element


arr = [-20, 25, 50, -45, 100, -36]
print(minimum_element_in_array(arr))


arr = [-20, -25, -50, -45, -1, -36]
print(minimum_element_in_array(arr))

arr = [20, 25, 50, 45, 1, 36]
print(minimum_element_in_array(arr))


#################################################################################################################
# a) Time Complexity : O(n)
# b) Space Complexity: O(1)
####################################################################################################################
