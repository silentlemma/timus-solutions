# 2063. Same colours without looking

[Timus 2063](https://acm.timus.ru/problem.aspx?space=1&num=2063) · difficulty 432 · constructive

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A row holds n balls, each black or white, in an unknown arrangement. A
query `? v u` swaps the balls at positions v and u if v holds a black
ball and u a white one, and does nothing otherwise; the program is never
told what happened. After any number of queries it makes one claim
`! v u`: two positions that now hold balls of the same colour.

One test plays several games, the i-th one with n = i + 1. All tests
except the first have 99 games, n = 2, …, 100, and the program must win
at least 80 of them; the tests are fixed in advance and do not adapt to
the program. The first test is the example and only its format is
checked. At most 500 000 lines may be printed per test. The limits are
1 second and 64 MB.

## Input

The number of games m (99 in every test but the first), then the
starting rows in an encoded form that the program should not try to
read.

## Output

m game descriptions, each a sequence of `? v u` lines followed by one
`! v u` line, with 1 ≤ v, u ≤ n and v ≠ u.

## Checking

A checker plays every game. With 99 games at least 80 claims must be
right; in the example only the format is checked.

## Examples

### Example 1

Input:

```
2
01
101
```

Output:

```
? 1 2
? 2 1
? 1 2
! 2 1
? 1 2
? 3 1
! 1 2
```

## Solution

Sort the balls blindly. A query on neighbours `? i i+1` moves a white
ball left past a black one, so the queries of bubble sort — for every
end from n − 1 down to 1, the pairs (1, 2), (2, 3), …, (end, end + 1) —
put all white balls before all black ones whatever the arrangement was.
This takes n (n − 1) / 2 queries per game, 166 650 queries in all for
n = 2, …, 100. Including 99 claims, the output has 166 749 lines,
well within the limit.

Now the row is some white balls followed by some black balls. Two
neighbours (j, j + 1) differ only at the single boundary between the
colours, and if the row has one colour there is no boundary at all. A
claim on a neighbouring pair chosen uniformly at random therefore loses
with probability at most 1 / (n − 1) for any fixed row. Under independent
uniform choices over the 99 games, the expected number of losses is at most
1/1 + 1/2 + … + 1/99 ≈ 5.2, and losing 20 or more games happens with
probability at most about 2.6·10⁻⁹.

A pitfall is always claiming (1, 2): this loses every game in test gen9,
which puts a single white ball first. Always claiming (n − 1, n) similarly
fails test gen10. The programs vary the pair using the splitmix64 generator
seeded with the FNV-1a hash of the whole input; the encoded rows are never
decoded. This is deterministic for a fixed input. Input-derived seeding
does not establish independent uniform choices, so the probability bound
above describes an ideal random model, not a guarantee for these programs.

Test 01 checks only the format, but command tokens must still be exactly
`?` or `!`; the malformed token `?!` must be rejected.

The example only shows the format: in its first game the claim (2, 1)
is wrong, in the second it is right.

## Optimized solutions

`2063_constructive_sorting.py`. Python now also offers Batcher’s padded odd-even merge network, beside both bubble variants. Skip comparators whose right endpoint is virtual black padding; the real prefix still sorts exactly. Keep the full raw-input FNV hash and the same splitmix64 adjacent claims, hence the same result for every fixed input; no independent-randomness or per-game deterministic-win claim is introduced. Read 4096-byte blocks and emit through a bytearray flushed at the 4096-byte threshold, rather than retain per-size bubble query lists. For input I and game sizes nᵢ<=100: O(I+Σ nᵢ log² nᵢ) work and O(B+log n_max) auxiliary storage, B=4096; decimal width is bounded by these limits. The old bubble sources and their own receipts remain.

Exact-source CPython 3.12 Accepted #11326665: 0.14 s / 1008 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 1/46, memory rank 6/46. Below 1024 KB, strict admission uses time only.

- `2063_constructive_sorting.py`: 0.14 s / 1008 KB; retained teaching base `2063_constructive.py` (Python 3.12 x64): 0.125 s / 8008 KB; time change +12.0%; memory change -87.4%.

`2063_constructive_sorting.java`. Java now also offers Batcher’s padded odd-even merge network, beside both readable and compact bubble variants. Omit comparisons ending in virtual black padding; the real prefix sorts identically. Preserve every input byte in the same FNV seed and the same unsigned splitmix64 adjacent claim, so each fixed input has the same outcome as the old bubble strategy. The probability limitation remains; this is not a deterministic per-game win guarantee. Input is hashed in 1024-byte blocks and commands streamed through a 16384-byte output buffer. Time O(I+Σ nᵢ log² nᵢ), auxiliary space O(log n_max) recursion plus fixed buffers; indices<=100 have bounded decimal width. Old bubble files and their receipts remain.

Exact-source Java 1.8 Accepted #11326597: 0.109 s / 604 KB. Saved current-Java comparison, 2026-11-20: time rank 1/25, memory rank 1/25. With memory below 1024 KB, strict admission uses time only.

- `2063_constructive_sorting.java`: 0.109 s / 604 KB; retained teaching base `2063_constructive.java`: 0.14 s / 9992 KB; time change -22.1%; memory change -94.0%.

`2063_constructive_sorting.cpp`. The C++ Batcher network now streams its command text through a fixed 16 KiB output buffer. Input is read in 16 KiB blocks and every original byte updates the same FNV-1a seed; only the initial game count is decoded. Splitmix64, comparator order and adjacent claims stay identical for identical input bytes. This removes full-input and growing-output retention, without changing the existing input-derived probabilistic strategy or claiming independent randomness. For I input bytes and sizes nᵢ, time is O(I+Σ nᵢ log² nᵢ), auxiliary storage O(log n_max) recursion plus fixed buffers; output is streamed, not retained. The bubble-sort teaching files remain. Indices are at most 100 in this task, so printing one comparator uses a bounded number of decimal digits.

Exact-source Accepted #11326647: 0.015 s / 124 KB. Saved current C/C++ compiler cohort, 2026-11-20: time rank 1/56, memory rank 1/56.

`2063_constructive_optimized.java`. Preserve the existing probabilistic strategy and its deterministic input-derived seed. Stream all B input bytes through the same FNV-1a update while parsing only the initial game count; arrangements are not decoded. Splitmix64 and the complete bubble compare-exchange schedule are unchanged, so identical input bytes yield the same adjacent-pair claims as the old source. The sorted row has at most one bad adjacent boundary, but a claim can still fail: this is not a per-game deterministic guarantee. The 99-game judge requires at least 80 successes. For sizes 2..100 the schedule emits 166650 queries plus 99 claims, below 500000 lines. Time O(B+Σ nᵢ²), auxiliary storage O(1) fixed input/output buffers instead of copies of all input and a growing output builder.

Compared with `2063_constructive.java`: time 0.14 s → 0.156 s; memory 9 992 KB → 580 KB.

`2063_constructive_optimized.py`. Keep the original bubble-sort command network and exactly the same FNV-1a hash of every raw input byte and splitmix64 claim per game. Hash in 4096-byte blocks, parsing only the game count; encoded arrangements are not decoded. Retain only one game’s adjacent-query byte strings and stream commands through a bounded output buffer, replacing the list of all command lines. With m games, total output work is O(m³ log(m+2)), input hashing O(I), and storage O(B+m log(m+2)); the query/claim sequence and fixed-input wins are unchanged. This preserves the existing deterministic seed’s limitations and does not claim independent randomness.

Compared with `2063_constructive.py`: time 0.125 s → 0.187 s; memory 8008 KB → 2 776 KB.

C++, Go and Rust replace the bubble comparisons with Batcher’s [odd-even merge sorting network](https://doi.org/10.1145/1468075.1468121). Pad to the next power of two with virtual black balls, then omit comparisons whose right endpoint is virtual. Every comparator points from a smaller index to a larger one, so a virtual black ball can never change: comparing any real value with a right-hand black padding value is a no-op. The real prefix therefore sorts exactly as in the full network. Odd and even subsequences are merged recursively, followed by the intervening adjacent comparisons; each game uses O(n log² n) commands rather than O(n²). The original FNV seed over all raw input bytes and one splitmix64 claim per game are preserved. Both networks finish with the same sorted row and the same claim, so the result on each fixed input is unchanged. This does not turn input-derived seeding into independent randomness. Go hashes input in bounded chunks and formats commands into a fixed output buffer without allocating strings per command; C++ streams the same network as described above; Rust retains the smaller command text. Ordinary bubble files remain; Java and Python have the separate compact variants described here.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.031 s for the base and uses 1 124 KB versus 3208 KB.

The existing Java and Python basic files remain as teaching versions. The separate new variants below have their own Accepted rows; no identical copies are used.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`2063_constructive_optimized.java`: time place 13/25, memory place 1/25 in this comparable sample.

`2063_constructive_optimized.py`: time place 3/46, memory place 22/46 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2063_constructive.cpp](2063_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.046 s | 3084 KB | 11325591 |
| [2063_constructive.go](2063_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 980 KB | 11294278 |
| [2063_constructive.java](2063_constructive.java) \* | Java 1.8 | constructive | O(n^2) | AC | 0.14 s | 9992 KB | 11325570 |
| [2063_constructive.py](2063_constructive.py) \* | Python 3.12 x64 | constructive | O(n^2) | AC | 0.125 s | 8008 KB | 11294295 |
| [2063_constructive.rs](2063_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 3208 KB | 11325615 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2063_constructive_sorting.cpp](2063_constructive_sorting.cpp) | G++ 13.2 x64 | constructive, sorting | O(I+Σ nᵢ log² nᵢ) time; O(log n_max) space | AC | 0.015 s | 124 KB | 11326647 |
| [2063_constructive_sorting.rs](2063_constructive_sorting.rs) \* | Rust 1.75 x64 | constructive, sorting | O(n log² n) | AC | 0.046 s | 1124 KB | 11315037 |
| [2063_constructive_sorting.go](2063_constructive_sorting.go) | Go 1.14 x64 | constructive, sorting | O(n log² n) | AC | 0.031 s | 300 KB | 11315319 |
| [2063_constructive_sorting.java](2063_constructive_sorting.java) | Java 1.8 | constructive, sorting | O(I+Σ nᵢ log² nᵢ) time; O(log n_max) space | AC | 0.109 s | 604 KB | 11326597 |
| [2063_constructive_optimized.java](2063_constructive_optimized.java) \* | Java 1.8 | constructive | O(B+Σ nᵢ²) | AC | 0.156 s | 580 KB | 11325124 |
| [2063_constructive_sorting.py](2063_constructive_sorting.py) | Python 3.12 x64 | constructive, sorting | O(I+Σ nᵢ log² nᵢ) time; O(B+log n_max) space | AC | 0.14 s | 1008 KB | 11326665 |
| [2063_constructive_optimized.py](2063_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(I+m³ log(m+2)) time; O(B+m log(m+2)) space | AC | 0.187 s | 2776 KB | 11325494 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
