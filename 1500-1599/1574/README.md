# 1574. Mathematicians and Brackets

[Timus 1574](https://acm.timus.ru/problem.aspx?space=1&num=1574) · difficulty 353 · strings

Original problem by Alexander Toropov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a non-empty line of up to 100000 brackets, count the cyclic shifts, by 0 to
n − 1 characters, that turn it into a correct bracket sequence. Shifts
by different amounts count separately even when they give the same line.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The line of brackets.

## Output

The number of such shifts.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
)(()
```

Output:

```
1
```

### Example 2

Input:

```
)()(
```

Output:

```
2
```

### Example 3

Input:

```
()
```

Output:

```
1
```

## Solution

If the numbers of opening and closing brackets differ, no shift works.
Otherwise take the balance after each prefix: opening brackets minus
closing ones. A shift that starts right after position i changes every
balance by −p(i), where p(i) is the balance there, so it never goes
below zero exactly when p(i) is the lowest balance of all. The answer is
the number of prefixes whose balance equals that minimum. `O(n)`.

Pitfalls:

- a line such as `)()(` gives the same correct line by two different
  shifts, and both count (the second example);
- the shift by zero counts too (the third example);
- an unbalanced line has no answer but 0, even when a shift keeps every
  balance non-negative (tests 04, 05).

## Optimized solutions

`1574_strings_optimized.java`. Java keeps the online balance, minimum prefix balance and number of visits to that minimum. Scan input in 16384-byte blocks, ignoring non-bracket separators. A new minimum resets the count to one; an equal minimum increments it. If final balance is nonzero, return zero. Otherwise prefixes of lengths 1..N count exactly the valid cyclic cuts: the full prefix replaces the empty prefix, which is the same cut. No bracket string or prefix array is retained. Time O(N), auxiliary space O(1) with fixed buffering; counters fit int for N<=100000. The teaching prefix-array version and the separately documented Python implementation remain available.

Exact-source Java 1.8 Accepted #11327330: 0.109 s / 560 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/22, memory 2/22. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11325019 was 0.125 s / 480 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1574_strings_optimized.java`: 0.109 s / 560 KB; retained teaching base `1574_strings.java`: 0.125 s / 1196 KB.

`1574_strings_optimized.py`. Keep online balance, lowest prefix and the count of visits to that minimum; a nonzero final balance yields zero. For a balanced string, excluding the empty prefix still counts exactly the valid cyclic shifts. Python now reads fixed B=4096-byte blocks instead of the whole bracket string, retaining no input-length array or string. Both time O(N) and O(B) buffered storage hold, plus bounded counters; flush before direct exit. Java already streams, and the teaching prefix-array solution remains.

Exact-source CPython 3.12 Accepted #11326664: 0.093 s / 676 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 1/45, memory rank 9/45. Below 1024 KB, strict admission uses time only.

- `1574_strings_optimized.py`: 0.093 s / 676 KB; retained teaching base `1574_strings.py` (Python 3.12 x64): 0.093 s / 5252 KB; time change +0.0%; memory change -87.1%.

`1574_strings_optimized.cpp`. Keep the exact online minimum-prefix-balance count. Read brackets in 16 KiB blocks with fread instead of one locked getchar call per character. A new lower balance resets the count to one; an equal minimum increments it. Ignore non-bracket separators as before, and output zero unless the final balance is zero. The nonempty full-length prefix represents the cyclic cut at the start. Time O(n), fixed auxiliary storage.

Exact-source Accepted #11326997: 0.015 s / 92 KB. Saved G++ 13.2 sample, 2026-11-20: time rank 1/58, memory rank 1/56. Teaching sources remain unchanged.

Earlier documented Python measurement: Compared with `1574_strings.py`: time 0.093 s → 0.14 s; memory 5252 KB → 1 412 KB.

The C++, Go and Rust variants count occurrences of the minimum prefix balance while reading the input. When a lower balance appears, reset the count to one. Count the prefixes of lengths 1 through n. When the final balance is zero, the length-n prefix replaces the empty prefix and the two represent the same cyclic cut. C++ uses buffered standard I/O, Go reads fixed-size blocks and Rust reads through the standard input buffer. Each takes O(n) time and O(1) extra space.

The retained accepted base implementations [1574_strings.rs](1574_strings.rs) also meet strict fast-set admission in the saved comparison: top ten or top 15% for the required metrics. They are reused without identical copies; the other teaching sources remain. An asterisk denotes the separate language rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1574_strings.cpp](1574_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 500 KB | 11287829 |
| [1574_strings.go](1574_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1768 KB | 11287832 |
| [1574_strings.java](1574_strings.java) \* | Java 1.8 | strings | O(n) | AC | 0.125 s | 1196 KB | 11287835 |
| [1574_strings.py](1574_strings.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 5252 KB | 11287834 |
| [1574_strings.rs](1574_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 2068 KB | 11287836 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1574_strings_optimized.cpp](1574_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 92 KB | 11326997 |
| [1574_strings_optimized.go](1574_strings_optimized.go) \* | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 824 KB | 11310380 |
| [1574_strings_optimized.rs](1574_strings_optimized.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 208 KB | 11310379 |
| [1574_strings_optimized.java](1574_strings_optimized.java) | Java 1.8 | strings | O(N) time; O(1) auxiliary space | AC | 0.109 s | 560 KB | 11327330 |
| [1574_strings_optimized.py](1574_strings_optimized.py) | Python 3.12 x64 | strings | O(N) time; O(B) buffer space | AC | 0.093 s | 676 KB | 11326664 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
