def find_kth_largest_smallest(arr, k):
    # Sort the array in ascending order
    arr_sorted = sorted(arr)
    # Return the kth smallest number
    kth_smallest = arr_sorted[k-1]
    # Return the kth largest number
    kth_largest = arr_sorted[-k]
    return kth_smallest, kth_largest
arr = [3, 1, 7, 4, 2, 9, 5, 8, 6]
k = 3
kth_smallest, kth_largest = find_kth_largest_smallest(arr, k)
print("The {}rd smallest number in the array is: {}".format(k, kth_smallest))
print("The {}rd largest number in the array is: {}".format(k, kth_largest))
