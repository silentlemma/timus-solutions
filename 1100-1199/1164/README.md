# 1164. Which letters are left after finding all words of a fillword

[Timus 1164](https://acm.timus.ru/problem.aspx?space=1&num=1164) · difficulty 207 · strings

Original problem by Alex Selivanov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grid of `N×M` capital letters (`2 ≤ N, M ≤ 10`) hides `P ≤ 100` words.
Each word occupies a path of side-adjacent cells, and no cell belongs to
two words or twice to the same word. A valid placement always exists.
Print the letters of the cells not used by any word, in alphabetical
order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M` and `P`, then `N` rows of the grid, then the `P` words.

## Output

The leftover letters, sorted, on one line.

## Checking

Compare the remaining uppercase-letter token exactly; an empty remainder permits empty output. The new exact Python source passed 11 repository fixtures under PyPy 3.10. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
3 3 2
EBG
GEE
EGE
BEG
GEE
```

Output:

```
EEG
```

## Solution

No path search is needed. For each letter `c`, let `G[c]` count its
cells in the grid and `U[c]` its occurrences in the listed words. Any valid
placement uses exactly `U[c]` different cells carrying `c`: paths cannot
reuse cells, and different words cannot overlap. Thus every placement
leaves exactly `G[c] − U[c]` copies of `c`, independently of its geometry.
The promise that a placement exists guarantees nonnegative differences.

Count grid letters, subtract word letters with multiplicity, and emit
each letter from `A` through `Z` the remaining number of times. This
produces precisely the leftover multiset in sorted order. Duplicate
words still consume their letters separately. If all cells are used,
print an empty line. The promise also gives total word length
`W ≤ N M ≤ 100`, and hence each word fits in 100 characters.

Time is `O(N M + W + 26)`. Native bases keep 26 counters; Python's
readable base uses `Counter`. Including stored input and output, `O(N M + W)`
space is a bound for all versions; streaming versions need less input
storage. All five original Accepted sources are retained unchanged.

## Optimized solutions

`1164_strings_optimized.java`. Java keeps the same 26 letter balances: add every grid letter, subtract every given word, then emit positive balances alphabetically. Every valid placement consumes exactly that multiset, so no path search is needed. countLetters scans uppercase token bytes directly from a 1024-byte refillable buffer instead of allocating word strings, decoding UTF-8 and making character arrays. The answer still uses StringBuilder. With W word letters and A output letters, time O(N*M+W+A); auxiliary space O(A+26) plus the fixed input buffer. Teaching versions remain unchanged.

Exact-source Java 1.8 Accepted #11327328: 0.093 s / 456 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/32, memory 2/32. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324785 was 0.109 s / 500 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1164_strings_optimized.java`: 0.093 s / 456 KB; retained teaching base `1164_strings.java`: 0.109 s / 1640 KB.

`1164_strings_optimized.rs`. Keep the 26 letter balances: add grid letters and subtract the given words. Stream the rows and words directly and emit remaining letters in order without storing input text or the answer string. O(I+A) time for input bytes I and output letters A; constant alphabet storage.

Compared with `1164_strings.rs`: time 0.015 s → 0.015 s; memory 220 KB → 60 KB.

All placements consume the same multiset of letters. Keep the clear counting sources and the compact C++ counter. Python scans the grid and concatenated words for each of the fixed 26 capital letters, then emits each positive difference in sorted order. Multiplying a linear scan by a constant alphabet remains linear. It avoids importing Counter and keeping a separate dictionary per multiset, while retaining the input strings. Reading the existing text streams and writing the final string also avoids extra input wrappers. The measured improvement is memory only; preserve the slower-time tradeoff below.

- `1164_strings_optimized.cpp`: 0.015 s / 104 KB; base `1164_strings.cpp`: 0.015 s / 380 KB; relative change: time -0.0%, memory -72.6%.
- `1164_strings_optimized.py`: 0.109 s / 260 KB; base `1164_strings.py`: 0.078 s / 436 KB; relative change: time +39.7%, memory -40.4%.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1164_strings_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328513 (Go 1.14 x64): **0.015 s / 968 KB**. Archived comparison: `1164_strings.go` (Go 1.14 x64) — 0.031 s / 1184 KB (#11283056).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1164_strings.cpp](1164_strings.cpp) | G++ 13.2 x64 | strings | O(N M + W) | AC | 0.015 s | 380 KB | 11283052 |
| [1164_strings.go](1164_strings.go) | Go 1.14 x64 | strings | O(N M + W) | AC | 0.031 s | 1184 KB | 11283056 |
| [1164_strings.java](1164_strings.java) | Java 1.8 | strings | O(N M + W) | AC | 0.109 s | 1640 KB | 11283063 |
| [1164_strings.py](1164_strings.py) | Python 3.12 x64 | strings | O(N M + W) | AC | 0.078 s | 436 KB | 11283059 |
| [1164_strings.rs](1164_strings.rs) | Rust 1.75 x64 | strings | O(N M + W) | AC | 0.015 s | 220 KB | 11283064 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1164_strings_optimized.cpp](1164_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(N M + W) | AC | 0.015 s | 104 KB | 11308330 |
| [1164_strings_optimized.py](1164_strings_optimized.py) | PyPy 3.10 x64 | strings | O(N M + W) | AC | 0.109 s | 260 KB | 11309679 |
| [1164_strings_optimized.java](1164_strings_optimized.java) | Java 1.8 | strings | O(N M + W + A) time; O(A + 26) space + fixed buffer | AC | 0.093 s | 456 KB | 11327328 |
| [1164_strings_optimized.rs](1164_strings_optimized.rs) | Rust 1.75 x64 | strings | O(I+A) time; O(26) space | AC | 0.015 s | 60 KB | 11325544 |
| [1164_strings_optimized.go](1164_strings_optimized.go) | Go 1.14 x64 | strings | O(N M + W) | AC | 0.015 s | 968 KB | 11328513 |
