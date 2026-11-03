# 1138. The longest run of jobs where every raise is a whole number of percent

[Timus 1138](https://acm.timus.ru/problem.aspx?space=1&num=1138) · difficulty 204 · dp

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A programmer's first salary was exactly `s`, every next salary is a
positive integer larger than the previous one by a whole number of
percent, and the last salary is at most `n`, with `1 ≤ n, s ≤ 10000`. Find
the largest possible number of jobs, counting the first one.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `s`.

## Output

The largest number of jobs.

## Checking

Compare one integer token. The retained native additions have 380 saved extra main-program checks each: 320 tiny exact-path enumerations and 60 boundary regressions. The revised teaching Python has 7730 source executions against a literal salary-DAG oracle, 7260 successor-set comparisons, 12 repository tests and 169 extra PyPy target checks, including maximum n. These counts are distinct checks, not native-language totals.

## Examples

### Example 1

Input:

```
10 2
```

Output:

```
5
```

## Solution

Let `jobs[a]` be the longest run starting at `s` and ending at salary `a`.
A raise to `b>a` is valid exactly when `100(b−a)` is divisible by `a`.
The four native teaching programs try every larger integer salary `b`,
updating `jobs[b] = max(jobs[b], jobs[a]+1)` for valid raises. Only `jobs[s]=1`
is initialized. Salaries strictly increase, so ascending processing is a
topological order: induction proves that every longest path is considered.
These versions use `O(n²)` time and `O(n)` memory.

The accepted teaching Python uses another direct enumeration: for each
reachable `a`, try every positive integer percentage `p` up to
`floor(100(n−a)/a)`. Accept it only when `a*p % 100 == 0`, then update salary
`a+a*p/100`. Each valid successor has exactly one such percentage, so the
same DP proof applies. This requires no gcd argument. Its worst-case bound
is `O(P n log n)` percentage checks, `P=100`, and `O(n)` memory; it is not the
quadratic pair scan. It was accepted under PyPy 3.10. The earlier Python
pair scan exceeded the time limit and is not published.

Return zero if `s>n`; count the first job if `s≤n`. Raises must be positive.
Skip unreachable salaries. Products are at most one million and job counts
at most 10000, so native 32-bit arithmetic suffices.

## Optimized solutions

Put `P=100`, `g=gcd(a,P)`. Since `a/g` and `P/g` are coprime,
`a | P(b−a)` is equivalent to `(a/g) | (b−a)`. Thus the valid successors
are exactly `a+a/g, a+2a/g, …`. Generate only these successors instead of
testing all salaries or all percentages. The same topological DP remains
correct. There are at most `Pn/a` updates at salary `a`, hence
`O(P n log n+n log P)` time including gcd computations and `O(n)` memory.
Java additionally precomputes `gcd(r,100)` for the 100 possible residues
and uses StreamTokenizer rather than Scanner.

All five earlier gcd programs are preserved. They are different from the
direct teaching enumerations, so their existing `dp` names remain. The
additional Java `_optimized` keeps the gcd algorithm. Comparisons below use
the actual preferred base of each language. In particular, the Python
comparison includes the CPython/PyPy runtime difference; its memory saving
does not imply a better rank in both metrics.

- `1138_dp.cpp`: 0.015 s / 224 KB; base `1138_bruteforce_dp.cpp`: 0.125 s / 208 KB; relative change: time -88.0%, memory +7.7%.
- `1138_dp.go`: 0.031 s / 1144 KB; base `1138_bruteforce_dp.go`: 0.546 s / 1140 KB; relative change: time -94.3%, memory +0.4%.
- `1138_dp.java`: 0.125 s / 1680 KB; base `1138_bruteforce_dp.java`: 0.296 s / 460 KB; relative change: time -57.8%, memory +265.2%.
- `1138_dp.py`: 0.093 s / 508 KB; base `1138_bruteforce_dp.py`: 0.140 s / 1988 KB; relative change: time -33.6%, memory -74.4%.
- `1138_dp.rs`: 0.015 s / 256 KB; base `1138_bruteforce_dp.rs`: 0.234 s / 236 KB; relative change: time -93.6%, memory +8.5%.
- `1138_dp_optimized.java`: 0.093 s / 448 KB; base `1138_bruteforce_dp.java`: 0.296 s / 460 KB; relative change: time -68.6%, memory -2.6%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1138_bruteforce_dp.cpp`; covering source `1138_dp.cpp`; time/memory places 1/2, other-author entries 64/64.

- Go: preferred teaching base `1138_bruteforce_dp.go`; covering source `1138_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1138_bruteforce_dp.java`; covering source `1138_dp_optimized.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1138_bruteforce_dp.py`; covering source `1138_dp.py`; time/memory places 2/3, other-author entries 10/10.

- Rust: preferred teaching base `1138_bruteforce_dp.rs`; covering source `1138_dp.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1138_bruteforce_dp.cpp](1138_bruteforce_dp.cpp) | G++ 13.2 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.125 s | 208 KB | 11308262 |
| [1138_bruteforce_dp.go](1138_bruteforce_dp.go) | Go 1.14 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.546 s | 1140 KB | 11308263 |
| [1138_bruteforce_dp.java](1138_bruteforce_dp.java) | Java 1.8 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.296 s | 460 KB | 11308265 |
| [1138_bruteforce_dp.py](1138_bruteforce_dp.py) | PyPy 3.10 x64 | bruteforce, dp | O(P n log n) time; O(n) space, P=100 | AC | 0.140 s | 1988 KB | 11309354 |
| [1138_bruteforce_dp.rs](1138_bruteforce_dp.rs) | Rust 1.75 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.234 s | 236 KB | 11308269 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1138_dp.cpp](1138_dp.cpp) | G++ 13.2 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.015 s | 224 KB | 11279425 |
| [1138_dp.go](1138_dp.go) | Go 1.14 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.031 s | 1144 KB | 11279426 |
| [1138_dp.java](1138_dp.java) \* | Java 1.8 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.125 s | 1680 KB | 11279429 |
| [1138_dp.py](1138_dp.py) \* | Python 3.12 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.093 s | 508 KB | 11279428 |
| [1138_dp.rs](1138_dp.rs) | Rust 1.75 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.015 s | 256 KB | 11279431 |
| [1138_dp_optimized.java](1138_dp_optimized.java) | Java 1.8 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.093 s | 448 KB | 11308275 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
