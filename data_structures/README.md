


## Linked List

Python does not have a built-in linked list. Normally, in an interview, you would be given a definition like this.

```python
class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
```

    append to end is O(N).
    finding an element is O(N).


## Stack
Python's list also doubles as a stack. For a list l = []

```python
l = []

l.append(1)     # push:  O(1)
l.pop()         # pop:  O(1)
len(l)          # size:  O(1)
l[-1]         # top:  O(1)
```

## Queue

Python's collections.deque is a double-ended queue, which means you can push and pop an element from either end in constant time. In the coding interviews, this is what we normally use when we need a queue. For a deque q = deque()
```python
from collections import deque

q = deque()
q.append(1)    #enqueue: O(1)
q.pop()        #dequeue:  O(1). Note that it's pop*left*. pop is also supported but it's for getting element at the end of the double-ended queue.
q.popleft()
q[0]           # peek: O(1). Accesses the first element of the queue just like an array.
len(q)         # size: O(1)
```
## Hash Table

Python's dict is an implementation of a hash table. For a dictionary d = {},

```python
d = {'a': "hello", 'b': "world"}
d['a']             # get using a key: O(1), gives KeyError if key isn't in the dictionary
d['c'] = "!"       # set a key, value: O(1)
del d['c'],        # remove a key: O(1)
len(d)             # size: , O(1), returns the number of items in the dictionary.
```
It's worth mentioning that these are average-case time complexities. A hash table's worst time complexity is actually O(N) due to hash collision and others. For the vast majority of the cases and certainly most coding interviews, the assumption of constant time lookup/insert/delete is valid.

Use a hash table if you want to create a mapping from A to B. Many starter interview problems can be solved with a hash table.

Python dict has a convenient subclass Counter for counting hashable objects. When you pass an iterable object, such as a list or a string, to Counter(), it will return a new dict with elements as keys and their counts as values.

### Counter
```python
import collections.Counter
word = "occur"
counter = Counter(word)
# counter = {'o': 1, 'c': 2, 'u': 1, 'r': 1}

print(counter['c'])    # prints out 2
print(counter['y'])    # prints out 0 for a non-existent element

# the number of unique elements in word can be obtained by the length of its counter
num_of_unique_elements = len(counter)
# num_of_unique_elements = 4
```

## Hash Set

Python's set is an implementation of hash set but it is implemented over a Hash Table (dict). It's useful in answering the existence queries in constant time. For a set s = set(),
```python
s = set([ 'b', 'c', 'd'])
a = 'a'
b = set([ 'e', 'f'])
a in s       # is a in set s: a in s, O(1)
s.add(a)     # adding a to set: O(1). Duplicates will be discarded.
s.discard(a)  # removing a from set: O(1). Does nothing if a is not in the set.

s.update(b)  # adding all elements of b to set: O(len(b)). If an element is already in the set, it will be discarded.
s.union(b)  # returns a new set with all elements of s and b: O(len(s) + len(b)). Does not modify s.
```

Hash set is useful when you only need to know existence of a key. Example use cases include DFS and BFS on graphs.

## Tree

Python does not have built-in tree support. Normally at an interview, you'd be given the following implementation for binary tree.
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

For n-nary trees:

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
```

## Infinity

Infinity is useful when you want to initialize a variable that is greater or smaller than any value that your algorithm may want to compare with. There are 2 ways to represent infinity as an integer in Python. The first one is to use float values:

```python
positive_inf = float('inf')
negative_inf = float('-inf')
```

Since Python 3.5, we can also use the math module to represent infinite integers:

```python
import math

positive_inf = math.inf
negative_inf = -math.inf

```

