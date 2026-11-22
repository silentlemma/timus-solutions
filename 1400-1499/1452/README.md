# 1452. Pascal vs. C++

[Timus 1452](https://acm.timus.ru/problem.aspx?space=1&num=1452) · difficulty 607 · hashing

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
with no table of pairs: memory stays O(N), within the 16 MB limit.
With a single distinct value the answer is one element.
`O(N + m²)` expected time.

Pitfalls:

- repeated values count once (tests 02, 04, 07, gen4);
- a progression through every value requires a full-length walk
  (gen3);
- a table of all pairs, as in the usual O(N²) dynamic programme, needs
  more memory than allowed with some representations.

## Language notes

- Python runs on CPython and prunes the pairs. Some extreme values in
  no three-term progression are dropped first, and a pair x < y is
  walked only when a progression from x with step y − x could still beat
  the best one so far: its member at that length must be at most the
  largest value and present in the table. The earlier version that
  walked every pair exceeded the 0.25 s limit on the judge's test 9
  under CPython and on test 28 under PyPy.

## Optimized solutions

`1452_hashing_optimized.cpp`. Keep the exact open-addressing table of distinct values and their first input positions. An 8 KiB bit filter records a fingerprint bit on insertion. A zero bit proves absence and skips the table probe; a set bit may collide, so every possible hit still checks the FULL integer key in the table. Endpoint/predecessor pruning and exact progression reconstruction are unchanged. This fixed prefilter preserves the original exact progression search.

Exact-source Accepted #11326982: 0.015 s / 168 KB. Saved G++ 13.2 sample, 2026-11-20: time rank 1/51, memory rank 1/51. Teaching sources remain unchanged.

The optimized C++ version stores each distinct value and its first input index in a fixed open-addressing table. It tests a candidate difference only when the term needed to beat the current best can exist and the progression has no predecessor in the input. The answer is rebuilt from its first value and difference. The metrics come from submission 11326982.

Rust keeps values and their original indices in separate arrays, with 16-bit integers for indices. Submission 11318214 took 0.031 s and used 292 KB. The simple version took 0.093 s and used 620 KB.

Java uses a fixed-size hash table with open addressing and skips differences that cannot improve the longest progression. Submission 11318310 took 0.187 s and used 492 KB, versus 0.187 s and 924 KB for the simple version.

Go uses a fixed-size hash table with open addressing and skips differences that cannot improve the longest progression. Submission 11321984 took 0.062 s and used 864 KB, versus 0.125 s and 1376 KB for the simple version.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322326 · Go 1.14 x64 №11322327 · Java 1.8 №11322328 · Python 3.12 x64 №11322330 · Rust 1.75 x64 №11322331.

The optimized Python version uses integer bitsets for values in a dense interval. For sparse values it uses hashing to check the necessary endpoint before extending a progression. Submission 11322818 took 0.109 s and used 1884 KB, versus 0.140 s and 1608 KB for the simple version. It ranks first by both metrics in the public Python/PyPy table.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1452_hashing.cpp](1452_hashing.cpp) | G++ 13.2 x64 | hashing | O(N + m^2) | AC | 0.093 s | 248 KB | 11322326 |
| [1452_hashing.go](1452_hashing.go) | Go 1.14 x64 | hashing | O(N + m^2) | AC | 0.125 s | 1376 KB | 11322327 |
| [1452_hashing.java](1452_hashing.java) | Java 1.8 | hashing | O(N + m^2) | AC | 0.187 s | 924 KB | 11322328 |
| [1452_hashing.py](1452_hashing.py) | Python 3.12 x64 | hashing | O(N + m^2) | AC | 0.14 s | 1608 KB | 11322330 |
| [1452_hashing.rs](1452_hashing.rs) | Rust 1.75 x64 | hashing | O(N + m^2) | AC | 0.093 s | 620 KB | 11322331 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1452_hashing_optimized.cpp](1452_hashing_optimized.cpp) | G++ 13.2 x64 | hashing | O(N + m^2) | AC | 0.015 s | 168 KB | 11326982 |
| [1452_hashing_optimized.rs](1452_hashing_optimized.rs) \* | Rust 1.75 x64 | hashing | O(N + m^2) | AC | 0.031 s | 292 KB | 11318214 |
| [1452_hashing_optimized.go](1452_hashing_optimized.go) \* | Go 1.14 x64 | hashing | O(N + m^2) | AC | 0.062 s | 864 KB | 11321984 |
| [1452_hashing_optimized.java](1452_hashing_optimized.java) \* | Java 1.8 | hashing | O(N + m^2) | AC | 0.187 s | 492 KB | 11318310 |
| [1452_bitmask_hashing.py](1452_bitmask_hashing.py) | Python 3.12 x64 | bitmask, hashing | O(N + m^2) | AC | 0.109 s | 1884 KB | 11322818 |

\* Accepted. The C++ rating target remains open. The Rust rating target remains open. The Go rating target remains open. The Java rating target remains open.
