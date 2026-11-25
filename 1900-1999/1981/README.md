# 1981. Counting diagonals by direction

[Timus 1981](https://acm.timus.ru/problem.aspx?space=1&num=1981) · difficulty 444 · math, combinatorics

Original problem by Grigory Nazarov, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For a regular `n`-gon, count the diagonals that have at least one other
parallel diagonal, and independently count the diagonals that have at
least one perpendicular diagonal. A diagonal joins two nonadjacent
vertices. Count qualifying diagonals, rather than pairs; one diagonal
may belong to both answers.

The integer size satisfies `4≤n≤100000`. Time limit: 0.5 seconds; memory
limit: 64 MB.

## Input

One integer `n`.

## Output

Two integer counts: parallel first, perpendicular second.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
4
```

Output:

```
0 2
```

## Solution

Number vertices `0,…,n−1` in circular order. A chord joining `i,j` has
direction angle `π(i+j)/n+π/2`, modulo `π`. Thus its unoriented
direction class is `r=(i+j) mod n`.

First count diagonals in each class. For odd `n`, the equation `i+j≡r`
gives `(n−1)/2` unordered distinct-vertex pairs: one of the `n` ordered
solutions is a repeated vertex. Exactly one pair is a side. Every class
therefore contains `d=(n−3)/2` diagonals. If `d≥2`, all `n d` qualify as
parallel; otherwise none do.

For even `n`, put `h=n/2`. There are `h` classes of each parity. An even
class has two repeated-vertex ordered solutions and no sides, so its
diagonal count is `h−1`. An odd class has no repeated-vertex solution
but contains two sides, so its count is `h−2`. For each class size `d`,
contribute `d` when `d≥2` and zero otherwise, then multiply the sum for
the two parities by `h`. This handles the small polygons directly from
class sizes.

Perpendicular direction classes differ by `n/2`. This is impossible when
`n` is odd, so the second answer is zero. When `n` is even and `h` is
even, the partner class has the same parity and the same positive size
as the original. When `h` is odd, `h≥3`, and both class sizes are
positive. Hence every diagonal has a perpendicular partner for even `n`,
giving the total `n(n−3)/2`.

The direction identity partitions every diagonal exactly once. The
class-size condition is equivalent to having a distinct parallel
partner, and the shift by `n/2` classes characterizes perpendicular
partners. These facts prove both counts.

For the square in the example, each of the two diagonal directions
contains one diagonal, so neither has a parallel partner. The two
directions are perpendicular, giving answers `0 2`.

All expressions take `O(1)` time and `O(1)` additional memory. Use
64-bit integer arithmetic: the maximum answer is `4,999,850,000`, which
exceeds even an unsigned 32-bit integer.

Pitfalls:

- A direction class of size one contributes no parallel diagonal.
- Exclude polygon sides and repeated endpoints when counting chord classes.
- Directions are taken modulo `π`, so opposite orientations are the same class.
- The requested counts concern diagonals, not unordered pairs of diagonals.
- Promote before multiplying; intermediate products also exceed 32 bits.

## Optimized solutions

The new C++, Go and Rust sources keep exactly the same direction-class formulas and 64-bit products as the simple versions. Only input/output storage changes: C++ uses C stdio, Go bounded buffers and standard handles, and Rust bounded digit storage with a C entry point and C-runtime character I/O. These are constant-factor and memory changes, not a faster asymptotic algorithm. The five simple sources remain unchanged; Java reuses its admitted base in the fast set.

The accepted G++ 13.2 x64 run takes 0.031 s versus 0.015 s for the base and uses 108 KB versus 440 KB.

In the earlier comparison snapshot, the base implementations [1981_math.java](1981_math.java), [1981_math.py](1981_math.py) met the top-15% or top-ten admission rule on both metrics. Their measured results are kept in the Simple table.

## Language notes

These notes describe the simple implementations.

Python uses exact integers. C++, Go and Java use signed 64-bit values
throughout the formulas; Rust uses `u64`. No trigonometry is used in the
submitted programs.

Read the value directly as bytes and evaluate the two counting formulas from its parity and half. Accepted submission 11324245 took 0.062 s and used 504 KB. The simple version took 0.093 s and used 460 KB. The recorded memory use is higher than for the simple version.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1981_math.cpp](1981_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 440 KB | 11292331 |
| [1981_math.go](1981_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB | 11292332 |
| [1981_math.java](1981_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 376 KB | 11329297 |
| [1981_math.py](1981_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 460 KB | 11292333 |
| [1981_math.rs](1981_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB | 11292335 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1981_math_optimized.cpp](1981_math_optimized.cpp) \* | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 108 KB | 11315134 |
| [1981_math_optimized.go](1981_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 332 KB | 11315136 |
| [1981_math_optimized.rs](1981_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11315137 |
| [1981_math_optimized.py](1981_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 504 KB | 11324245 |

\* Accepted; the rating target is not yet met. This version may be optimized further.

**Current measurements.** The solution tables record the exact preserved sources and their latest Accepted runs. Earlier performance comparisons describe historical runs; current admission follows the shared [rating criteria](../../RATING_CRITERIA.md).
