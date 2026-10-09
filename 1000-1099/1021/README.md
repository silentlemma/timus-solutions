# 1021. A pair from two sorted lists with a given sum

[Timus 1021](https://acm.timus.ru/problem.aspx?space=1&num=1021) · difficulty 148 · two_pointers, hashing

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two lists of integers are given: the first sorted in increasing order, the
second in decreasing order (`1 ≤ N_i ≤ 50 000` numbers each, every number
from -32768 to 32767). Decide whether one number from each list can be
chosen so that they sum to exactly 10000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first list: its size, then its numbers, one per line. Then the second
list in the same format.

## Output

`YES` if such a pair exists, `NO` otherwise.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
-5
3
9998
3
10
7
2
```

Output:

```
YES
```

### Example 2

Input:

```
3
1
2
3
3
9000
50
0
```

Output:

```
NO
```

## Solution

**Two pointers.** Put a pointer `i` at the start of the increasing list and
`j` at the start of the decreasing one, so `up[i]` is the smallest remaining
number of the first list and `down[j]` the largest of the second. Compare
`up[i] + down[j]` with 10000:

- equal — the pair is found;
- smaller — `up[i]` cannot be part of any pair, because even the largest
  remaining `down[j]` is not enough: move `i` forward;
- larger — `down[j]` cannot be part of any pair, because even the smallest
  remaining `up[i]` is too much: move `j` forward.

When a pointer runs off its list, there is no pair. Every step discards one
number: `O(N_1 + N_2)`.

**Hashing.** Put `10000 - b` for every `b` of the second list into a set and
check whether any number of the first list is in it — also linear on
average, and it does not need the sorting.

Pitfalls:

- the second list is sorted the other way: walk both lists from the
  beginning;
- the sum 10000 may need the extreme values, e.g. `32767 + (-22767)`.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: two pointers.
- **Python**: a set intersection, which runs at C speed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1021_hashing.py](1021_hashing.py) | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.078 s | 10700 KB |
| [1021_two_pointers.cpp](1021_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.078 s | 576 KB |
| [1021_two_pointers.go](1021_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 2620 KB |
| [1021_two_pointers.java](1021_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 904 KB |
| [1021_two_pointers.rs](1021_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 2112 KB |
