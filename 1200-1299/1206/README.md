# 1206. Pairs of numbers whose digit sums add up

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · difficulty 124 · combinatorics

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let `S(N)` be the digit sum of `N`. For `2 ≤ K ≤ 50`, count the ordered
pairs of `K`-digit numbers `A` and `B`, without leading zeros, with
`S(A + B) = S(A) + S(B)`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`.

## Output

The number of pairs.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
4
```

Output:

```
5989500
```

## Solution

Every carry in the addition turns a 10 in one position into a 1 in the
next, lowering the digit sum by 9. So the equality holds exactly when no
position carries, that is when the digits in each position add up to at
most 9. The positions are then independent. In the leading position both
digits are from 1 to 9, which allows `8 + 7 + … + 1 = 36` pairs; in each
of the other `K − 1` positions the digits are from 0 to 9, which allows
`10 + 9 + … + 1 = 55` pairs. The answer is `36 · 55^(K−1)`, a number of
up to 87 digits. `O(K²)` with schoolbook multiplication.

The result needs O(K) decimal digits or bits up to a constant factor. Simple C++/Rust keep growing decimal-digit vectors and Rust also builds an O(K) output String; Go/Java/Python keep arbitrary-precision integers and decimal output, with O(K) live value/output storage plus arithmetic-library workspace and input buffers. The schoolbook O(K²) time is a conservative arithmetic/conversion model, not a claim that built-in exponentiation repeats K multiplications. Optimized Java allocates exactly 2K digit entries plus O(K) answer bytes; optimized C++ reserves a fixed 100-entry stack array for K ≤ 50. The proof 36·55^(K−1) < 100^K gives at most 2K digits, with equality at K=2 and K=3.

Pitfalls:

- the answer outgrows 64 bits already at `K = 12`;
- the leading digits cannot be 0, so their count differs from the
  others.

The formula was checked by brute force over all pairs for `K = 2` and
`K = 3`, and every `K` was compared with a separately written solution.

## Optimized solutions

`1206_combinatorics_optimized.java`. Keep the carry-free counting formula 36*55^(K-1). For K<=50, store the at-most-100 decimal digits explicitly and multiply by 55 online K-1 times, then emit bytes directly. This changes the arithmetic representation, not the counting argument, and stores no precomputed answers. Conservative O(K²) digit work and O(K) digit storage replace BigInteger initialization; the simple BigInteger formula remains available.

Historical exact-source Java 1.8 Accepted #11327341 is 0.109 s / 308 KB; saved 2026-11-20 comparison is time 14/141, memory 1/141. It meets the shared time-only criterion below 1024 KB, without a separate first-place target or marker. Earlier #11304422 is the separate historical pair 0.125 s / 448 KB. This review changes only the capacity comment from fewer than 2K to at most 2K; executable bytes apart from that comment are identical.

- `1206_combinatorics_optimized.java`: 0.109 s / 308 KB; retained teaching base `1206_combinatorics.java`: 0.14 s / 1748 KB.

The selected exact-source CPython 3.12 Accepted #11327017 for `1206_combinatorics_optimized.py` is 0.078 s / 612 KB; saved 2026-11-20 ranks are time 2/76, memory 60/76. Below 1024 KB it passes on time alone. Compared with current base #11283600, 0.109 s / 416 KB, time decreases by 28.44% and memory increases by 47.12%: this is not a 30% gain in either metric. Historical PyPy 3.10 #11324911 is the distinct pair 0.140 s / 252 KB; the memory-saving comparison later refers to that run, not to the selected CPython row.

The optimized C++ solution multiplies the same decimal digits by 55, but
in a fixed array of 100 entries on the stack instead of a growing
`std::vector`: since `K ≤ 50`, the answer `36 · 55^(K−1)` is below
`100^K` and has at most 100 digits (in fact at most 87). Without
`<vector>` the program carries no container code at all:
{1206_combinatorics_optimized.cpp}.

### Measured gains

These are historical differences between the paired Accepted runs, not a universal 30%-gain admission rule. The simple sources remain; negative reduction denotes increased cost. Current admission is evaluated by the shared rating policy.

- `1206_combinatorics_optimized.cpp`: time reduction +0.00%; memory
  reduction +46.81%; base: `1206_combinatorics.cpp`.

`1206_combinatorics_optimized.py`. Keep the exact formula 36*55^(K-1) and Python arbitrary-precision integers. Both the basic ** expression and pow here already use integer exponentiation; no new counting algorithm is claimed. A conservative schoolbook bit-cost bound, including decimal conversion, is O(K²) time and O(K) bits for the answer. The changed implementation reads the one input token and finishes without the function wrapper and normal teardown. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its historical PyPy Accepted demonstrates a memory reduction; the selected current CPython Accepted instead trades increased memory for a lower recorded time. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1206_combinatorics.py`: time 0.109 s → 0.14 s; memory 416 KB → 252 KB.

## Language notes

Apply the shared [rating criteria](../../RATING_CRITERIA.md) and source-bound cache. Both C++, Go, Rust and the receipt-bound optimized Java/Python sources meet the numerical criteria. Simple Java/Python miss them and remain unstarred teaching versions. The Java comment-only revision still needs fresh Accepted as noted above. Below 1024 KB compare time only; Go at 1200 KB requires both metrics and uses its two exact-version rivals. Rust uses its one-rival reference comparison. No separate first-place, 30%-gain or historical PyPy rank replaces current coverage.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB | 11283595 |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB | 11283596 |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.14 s | 1748 KB | 11283601 |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB | 11283600 |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB | 11283602 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics_optimized.cpp](1206_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 100 KB | 11304421 |
| [1206_combinatorics_optimized.java](1206_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(K²) time; O(K) space | AC | 0.078 s | 356 KB | 11331216 |
| [1206_combinatorics_optimized.py](1206_combinatorics_optimized.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.078 s | 612 KB | 11327017 |
