from sorting_algorithms.algorithms import bubbleSort, insertionSort,  selectionSort



if __name__ == "__main__":

    data = [-2, 45, 0, 11, -9]

    # print(bubbleSort(data))
    # print('Sorted Array in Ascending Order:')
    # print(data)

    # unsorted_list = data
    # res = insertionSort(unsorted_list)
    # print(" ".join(map(str, res)))


    unsorted_list = data
    res = selectionSort(unsorted_list)
    print(" ".join(map(str, res)))