# 1925. One Final Value to Match an Aggregate

[Timus 1925](https://acm.timus.ru/problem.aspx?space=1&num=1925) · difficulty 70 · math

Original problem by Pavel Ageev, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence of n past rounds is known. In round i, a displayed value bᵢ
had intended input bᵢ−2, but the actual input was gᵢ. The current round
displays k. Only the total over all n+1 rounds is checked: actual inputs
must sum to the sum of intended inputs. Choose a nonnegative integer
for the current round, or report that none exists. Past rounds need not
be individually correct. Limits: 1 second, 64 MB.

## Input

n,k with 1≤n,k≤100, followed by n pairs bᵢ,gᵢ, each in 0..100.

## Output

Print the required nonnegative integer, including zero if appropriate.
There is no upper bound of 100 on this output. If impossible, print
exactly `Big Bang!`, with its space, capitalization and exclamation mark.

## Checking

Compare whitespace-separated tokens exactly: either the integer or
the two tokens `Big` and `Bang!`.

## Examples

```
6 5
3 1
3 1
5 3
6 5
5 5
7 2
```

```
3
```

```
1 3
4 6
```

```
Big Bang!
```

## Solution

Let x be today's input. The check compares the sums over all n + 1
rounds: g₁ + … + gₙ + x = (b₁ − 2) + … + (bₙ − 2) + (k − 2). So
x = k − 2 + Σ(bᵢ − gᵢ − 2); if it is negative, no input works and the
answer is `Big Bang!`. `O(n)`.

Pitfalls:

- the running total may become negative in the middle and still end
  nonnegative, so decide only at the end;
- zero is a valid answer;
- every round, today's included, subtracts 2.

## Optimized solutions

`1925_math_optimized.py`. Keep current-2+sum(displayed-entered-2). Accumulate directly in a local loop instead of a separate helper and pair generator. Decide only after every pair: an intermediate negative value may recover; zero is valid. Print the final value or exactly Big Bang!. O(N) time and token storage under the bounded integer widths; O(1) arithmetic state. The teaching helper remains.

Reused exact historical CPython 3.12 Accepted #11302116: 0.078 s / 436 KB. In the saved 2026-11-20 comparable compiler cohort: time rank 2/59, memory rank 31/59. Below 1024 KB, strict admission uses time only and passes. The asterisk follows the separate language rating target. These are paired measurements of this source, not a new submission or a guaranteed portable speedup. This version uses normal interpreter exit.

- `1925_math_optimized.py`: 0.078 s / 436 KB; retained teaching base `1925_math.py` (Python 3.12 x64): 0.093 s / 504 KB. Both base time and memory remain documented even where one metric increases.

`1925_math_optimized.rs`. Keep the balance equation current-2+sum(displayed-entered-2). Process every historical pair before deciding: an intermediate negative balance may recover later. Print the final integer including zero, or exactly Big Bang! only if it is negative. Time O(N), constant arithmetic state under the input limits. Read and add each pair directly, removing the stored history vector and decoded input. Auxiliary state O(1). The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1925_math.rs`: time 0.031 s → 0.062 s; memory 236 KB → 56 KB.

The optimized C++ solution reads the pairs with `scanf` instead of
`iostream` and adds them up at once instead of storing the history:
124 KB instead of 428 KB.

The optimized Java solution reads the input in 1 KB blocks and parses it
by hand instead of using `Scanner`, and adds the readings up as they are
read instead of storing them: 0.078 s instead of 0.140 s and 364 KB
instead of 1796 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1925_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1925_math.cpp](1925_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 428 KB | 11291544 |
| [1925_math.go](1925_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1088 KB | 11291551 |
| [1925_math.java](1925_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1796 KB | 11291560 |
| [1925_math.py](1925_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 504 KB | 11291556 |
| [1925_math.rs](1925_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11291566 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1925_math_optimized.cpp](1925_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 124 KB | 11303650 |
| [1925_math_optimized.java](1925_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.078 s | 364 KB | 11303789 |
| [1925_math_optimized.py](1925_math_optimized.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 436 KB | 11302116 |
| [1925_math_optimized.rs](1925_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.062 s | 56 KB | 11324855 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
