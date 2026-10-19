# 1846. GCD 2010

[Timus 1846](https://acm.timus.ru/problem.aspx?space=1&num=1846) · difficulty 155 · segment_tree

Original problem by Alexey Samsonov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A multiset of positive integers starts empty. Each operation adds a
number or removes one copy of a number that is there. After every
operation print the greatest common divisor of the whole multiset; the
gcd of an empty multiset is declared to be 1.

## Input

q (1 ≤ q ≤ 10⁵), then q lines "+ x" or "- x" with 1 ≤ x ≤ 10⁹. Only
numbers present are removed.

## Output

The gcd after each operation, one per line.

## Examples

### Example 1

Input:

```
5
+ 8
+ 6
+ 8
- 8
- 8
```

Output:

```
8
2
2
2
6
```

## Solution

A gcd cannot be undone, so removing a number needs a structure. Give
every addition its own leaf of a segment tree over the operations, and
keep for each value a stack of the leaves that hold it. Adding x writes
x into the leaf of that operation; removing x empties the top leaf of
its stack, writing 0, which leaves any gcd unchanged since
gcd(a, 0) = a. Each internal node holds the gcd of its children, so the
root is the gcd of the multiset, and a root of 0 means the multiset is
empty: print 1. Updating a leaf recomputes its ancestors, and the walk
up can stop at the first node whose value stays the same, since nothing
above it changes then. `O(q log q log x)`.

In the example the leaves hold 8, 6 and 8, so the gcd is 2. Removing
the two 8s empties two leaves and leaves 6.

Pitfalls:

- the empty multiset prints 1, not 0;
- equal numbers may be added several times and removed one at a time;
- with half a second, stopping the walk early and reading the input
  quickly both matter; the Python solution runs on PyPy.

The answers agree with an independent accepted implementation on thirty
random files of up to 10⁵ operations.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1846_segment_tree.cpp](1846_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.171 s | 8616 KB |
| [1846_segment_tree.go](1846_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 14000 KB |
| [1846_segment_tree.java](1846_segment_tree.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.140 s | 10080 KB |
| [1846_segment_tree.py](1846_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.250 s | 37060 KB |
| [1846_segment_tree.rs](1846_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.046 s | 12328 KB |
