## O(N^2)
### Bubble Sort  

```python
from sorting_algorithms.algorithms import bubbleSort

data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)
```

### Insertion Sort

```python
from sorting_algorithms.algorithms import insertionSort
unsorted_list = [int(x) for x in input().split()]
res = insertionSort(unsorted_list)
print(" ".join(map(str, res)))
```