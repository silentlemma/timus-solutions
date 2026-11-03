# 1200. How many horns and hooves to make

[Timus 1200](https://acm.timus.ru/problem.aspx?space=1&num=1200) · difficulty 257 · math

Original problem by Magaz Asanov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each horn earns `A` roubles and each hoof `B` roubles, with
`-10000 ≤ A, B ≤ 10000` given to two decimals. At most `K ≤ 10000` items
in total can be sold, and racketeers take the square of the number of
items of each kind. Choose `x` horns and `y` hooves with `x + y ≤ K` to
maximise `A·x + B·y − x² − y²`; among the best plans take the fewest
horns, then the fewest hooves.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`A` and `B`, then `K`.

## Output

The best profit to two decimals, then `x` and `y`.

## Examples

### Example 1

Input:

```
34.20 61.70
45
```

Output:

```
1239.50
16 29
```

## Solution

Convert the two prices to integer kopecks `a,b`. The objective is
`P(x,y)=a·x+b·y−100(x²+y²)`, with integer `x,y≥0` and `x+y≤K`.
Producing nothing is allowed, so the optimum is nonnegative.

The simple algorithm enumerates horns `x=0..K`. For fixed `x`, the hoof
profit is a concave parabola with real peak `b/200`, restricted to
`0≤y≤K−x`. Test the two neighboring integers after clamping to that range;
if the peak is negative, the best is zero. Every feasible `x` is examined
and its best `y` included, proving the global optimum. Visit `x` and the
two `y` candidates in increasing order and update only on strictly greater
profit: equal profit keeps fewer horns, then fewer hooves. All five
Accepted scans preserve this tie rule. Time `O(K)`, constant-size working
state apart from bounded input/output.

Exact cent scores avoid floating-point comparisons of profits. Existing
bases round each parsed two-decimal price times 100 to an integer. At
`|A|,|B|≤10000`, binary floating error is far below half a kopeck, so
that initial cent conversion is safe. Later calculations are integral.
For `K≤10000`, absolute intermediate expressions are at most `2·10¹⁰`,
and the maximum profit is at most `5·10⁹` kopecks; use signed 64-bit
arithmetic in native languages, not 32-bit scores.

## Optimized solutions

The profit is a separable concave quadratic on an integer triangle. An interior optimum rounds both independent peaks; if those choices violate capacity, an optimum lies on an edge. Substituting the capacity equality gives a one-variable concave quadratic, so its neighboring integers and endpoints suffice. The Java version explicitly checks this constant candidate set; Python performs the equivalent tie-aware projection directly. Scores are exact integer kopecks, with ties resolved by fewer horns and then fewer hooves. This replaces the linear scan with a different constant-size geometric algorithm.

- `1200_math_geometry.java`: 0.109 s / 868 KB; base `1200_math.java`: 0.140 s / 2096 KB; relative change: time -22.1%, memory -58.6%.
- `1200_math_geometry.py`: 0.125 s / 284 KB; base `1200_math.py`: 0.093 s / 488 KB; relative change: time +34.4%, memory -41.8%.

## Checking

Compare the profit in exact kopecks and both production counts;
the lexicographic tie rule matters. The actual Java candidate passed
13 repository inputs in Docker and obtained an exact-source Accepted.
The constant-candidate method's Python implementation was independently
checked against every integer point on 8400 valid small triangles, plus
400 zero-capacity extension cases outside the stated `K≥1` input range.
These 8800 total checks were Python executions, not 8800 Java runs. Useful cases
include both prices negative, zero production, unused capacity, a tight
diagonal, and half-integer peaks giving equal profits.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1200_math.cpp`; covering source `1200_math.cpp`; time/memory places 1/2, other-author entries 54/54.

- Go: preferred teaching base `1200_math.go`; covering source `1200_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1200_math.java`; covering source `1200_math_geometry.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1200_math.py`; covering source `1200_math_geometry.py`; time/memory places 8/1, other-author entries 12/12.

- Rust: preferred teaching base `1200_math.rs`; covering source `1200_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1200_math.cpp](1200_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 156 KB | 11283537 |
| [1200_math.go](1200_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.031 s | 1096 KB | 11283538 |
| [1200_math.java](1200_math.java) | Java 1.8 | math | O(K) | AC | 0.140 s | 2096 KB | 11283540 |
| [1200_math.py](1200_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.093 s | 488 KB | 11283539 |
| [1200_math.rs](1200_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 260 KB | 11283542 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1200_math_geometry.java](1200_math_geometry.java) | Java 1.8 | math, geometry | O(1) | AC | 0.109 s | 868 KB | 11308035 |
| [1200_math_geometry.py](1200_math_geometry.py) \* | PyPy 3.10 x64 | math, geometry | O(1) | AC | 0.125 s | 284 KB | 11309374 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
