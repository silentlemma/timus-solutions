# 1082. Input that makes a quicksort count a given number of steps

[Timus 1082](https://acm.timus.ru/problem.aspx?space=1&num=1082) · difficulty 126 · constructive

Original problem by Nikita Shamgunov, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A given program reads `N` integers (`1 ≤ N ≤ 1000`) and sorts them with
a quicksort: the first element of a range is the pivot, and two indices
move towards each other, `j` from the right while elements are greater
than the pivot and `i` from the left while they are smaller, swapping
when they have not crossed (Hoare's partition). The program counts every
single move of `i` and `j` over all calls and wins if the total is
exactly `(N² + 3N − 4)/2`. Print `N` integers within `10^9` in absolute
value that make it win.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

`N` integers separated by spaces.

## Checking

Any suitable numbers are accepted. The checker runs the same partition on
the output and compares the count with `(N² + 3N − 4)/2`.

## Examples

### Example 1

Input:

```
3
```

Output:

```
1 2 3
```

## Solution

Print the sorted numbers `1, 2, …, N`. On a sorted range of length `k`
with the pivot at its left end, `j` walks from the right end all the way
to the pivot, `k` moves, and `i` makes one move onto the pivot; they meet
at once, so the range splits into the pivot alone and the other `k − 1`
elements, still sorted. The count is `k + 1` for every `k` from `N` down
to 2:

`(N + 1) + N + … + 3 = (N² + 3N − 4)/2`,

which is exactly the target. `O(N)`.

Pitfalls:

- other orders give other counts: for `3 2 1` the program counts 8
  moves instead of 7, because the swap changes how the ranges split;
- for `N = 1` the program counts nothing, and the target is 0 too.

The checker simulates the partition with an explicit stack and compares
the count.

## Language notes

- All languages print `1 … N` joined by spaces.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1082_constructive.cpp](1082_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 128 KB |
| [1082_constructive.go](1082_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1116 KB |
| [1082_constructive.java](1082_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 1592 KB |
| [1082_constructive.py](1082_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.062 s | 452 KB |
| [1082_constructive.rs](1082_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 252 KB |
