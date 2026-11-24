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

`2095_math_optimized.java`. Keep exact quotient-block elimination, advancing the upper and lower surviving prefixes together. Stop immediately when they coincide. If L=1, quiet(0)=0, so only the upper prefix needs evaluation. Replace Math.min with an integer comparison when choosing the safe shared jump. Every step still deletes floor(c/k); grouping uses j=floor((c−qk)/(2q))+1 while quotient q stays unchanged. O(R^(1/3)) time and O(1) numeric state. Consume both bounds before reusing the 64-byte input buffer for the decimal answer, flush it, then call Runtime.getRuntime().halt(0). All 45150 intervals with 1≤L≤R≤300 match an independent single-step oracle; 2000 large intervals match the accepted parent, with 1000 actual-main I/O probes. Current 0.093 s/464 KB and historical 0.125 s/320 KB are separate pairs: faster here costs more memory. The readable single-step sieve and all other language implementations remain.

Exact-source Java 1.8 Accepted #11327888: 0.093 s / 464 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/44, memory 1/44. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11309305 was 0.125 s / 320 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2095_math_optimized.java`: 0.093 s / 464 KB; retained teaching base `2095_math.java`: 0.125 s / 1556 KB.

Keep the single-step sieve as the teaching base. Before step k let c=qk+r be the surviving prefix size. After j deletions of q, the quotient stays q exactly while 2 qj<=r; its upper inequality only loosens. Apply r//(2 q)+1 steps together: c-=q*j,k+=j. The next positive quotient is strictly smaller. Before k, (k-1)c<=N+(k-2)(k-1)/2 by induction from c<-c-floor(c/k). For K=ceil(N^(1/3))+1, fewer than K early steps occur, and thereafter q<=K, so at most K further quotient blocks remain: O(N^(1/3))time/O(1)state. Evaluate quiet(R)-quiet(L-1). Go uses bounded portable native I/O. Java uses the same exact blocks. Python computes each prefix separately and uses divmod to obtain the quotient and remainder together. All calculations use exact integers.

- `2095_math_optimized.go`: 0.015 s / 280 KB; base `2095_math.go`: 0.031 s / 1076 KB; relative change: time -51.6%, memory -74.0%.

- `2095_math_optimized.py`: 0.062 s / 368 KB; base `2095_math.py`: 0.078 s / 368 KB; relative change: time -20.5%, memory -0.0%.

`2095_math_optimized.rs`. Keep the exact single-step removal sieve for each prefix: c becomes c-floor(c/k), increasing k from two until c<k. Evaluate quiet(R)-quiet(L-1), including quiet(0)=0. Only two loop variables are needed per prefix, for O(√R) time and O(1) auxiliary state. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `2095_math.rs`: time 0.015 s → 0.031 s; memory 204 KB → 52 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2095_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [2095_math_optimized.java](2095_math_optimized.java) | Java 1.8 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.093 s | 464 KB | 11327888 |
| [2095_math_optimized.py](2095_math_optimized.py) | Python 3.12 x64 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.062 s | 368 KB | 11309302 |
| [2095_math_optimized.rs](2095_math_optimized.rs) | Rust 1.75 x64 | math | O(√R) | AC | 0.031 s | 52 KB | 11325120 |
