# python code to check whether given list is sorted or not

def is_list_sorted(arr):
    ascending_flag = -1
    descending_flag = -1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            descending_flag += 1
        if arr[i] < arr[i+1]:
            ascending_flag += 1
        if not ((i != ascending_flag and i == descending_flag) or (i == ascending_flag and i != descending_flag)):
            return -1
    return 1


# Case1: when the array is not sorted.
x = [11, 18, 25, 34, 56, -1]
print(is_list_sorted(x))


# Case2: when the array is sorted.
x = [11, 18, 25, 34, 56]
print(is_list_sorted(x))


# By default we need to write worst case scenario
####################################################################################################################
# 1) Time complexity : O(n)
# 2) Space Complexity : O(1)
####################################################################################################################


