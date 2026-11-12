# 1069. Rebuilding a tree from its Prüfer code

[Timus 1069](https://acm.timus.ru/problem.aspx?space=1&num=1069) · difficulty 513 · trees

Original problem by Magaz Asanov, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree on vertices `1 … N` (`2 ≤ N ≤ 7500`) is encoded like this: take the
leaf with the smallest number, remove it and write down its neighbour;
repeat until one vertex is left (it is always `N`). The `N − 1` written
numbers are the code. Given the code, print the adjacency list of every
vertex.

Time limit: 0.25 seconds. Memory limit: 8 MB.

## Input

The code: `N − 1` numbers separated by spaces and line breaks.

## Output

For each vertex in increasing order, a line `v: a b c …` with its
neighbours in increasing order.

## Checking

The output is compared line by line; within a line, token by token.

## Examples

### Example 1

Input:

```
2 1 6 2 6
```

Output:

```
1: 4 6
2: 3 5 6
3: 2
4: 1
5: 2
6: 1 2
```

## Solution

During the encoding a vertex is written once for every neighbour removed
before it, and it becomes a leaf when only one neighbour is left. The
counter `1 + (the number of times v occurs in the code)` equals the degree
for `v != N` and the degree plus one for `N`. Before each step, the
remaining vertices with counter 1 are exactly the leaves other than `N`.

The decoder follows the encoding step by step. Start with the counters
above and a min-heap of the vertices with counter 1. For each number `c` of
the code, the smallest leaf is the vertex that was removed: join it to `c`
and decrease the counter of `c`; when it drops to 1, put `c` into the
heap. Then sort every adjacency list. `O(N log N)`.

Pitfalls:

- this code has `N − 1` numbers and ends with `N`, one more than the usual
  Prüfer code, so `N` is the count of numbers plus one;
- vertex `N` never leaves the heap too early: a tree always has at least
  two leaves, so a smaller one is always there;
- the numbers may be spread over lines in any way, so they are read as
  tokens;
- the limits are tight (0.25 seconds and 8 MB), so the output is
  buffered and the lists are kept compact.

The answers were checked the other way round: the printed tree, encoded
again by the definition, gives back the input.

## Optimized solutions

Go removes both the leaf heap and adjacency sorting. A monotone pointer scans to the next label absent from the remaining code. After attaching that leaf to the next code label, use that label immediately if its last occurrence vanished and it lies below the pointer. All earlier labels were removed or still occurred in the code, and only this counter changed. Otherwise advance the pointer to find the smallest available leaf. Store each removed leaf’s parent. The last code symbol is N, so N remains the root. Descending vertex IDs prepended to parent child-lists make every child-list increasing. Merge each list with its one parent while printing, so sorted adjacency also takes linear time. Labels and counts fit uint16 for N≤7500. Time and storage O(N), bounded I/O. All heap-based teaching sources remain; the other four families reuse admitted bases.

The accepted base implementations [1069_trees.cpp](1069_trees.cpp), [1069_trees.java](1069_trees.java), [1069_trees.py](1069_trees.py), [1069_trees.rs](1069_trees.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

C++/Rust retain min-heaps, Java PriorityQueue and sized adjacency arrays, Python heapq. Original Go uses container/heap; new Go uses a monotone leaf pointer and sorted child/parent merging, with uint16 labels/counts and bounded standard-handle I/O.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1069_trees.cpp](1069_trees.cpp) | G++ 13.2 x64 | trees | O(N log N) | AC | 0.015 s | 420 KB | 11278893 |
| [1069_trees.go](1069_trees.go) | Go 1.14 x64 | trees | O(N log N) | AC | 0.031 s | 2564 KB | 11278897 |
| [1069_trees.java](1069_trees.java) | Java 1.8 | trees | O(N log N) | AC | 0.125 s | 1972 KB | 11278900 |
| [1069_trees.py](1069_trees.py) \* | Python 3.12 x64 | trees | O(N log N) | AC | 0.109 s | 3176 KB | 11278899 |
| [1069_trees.rs](1069_trees.rs) \* | Rust 1.75 x64 | trees | O(N log N) | AC | 0.062 s | 1188 KB | 11278902 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1069_trees_two_pointers.go](1069_trees_two_pointers.go) \* | Go 1.14 x64 | trees, two_pointers | O(N) | AC | 0.015 s | 912 KB | 11315466 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
