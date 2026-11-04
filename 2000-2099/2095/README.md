# 2095. Count the days a repeated removal sieve keeps

[Timus 2095](https://acm.timus.ru/problem.aspx?space=1&num=2095) · difficulty 277 · math

Original problem by Dmitry Ivankov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Days are numbered 1, 2, 3, … Every second day is a report; of the days
left, every third is a report; of those left, every fourth, and so on
forever. The days that are never removed are quiet. Count the quiet
days in [l; r]. The limits are 1 second and 64 MB.

## Input

l and r, 1 ≤ l ≤ r ≤ 10⁹.

## Output

The number of quiet days from l to r.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
1 10
```

Output:

```
3
```

## Solution

Let f(n) be the number of quiet days among the first n. The removals
always take positions in the list of remaining days, so among the first
c remaining days step k removes exactly ⌊c / k⌋ of them, and the
remaining days among the first n stay a prefix of the list. Hence
f(n) is found by c ← c − ⌊c / k⌋ for k = 2, 3, … while c ≥ k; once c < k
no further step touches the prefix. The count c shrinks roughly like
n / k, so the loop stops after about 2√(n/π) steps, some 3.6·10⁴ for 10⁹. The
answer is f(r) − f(l − 1).

In the example f(10): 10 → 5 → 4 → 3, and the quiet days are 1, 3
and 7.

## Optimized solutions

Keep the single-step sieve as the teaching base. Before step k let c=qk+r be the surviving prefix size. After j deletions of q, the quotient stays q exactly while 2 qj<=r; its upper inequality only loosens. Apply r//(2 q)+1 steps together: c-=q*j,k+=j. The next positive quotient is strictly smaller. Before k, (k-1)c<=N+(k-2)(k-1)/2 by induction from c<-c-floor(c/k). For K=ceil(N^(1/3))+1, fewer than K early steps occur, and thereafter q<=K, so at most K further quotient blocks remain: O(N^(1/3))time/O(1)state. Evaluate quiet(R)-quiet(L-1). Go uses bounded portable native I/O. Java uses the same exact blocks. Python computes each prefix separately and uses divmod to obtain the quotient and remainder together. All calculations use exact integers.

- `2095_math_optimized.go`: 0.015 s / 280 KB; base `2095_math.go`: 0.031 s / 1076 KB; relative change: time -51.6%, memory -74.0%.
- `2095_math_optimized.java`: 0.125 s / 320 KB; base `2095_math.java`: 0.125 s / 1556 KB; relative change: time -0.0%, memory -79.4%.
- `2095_math_optimized.py`: 0.062 s / 368 KB; base `2095_math.py`: 0.078 s / 368 KB; relative change: time -20.5%, memory -0.0%.

## Language notes

The saved snapshots are from 1 and 4 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `2095_math.cpp`; covering source `2095_math.cpp`; time/memory places 1/1, other-author entries 38/38.

- Go: preferred teaching base `2095_math.go`; covering source `2095_math_optimized.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2095_math.java`; covering source `2095_math_optimized.java`; time/memory places 2/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `2095_math.py`; covering source `2095_math_optimized.py`; time/memory places 1/1, other-author entries 60/60.

- Rust: preferred teaching base `2095_math.rs`; covering source `2095_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2095_math.cpp](2095_math.cpp) | G++ 13.2 x64 | math | O(sqrt r) | AC | 0.015 s | 108 KB | 11309238 |
| [2095_math.go](2095_math.go) | Go 1.14 x64 | math | O(sqrt r) | AC | 0.031 s | 1076 KB | 11294664 |
| [2095_math.java](2095_math.java) | Java 1.8 | math | O(sqrt r) | AC | 0.125 s | 1556 KB | 11309239 |
| [2095_math.py](2095_math.py) | Python 3.12 x64 | math | O(sqrt r) | AC | 0.078 s | 368 KB | 11294665 |
| [2095_math.rs](2095_math.rs) | Rust 1.75 x64 | math | O(sqrt r) | AC | 0.015 s | 204 KB | 11309240 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2095_math_optimized.go](2095_math_optimized.go) | Go 1.14 x64 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.015 s | 280 KB | 11309760 |
| [2095_math_optimized.java](2095_math_optimized.java) \* | Java 1.8 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.125 s | 320 KB | 11309305 |
| [2095_math_optimized.py](2095_math_optimized.py) | Python 3.12 x64 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.062 s | 368 KB | 11309302 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
