# 1041. The cheapest basis from a set of vectors

[Timus 1041](https://acm.timus.ru/problem.aspx?space=1&num=1041) · difficulty 4654 · math, greedy

Original problem by Dmitry Filimonenkov, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `M` integer vectors of dimension `N` (`3 ≤ N ≤ 50`,
`N ≤ M ≤ 2000`, coordinates at most 2000 in absolute value), each with a
price from 1 to 15000. Choose `N` linearly independent vectors with the
smallest total price. Among all cheapest choices, output the
lexicographically smallest list of their numbers in increasing order. If
no `N` of the vectors are independent, output `0`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M` and `N`, then `M` lines with the coordinates of the vectors, then `M`
lines with their prices.

## Output

The smallest total price and then the `N` numbers of the chosen vectors
in increasing order, one per line; or `0`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5 3
1 0 0
0 1 0
0 0 1
0 0 2
0 0 3
10
20
30
10
10
```

Output:

```
40
1
2
4
```

### Example 2

Input:

```
4 3
1 2 3
2 4 6
0 1 1
1 3 4
1
1
1
1
```

Output:

```
0
```

## Solution

Linearly independent sets of vectors form a matroid, and for a matroid
the greedy algorithm is optimal: go through the vectors from the cheapest
and keep a vector whenever it is independent of the vectors kept so far.
Among equal prices, go in increasing order of numbers. This also gives
the lexicographically smallest list. All cheapest bases contain a basis of
every price level `c` taken over the span of the cheaper vectors. The
choices on different levels are independent of each other, and on each
level the greedy pass in increasing order of numbers gives a basis whose
`k`-th smallest number is the smallest possible for every `k`.

The independence test is Gaussian elimination: keep the kept vectors in
echelon form (each row has a pivot coordinate equal to 1 and zero in the
pivots of the earlier rows). Reduce a candidate by every row; if anything
non-zero remains, it is independent and becomes a new row. This takes
`O(M · N^2)` operations.

Exact arithmetic matters: with floating point, nearly parallel integer
vectors can be judged wrong. The solutions compute modulo the prime
`2^31 − 1`. A set that is independent modulo a prime is independent over
the rationals (some minor is non-zero modulo the prime, hence non-zero).
The converse fails only if the prime divides every non-zero `N × N` minor,
which for these sizes and data is practically impossible. The tests were
checked with exact fractions.

Pitfalls:

- greedy by price alone is not enough: equal prices must be taken in
  increasing order of numbers for the smallest list;
- the vectors are printed in increasing order, not in the order they were
  chosen;
- when even all `M` vectors span less than `N` dimensions, the answer is
  `0`.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: 64-bit integers; products of two
  residues below `2^31` fit easily.
- **Python**: the basis is kept fully reduced (each row is zero in every
  other row's pivot). The remainder of a candidate in a free coordinate is
  then one dot product with the candidate's pivot coordinates, computed by
  `sum(map(mul, ...))`, which is fast enough in CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1041_math_greedy.cpp](1041_math_greedy.cpp) | G++ 13.2 x64 | math, greedy | O(M·N^2) | AC | 0.093 s | 760 KB |
| [1041_math_greedy.go](1041_math_greedy.go) | Go 1.14 x64 | math, greedy | O(M·N^2) | AC | 0.046 s | 3280 KB |
| [1041_math_greedy.java](1041_math_greedy.java) | Java 1.8 | math, greedy | O(M·N^2) | AC | 0.234 s | 4492 KB |
| [1041_math_greedy.py](1041_math_greedy.py) | Python 3.12 x64 | math, greedy | O(M·N^2) | AC | 0.203 s | 10176 KB |
| [1041_math_greedy.rs](1041_math_greedy.rs) | Rust 1.75 x64 | math, greedy | O(M·N^2) | AC | 0.062 s | 1640 KB |
