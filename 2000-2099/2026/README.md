# 2026. Maximize an alternating letter sum

[Timus 2026](https://acm.timus.ru/problem.aspx?space=1&num=2026) · difficulty 594 · greedy

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Complete a string by replacing every `?` with a lowercase English
letter, leaving all existing letters unchanged. The completed string
must contain at least `k` distinct letters. A letter's value is its
alphabet position, from `a = 1` to `z = 26`. Its quality is the sum of
values in odd-numbered positions minus the sum in even-numbered
positions, numbering from one. Output any completion with maximum
quality, or report that no completion satisfies the distinct-letter
requirement.

Limits: length `1 ≤ n ≤ 100000`, `1 ≤ k ≤ 26`, 1 second, 64 MB. Quality
may be negative.

## Input

The first line is the pattern of lowercase letters and question marks.
The second is `k`.

## Output

Print an optimal completed string, or `-1` if impossible. Print the
string itself, not its quality. A valid string can have quality −1 and
must still be printed.

## Checking

A checker verifies the letters, the fixed positions and the number of
distinct letters and compares the quality with the optimum; any optimal
completion is accepted.

## Examples

```
??
1
```

```
za
```

```
??
3
```

```
-1
```

```
aza
1
```

```
aza
```

```
aza
3
```

```
-1
```

## Solution

Let `F` be the set of letters already fixed in the pattern. Let `P` and
`M` be the counts of free positive and negative positions, respectively.
With zero-based indices, even positions are positive. We need `r =
max(0, k-|F|)` new distinct letters. Since `k ≤ 26`, at least `r`
letters are absent from `F`. Feasibility is exactly `P+M ≥ r`: each new
letter needs a different free position, and enough positions allow such
an assignment.

Ignoring diversity, fill every positive hole with `z` and every negative
hole with `a`. This baseline has the greatest unconstrained quality.
Replacing a baseline positive letter by value `c` loses `26-c`; a
negative replacement loses `c-1`. Every loss is nonnegative.

List the missing letter values in increasing order. If `x` new letters
are represented on positive holes, the smallest loss is obtained by
taking the `x` largest missing values. If `y` are represented on
negative holes, take the `y` smallest missing values. Build prefix costs
`high[x]` for those largest values and `low[y]` for the smallest. Try
every `max(0,r-M) ≤ x ≤ min(r,P)`, with `y = r-x`, and minimize
`high[x]+low[y]`.

Fill the baseline, then put those `x` largest missing letters in any `x`
positive holes and the `y` smallest in any `y` negative holes, once
each. The two chosen sets are disjoint: together they have `r` elements,
at most the number of missing letters. All other holes keep the baseline
letters. Any tie between choices of `x` is valid.

For correctness, take any valid completion and choose any `r` distinct
letters absent from `F`, together with one representative hole for each.
Suppose `x` representatives are positive and `y` negative. Their loss is
no greater than the completion's total loss, since all other losses are
nonnegative. Those `x` positive representatives cost at least `high[x]`,
and the `y` negative ones at least `low[y]`. Thus every valid completion
loses at least the minimum tried by the algorithm. Both independent
minima can be achieved simultaneously because the largest `x` and
smallest `y` missing sets are disjoint. Our construction achieves this
lower bound while introducing `r` distinct letters, proving global
optimality. Extra distinct baseline letters are allowed: the requirement
is at least `k`, not exactly `k`.

In the first sample, `za` has quality `26-1 = 25`, the unconstrained
maximum; using two letters is allowed when `k = 1`. Two positions cannot
contain three types in the second. In the third, the fixed string is the
only choice and has quality `1-26+1 = -24`. The same fixed string has
only two types, making the fourth impossible.

With alphabet size `σ = 26`, time and space are `O(n + σ)`, hence `O(n)`
here. The program stores free-position indices and the answer, while
prefix costs have size `σ+1`. An alternative is the checker's DP: for
each missing letter, skip it or represent it on one available sign,
tracking the two representative counts.

Pitfalls:

- Count only fixed letters in `F`; baseline `a` and `z` may later be
  overwritten.
- Preserve fixed letters and distinguish one-based signs from zero-based
  indices.
- Do not require exactly `k` types or compare with one particular
  optimal string.
- If `r = 0`, use the unconstrained baseline; an already fixed negative
  score is still valid.
- For example, `ab` with `k = 2` is feasible with quality −1; the output
  is `ab`, not `-1`.

## Language notes

All arithmetic fits ordinary integers. C++, Go and Rust store free
indices in vectors or slices; Java uses integer arrays. Go and Rust
process ASCII bytes, and Python uses characters. Buffered input handles
a 100000-character token; Go uses `fmt.Fscan`, avoiding Scanner's
default token-size limit. CPython needs no alternative runtime.

## Optimized solutions

The C++ version counts free positions of each parity on the first pass. Once the greedy split is known, a second pass fills the same character buffer in place, using the missing letters from the corresponding end of the alphabet. It takes O(n + σ) time, and the buffer for the input and output needs O(n) space with only O(σ) additional storage. The metrics come from submission 11316965.

The Rust version also counts the free positions by parity and fills the input buffer in place. It uses O(n + σ) time and O(σ) storage apart from the input and output buffer. Metrics come from submission 11317093.

The Java version counts the holes by parity and fills a single byte buffer in place. Submission 11317096 used 628 KB instead of 2448 KB and took 0.125 s instead of 0.109 s.

The Python version also counts the free positions by parity and fills a bytearray in place. It uses O(n + σ) time and O(σ) storage apart from the input and output buffer. Metrics come from submission 11317086.

The Go version also counts the free positions by parity and fills the input buffer in place. It uses O(n + σ) time and O(σ) storage apart from the input and output buffer. Metrics come from submission 11317080.

**Timus submissions for the simple versions**

Java 1.8 №11317029.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2026_greedy.cpp](2026_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 1008 KB | 11322047 |
| [2026_greedy.go](2026_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 6072 KB | 11322049 |
| [2026_greedy.java](2026_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 2448 KB | 11317029 |
| [2026_greedy.py](2026_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 5432 KB | 11322050 |
| [2026_greedy.rs](2026_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 2088 KB | 11322051 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2026_greedy_optimized.cpp](2026_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n + σ) | AC | 0.015 s | 204 KB | 11316965 |
| [2026_greedy_optimized.go](2026_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n + σ) | AC | 0.031 s | 1172 KB | 11317080 |
| [2026_greedy_optimized.py](2026_greedy_optimized.py) | Python 3.12 x64 | greedy | O(n + σ) | AC | 0.093 s | 800 KB | 11317086 |
| [2026_greedy_optimized.rs](2026_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(n + σ) | AC | 0.046 s | 456 KB | 11317093 |
| [2026_greedy_optimized.java](2026_greedy_optimized.java) | Java 1.8 | greedy | O(n + σ) | AC | 0.125 s | 628 KB | 11317096 |

\* Accepted. The Go rating target remains open. Accepted. The Rust rating target remains open.
