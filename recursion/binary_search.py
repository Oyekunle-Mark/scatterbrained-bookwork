def binary_search(arr, target, low, high):
    # find the mid of high and low
    mid = (low + high) // 2
    # if item at index is target return
    if arr[mid] == target:
        return True
    # if state a base case of low is greater than or equals high
    elif low >= high:
        # return false
        return False
    # otherwise
    else:
        # if mid of arr is greater than target
        if arr[mid] > target:
            # recursively call binarysearch with low and mid
            binary_search(arr, target, low, mid)
        # otherwise
        else:
            # recursively call binarysearch with mid and high
            binary_search(arr, target, mid, high)
