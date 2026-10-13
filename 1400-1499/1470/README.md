# 1470. UFOs

[Timus 1470](https://acm.timus.ru/problem.aspx?space=1&num=1470) · difficulty 253 · fenwick

Original problem by Dmitry Zhukov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cube of N × N × N unit sectors (1 ≤ N ≤ 128, coordinates from 0 to
N − 1) starts empty. Records arrive one per line. "1 x y z K" changes
the number of objects in sector (x, y, z) by K (−20000 ≤ K ≤ 20000);
no sector ever goes below zero. "2 x1 y1 z1 x2 y2 z2" asks how many
objects lie in the box x1 ≤ x ≤ x2, y1 ≤ y ≤ y2, z1 ≤ z ≤ z2. "3"
ends the input. There are at most 100002 records.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then the records, the last of them "3".

## Output

The answer to each question on its own line.

## Examples

### Example 1

Input:

```
2
2 1 1 1 1 1 1
1 0 0 0 1
1 0 1 0 3
2 0 0 0 0 0 0
2 0 0 0 0 1 0
1 0 1 0 -2
2 0 0 0 1 1 1
3
```

Output:

```
0
1
4
2
```

## Solution

A Fenwick tree works in any number of dimensions: cell (i, j, w) holds
the sum over the block of sectors whose indices end at i, j and w and
are as long as their lowest set bits. A change walks i upwards and,
inside it, j and w upwards; a prefix sum over [1, x] × [1, y] × [1, z]
walks all three downwards. Each walk has at most 8 steps per axis, so an
update or prefix sum costs at most 8³ cell visits. The sum over a box comes from
inclusion and exclusion over its eight corners, the corners on the
lower side shifted by one. The tree takes (N + 1)³ 64-bit cells, about
17 MB. `O(log³ N)` per record.

Pitfalls:

- the coordinates start at 0, while a Fenwick tree starts at 1, so
  every index moves up by one (tests 03, 04);
- the counts in all sectors together reach 2·10⁹, and the partial sums
  of the eight-corner formula go past the 32-bit range, so sums are
  64-bit (gen4);
- questions may come before any change and a change may be 0 (tests
  01, 02).

## Language notes

- Python runs under PyPy: the largest tests take about 7.5 s with
  CPython and about 0.35 s with PyPy. The tree is an `array("q")`,
  because a list of large integers would not fit in 64 MB.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1470_fenwick.cpp](1470_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(log^3 N) per record | AC | 0.375 s | 16552 KB |
| [1470_fenwick.go](1470_fenwick.go) | Go 1.14 x64 | fenwick | O(log^3 N) per record | AC | 0.156 s | 20044 KB |
| [1470_fenwick.java](1470_fenwick.java) | Java 1.8 | fenwick | O(log^3 N) per record | AC | 0.281 s | 20908 KB |
| [1470_fenwick.py](1470_fenwick.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per record | AC | 0.890 s | 61120 KB |
| [1470_fenwick.rs](1470_fenwick.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per record | AC | 0.125 s | 19804 KB |
