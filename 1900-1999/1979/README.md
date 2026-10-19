# 1979. Resource labels with equal cube cycles

[Timus 1979](https://acm.timus.ru/problem.aspx?space=1&num=1979) · difficulty 1360 · constructive

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each face of a cube is divided into an `n×n` grid. A path entering a
cell must leave through its opposite edge, and may not pass through a
grid vertex. Such a closed path visits `4n` cells. Place every integer
from `1` to `6n²` exactly once on the cells so that the sum along any
complete path is the same, for every starting cell and direction.

The size satisfies `1≤n≤100`. Time limit: 1 second; memory limit: 64 MB.

## Input

A single integer `n`.

## Output

Print a T-shaped cube net with face names arranged as below. The first
`n` rows contain `n` labels each for `U`; the next `n` rows contain `4n`
labels each for `A,B,C,D`; the final `n` rows contain `n` labels each
for `V`.

```text
U
A B C D
V
```

## Checking

A checker verifies the rows and the permutation and follows every closed
path on the folded cube; any valid layout is accepted.

## Examples

Input:

```
2
```

Output:

```
20 13
11 8
3 15 19 4 12 24 18 5
1 7 9 23 21 17 6 16
10 22
14 2
```

## Solution

Let `a=n²` and `M=6a+1`. Number three faces with the lower half of the
labels in row-major order. For zero-based indices `r,c`, write
`A(r,c)=rn+c+1`, `B(r,c)=a+rn+c+1`, and `U(r,c)=2a+rn+c+1`.

Fill their opposite faces with complements. In the displayed net,
opposite faces `A,C` and `B,D` have reversed columns, while `U,V` have
reversed rows. Thus set `C(r,c)=M−A(r,n−1−c)`, `D(r,c)=M−B(r,n−1−c)`,
and `V(r,c)=M−U(n−1−r,c)`.

The first three faces use exactly `1,…,3a`. Their complements use
exactly `3a+1,…,6a`, so all required labels occur once.

To prove the cycle property, view a cell by its physical coordinates on
the cube. Continuing through opposite edges preserves one tangential
coordinate; the path follows a belt across four faces. Opposite faces in
that belt contain matching strips. The chosen row and column reversals
pair cells that have the same tangential coordinates under reflection
through the cube's middle plane. Each pair sums to `M`. A belt has `2n`
such pairs, giving the common sum `2nM`. This works for odd and even
sizes, including `n=1`.

In the sample, `n=2`, so the common sum is `4·25=100`. For example, the
first row of the middle band is one eight-cell belt and sums to 100.
Other directions have the same total.

All labels are computed directly from their output positions. Time is
`O(n²)`, optimal for printing `6n²` numbers. Additional working memory
is `O(n)` or less.

Pitfalls:

- Opposite faces in this net need a reversal: columns for `A,C` and
  `B,D`, rows for `U,V`.
- Pair by reflection in the middle plane; a central antipodal map
  changes the fixed belt coordinate.
- The middle band contains four faces on each row, while the upper and
  lower bands contain one.
- Resources on a starting cell are counted once per complete cycle.

## Language notes

All versions use the same direct formulas. Python builds one row at a
time, and Java writes one row through a buffered writer. C++, Go and
Rust stream the labels with buffered output.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1979_constructive.cpp](1979_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 424 KB |
| [1979_constructive.go](1979_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 1372 KB |
| [1979_constructive.java](1979_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.125 s | 3008 KB |
| [1979_constructive.py](1979_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.125 s | 564 KB |
| [1979_constructive.rs](1979_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.062 s | 244 KB |
