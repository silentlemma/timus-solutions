# 1491. Totals after inclusive range additions

[Timus 1491](https://acm.timus.ru/problem.aspx?space=1&num=1491) · difficulty 203 · prefix_sums

Original problem by Alexander Toropov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `2 ≤ N ≤ 100000` positions with initial total zero.
Operation 0 gives `c` coins to every position `a..b`, inclusive; then
there is one more operation for each `i = 1..N`. Every operation has
`1 ≤ a ≤ b ≤ N`, `1 ≤ c ≤ 10000`. Operation `i` excludes its own
position (`a_i > i` or `b_i < i`); operation 0 is unrestricted.
Find all final totals. No cost is subtracted from any position.
Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, followed by the initial triple `a b c` and then the `N` further triples in order.

## Output

The `N` totals in position order, separated by spaces.

## Checking

The actual packed Python candidate passed 812 inputs: 800 small
legal instances checked by directly adding each gift to every recipient,
plus 12 boundary/maximal instances with independently known totals.
Those cover `N = 2, 1023, 1024, 1025, 2048, 100000`, totals of one billion
and large negative difference cells. Gifts exclude their respective
givers as required. The maximum legal total is `N × 10000`, since a
position does not receive its own gift; the looser bound above also
safely covers every intermediate cell. Each of the five actual candidates
also passed 14 repository inputs in Docker and received its own Accepted.
The 812 oracle checks were Python runs, not 812 executions of every language.

## Examples

### Example 1

Input:

```
4
2 3 2
2 4 1
3 4 1
1 2 1
1 1 1
```

Output:

```
2 4 4 2
```

### Example 2

Input:

```
7
1 7 1
2 3 4
3 5 3
1 2 1
5 7 4
2 4 10
3 4 2
1 6 3
```

Output:

```
5 19 23 19 11 8 5
```

## Solution

Use a zero-initialized difference array with `N + 2` cells.
For each of the `N + 1` operations, add `c` at `a` and subtract `c`
at `b + 1`. Take prefix sums at positions `1..N` to obtain the totals.

For one operation, its contribution to prefix `j` is `+c` once `j ≥ a`,
then `−c` once `j ≥ b + 1`: exactly `c` for `a ≤ j ≤ b` and zero outside.
Summing these identities proves the algorithm for all operations.
The extra cell at `N + 1` permits an interval ending at `N`; it is not
printed. The first operation must not be forgotten. The self-exclusion
restriction does not change these additions.

Time and auxiliary storage are `O(N)`, with bounded-length input and
output numbers. The readable native bases use 64-bit difference cells;
Python uses ordinary integer lists. All five original Accepted sources
remain unchanged.

## Optimized solutions

Let `S` be the sum of all operation amounts, at most
`(N + 1) × 10000 ≤ 1000010000 < 2^31`. Each operation changes a particular
difference cell by at most its amount, so even intermediate cells lie
in `[-S,S]`. Every running total is a sum of active positive amounts,
hence lies in `[0,S]`. Signed 32-bit cells and accumulators are therefore
safe, including large negative endpoint differences.

Use 32-bit arrays instead of native 64-bit cells or Python object lists;
the counter array occupies `4 × (N + 2)` bytes on the tested runtime ABI.
C++ and Java use fixed 4 KiB input/output buffers and ten-byte temporary
digit arrays, sufficient for the bound. Go shrinks its input buffer
from 1 MiB to 4 KiB and keeps buffered output. Rust streams locked input
and buffered output instead of retaining the input and all answer strings.
Python uses `array("i")`, streams the stated input lines, and writes
groups of at most 1024 answer strings. At a full group it emits a space
if more totals remain, otherwise a newline; a partial final group also
ends in a newline. No separator is lost across group boundaries.

Time remains `O(N)` and storage `O(N)`; these are implementation and
memory improvements of the same difference-array algorithm, so the
suffix is `_optimized`. Every published file has its own exact-source
Accepted and reduces memory by at least 30%. A smaller footprint does
not imply a faster recorded time; both metrics are listed below.

Measured changes against the original same-language base:

- C++: 0.187 s / 980 KB → 0.046 s / 516 KB; memory reduction 47.3%.
- Go: 0.031 s / 4540 KB → 0.031 s / 2972 KB; memory reduction 34.5%.
- Java: 0.109 s / 8872 KB → 0.125 s / 852 KB; memory reduction 90.4%.
- Python: 0.328 s / 35944 KB → 0.250 s / 1236 KB; memory reduction 96.6%.
- Rust: 0.046 s / 9428 KB → 0.062 s / 584 KB; memory reduction 93.8%.

## Language notes

The established comparison profile requires top 15% or the first 10 places in both time and memory for C++; Go, Java, Python/PyPy and Rust require first place in both. Ties share a place, and empty samples are recorded separately.

Snapshot of 2 November 2026 (time place / memory place; filtered other-author entries):

- C++: 5 / 3; 113 / 113; target met.
- Go: 1 / 1; 0 / 0; empty sample; formal coverage is not competitive proof.
- Java: 1 / 1; 4 / 4; target met.
- Python: 10 / 1; 20 / 20; rating target still open.
- Rust: 1 / 1; 0 / 0; empty sample; formal coverage is not competitive proof.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1491_prefix_sums.cpp](1491_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.187 s | 980 KB | 11287189 |
| [1491_prefix_sums.go](1491_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 4540 KB | 11287190 |
| [1491_prefix_sums.java](1491_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 8872 KB | 11287195 |
| [1491_prefix_sums.py](1491_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.328 s | 35944 KB | 11287194 |
| [1491_prefix_sums.rs](1491_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 9428 KB | 11287196 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1491_prefix_sums_optimized.cpp](1491_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.046 s | 516 KB | 11308370 |
| [1491_prefix_sums_optimized.go](1491_prefix_sums_optimized.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 2972 KB | 11308372 |
| [1491_prefix_sums_optimized.java](1491_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.125 s | 852 KB | 11308375 |
| [1491_prefix_sums_optimized.py](1491_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.250 s | 1236 KB | 11308367 |
| [1491_prefix_sums_optimized.rs](1491_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.062 s | 584 KB | 11308383 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
