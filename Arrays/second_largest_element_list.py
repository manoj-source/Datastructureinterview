# To find the second largest element in the list

def second_largest_element(arr):
    if arr[0] > arr[1]:
        first_max = arr[0]
        second_max = arr[1]
    else:
        first_max = arr[1]
        second_max = arr[0]
    for i in range(2, len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        if arr[i] > second_max and arr[i] != first_max:
            second_max = arr[i]
        if first_max == second_max and second_max != arr[i]:
            second_max = arr[i]
    return second_max


# Case1 : without repeatation
arr = [1, 10, 34, 56, 21, 13]
print(second_largest_element(arr))

# Case2: with Repeatation
arr = [1, 10, 34, 56, 21, 56, 13]
print(second_largest_element(arr))


########################################################################################################################
# Time complexity : O(n)
# Space complexity: 0(1)
########################################################################################################################
