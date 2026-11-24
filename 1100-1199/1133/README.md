# 1133. Finding a term of a Fibonacci-like sequence from two other terms

[Timus 1133](https://acm.timus.ru/problem.aspx?space=1&num=1133) · difficulty 225 · number_theory

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An integer sequence, infinite both ways, satisfies
`F(k + 2) = F(k + 1) + F(k)` for every `k`. Given `F(i)` and `F(j)` for
`i ≠ j`, find `F(n)`. All indices are in `[−1000, 1000]`, and every term
from the smallest to the largest of `i, j, n` is within `±2·10⁹`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Five integers: `i`, `F(i)`, `j`, `F(j)`, `n`.

## Output

`F(n)`.

## Checking

The answer is compared as one integer token. The actual new Python
source matched an independent forward/backward integer recurrence on
2500 generated valid queries and 100 all-zero queries, including reversed,
negative and outside indices and the full 2000-index span. Both actual
new programs separately passed all 13 repository inputs in Docker and
have exact-source Accepted receipts. The 2600 differential checks are
Python executions, not 2600 Java executions.

## Examples

### Example 1

Input:

```
3 5 -1 4 5
```

Output:

```
12
```

## Solution

Put the known terms in index order, `i < j`, and let `D=j−i`.
Let `H(0)=0, H(1)=1` be ordinary Fibonacci numbers. Repeated substitution
gives `F(j)=H(D−1)·F(i)+H(D)·F(i+1)`. Since `D≥1`, `H(D)>0`:
the next term is uniquely determined by exact integer division. Walk
forward using addition, or backward using `F(k−1)=F(k+1)−F(k)`, to reach
the requested index. This proves both existence-based reconstruction and
the returned value's uniqueness.

The new Python, Go and Java `math` files use arbitrary-precision integers
directly. They need no chosen prime, modular inverse, or proof that a
denominator is invertible. This is the preferred teaching version in
these three languages. If `W=max(i,j,n)−min(i,j,n)`, there are `O(W)`
big-integer operations; coefficients have `O(W)` bits. A conservative
bit-time bound is `O(W²)`, with `O(W)` auxiliary live bits under the fixed
input-value bound. It is not a constant-cost `O(W)` integer algorithm.

The retained fixed-width `number_theory` files compute the same expression
modulo the prime `P=4294967291`. It exceeds the `4·10⁹+1` possible answers;
the representative above `P/2` denotes a negative result. Every relevant
Fibonacci denominator, with index 1 through 2000, is nonzero modulo `P`
(checked by exact recurrence), so Fermat inversion is valid. Products fit
unsigned 64 bits. This gives `O(W)` fixed-width time and constant numeric
storage, and avoids external big-integer libraries in C++ and Rust.

Read all five values as whitespace-separated tokens. Indices can be
reversed, negative, adjacent, or outside the two given positions; leading
zeros and negative terms cause no special arithmetic case. The all-zero
sequence remains valid even at the most distant indices. Exact arithmetic
and the modular implementations were compared on independent recurrences,
including long zero ranges and queries outside the given interval.

## Optimized solutions

`1133_number_theory_optimized.rs`. Keep the identical modular Fibonacci reconstruction: step coefficients from i to j, invert modulo P=4294967291, then step forward or backward to n and decode the signed answer. Only the five-integer input path and direct output change; recurrence, modular inverse and overflow-safe u64 products are unchanged. Time O(|j-i|+|n-i|+log P), O(1) auxiliary storage. The measured memory gain is not a different asymptotic algorithm.

Compared with `1133_number_theory.rs`: time 0.015 s → 0.031 s; memory 220 KB → 52 KB.

The unchanged Go modular source is a different, optimized algorithm relative
to the preferred direct big-integer Go base: 1064 KB instead of 1544 KB,
31.1% less memory. Its 0.015 s versus 0.031 s is only one timer tick;
we do not claim a reliable speedup. The earlier modular Java/Python
sources remain accepted mathematical alternatives, without an optimized label.

The new Java and Python `math_optimized` sources keep the direct exact
arithmetic algorithm and add a proven early exit. If both given terms
are zero, the reconstruction identity has `H(D) > 0`, so the adjacent
unknown term must also be zero. Addition forward and subtraction backward
then force the entire sequence to zero. We may return before constructing
large Fibonacci coefficients. For other inputs, the algorithm is unchanged:
`O(W²)` conservative bit time and `O(W)` live bits; the zero case has
constant arithmetic work. This is an implementation shortcut, not a
table of answers or a change to the recurrence.

Compare against the preferred `math` bases, not the former modular files.
Java Accepted uses 536 KB versus 828 KB, 35.3% less; 0.093 s versus
0.109 s is one tick, not reliable speedup evidence. Python is explicitly
PyPy 3.10: 256 KB versus the CPython base's 436 KB, 41.3% less, but
0.140 s versus 0.078 s, 79.5% more recorded time. The comparison is within
the agreed Python language family and includes the interpreter change;
it does not isolate the shortcut's effect. Both versions qualify by
judge-reported memory. Keep the clearer direct versions for learning.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1133_number_theory_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1133_number_theory.cpp](1133_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(W) | AC | 0.015 s | 128 KB | 11279389 |
| [1133_math.go](1133_math.go) | Go 1.14 x64 | math | O(W²) bit time | AC | 0.031 s | 1544 KB | 11308040 |
| [1133_math.java](1133_math.java) | Java 1.8 | math | O(W²) bit time | AC | 0.109 s | 828 KB | 11308043 |
| [1133_math.py](1133_math.py) | Python 3.12 x64 | math | O(W²) bit time | AC | 0.078 s | 436 KB | 11308038 |
| [1133_number_theory.rs](1133_number_theory.rs) | Rust 1.75 x64 | number_theory | O(W) | AC | 0.015 s | 220 KB | 11279395 |
| [1133_number_theory.java](1133_number_theory.java) | Java 1.8 | number_theory | O(W) | AC | 0.156 s | 1688 KB | 11279393 |
| [1133_number_theory.py](1133_number_theory.py) | Python 3.12 x64 | number_theory | O(W) | AC | 0.078 s | 480 KB | 11297961 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1133_number_theory.go](1133_number_theory.go) | Go 1.14 x64 | number_theory | O(W) | AC | 0.015 s | 1064 KB | 11279391 |
| [1133_math_optimized.java](1133_math_optimized.java) | Java 1.8 | math | O(W²) bit time | AC | 0.093 s | 536 KB | 11308413 |
| [1133_math_optimized.py](1133_math_optimized.py) \* | PyPy 3.10 x64 | math | O(W²) bit time | AC | 0.140 s | 256 KB | 11308412 |
| [1133_number_theory_optimized.rs](1133_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(abs(j-i)+abs(n-i)+log P) time; O(1) space | AC | 0.031 s | 52 KB | 11325541 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
