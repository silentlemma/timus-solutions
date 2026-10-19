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

## Language notes

Python uses exact integers. C++, Go and Java use signed 64-bit values
throughout the formulas; Rust uses `u64`. No trigonometry is used in the
submitted programs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1981_math.cpp](1981_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 440 KB |
| [1981_math.go](1981_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB |
| [1981_math.java](1981_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 448 KB |
| [1981_math.py](1981_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 460 KB |
| [1981_math.rs](1981_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB |
