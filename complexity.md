# Run Time Complexity

max ops = 10 ^ 7
    
    # When n<20                 2^n, n!             (brute force, backtracking)
    # When n<3000               n^2                 (dynamic programming)
    # When 3000 < n < 10^6      O(n), O(n log n)    two pointers, greedy, heap, sorting
    # When n > 10^6             O(log n), O(1)      binary search, math



## O(log(N))

log(N) grows VERY slowly. log(1,000,000) is only about 20. In fact, lookup by primary key in a relational database is log(N) (many mainstream relational databases such as postgres use B-trees for indexing by default, and searching in a B-tree is log(N)).

- Binary search or variant
- Balanced binary search tree lookup
- Processing the digits of a number
- Typically for n > 10⁸

Note: Unless specified, we assume that log(N) refers to log₂(N) or "log base 2 of N"

The following code is O(log(N)) because N is halved each iteration, so the amount of work is logarithmic:

```python
N = 100000000
while N > 0:
  # some constant operation
  N //= 2
```

## O(N)
Linear time typically means looping through a linear data structure a constant number of times. Most commonly, this means

- Going through array/linked list
- Two pointers
- Some types of greedy
- Tree/graph traversal
- Stack/Queue
- Typically for n ≤ 10⁶

The following examples are both O(N):
```python
for i in range(1, N + 1):
  # constant time code

i = 0
while i < N:
  # constant time code
  i += 1
```

## O(K log(N))

- Heap push/pop K times. When you encounter problems that seek the "top K elements", you can often solve them by pushing and popping to a heap K times, resulting in an O(K log(N)) runtime. e.g., K closest points, merge K sorted lists.
- Binary search K times.
- Typically for n ≤ 10⁶

# O(N log(N))
- Sorting. The default sorting algorithm's expected runtime in all mainstream languages is N log(N). For example, java uses a variant of merge sort for object sorting and a variant of Quick Sort for primitive type sorting.
- Divide and conquer with a linear time merge operation. Divide is normally log(N), and if merge is O(N) then the overall runtime is O(N log(N)). An example problem is smaller numbers to the right.
- Typically for n ≤ 10⁶

```python
n = int(input())
ar = []
for i in range(N):
  m = int(input())
  ar.append(m)          # Inserting complexity is O(N)
ar.sort()               # Sorting complexity is O(N log N)
                        # Total is O(N log N) (because it's dominant).
```

## O(N^2)
Also called quadratic time.

- Nested loops, e.g., visiting each matrix entry
- Many brute force solutions
- Typically for n ≤ 3000

For small N < 1000, this is not that bad for modern computers. 

This example is O(N^2) because the outer loop runs O(N) iterations and the inner loop O(N) as well:

```python
for i in range(1, N + 1):
  for j in range(1, N + 1):
    # constant time code
```
For this example, the outer loop runs O(N) iterations, and the inner loop runs anywhere between 1 and N iterations. Since Big O notation calculates worst-case time complexity, we treat the inner loop as a factor of N. Thus, this code is O(N^2)

```python
for a in range(1, N + 1):
  for j in range(a, N + 1):
    # constant time code
```

## O(2^N)
Grows very rapidly. Often requires memoization to avoid repeated computations and reduce complexity.

- Combinatorial problems, backtracking, e.g. subsets
- Often involves recursion and is harder to analyze time complexity at first sight
- Typically for n ≤ 20

A recursive Fibonacci algorithm is O(2^N) because for any Fib(i) where i > 1, we call Fib(i - 1) and Fib(i - 2).

```python
def Fib(n):
  if n == 0 or n == 1:
    return 1
  return Fib(n - 1) + Fib(n - 2)
```

## O(N!)
Grows insanely rapidly. Only solvable by computers for small N. Often requires memoization to avoid repeated computations and reduce complexity.

- Combinatorial problems, backtracking, e.g. permutations
- Often involves recursion and is harder to analyze time complexity at first sight
- Typically for n ≤ 12


## Amortized Time Complexity
The idea of amortized time is doing a very costly task once in a while. The costly task is done so rarely that it is dilluted away. For example, if we had N O(1) tasks but only a single O(N) task, we could still consider the total O(N) instead of O(N^2) if N is large enough.

The key takeaway is that amortized time is the average time taken per operation.

The following is an implementation of an O(1) append function for a dynamically sized array:

```python
size = None # number of elements in array
capacity = None # maximum number of elements array can store
arr = []
...
def append(x):
  if size == capacity:
    new_arr = [None] * (2 * capacity)
    capacity *= 2
    for i in range(size):
      new_arr[i] = arr[i]
    arr = new_arr
  arr[size] = x
  size += 1
```
In the example from the article about dynamically sized arrays, most of the time when you call append(x), it takes constant time, or O(1), because you simply place the new element at the end. Sometimes, though, you need to resize the array when it's full. In that case, you have to allocate a larger array and copy all the elements, which is an expensive O(N) operation (where N is the number of elements).

However, this expensive resizing happens only occasionally (as the capacity doubles each time), so if you look at the total time for, say, N appends, and divide by the number of operations, the average time per operation remains constant (O(1)). This is what we call amortized O(1) time

## Big O Notation Practice
What is the asymptotic time bound of functions with these time complexities?

    - 3N + 2N + N         ->    O(N)
    - 2N^3 + 5N^2         ->    O(N^3)         
    - N + log(N)          ->    O(N)
    - N^2log(N)           ->    O(N^2 log(N))    
    - 2^N + N^2           ->    O(2^N)
    - 10                  ->    O(1)

What is the time complexity of this code?

```python
# Time Complexity Analysis
# O(N) — Both loops iterate O(N) times with O(1) operations each iteration.

N = int(input())
ar = [0] * N
for i in range(N):              # O(N)
  ar[i] = int(input())
max_val = ar[0]
for i in range(1, N):           # O(N)
  max_val = max(max_val, ar[i])
print(max_val)
```

```python
# Time Complexity Analysis
# O(N^2 log(N)) — The second for loop has O(N) iterations and it takes O(N log(N)) to sort for each interation
N = int(input())
ar = [[0] * N for _ in range(N)]
for i in range(N):
  for j in range(N):            
    ar[i][j] = int(input())     
      
for i in range(N):              # O(N)
  ar[i].sort()                  # O(N log(N))
                                # Total: O(N^2 log(N))
```
```python
# assume an O(1) swap(a, b) function that swaps the values a and b
# Time Complexity Analysis
# O(N^2) — The outer loop iterates O(N) times, the inner loops O(N / 2) times which is O(N), and swapping is O(1)
N = int(input())
ar = [[0] * N] * N
for i in range(N):                  # O(N)
  for j in range(N/2):              # O(N)
    swap(ar[i][j], ar[i][N - j])
                                    # Total: O(N^2)
``` 

```python
# Time Complexity Analysis
# O(log(N)) — N is divided by 2 each time, so the amount of work is logarithmic with respect to N.

N = int(input())
bin = []
while N != 0:
  bin.append(N)
  N //= 2
```

```python
# assume the log2(N) function takes O(1) time
# assume string concatenation takes O(1) time

# Time complexity Analysis
# O(N) — By logarithm rules, O(2^log(N)) = O(N) strings are formed.

def func(str, idx, len):                # O(2^N)
  if idx == len:
    # ...  an O(1) op
  else:
    func(str + "a", idx + 1, len)
    func(str + "b", idx + 1, len)
...
N = int(input())
func("", 0, int(log2(N)))               # O(2^log(N)) = O(N)
```
