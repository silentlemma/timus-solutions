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
win or loss needs a margin of at least one goal. The equal part can sit
in any match. So W wins and R losses are possible
exactly when

- W = R = 0 and K = L;
- R = 0, W ≥ 1 and K − L ≥ W (all of L sits in the equal part);
- W = 0, R ≥ 1 and L − K ≥ R;
- W ≥ 1, R ≥ 1, W ≤ K and R ≤ L, with W + R ≤ N in every case.

Now maximise and minimise N + 2W − R in each case: with d = K − L, no
losses give N + 2·min(d, N) at most and N + 2 (or N if d = 0) at least;
for d < 0, no wins give N − 1 at most and N − min(−d, N) at least;
wins and losses together give N − 1 + 2·min(K, N − 1) at most and
N + 2 − min(L, N − 1) at least, which needs K, L ≥ 1 and N ≥ 2. The
answer is the best over the cases that apply. The values reach 3·10⁹,
so 64-bit integers are needed. `O(1)`.

Pitfalls:

- the minimum may mix wins and losses: in example 1 a win and a loss
  give 3 points, fewer than a win and a draw;
- a team that scored but conceded nothing has at least one win, so the
  minimum is N + 2, not N (tests 03, 10);
- 1:1 in a single match can only be a draw (test 09);
- 3·10⁹ − 3 overflows 32-bit integers (test 06).

## Optimized solutions

Java reads the three integers into a fixed-size buffer and uses the same point formulas. Submission 11318275 took 0.109 s and used 480 KB.

Rust evaluates the score bounds directly and writes the two integers into a fixed buffer. Rust 1.75 x64, submission 11323307. Time 0.031 → 0.046 s, memory 216 → 48 KB.

Python computes the minimum and maximum points directly. When both teams scored, it also considers reserving one match for the opposite outcome. Python 3.12 x64, submission 11320787. Time 0.093 → 0.093 s, memory 488 → 484 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321851 · Go 1.14 x64 №11322271 · Java 1.8 №11322272 · Python 3.12 x64 №11322274 · Rust 1.75 x64 №11322276.

Go reads the three integers into a fixed buffer and writes both point totals in one call. Go 1.14 x64, submission 11322414. Time 0.031 → 0.046 s, memory 1152 → 796 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1534_math.cpp](1534_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 388 KB | 11321851 |
| [1534_math.go](1534_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1152 KB | 11322271 |
| [1534_math.java](1534_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1656 KB | 11322272 |
| [1534_math.py](1534_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.109 s | 456 KB | 11322274 |
| [1534_math.rs](1534_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 216 KB | 11322276 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1534_math_optimized.java](1534_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 480 KB | 11318275 |
| [1534_math_optimized.rs](1534_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 48 KB | 11323307 |
| [1534_math_optimized.py](1534_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 484 KB | 11320787 |
| [1534_math_optimized.go](1534_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 796 KB | 11322414 |

\* The marked versions have room to improve in the ratings.
