# 1249. Are all dark regions rectangles?

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · difficulty 221 · implementation

Original problem by Nikita Shamgunov and Leonid Volkov, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An N × M image of 0s and 1s (N, M ≤ 3000) is given. Decide whether every
connected region of 1s (cells joined by a side) is a rectangle with sides
along the axes.

Time limit: 2.5 seconds. Memory limit: 4 MB.

## Input

N and M, then N lines of M digits separated by spaces.

## Output

`Yes` or `No`.

## Examples

### Example 1

Input:

```
2 2
0 1
1 1
```

Output:

```
No
```

### Example 2

Input:

```
3 3
0 0 1
1 1 0
1 1 0
```

Output:

```
Yes
```

## Solution

A region fails to be a rectangle exactly when it has an inner corner
somewhere, and an inner corner is a 2 × 2 window with exactly three dark
cells. Conversely, if no window has three dark cells, every region is a
rectangle: walking along a region's edge it can never turn inwards. So
the whole check is: no 2 × 2 window holds exactly three 1s.

The real constraint is memory: the image has up to 9 million cells, and
the input text is about 18 MB, against a limit of 4 MB. A window needs
only two rows, so the program keeps the previous row and the current one,
reads the input as a stream, and stops at the first bad window. `O(N·M)`
time, `O(M)` memory.

Pitfalls:

- reading the whole input at once, or storing a byte per cell, breaks the
  4 MB limit;
- two regions touching only at a corner are fine: that window has two
  dark cells (the second example).

The rule was compared with finding each region and checking that it fills
its bounding box, on 400 random small images.

## Language notes

- Python reads one line at a time, turns it into an integer used as a
  bitset, and finds a bad window with bit operations: an odd number of
  set bits among the four, at least two of them set.
- Java and Rust read the input byte by byte through a small buffer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·M) | AC | 0.531 s | 208 KB |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N·M) | AC | 0.093 s | 1096 KB |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N·M) | AC | 0.156 s | 452 KB |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N·M) | AC | 0.218 s | 1532 KB |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N·M) | AC | 0.031 s | 224 KB |
