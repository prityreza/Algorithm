def partition(arr, low, high):  # function for partition
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:  # if elements we are checking is less than the pivot


            i = i + 1  # increase the smaller element by 1 first
            arr[i], arr[j] = arr[j], arr[i]  # then swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # at last swap the pivot at the right place
    return (i + 1)


def quickSort(arr, low, high):  # recursive quicksort function
    if low < high:
        pi = partition(arr, low, high)  # pi is the partition element array index