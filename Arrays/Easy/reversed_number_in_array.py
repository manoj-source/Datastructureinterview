# To reverse the elements in the list(In Linear time constant).

def reverse_elements_in_list(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1


# Case1: For the even array length.
arr = [1, 2, 3, 4]
reverse_elements_in_list(arr)
print(arr)

# Case2: For the odd array length.
arr = [1, 2, 3, 4, 5]
reverse_elements_in_list(arr)
print(arr)


###################################################################################################################
# Time Complexity  : O(n/2)
# Space complexity : O(1)
####################################################################################################################


# Using the default method in python

# using list slicing ----------> arr[::-1]
# using list comprehension ----> [arr[len(arr)-i-1] for i in range(len(arr))]
# using array reverse method --> arr.reverse()


####################################################################################################################
