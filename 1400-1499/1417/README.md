# 1417. Space Poker

[Timus 1417](https://acm.timus.ru/problem.aspx?space=1&num=1417) · difficulty 1884 · math

Original problem by Stanislav Vasiliev, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A player and a croupier each show from 1 to N fingers (1 < N ≤ 100).
An N × N table gives the player's prize for every pair: 1000 on the
diagonal, where the counts match, and a whole number from 0 to 10
elsewhere. The player pays 20 per round; the casino seeks maximum
expected profit against an optimal player. Find the probabilities with
which the croupier should show each count so that the player's expected
prize does not depend on the count the player shows. Print them with 5
digits after the point.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then the table: row i for the player's count i, column j for the
croupier's count j.

## Output

N probabilities, one per line.

## Examples

### Example 1

Input:

```
3
1000 10 10
0 1000 1
5 3 1000
```

Output:

```
0.32986
0.33623
0.33391
```

## Solution

With probabilities p the player showing i expects Σⱼ A[i][j]·pⱼ, and
these must all equal one value v. Solve A·x = (1, …, 1) by Gaussian
elimination with partial pivoting; then p = x / Σx and v = 1 / Σx.

The diagonal of 1000 outweighs the rest of its row (at most 99 · 10 =
990), so A is not singular. The map Fᵢ(x) = (1 − Σⱼ≠ᵢ A[i][j]·xⱼ) / 1000
preserves [10⁻⁵, 10⁻³]ᴺ and contracts by at most 0.99, so its fixed point
x is positive. Thus the answer always exists with positive probabilities.
`O(N³)`.

Pitfalls:

- rows belong to the player and columns to the croupier, so the system
  is A·p = v·1, not its transpose (tests 03, 05);
- equal consolation prizes everywhere give equal probabilities (tests
  02, 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1417_math.cpp](1417_math.cpp) | G++ 13.2 x64 | math | O(N^3) | AC | 0.015 s | 308 KB |
| [1417_math.go](1417_math.go) | Go 1.14 x64 | math | O(N^3) | AC | 0.031 s | 1240 KB |
| [1417_math.java](1417_math.java) | Java 1.8 | math | O(N^3) | AC | 0.125 s | 1208 KB |
| [1417_math.py](1417_math.py) | Python 3.12 x64 | math | O(N^3) | AC | 0.140 s | 1732 KB |
| [1417_math.rs](1417_math.rs) | Rust 1.75 x64 | math | O(N^3) | AC | 0.031 s | 420 KB |
