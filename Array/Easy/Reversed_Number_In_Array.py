# To reverse the elements in the array in the constant linear time (Two pointer Approach)
# Input :
#           Elements in the array can be positive and negative.
def reverse_elements_in_array(arr):
    first_pointer = 0                                      # first pointer
    last_pointer = len(arr) - 1                            # last pointer
    while first_pointer < last_pointer:
        arr[first_pointer], arr[last_pointer] = arr[last_pointer], arr[first_pointer]      # swapping
        first_pointer += 1
        last_pointer -= 1


# Case1: For even array length.
arr = [1, 2, 3, 4]
reverse_elements_in_array(arr)
print(arr)

# Case2: For the odd array length.
arr = [1, 2, 3, 4, 5]
reverse_elements_in_array(arr)
print(arr)


#######################################################################################################
# Time Complexity  : O(log2(n))
# Space complexity : O(1)
#######################################################################################################

