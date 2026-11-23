# 2098. Pay cash or pay more for insurance

[Timus 2098](https://acm.timus.ru/problem.aspx?space=1&num=2098) · difficulty 325 · math

Original problem by Denis Dublennykh, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

After a minor accident a driver can pay b roubles in cash, or register
it and let the insurance pay. The insurance costs c now and grows by d
every year, so the next k years cost c + d, c + 2d, …, c + kd; after a
registered accident those k payments are p percent higher. Say which
option is cheaper (Insurance on a tie) and by how much. The limits are
1 second and 64 MB.

## Input

b (up to 10⁵), then c and d (up to 10⁴), then k and p (up to 100).

## Output

`Cash` or `Insurance`, then the saving with an absolute or relative
error of at most 10⁻⁶.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
10000
5000 1000
3 50
```

Output:

```
Cash
500.00
```

### Example 2

Input:

```
15000
2500 1000
4 25
```

Output:

```
Insurance
10000.00
```

## Solution

Both options pay the usual insurance S = k·c + d·k(k + 1)/2 for the next
k years. Cash adds b, registration adds S·p/100. Comparing 100·b with
S·p keeps everything in integers (at most about 5·10⁹), and their
absolute difference divided by 100 is the saving, printed exactly with two
decimals.

In the first example S = 21000, so registration costs 10500 more while
cash costs 10000 more: Cash, by 500.

## Optimized solutions

`2098_math_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `2098_math.java`: time 0.125 s → 0.093 s; memory 1 716 KB → 904 KB.

Rust compares 100b with the integer surcharge p·k·(2c+d(k+1))/2. Their absolute difference is already the saving in hundredths, so it is printed as an integer part and two fractional digits. A tie selects Insurance. All calculations use 64-bit integers and require no floating-point formatting. Fixed byte buffers hold the input and complete response. Rust reads and writes through the C runtime.

The accepted base implementations [2098_math.cpp](2098_math.cpp), [2098_math.go](2098_math.go), [2098_math.java](2098_math.java), [2098_math.py](2098_math.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`2098_math_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328655 (Go 1.14 x64): **0.015 s / 928 KB**. Archived comparison: `2098_math.go` (Go 1.14 x64) — 0.031 s / 1080 KB (#11294672).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`2098_math_optimized.java`: time place 3/32, memory place 9/32 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2098_math.cpp](2098_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 136 KB | 11294670 |
| [2098_math.go](2098_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB | 11294672 |
| [2098_math.java](2098_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1716 KB | 11325556 |
| [2098_math.py](2098_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB | 11294673 |
| [2098_math.rs](2098_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 228 KB | 11294676 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2098_math_optimized.rs](2098_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 60 KB | 11311232 |
| [2098_math_optimized.java](2098_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 904 KB | 11324795 |
| [2098_math_optimized.go](2098_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 928 KB | 11328655 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
