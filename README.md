## O(log(N))
- Binary search

## O(N log(N))
- Quick sort
- Merge Sort

## O(N^2)
- Bubble sort
- Insertion sort
- Selection sort
- Matrix multiplication     

## O(2^N)
- Fibonacci sequence
- Tower of Hanoi
- Subset sum problem
- Permutations of a set
- Combinatorial problems



## Keyword to Algorithm

This is a mapping of keywords you'll see in coding problems to the algorithms that solve them. If you are not experienced with solving coding problem, it may not make much sense now but don't worry we will learn all these later.

Use this guide as a reference when you're trying to identify which algorithm might be appropriate for a particular problem. The keywords and phrases listed below often signal that a specific algorithm or data structure approach would be effective.

### "Top k"

    Heap: K closest points

### "How many ways.."

    DFS: Decode ways
    DP: Robot paths

### "Substring"

    Sliding window: Longest substring without repeating characters

### "Palindrome"

    two pointers: Valid Palindrome
    DFS: Palindrome Partitioning
    DP: Palindrome Partitioning II

### "Tree"

    shortest, level-order
        BFS: Binary Tree Level-Order Traversal
    else: DFS: Max Depth

### "Parentheses"

    Stack: Valid Parentheses

### "Subarray"

    Sliding window: Maximum subarray sum
    Prefix sum: Subarray sum
    Hashmap: Continuous subarray sum

### Max subarray

    Greedy: Kadane's Algorithm

### "X Sum"

    Two pointer: Two sum

### "Max/longest sequence"

    Dynamic programming, DFS: Longest increasing subsequence
    mono deque: Sliding window maximum

### "Minimum/Shortest"

    Dynamic programming, DFS: Minimal path sum
    BFS: Shortest path

### "Partition/split ... array/string"

    DFS: Decode ways

### "Subsequence"

    Dynamic programming, DFS: Longest increasing subsequence
    Sliding window: Longest increasing subsequence

### "Matrix"

    BFS, DFS: Flood fill, Islands
    Dynamic programming: Maximal square

### "Jump"

    Greedy/DP: Jump game

### "Game"

    Dynamic programming: Divisor game, Stone game

### "Connected component", "Cut/remove" "Regions/groups/connections"

    Union Find: Number of connected components, Redundant connections

### Transitive relationship

If the items are related to one another and the relationship is transitive, then chances are we can build a graph and use BFS or Union Find.

    string converting to another, BFS: Word Ladder
    string converting to another, BFS, Union Find: Sentence Similarity
    numbers having divisional relationship, BFS, Union Find: Evaluate Division

"Interval"

    Greedy: sort by start/end time and then go through sorted intervals Interval Pattern
