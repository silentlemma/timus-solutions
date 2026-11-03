# 1183. The shortest regular bracket sequence containing a given one

[Timus 1183](https://acm.timus.ru/problem.aspx?space=1&num=1183) · difficulty 197 · dp

Original problem by Andrew Stankevich, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given up to 100 characters from `(`, `)`, `[`, `]`, print a shortest
regular bracket sequence that contains them as a subsequence.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The brackets on one line, possibly empty.

## Output

A shortest regular sequence containing them.

## Checking

Check a balanced typed-bracket result, the input subsequence and minimum added length. New Java passed 507 actual main invocations with a fresh classloader; the independent oracle maximizes noncrossing matching pairs, including empty and 100-character inputs.

## Examples

### Example 1

Input:

```
([(]
```

Output:

```
()[()]
```

## Solution

Let `d[i][j]` be the fewest insertions making `s[i..j)` regular.
The empty interval costs zero; a singleton costs one. For a longer interval,
try wrapping `d[i+1][j−1]` when the endpoints are a matching opening/closing
pair, and every split `d[i][k]+d[k][j]`, `i<k<j`.

Why is this complete? A balanced completion pairs brackets without crossing.
An optimal completion needs no pair consisting of two inserted brackets:
deleting such a matched pair preserves balance and the input subsequence.
If the first original bracket is unmatched to another original bracket,
complete it as a singleton and split. Otherwise its partner is either the
last original bracket (wrap) or an earlier one (split after that partner).
Noncrossing pairs keep both subproblems independent. Induction on interval
length proves the recurrence. Remembering a winning transition reconstructs
an optimal balanced supersequence, preserving every original character.
Time `O(n³)`, storage `O(n²)` for `n≤100`.

Read one whole line, including an empty line; output then is empty too.
Any minimum-length balanced answer containing the input as a subsequence
is allowed. The original five Accepted sources retain their explicit
decision tables. Python reconstructs with an explicit stack; the others
use recursion of depth at most `n`.

## Optimized solutions

The minimum-insertion interval DP remains unchanged. C++ stores costs as bytes, stops split enumeration at the interval parity lower bound, and reconstructs an optimum from costs without a separate choice table. Java stores only `i≤j` half-open intervals, including empty ones, in an upper triangle. Its index is `i(2N+1−i)/2+j`, using `(N+1)(N+2)/2` bytes instead of a full square. Every cost is between zero and N≤100, so signed bytes are sufficient. Java reconstructs with a bounded explicit task stack: paired endpoints schedule their interior and a closing bracket; a split schedules the right then left interval. This preserves the input as a subsequence and emits exactly an optimal completion. The output has at most 2N brackets. Worst-case time remains `O(N^3)` and memory `O(N^2)`; the reduction is in representation and reconstruction overhead. All readable base sources are retained.

- `1183_dp_optimized.cpp`: 0.015 s / 80 KB; base `1183_dp.cpp`: 0.015 s / 460 KB; relative change: time -0.0%, memory -82.6%.
- `1183_dp_optimized.java`: 0.109 s / 416 KB; base `1183_dp.java`: 0.078 s / 616 KB; relative change: time +39.7%, memory -32.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1183_dp.cpp`; covering source `1183_dp_optimized.cpp`; time/memory places 1/1, other-author entries 89/89.

- Go: preferred teaching base `1183_dp.go`; covering source `1183_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1183_dp.java`; covering source `1183_dp_optimized.java`; time/memory places 2/1, other-author entries 6/6.

- Python/PyPy: preferred teaching base `1183_dp.py`; covering source `1183_dp.py`; time/memory places 1/1, other-author entries 23/23.

- Rust: preferred teaching base `1183_dp.rs`; covering source `1183_dp.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1183_dp.cpp](1183_dp.cpp) | G++ 13.2 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.015 s | 460 KB | 11283343 |
| [1183_dp.go](1183_dp.go) | Go 1.14 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.031 s | 1232 KB | 11283344 |
| [1183_dp.java](1183_dp.java) | Java 1.8 | dp | O(N^3) time; O(N^2) space | AC | 0.078 s | 616 KB | 11283347 |
| [1183_dp.py](1183_dp.py) | Python 3.12 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.078 s | 876 KB | 11283345 |
| [1183_dp.rs](1183_dp.rs) | Rust 1.75 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.001 s | 308 KB | 11283349 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1183_dp_optimized.cpp](1183_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.015 s | 80 KB | 11308418 |
| [1183_dp_optimized.java](1183_dp_optimized.java) \* | Java 1.8 | dp | O(N^3) time; O(N^2) space | AC | 0.109 s | 416 KB | 11309557 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
