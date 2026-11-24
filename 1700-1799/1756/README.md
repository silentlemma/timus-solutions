# 1756. One and a Half Diggers

[Timus 1756](https://acm.timus.ru/problem.aspx?space=1&num=1756) · difficulty 179 · math

Original problem by Magaz Asanov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

m diggers dig a trench in exactly d₁ days, all working every day. Plan
how many diggers work on each of d₂ days so that the same trench is
dug in exactly d₂ days with as few diggers hired as possible. A day
with nobody working is allowed.

## Input

m, d₁ and d₂ (1 ≤ m, d₁, d₂ ≤ 10000).

## Output

d₂ numbers: the diggers working on each day. Any best plan is
accepted.

## Examples

### Example 1

Input:

```
3 1 2
```

Output:

```
1 2
```

## Solution

The trench takes W = m·d₁ digger-days. The number of diggers to hire
is the largest daily number, and d₂ days with at most k diggers each
give at most k·d₂ digger-days, so at least ⌈W / d₂⌉ diggers are
needed. That many are enough: with W = q·d₂ + r, put q diggers on
d₂ − r days and q + 1 on the other r. `O(d₂)`.

In the example W = 3 over 2 days: one day with 1 digger and one with 2,
so two diggers are hired, not one and a half.

Pitfalls:

- m·d₁ reaches 10⁸, which is fine in 32 bits but worth noticing;
- when W < d₂ some days have nobody working;
- the daily numbers must add up to W exactly, not just reach it.

The plans pass a checker that tests the sum and the busiest day, on
small, random and near-limit inputs; an independent accepted
implementation prints the same days in another order.

## Optimized solutions

`1756_math_optimized.java`. Java keeps the optimal balanced-day plan: total=m*d1, low=total/d2 and extra=total%d2. Emit d2-extra days with low workers and extra days with low+1, reaching the minimum possible peak ceil(total/d2). Zero-worker days remain valid. Convert each of the two numbers to decimal bytes once; a reusable block of at most 16384 bytes repeats space-number groups instead of building the whole output line or writing each day separately. Zero-length runs are skipped without changing the first-number state. Time O(d2) for the bounded digits, auxiliary space fixed. The teaching construction is unchanged.

Exact-source Java 1.8 Accepted #11327526: 0.093 s / 444 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/54, memory 1/54. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11307303 was 0.171 s / 456 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1756_math_optimized.java`: 0.093 s / 444 KB; retained teaching base `1756_math.java`: 0.125 s / 2020 KB.

The optimized Python solution formats the two possible daily numbers
once and builds the line by repeating the two strings, instead of making
a list of up to 10000 integers and converting each of them to a string:
{1756_math_optimized.py}.

The optimized Rust solution formats the two possible daily numbers once
and writes them straight to a `BufWriter`, instead of making up to
10000 strings and joining them into one more: {1756_math_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1756_math_optimized.py`: time reduction +37.60%; memory reduction
  +59.93%; base: `1756_math.py`.

- `1756_math_optimized.rs`: time reduction +51.61%; memory reduction
  +68.39%; base: `1756_math.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1756_math.cpp](1756_math.cpp).
- [1756_math.go](1756_math.go).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1756_math.cpp](1756_math.cpp) | G++ 13.2 x64 | math | O(d2) | AC | 0.015 s | 124 KB | 11304258 |
| [1756_math.go](1756_math.go) | Go 1.14 x64 | math | O(d2) | AC | 0.031 s | 1060 KB | 11289576 |
| [1756_math.java](1756_math.java) | Java 1.8 | math | O(d2) | AC | 0.125 s | 2020 KB | 11304259 |
| [1756_math.py](1756_math.py) | Python 3.12 x64 | math | O(d2) | AC | 0.125 s | 1148 KB | 11289577 |
| [1756_math.rs](1756_math.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.031 s | 620 KB | 11304260 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1756_math_optimized.java](1756_math_optimized.java) | Java 1.8 | math | O(d2) time; O(1) auxiliary space | AC | 0.093 s | 444 KB | 11327526 |
| [1756_math_optimized.py](1756_math_optimized.py) | Python 3.12 x64 | math | O(d2) | AC | 0.078 s | 460 KB | 11307291 |
| [1756_math_optimized.rs](1756_math_optimized.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.015 s | 196 KB | 11307300 |
