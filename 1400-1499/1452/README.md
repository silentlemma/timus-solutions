# 1452. Pascal vs. C++

[Timus 1452](https://acm.timus.ru/problem.aspx?space=1&num=1452) · difficulty 608 · hashing

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence has N elements (2 ≤ N ≤ 2000), integers from 0 to 10⁹.
Choose as many elements as possible with different values that form
consecutive members of an increasing arithmetic progression; their order
in the sequence does not matter. Print the count and the numbers of the
chosen elements in any order.

Time limit: 0.25 seconds. Memory limit: 16 MB.

## Input

N, then the N elements.

## Output

The count, then the element numbers. Any longest progression is
accepted.

## Examples

### Example 1

Input:

```
6
7 3 2 3 5 9
```

Output:

```
4
4 5 1 6
```

## Solution

Only the set of values matters, so keep each value once in a hash table
together with the number of one element holding it, and sort the
distinct values. Every progression of at least two members is fixed by
its first two members x < y, with step d = y − x. Walk it only from its
true start, that is when x − d is absent: then follow y + d, y + 2d, ...
while they are in the table.

Each pair of neighbouring members of a maximal progression lies in
exactly one walk, and each pair (x, y) costs one look-up for the start
test, so the whole search makes O(m²) look-ups for m distinct values,
with no table of pairs: memory stays O(m), which the 16 MB limit
demands. With a single distinct value the answer is one element.
`O(m²)` expected time.

Pitfalls:

- repeated values count once (tests 02, 04, 07, gen4);
- a progression through every value is the slowest case for the walks
  (gen3);
- a table of all pairs, as in the usual O(N²) dynamic programme, needs
  more memory than allowed in most languages.

## Language notes

- Python runs under PyPy and still exceeds the 0.25 s limit on the
  judge's test 28 (under CPython already on test 9); it is kept marked
  TLE: it passes all the tests here but is not claimed to be fast enough
  for every test of the judge.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1452_hashing.cpp](1452_hashing.cpp) | G++ 13.2 x64 | hashing | O(m^2) | AC | 0.093 s | 264 KB |
| [1452_hashing.go](1452_hashing.go) | Go 1.14 x64 | hashing | O(m^2) | AC | 0.125 s | 1380 KB |
| [1452_hashing.java](1452_hashing.java) | Java 1.8 | hashing | O(m^2) | AC | 0.203 s | 952 KB |
| [1452_hashing.py](1452_hashing.py) | PyPy 3.10 x64 | hashing | O(m^2) | TLE (test 28) | 0.265 s | 3224 KB |
| [1452_hashing.rs](1452_hashing.rs) | Rust 1.75 x64 | hashing | O(m^2) | AC | 0.109 s | 632 KB |
