# 1534. Football in Gondor

[Timus 1534](https://acm.timus.ru/problem.aspx?space=1&num=1534) · difficulty 585 · math

Original problem by Sergey Pupyrev, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A team played N matches, scoring K goals and conceding L in total
(0 ≤ K, L ≤ 10⁹, 1 ≤ N ≤ 10⁹). A win gives 3 points, a draw 1, a loss
0. Find the largest and the smallest number of points the team could
have.

Time limit: 1 second. Memory limit: 64 MB.

## Input

K, L and N on one line.

## Output

The largest and the smallest number of points.

## Examples

### Example 1

Input:

```
3 2 2
```

Output:

```
4 3
```

### Example 2

Input:

```
3 1 2
```

Output:

```
6 3
```

### Example 3

Input:

```
3 0 4
```

Output:

```
10 6
```

### Example 4

Input:

```
3 0 1
```

Output:

```
3 3
```

## Solution

With W wins and R losses the team has 3W + (N − W − R) = N + 2W − R
points. Split every match's goals into a part both sides scored equally
and the margin: the equal parts add up to some X ≥ 0 on both sides, the
margins of the wins to K − X and those of the losses to L − X, and each
win or loss needs a margin of at least one goal. Any X works, as the
equal part can sit in any match. So W wins and R losses are possible
exactly when

- W = R = 0 and K = L;
- R = 0, W ≥ 1 and K − L ≥ W (all of L sits in the equal part);
- W = 0, R ≥ 1 and L − K ≥ R;
- W ≥ 1, R ≥ 1, W ≤ K and R ≤ L, with W + R ≤ N in every case.

Now maximise and minimise N + 2W − R in each case: with d = K − L, no
losses give N + 2·min(d, N) at most and N + 2 (or N if d = 0) at least;
no wins give N − 1 at most and N − min(−d, N) at least; wins and losses
together give N − 1 + 2·min(K, N − 1) at most and
N + 2 − min(L, N − 1) at least, which needs K, L ≥ 1 and N ≥ 2. The
answer is the best over the cases that apply. The values reach 3·10⁹,
so 64-bit integers are needed. `O(1)`.

Pitfalls:

- the minimum may mix wins and losses: in example 1 a win and a loss
  give 3 points, fewer than a win and a draw;
- a team that conceded nothing still has at least one win, so the
  minimum is N + 2, not N (tests 03, 10);
- 1:1 in a single match can only be a draw (test 09);
- 3·10⁹ − 3 overflows 32-bit integers (test 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1534_math.cpp](1534_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB |
| [1534_math.go](1534_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1084 KB |
| [1534_math.java](1534_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1680 KB |
| [1534_math.py](1534_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 488 KB |
| [1534_math.rs](1534_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 228 KB |
