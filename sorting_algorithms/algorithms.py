
def bubbleSort(unsorted_list: list[int]) -> list[int]:
    n = len(unsorted_list)
    # Iterate through all list elements in reversed order

    for i in reversed(range(n)):
        # Track whether a swap occurred in this pass
        swapped = False
        for j in range(i):

            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # If no two elements were swapped, the list is sorted
        if not swapped:
            return unsorted_list
    return unsorted_list


def insertionSort(unsorted_list: list[int]) -> list[int]:
    for i in range(len(unsorted_list)):
        current = i
        # gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            # swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

def selectionSort(unsorted_list: list[int]) -> list[int]:

    n = len(unsorted_list)
    for i in range(n):
        # Assume the current position as minimum
        min_index = i

        # Find the minimum element's index from the rest of the list
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list
