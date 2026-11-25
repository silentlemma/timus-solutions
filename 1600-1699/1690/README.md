# 1690. Army of Mages

[Timus 1690](https://acm.timus.ru/problem.aspx?space=1&num=1690) · difficulty 638 · constructive

Original problem by Eugene Kurpilyanskiy, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are 5n candidates living at distinct lattice points. Two mages
respect each other when the segment between their houses passes
through another lattice point. Choose n candidates who all respect one
another, or report that it is impossible.

## Input

n (1 ≤ n ≤ 5000), then the 5n houses, integers up to 10000 in absolute
value.

## Output

OK and the numbers of the chosen candidates, or IMPOSSIBLE. Any valid
army is accepted.

## Examples

### Example 1

Input:

```
2
1 1
5 5
0 0
2 2
0 10
6 6
7 7
8 8
9 9
10 10
```

Output:

```
OK
2 1
```

## Solution

The segment from (x1, y1) to (x2, y2) has a lattice point strictly
inside exactly when gcd(|x1 − x2|, |y1 − y2|) ≥ 2. In particular two
houses with the same parities of x and of y differ by even amounts, so
the midpoint of their segment is a lattice point.

There are only four parity classes, and 5n houses in four classes put
at least ⌈5n / 4⌉ ≥ n houses into one of them. So the answer is always
OK: take any n houses from the largest class. `O(n)`.

Pitfalls:

- IMPOSSIBLE never happens;
- the parity of a negative coordinate must come out as 0 or 1: −3 is
  odd, which `x & 1` gets right in two's complement while `x % 2` gives
  −1 in C-like languages (test 03).

The checker accepts any n distinct candidates who pairwise respect one
another, testing every pair unless they share a parity class. The
answers of an independent accepted implementation pass it too.

## Optimized solutions

The C++ version outputs the first parity class that reaches n houses. Among the first 4(n − 1) + 1 houses, at least one of the four classes must reach that count, so the remaining coordinates need not be read. The version uses 16-bit indices. Time and space are O(n). The metrics come from submission 11316979.

Java also stops when the first parity class reaches n houses. It parses coordinates directly from buffered input and stores candidate indices in one compact 16-bit array. Time and extra space are O(n). Metrics come from submission 11317072.

Rust also stops when the first parity class reaches n houses. It parses coordinates directly from buffered input and stores candidate indices in one compact 16-bit array. Time and extra space are O(n). Metrics come from submission 11317069.

Go also stops when the first parity class reaches n houses. It parses coordinates directly from buffered input and stores candidate indices in one compact 16-bit array. Time and extra space are O(n). Metrics come from submission 11317064.

Python also stops when the first parity class reaches n houses. It reads coordinates line by line and stores the selected indices in compact 16-bit arrays. Time and extra space are O(n). Metrics come from submission 11317060.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11317205 · Java 1.8 №11317207 · Rust 1.75 x64 №11317211.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1690_constructive.cpp](1690_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 292 KB | 11317205 |
| [1690_constructive.go](1690_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.046 s | 4436 KB | 11322031 |
| [1690_constructive.java](1690_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1832 KB | 11317207 |
| [1690_constructive.py](1690_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.125 s | 6128 KB | 11322032 |
| [1690_constructive.rs](1690_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 2116 KB | 11317211 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1690_constructive_optimized.cpp](1690_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 132 KB | 11316979 |
| [1690_constructive_optimized.py](1690_constructive_optimized.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 952 KB | 11317060 |
| [1690_constructive_optimized.go](1690_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 948 KB | 11317064 |
| [1690_constructive_optimized.rs](1690_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 248 KB | 11317069 |
| [1690_constructive_optimized.java](1690_constructive_optimized.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 744 KB | 11317072 |

\* Accepted. The Go rating target remains open. Accepted. The Java rating target remains open.
