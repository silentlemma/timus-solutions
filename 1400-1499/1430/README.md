# 1430. Crime and Punishment

[Timus 1430](https://acm.timus.ru/problem.aspx?space=1&num=1430) · difficulty 461 · number_theory

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Goods cost A or B each, any number of each can be bought, and there are
N to spend (1 ≤ A, B, N ≤ 2·10⁹). Find counts x and y with
x·A + y·B ≤ N as large as possible; any best pair will do.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

A, B and N.

## Output

x and y.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. Output two nonnegative counts in the original price order. Their cost must not exceed N and must equal the maximum achievable spend; any tied optimal pair is valid.

## Examples

### Example 1

Input:

```
8 5 22
```

Output:

```
2 1
```

## Solution

Let A ≥ B (otherwise swap them and swap the answer back). If x ≥ B,
then B goods at A can be traded for A goods at B at the same total, so
some best answer has x < B; and x·A ≤ N gives x ≤ N / A. So x runs from
0 to min(N / A, B − 1), and for each x the rest buys y = (N − x·A) / B
goods at B. Since A ≥ B, either B ≤ √N or N / A < √N, so there are at
most about 44 722 values of x; the loop also stops as soon as all N is
spent. `O(√N)`.

Pitfalls:

- products like x·A fit in signed 32 bits (tests 03, 06);
- if both prices exceed N, nothing is bought (test 12);
- the answer is not unique, so the tests use a checker (test 02).

## Optimized solutions

The new C++, Go and Rust versions preserve the bounded purchase enumeration. After ordering A≥B, let g=gcd(A,B). Exchanging B/g items of price A for A/g items of price B preserves cost, so it suffices to test 0≤x≤min(floor(N/A),B/g−1). For each x the unspent amount is r=(N−xA) mod B. Initialize N mod B and update by subtracting A mod B, adding B only on underflow; no division occurs inside the loop. Keep the smallest remainder and recover y once at the end. Every achievable cost is a multiple of g, so N mod g is a proven lower bound on the remainder and permits early exit. The worst-case enumeration remains O(√N), plus the Euclidean gcd; this is an arithmetic/constant-factor improvement. Bounded Go handle I/O and Rust C-runtime I/O also reduce runtime storage. All simple sources remain; Java/Python reuse admitted bases.

The accepted base implementations [1430_number_theory.java](1430_number_theory.java), [1430_number_theory.py](1430_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1430_number_theory_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1430_number_theory.java`: time 0.109 s → 0.109 s; memory 1684 KB → 492 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1430_number_theory.cpp](1430_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 128 KB | 11286201 |
| [1430_number_theory.go](1430_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 1068 KB | 11286202 |
| [1430_number_theory.java](1430_number_theory.java) \* | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 1684 KB | 11286204 |
| [1430_number_theory.py](1430_number_theory.py) \* | Python 3.12 x64 | number_theory | O(sqrt N) | AC | 0.109 s | 468 KB | 11286203 |
| [1430_number_theory.rs](1430_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N) | AC | 0.062 s | 220 KB | 11286205 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1430_number_theory_optimized.cpp](1430_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.015 s | 108 KB | 11315180 |
| [1430_number_theory_optimized.go](1430_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.031 s | 292 KB | 11315184 |
| [1430_number_theory_optimized.rs](1430_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.046 s | 56 KB | 11315187 |
| [1430_number_theory_optimized.java](1430_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 492 KB | 11324975 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
