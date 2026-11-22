# 1864. Get-Together at Den's

[Timus 1864](https://acm.timus.ru/problem.aspx?space=1&num=1864) · difficulty 177 · math

Original problem: folklore (prepared by Daniil Ayzenshteyn), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n friends came to Den's place; friend i bought aᵢ litres of juice, and
everybody, Den included, drank the same amount. Den then pays
100 roubles for the juice drunk by people who had not bought it, shared
fairly among the friends who bought more than they drank. How many
roubles does each friend get, rounded down?

## Input

n (2 ≤ n ≤ 100), then a₁, …, aₙ (0 ≤ aᵢ ≤ 100) with a positive sum.

## Output

The roubles of every friend, rounded down.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3
10 10 10
```

Output:

```
33 33 33
```

### Example 2

Input:

```
2
10 0
```

Output:

```
100 0
```

## Solution

With S litres in all, each of the n + 1 people drinks S/(n + 1), so
friend i bought aᵢ − S/(n + 1) litres for others when that is positive,
and nothing for others otherwise. The money is shared in proportion to
these amounts. Multiplying all of them by n + 1 keeps everything in
integers: eᵢ = max(0, aᵢ(n + 1) − S), and friend i gets
⌊100·eᵢ / Σ e⌋. The sum is never 0: the friends together bought S and
drank only nS/(n + 1). `O(n)`; Python takes `O(n²)`.

In the first example everybody drank 7.5 litres, and each friend paid
2.5 litres for Den, so the money is split in three: 33 each after
rounding.

Pitfalls:

- Den drinks too, so the share is S/(n + 1), not S/n;
- the friends who bought less than they drank get nothing;
- exact integers avoid any doubt about rounding down.

The shares agree with an independent accepted implementation on two
hundred random gatherings.

## Optimized solutions

`1864_math_optimized.java`. Keep exact contribution normalization: c_i=max(0,a_i(N+1)−sum(a)), share_i=floor(100c_i/sum(c)). Parse integers directly. Each percentage is 0..100, so encode one, two or three digits with its separator into at most four bytes per person, then write once. Contributions, floor division and total remain unchanged; do not round percentages to force a total of 100. O(N) time and O(N) contribution/output storage. The teaching version remains.

Exact-source Java 1.8 Accepted #11327834: 0.093 s / 368 KB. Saved 2026-11-20 compiler-cohort comparison: time 7/59, memory 1/59. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11307325 was 0.125 s / 520 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1864_math_optimized.java`: 0.093 s / 368 KB; retained teaching base `1864_math.java`: 0.125 s / 1720 KB.

`1864_math_optimized.py`. Keep exact scaled overpayments credit[i]=max(0,(N+1)*bought[i]-total) and floor(100*credit[i]/sum(credits)). The input total is positive; before clipping, the credits sum to total, so the clipped denominator is strictly positive. Integer arithmetic avoids rounding errors. Time O(N) after computing the common denominator once. The basic generator recomputed sum(over) for every friend, costing O(N²); cache that sum once. Purchased amounts, credits and joined output still occupy O(N) storage. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1864_math.py`: time 0.093 s → 0.14 s; memory 412 KB → 212 KB.

`1864_math_optimized.rs`. Keep exact scaled overpayments credit[i]=max(0,(N+1)*bought[i]-total) and floor(100*credit[i]/sum(credits)). The input total is positive; before clipping, the credits sum to total, so the clipped denominator is strictly positive. Integer arithmetic avoids rounding errors. Time O(N) after computing the common denominator once. Reuse one fixed 100-entry i64 array for purchases and then credits, eliminating separate vectors and answer strings. Explicit array storage is 800 bytes plus constant state; bounds N<=100,bought<=100 make products safe. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1864_math.rs`: time 0.031 s → 0.046 s; memory 236 KB → 48 KB.

The optimized C++ solution computes the same shares, but keeps the
purchases and the surpluses in two fixed arrays of 100 numbers, enough
since `n ≤ 100`, instead of two vectors allocated on the heap:
{1864_math_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1864_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +45.83%; base: `1864_math.cpp`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1864_math_optimized.py`: time place 18/20, memory place 1/20 in this comparable sample.

`1864_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math.cpp](1864_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 192 KB | 11304246 |
| [1864_math.go](1864_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1116 KB | 11290890 |
| [1864_math.java](1864_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1720 KB | 11290894 |
| [1864_math.py](1864_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.093 s | 412 KB | 11290893 |
| [1864_math.rs](1864_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11304247 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math_optimized.cpp](1864_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 104 KB | 11307321 |
| [1864_math_optimized.java](1864_math_optimized.java) \* | Java 1.8 | math | O(N) time and storage | AC | 0.093 s | 368 KB | 11327834 |
| [1864_math_optimized.py](1864_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.14 s | 212 KB | 11325076 |
| [1864_math_optimized.rs](1864_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 48 KB | 11325116 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
