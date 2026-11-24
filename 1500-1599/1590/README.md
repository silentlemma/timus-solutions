# 1590. Counting distinct substrings

[Timus 1590](https://acm.timus.ru/problem.aspx?space=1&num=1590) · difficulty 186 · strings

Original problem by Alexey Zhevak, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a nonempty string of `N ≤ 5000` lowercase Latin letters, count its distinct nonempty contiguous substrings. Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The string.

## Output

The number of distinct substrings.

## Checking

The output integer is compared as a whitespace-separated token.

## Examples

### Example 1

Input:

```
aaba
```

Output:

```
8
```

## Solution

The preferred simple algorithm sorts all suffixes lexicographically.
The suffix starting at position `i` has `N−i` nonempty prefixes. Among
these, exactly its longest common prefix with the preceding sorted suffix
has already appeared: suffixes sharing a given prefix form a contiguous
interval in lexicographic order. Thus the answer is `N(N+1)/2` minus the
sum of LCP lengths of adjacent sorted suffixes. The first suffix contributes
all its prefixes. This counts every distinct substring once.

The five `sorting_strings` files implement this direct algorithm. Sorting
may compare `O(N)` characters per comparison, so worst-case time is
`O(N² log N)`. C++ string views, Go slices and Rust borrowed slices require
`O(N)` auxiliary storage. Java 8 substrings and Python bytes slices are
copies, requiring `O(N²)` storage. Python finds each adjacent LCP by binary
search on prefix equality, using C-level byte comparisons; this retains
the stated time bound. All five implementations pass the judge.

All five original suffix-automaton sources are also retained. Their states
group substrings by end-position sets; state `v` contributes
`len(v)−len(link(v))` distinct lengths. Summing over non-root states gives
the same count in `O(N)` time and space for the fixed alphabet of 26 letters.
Clones copy transitions and inherit the old suffix link.

## Optimized solutions

`1590_strings_optimized.py`. Keep the suffix automaton, exact clone redirection and sum len(v)−len(link(v)). For N<=5000, at most 2N+1 states fit 16-bit indices. Store the fixed alphabet’s 26 transitions per state in one dense unsigned-16-bit array, with zero for missing transitions; lengths and signed suffix links use separate 16-bit arrays. Cloning copies exactly 26 transitions. The transition table is at most 520052 bytes; this is not total process memory. Time/space O(26N) for the fixed alphabet. The run uses 1120 KB versus the prior optimized 1084 KB, while time improves; retain all suffix-sorting and readable automaton versions.

Exact-source CPython 3.12 Accepted #11326686: 0.093 s / 1120 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 4/64, memory rank 1/64. At least 1024 KB: both strict metrics are required and pass.

- `1590_strings_optimized.py`: 0.093 s / 1120 KB; retained teaching base `1590_sorting_strings.py` (Python 3.12 x64): 0.109 s / 14664 KB; time change -14.7%; memory change -92.4%.

The preferred teaching algorithm sorts suffixes and subtracts adjacent longest common prefixes from the number of substring occurrences. The compact C++ variant sorts suffix starting positions without copying every suffix, reducing storage while retaining its worst-case quadratic-comparison cost. The compact Java and Rust suffix automata use flat edge lists; each clone copies its own list before redirection. The current Python compact automaton instead uses the dense 16-bit transition table described above. These are different algorithms and their names and measured comparisons remain separate. A memory saving may come with slower time, or the reverse.

- `1590_strings.java`: 0.093 s / 2412 KB; base `1590_sorting_strings.java`: 0.187 s / 28464 KB; relative change: time -50.3%, memory -91.5%.
- `1590_strings.py`: 0.109 s / 3132 KB; base `1590_sorting_strings.py`: 0.109 s / 14664 KB; relative change: time -0.0%, memory -78.6%.
- `1590_strings.rs`: 0.015 s / 2272 KB; base `1590_sorting_strings.rs`: 0.046 s / 300 KB; relative change: time -67.4%, memory +657.3%.
- `1590_strings_optimized.java`: 0.109 s / 748 KB; base `1590_sorting_strings.java`: 0.187 s / 28464 KB; relative change: time -41.7%, memory -97.4%.

- `1590_strings_optimized.rs`: 0.015 s / 504 KB; base `1590_sorting_strings.rs`: 0.046 s / 300 KB; relative change: time -67.4%, memory +68.0%.
- `1590_sorting_strings_optimized.cpp`: 0.031 s / 152 KB; base `1590_sorting_strings.cpp`: 0.015 s / 508 KB; relative change: time +106.7%, memory -70.1%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1590_sorting_strings.cpp`; covering source `1590_sorting_strings_optimized.cpp`; time/memory places 43/1, other-author entries 119/119.

- Go: preferred teaching base `1590_sorting_strings.go`; covering source `1590_sorting_strings.go`; time/memory places 1/1, other-author entries 2/2.

- Java: preferred teaching base `1590_sorting_strings.java`; covering source `1590_strings.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: Exact-source CPython 3.12 Accepted #11326686: 0.093 s / 1120 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 4/64, memory rank 1/64. At least 1024 KB: both strict metrics are required and pass.

- Rust: preferred teaching base `1590_sorting_strings.rs`; covering source `1590_sorting_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1590_sorting_strings.cpp](1590_sorting_strings.cpp) | G++ 13.2 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix views | AC | 0.015 s | 508 KB | 11308193 |
| [1590_sorting_strings.go](1590_sorting_strings.go) | Go 1.14 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix views | AC | 0.031 s | 1192 KB | 11308194 |
| [1590_sorting_strings.java](1590_sorting_strings.java) | Java 1.8 | sorting, strings | O(N² log N) time, O(N²) space for copied Java 8 suffix strings | AC | 0.187 s | 28464 KB | 11308195 |
| [1590_sorting_strings.py](1590_sorting_strings.py) | Python 3.12 x64 | sorting, strings | O(N² log N) time, O(N²) space for copied suffixes; prefix equality tested by binary search | AC | 0.109 s | 14664 KB | 11308191 |
| [1590_sorting_strings.rs](1590_sorting_strings.rs) | Rust 1.75 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix slices | AC | 0.046 s | 300 KB | 11308196 |
| [1590_strings.cpp](1590_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1428 KB | 11287986 |
| [1590_strings.go](1590_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2328 KB | 11287991 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1590_strings.java](1590_strings.java) | Java 1.8 | strings | O(N) | AC | 0.093 s | 2412 KB | 11287997 |
| [1590_strings.py](1590_strings.py) \* | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 3132 KB | 11287994 |
| [1590_strings.rs](1590_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.015 s | 2272 KB | 11287999 |
| [1590_strings_optimized.java](1590_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.109 s | 748 KB | 11308188 |
| [1590_strings_optimized.py](1590_strings_optimized.py) | Python 3.12 x64 | strings | O(26N) time and space | AC | 0.093 s | 1120 KB | 11326686 |
| [1590_strings_optimized.rs](1590_strings_optimized.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.015 s | 504 KB | 11308189 |
| [1590_sorting_strings_optimized.cpp](1590_sorting_strings_optimized.cpp) \* | G++ 13.2 x64 | sorting, strings | O(N^2 log N) | AC | 0.031 s | 152 KB | 11309286 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
