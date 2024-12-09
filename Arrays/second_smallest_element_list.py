# To find the second smallest element in the list

def second_smallest_element(arr):
    if arr[0] <= arr[1]:
        first_min = arr[0]
        second_min = arr[1]
    else:
        first_min = arr[1]
        second_min = arr[0]
    for i in range(2, len(arr)):
        if arr[i] < first_min:
            second_min = first_min
            first_min = arr[i]
        if arr[i] < second_min and arr[i] != first_min:
            second_min = arr[i]
        if first_min == second_min and second_min != arr[i]:
            second_min = arr[i]
    return second_min


# Case1 : without repeatation
arr = [1, 10, 34, 56, 21, 13]
print(second_smallest_element(arr))

# Case2: with Repeatation
arr = [1, 10, 34, 56, 21, 56, 1]
print(second_smallest_element(arr))


########################################################################################################################
# Time complexity : O(n)
# Space complexity: 0(1)
########################################################################################################################
