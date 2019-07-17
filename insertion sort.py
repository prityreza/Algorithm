def insertionSort(array):
    for i in range(1, len(array)):  # loop to go through the entire array , we start at i=1 cause i=0 is already sorted
        item_to_check = array[i]  # we keep the 2nd element ,i.e i=1 as our item to check
        j = i - 1  # we create another variable named j , and set it ti i-1, because that is the left element of our item, and
        # we wnat to compare our item with that element of j

        while j >= 0 and item_to_check < array[j]:
            # here we use a while loop which works on basis of two conditons
            # j>=0 means , if the index is less than zero i.e we don't have any elements left to compare loop breaks
            # the 2nd conditon states that for this while loop to work the item must be smaller than the left element
            array[j + 1] = array[j]
            # this line means , we create an empty space ,i.e by moving the left element one position into the right, so
            # we can insert the item into the right place

            j = -1
            # this line is to comtiniously move the element we compare with to the left so that all elements till the
            # already sorted part of our array is checked
        array[j + 1] = item_to_check
        ##After we have come out of while loop we insert out item into the right place


array = [1, 3, 4, 2]
insertionSort(array)
print("Sorted array is : \n")
for i in range(len(array)):
    print("%d" % array[i])