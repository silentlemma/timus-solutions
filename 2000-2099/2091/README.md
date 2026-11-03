# 2091. Two courses that split the programs most evenly

[Timus 2091](https://acm.timus.ru/problem.aspx?space=1&num=2091) · difficulty 271 · bitmask, bruteforce

Original problem by Dmitry Ivankov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × m table says which of m courses each of n programs includes.
Choose two different courses A and B; they split the programs into four
groups: with both, with A only, with B only, with neither. Make the
largest group as small as possible and output its size and the two
courses. Any optimal pair is accepted. The limits are 1 second and
64 MB.

## Input

n and m, 4 ≤ n, m ≤ 100, then the n rows of m zeros and ones.

## Output

The smallest possible size of the largest group, then the two courses.

## Checking

The repository checker verifies the optimum and a valid route/course pair; literal output equality is not required.

- `2091_bitmask.cpp` (G++ 13.2 x64): 13 repository cases.

- `2091_bitmask.go` (Go 1.14 x64): 13 repository cases.

- `2091_bitmask.java` (Java 1.8): 13 repository cases.

- `2091_bitmask.py` (Python 3.12 x64): 13 repository cases.

- `2091_bitmask.rs` (Rust 1.75 x64): 13 repository cases.

## Examples

### Example 1

Input:

```
6 4
0 0 0 1
0 0 1 0
0 1 1 1
1 1 1 1
0 0 0 0
1 0 0 1
```

Output:

```
2
1 3
```

## Solution

There are fewer than 5000 pairs of courses, and the groups of a pair are
counted in one pass over the programs, with the group number
2·[A] + [B]. Trying every pair costs O(m² n), half a million steps.

In the example courses 1 and 3 give the groups {4}, {6}, {2, 3} and
{1, 5}, so the largest has 2 programs.

## Optimized solutions

Keep the direct pair-and-program enumeration. Fast bitmask sources encode program membership once per course. For a pair with course counts ca,cb and intersection count t, the four groups have sizes t,ca-t,cb-t,N-ca-cb+t. Intersection plus population count therefore replaces scanning all N programs for each pair. Test distinct course pairs and minimize the largest group; ceil(N/4) is a universal lower bound, so reaching it permits a proven early exit. Duplicate program rows remain separate bits: their multiplicity must not be lost. For N<=100 native sources use two64-bit words per course; Python uses arbitrary-precision integers. Numerical state uses O(M ceil(N/W)) words; Python/Rust also retain O(NM)input storage. Time is O(NM+M² ceil(N/W)), with at most two native words under the actual bound. The checker accepts any pair attaining the optimum.

- `2091_bitmask.cpp`: 0.015 s / 112 KB; base `2091_bruteforce.cpp`: 0.015 s / 228 KB; relative change: time -0.0%, memory -50.9%.
- `2091_bitmask.go`: 0.015 s / 304 KB; base `2091_bruteforce.go`: 0.031 s / 1200 KB; relative change: time -51.6%, memory -74.7%.
- `2091_bitmask.java`: 0.125 s / 400 KB; base `2091_bruteforce.java`: 0.125 s / 5664 KB; relative change: time -0.0%, memory -92.9%.
- `2091_bitmask.py`: 0.078 s / 592 KB; base `2091_bruteforce.py`: 0.125 s / 676 KB; relative change: time -37.6%, memory -12.4%.
- `2091_bitmask.rs`: 0.015 s / 220 KB; base `2091_bruteforce.rs`: 0.015 s / 464 KB; relative change: time -0.0%, memory -52.6%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `2091_bruteforce.cpp`; covering source `2091_bitmask.cpp`; time/memory places 1/1, other-author entries 56/56.

- Go: preferred teaching base `2091_bruteforce.go`; covering source `2091_bitmask.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2091_bruteforce.java`; covering source `2091_bitmask.java`; time/memory places 2/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `2091_bruteforce.py`; covering source `2091_bitmask.py`; time/memory places 1/1, other-author entries 12/12.

- Rust: preferred teaching base `2091_bruteforce.rs`; covering source `2091_bitmask.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2091_bruteforce.cpp](2091_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 228 KB | 11308118 |
| [2091_bruteforce.go](2091_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m^2 n) | AC | 0.031 s | 1200 KB | 11294643 |
| [2091_bruteforce.java](2091_bruteforce.java) | Java 1.8 | bruteforce | O(m^2 n) | AC | 0.125 s | 5664 KB | 11308125 |
| [2091_bruteforce.py](2091_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m^2 n) | AC | 0.125 s | 676 KB | 11308827 |
| [2091_bruteforce.rs](2091_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 464 KB | 11308829 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2091_bitmask.cpp](2091_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.015 s | 112 KB | 11308002 |
| [2091_bitmask.go](2091_bitmask.go) | Go 1.14 x64 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.015 s | 304 KB | 11309740 |
| [2091_bitmask.java](2091_bitmask.java) \* | Java 1.8 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.125 s | 400 KB | 11308008 |
| [2091_bitmask.py](2091_bitmask.py) | Python 3.12 x64 | bitmask | O(NM+M² ceil(N/W)) time; O(NM+M ceil(N/W)) space | AC | 0.078 s | 592 KB | 11308000 |
| [2091_bitmask.rs](2091_bitmask.rs) | Rust 1.75 x64 | bitmask | O(NM+M² ceil(N/W)) time; O(NM+M ceil(N/W)) space | AC | 0.015 s | 220 KB | 11308009 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
