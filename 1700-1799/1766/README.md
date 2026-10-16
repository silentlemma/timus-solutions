# 1766. Humpty Dumpty

[Timus 1766](https://acm.timus.ru/problem.aspx?space=1&num=1766) · difficulty 1373 · math

Original problem by Sergey Pupyrev (prepared by Eugene Krokhalev), from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every cell of an 8 × 8 board holds a count from 1 to 1000. A walker
moves every second to one of the up to eight cells sharing a side or a
corner with its cell, picking each with probability proportional to
that cell's count. After an enormous time (100100100 days), find the
probability of finding the walker in each cell.

## Input

Eight lines of eight counts, rank 1 first.

## Output

Eight lines of eight probabilities in the same order, with an error of
at most 10⁻¹². The answer printed in the example is deliberately too
rough.

## Examples

### Example 1

Input:

```
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
```

Output:

```
0.007 0.012 0.012 0.012 0.012 0.012 0.012 0.007
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.007 0.012 0.012 0.012 0.012 0.012 0.012 0.007
```

## Solution

Let w(u) be the count of cell u and W(u) the sum of the counts around
it. The walker goes from u to a neighbour v with probability
w(v)/W(u). Weighting each cell by π(u) = w(u)·W(u) balances every pair
of neighbours: π(u)·w(v)/W(u) = w(u)·w(v) = π(v)·w(u)/W(v). So these
weights, scaled to sum to 1, form a distribution that one step leaves
unchanged. Every cell can reach every other, and three mutually
adjacent cells make the walk aperiodic, so from any start it settles
into this one distribution, and after so long nothing else is left.
The weights are whole numbers, divided only at the end. `O(64)`.

With all counts equal, π is proportional to the number of neighbours:
3 in a corner, 5 on an edge and 8 inside, 420 in all, so a corner gets
3/420 ≈ 0.00714 and an inner cell 8/420 ≈ 0.01905.

Pitfalls:

- the starting cell does not matter, as long as the walk has settled;
- 15 digits after the point keep the error well below 10⁻¹²;
- simulating the walk step by step converges slowly when counts of 1
  and 1000 are mixed.

The checker computes the exact distribution from the input with
fractions. Solving the balance equations exactly with fractions gives
the same distribution on six random boards, and running the walk for
20000 steps agrees on boards of random counts.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1766_math.cpp](1766_math.cpp) | G++ 13.2 x64 | math | O(64) | AC | 0.015 s | 140 KB |
| [1766_math.go](1766_math.go) | Go 1.14 x64 | math | O(64) | AC | 0.031 s | 1128 KB |
| [1766_math.java](1766_math.java) | Java 1.8 | math | O(64) | AC | 0.140 s | 1944 KB |
| [1766_math.py](1766_math.py) | Python 3.12 x64 | math | O(64) | AC | 0.078 s | 504 KB |
| [1766_math.rs](1766_math.rs) | Rust 1.75 x64 | math | O(64) | AC | 0.046 s | 276 KB |
