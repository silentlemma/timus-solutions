# 1690. Army of Mages

[Timus 1690](https://acm.timus.ru/problem.aspx?space=1&num=1690) · difficulty 637 · constructive

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1690_constructive.cpp](1690_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.046 s | 304 KB |
| [1690_constructive.go](1690_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.062 s | 4412 KB |
| [1690_constructive.java](1690_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 1840 KB |
| [1690_constructive.py](1690_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 6088 KB |
| [1690_constructive.rs](1690_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 2120 KB |
