# 1172. Counting round trips through three islands by ship only

[Timus 1172](https://acm.timus.ru/problem.aspx?space=1&num=1172) · difficulty 548 · combinatorics

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three islands have `N ≤ 30` cities each. Ships connect every two cities
on different islands, and there is no travel within an island. Starting
from a given city, count the round trips that visit every other city
exactly once and return; a trip and the same trip read backwards count
once.

Time limit: 1 second. Memory limit: 16 MB.

## Input

`N`.

## Output

The number of trips, with up to 121 digits.

## Examples

### Example 1

Input:

```
2
```

Output:

```
16
```

## Solution

Split a trip into its pattern of islands and the choice of cities. The
pattern is a cyclic sequence of `3N` island labels, starting with the
tourist's island, with `N` of each label and no two neighbours equal,
including the last and the first. For a fixed pattern, the other `N − 1`
cities of the home island fill its slots in `(N − 1)!` ways and each other
island in `N!` ways. Reading a trip backwards gives a different sequence
from the same start (the trip has at least three cities), so the total is
halved.

Patterns are counted with `ways[a][b][c][i]`: sequences that start on
island 0, use `a`, `b` and `c` slots of the three islands and end on island
`i`. Each value is the sum of two values for one fewer slot of island `i`,
ending elsewhere. The answer counts the full sequences that do not end on
island 0. Only two planes of fixed `a` are kept, which keeps the big
numbers few. `O(N³)` big-number additions.

Pitfalls:

- the cycle also forbids the last city being on the home island;
- the starting city is fixed, so the home island contributes `(N − 1)!`,
  not `N!`;
- the full table for `N = 30` would hold about 90,000 big numbers, while
  two planes need only about 6,000.

The answers were compared with a brute force over all orders for
`N ≤ 3` and with a separately written solution for every `N` up to 30.

The teaching Python version builds island patterns one position at a time. A dictionary counts prefixes by the three used counts and the last island. To extend a prefix, choose any different island with a free slot and add its count to the next layer. Only the current and next lengths are kept. At full length discard prefixes ending at home, then assign the labelled cities and divide by two. There are O(N²) states per length because the three counts sum to that length, so the DP takes O(N³) big-integer additions and O(N²) counters.

## Optimized solutions

The Go version keeps the same two-plane DP but stores pattern counts in three base-10⁹ limbs rather than allocating math/big objects for every cell. After fixing the starting island, a walk of at most 90 positions has at most 2⁸⁹ possible island words; this is below 10²⁷, so three limbs suffice even for intermediate counts. The two fixed planes occupy 69192 bytes of digit storage. The final factorial multiplications use fourteen limbs: 126 decimal digits cover the at-most-122-digit value before halving. Each small multiplier is at most 30²·29, so 64-bit products and carries suffice. All values are computed; there is no answer table. Time remains O(N³) fixed-limb additions. Standard handles replace fmt I/O, while the ordinary math/big base and the other four accepted language versions are preserved.

The accepted base implementations [1172_combinatorics.cpp](1172_combinatorics.cpp), [1172_combinatorics.java](1172_combinatorics.java), [1172_combinatorics.py](1172_combinatorics.py), [1172_combinatorics.rs](1172_combinatorics.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- Python, Go and Java use their big integers; C++ and Rust keep numbers
  as arrays of base-10⁹ digits with addition, multiplication by a small
  number and halving.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1172_combinatorics.cpp](1172_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 376 KB | 11283141 |
| [1172_combinatorics.go](1172_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 6024 KB | 11283143 |
| [1172_combinatorics.java](1172_combinatorics.java) | Java 1.8 | combinatorics | O(N³) big additions | AC | 0.125 s | 4580 KB | 11283148 |
| [1172_combinatorics.py](1172_combinatorics.py) \* | Python 3.12 x64 | combinatorics | O(N³) big additions | AC | 0.093 s | 884 KB | 11283145 |
| [1172_combinatorics.rs](1172_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N³) big additions | AC | 0.031 s | 568 KB | 11283151 |
| [1172_dp.py](1172_dp.py) | Python 3.12 x64 | dp | O(N³) big additions | AC | 0.14 s | 920 KB | 11315936 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1172_combinatorics_optimized.go](1172_combinatorics_optimized.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 404 KB | 11314877 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
