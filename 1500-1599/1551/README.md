# 1551. Sumo Tournament

[Timus 1551](https://acm.timus.ru/problem.aspx?space=1&num=1551) · difficulty 257 · math, sorting

Original problem by Sergey Pupyrev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A knockout tournament has 2ᴺ wrestlers (1 ≤ N ≤ 10) and N rounds; each
wrestler represents a prefecture. The organisers choose the starting
bracket. Find the largest K such that some bracket guarantees, whatever
the bouts' results, at least K rounds in which no two wrestlers of one
prefecture meet.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then 2ᴺ lines with a wrestler's name and prefecture.
Both fields contain 1–30 Latin letters.

## Output

K.

## Checking

Compare one integer token. New Python passed 168 prefecture distributions against an independent hash-frequency oracle: mixed case, 30-letter fields, singleton/all-equal groups and up to1024 wrestlers.

## Examples

### Example 1

Input:

```
3
Homasho Ishikawa
Tamakasuga Tokyo
Futeno Tochigi
Takekaze Tokyo
Kasugao Yamaguchi
Kotoshogiku Ishikawa
Kotomitsuki Tokyo
Miyabiyama Shizuoka
```

Output:

```
1
```

## Solution

In round r the bracket pairs up blocks of 2^(r−1) wrestlers, and since
any wrestler of a block may come out of it, round r is safe exactly when
the two halves of every block of 2^r share no prefecture.

Take the largest prefecture, with c wrestlers, and let its wrestlers win
every bout against other prefectures. Only bouts within this prefecture
eliminate its wrestlers, and each unsafe round can reduce their number
by at most half. Reducing c to one therefore needs at least ⌈log₂ c⌉
unsafe rounds, so K ≤ N − ⌈log₂ c⌉.

That bound is reached: with k = ⌈log₂ c⌉ for the largest c, sort the
wrestlers by prefecture and deal them round-robin into the 2ᵏ blocks of
the top k levels. A prefecture has at most 2ᵏ wrestlers, so they land in
different blocks; inside a block everyone is from a different
prefecture, so the first N − k rounds are safe. The answer is therefore
N − ⌈log₂ c⌉. Count prefectures, find the largest count, and increment k
from zero until 2ᵏ ≥ c; output N − k. An exhaustive bracket-and-outcome
oracle agreed on all 29 multiplicity patterns for N ≤ 3 and 1,200 random
inputs. `O(2ᴺ log 2ᴺ)` for counting.

Pitfalls:

- a single prefecture leaves no safe round (tests 02, 04);
- c = 4 needs only two unsafe rounds, c = 5 three (tests 06, 07);
- prefectures are compared as written, so Tokyo and tokyo differ
  (test 08).
- wrestler names do not affect the counts; both fields must still use
  1–30 Latin letters, without numeric suffixes (tests 04–07).

## Optimized solutions

The answer still depends only on the largest prefecture frequency c: `N−ceil(log2 c)`. The compact C++/Java variants discard wrestler names while reading and update the maximum frequency immediately. C++ retains its ordered map; Java uses a hash map with bounded byte input. Python instead keeps only prefecture strings, sorts them and takes the longest equal run. Equal prefecture names form exactly one contiguous block, so its length is the same frequency. This removes the Counter import, retained wrestler tokens and a separate hash-table entry per prefecture. Python trades expected-linear hashing for `O(M log M)` sorting, `M=2^N`, while reducing actual memory; it does not claim faster time. Case-sensitive full strings are compared, with no collision-prone fingerprints. `bit_length(c−1)` computes the exact ceiling. All simple versions remain, including the direct Counter version.

- `1551_math_optimized.cpp`: 0.015 s / 308 KB; base `1551_math.cpp`: 0.015 s / 544 KB; relative change: time -0.0%, memory -43.4%.
- `1551_math_optimized.java`: 0.093 s / 568 KB; base `1551_math.java`: 0.156 s / 3280 KB; relative change: time -40.4%, memory -82.7%.
- `1551_math_sorting.py`: 0.093 s / 464 KB; base `1551_math.py`: 0.062 s / 696 KB; relative change: time +50.0%, memory -33.3%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1551_math.cpp`; covering source `1551_math_optimized.cpp`; time/memory places 1/1, other-author entries 47/47.

- Go: preferred teaching base `1551_math.go`; covering source `1551_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1551_math.java`; covering source `1551_math_optimized.java`; time/memory places 1/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1551_math.py`; covering source `1551_math_sorting.py`; time/memory places 61/4, other-author entries 139/139.

- Rust: preferred teaching base `1551_math.rs`; covering source `1551_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1551_math.cpp](1551_math.cpp) | G++ 13.2 x64 | math | O(M log M) | AC | 0.015 s | 544 KB | 11287591 |
| [1551_math.go](1551_math.go) | Go 1.14 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.031 s | 1276 KB | 11287592 |
| [1551_math.java](1551_math.java) | Java 1.8 | math | O(M) expected frequency work, M=2^N | AC | 0.156 s | 3280 KB | 11287596 |
| [1551_math.py](1551_math.py) | Python 3.12 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.062 s | 696 KB | 11287594 |
| [1551_math.rs](1551_math.rs) | Rust 1.75 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.046 s | 576 KB | 11287598 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1551_math_optimized.cpp](1551_math_optimized.cpp) | G++ 13.2 x64 | math | O(M log M) | AC | 0.015 s | 308 KB | 11309254 |
| [1551_math_optimized.java](1551_math_optimized.java) | Java 1.8 | math | O(M) expected frequency work, M=2^N | AC | 0.093 s | 568 KB | 11309256 |
| [1551_math_sorting.py](1551_math_sorting.py) \* | Python 3.12 x64 | math, sorting | O(M log M) time; O(M) strings | AC | 0.093 s | 464 KB | 11309558 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
