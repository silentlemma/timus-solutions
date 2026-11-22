# 2068. Parity of the number of splits

[Timus 2068](https://acm.timus.ru/problem.aspx?space=1&num=2068) · difficulty 108 · games

Original problem by Alexey Danilyuk, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n heaps of nuts, each with an odd number of nuts. Two players
take turns; a move splits one heap into three non-empty heaps, each again
with an odd number of nuts. A player who cannot move loses. Daenerys
moves first, then Stannis. Find the winner under optimal play. The limits
are 1 second and 64 MB.

## Input

An odd n, 1 ≤ n ≤ 777, then n odd heap sizes from 1 to 54321.

## Output

`Daenerys` if she wins, otherwise `Stannis`.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
1
3
```

Output:

```
Daenerys
```

### Example 2

Input:

```
3
1 1 1
```

Output:

```
Stannis
```

### Example 3

Input:

```
5
777 313 465 99 1
```

Output:

```
Daenerys
```

## Solution

No strategy matters here. A move replaces one heap by three, so the
number of heaps grows by exactly two, and the total number of nuts never
changes. The game is over exactly when every heap holds one nut: a heap
of 3 or more odd nuts can always be split as 1 + 1 + (a − 2). At that
point there are as many heaps as nuts, so the number of moves made is
always (S − n) / 2, the sum of (aᵢ − 1) / 2 over the heaps.

Daenerys makes the odd-numbered moves, so she wins exactly when this
number is odd. In the third example the heaps give
388 + 156 + 232 + 49 + 0 = 825 moves, which is odd. The work is O(n).

## Optimized solutions

`2068_games_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327048 measures 0.078 s / 696 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 5/50, memory rank 37/50. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11325080, 0.109 s / 236 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`2068_games_optimized.java`. Keep the same XOR of ((heap−1)/2) parity. Read from the existing standard input stream without an additional byte array, and write the fixed winner bytes through System.out.write followed by flush. This avoids String encoding while using the ordinary permitted standard stream; no FileDescriptor access is used. O(N) time and constant auxiliary space.

Compared with `2068_games.java`: time 0.109 s → 0.093 s; memory 480 KB → 340 KB.

`2068_games_optimized.py`. Keep the fixed-total-moves invariant: a split adds two heaps, so heap a contributes (a-1)//2 moves before all nuts are singleton heaps. Only the sum parity matters. XOR each contribution parity as its integer arrives rather than storing all text tokens and summing the full count. A bounded 65536-byte tokenizer retains only parser blocks and an unfinished token; game state is one bit. Time O(N) for bounded heap sizes, storage bounded independently of N. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `2068_games.py`: time 0.093 s → 0.109 s; memory 388 KB → 236 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

Earlier PyPy comparison: `2068_games_optimized.py`: time place 33/50, memory place 1/50 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games.cpp](2068_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 124 KB | 11294416 |
| [2068_games.go](2068_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1108 KB | 11294420 |
| [2068_games.java](2068_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 480 KB | 11304044 |
| [2068_games.py](2068_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.093 s | 388 KB | 11304045 |
| [2068_games.rs](2068_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.015 s | 256 KB | 11304046 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games_optimized.py](2068_games_optimized.py) \* | Python 3.12 x64 | games | O(N) | AC | 0.078 s | 696 KB | 11327048 |
| [2068_games_optimized.java](2068_games_optimized.java) \* | Java 1.8 | games | O(N) time; O(1) space | AC | 0.093 s | 340 KB | 11325849 |


\* Accepted; the rating target is not yet met. This version may be optimized further.
