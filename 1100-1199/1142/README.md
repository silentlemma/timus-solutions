# 1142. Counting the orderings with ties of N objects

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · difficulty 155 · combinatorics

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Between any two of `N` comparable objects one of `a = b`, `a < b`,
`b < a` holds. Count the different ways to order `N` objects in this
sense, allowing ties: for three objects there are 13, from
`a = b = c` to `c < b < a`. Answer this for several `N` from 2 to 10; the
input ends with `-1`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Values of `N`, one per line, then `-1`.

## Output

The count for each `N`, one per line.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
2
3
-1
```

Output:

```
3
13
```

## Solution

An ordering with ties is a sequence of groups of equal objects, the
groups strictly increasing. Look at the first group: it is any nonempty
set of `k` objects, chosen in `C(n, k)` ways, and the remaining `n − k`
objects form an ordering with ties of their own. So with `a(0) = 1`

`a(n) = Σ_{k=1..n} C(n, k)·a(n − k)`.

These are the ordered Bell (Fubini) numbers 1, 1, 3, 13, 75, 541, …; the
largest needed, `a(10) = 102247563`, fits in 32 bits. The table is built
once with Pascal's triangle, and each query is a lookup. `O(10²)` to build.

Pitfalls:

- the input has no count; read until `-1`;
- the same `N` may be asked several times.

The values were compared with the independent formula
`a(n) = Σ k!·S(n, k)` with Stirling numbers of the second kind, and for
`n ≤ 6` with a listing of all orderings.

## Optimized solutions

`1142_combinatorics_optimized.go`. The recurrence and complete 11×11 Pascal matrix are unchanged. Precompute ordered-partition counts for L=10, then stream Q queries until the negative sentinel or EOF. This Go revision changes I/O overhead, not the combinatorial algorithm or table storage. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1142_combinatorics.go`: time 0.001 s → 0.015 s; memory 1084 KB → 272 KB.

`1142_combinatorics_optimized.py`. Keep the weak-order recurrence, but generate C(n,k) incrementally as choose*(n-k+1)//k instead of storing Pascal’s triangle. Retain only the L+1 answer counts, with L=10; precomputation takes O(L²) time. The Python program still retains split input and collected output, so its total space is O(L+I+O) for input/output sizes I,O. Stop on the first negative query. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1142_combinatorics.py`: time 0.031 s → 0.125 s; memory 436 KB → 220 KB.

`1142_combinatorics_optimized.rs`. Keep the weak-order recurrence but generate binomial coefficients incrementally, eliminating the 11×11 Pascal matrix. Use eleven u64 counts; queries are streamed until a negative value or EOF, with direct C-runtime byte output and no retained input/output strings. For maximum L=10 and Q queries, time O(L²+Q), auxiliary space O(L). The teaching Pascal-table implementation remains.

Compared with `1142_combinatorics.rs`: time 0.001 s → 0.001 s; memory 220 KB → 44 KB.

`1142_combinatorics_optimized.java`. Keep the ordered-partition recurrence. Read integers from a 1 KB byte buffer and retain only ways[0..L], L=10; generate each binomial coefficient multiplicatively instead of keeping a Pascal matrix. This removes StreamTokenizer, BufferedReader and PrintWriter. Answers are accumulated in a StringBuilder until a negative query or EOF, then printed together. For Q queries, time is O(L²+Q) and storage O(L+Q), including the buffered output; output storage is not constant. The simple version remains.

Exact-source Accepted #11326631: 0.046 s / 336 KB. In the saved Java 1.8 sample of 2026-11-20: time rank 3/44, memory rank 2/44. The asterisk still denotes the separate language rating target.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1142_combinatorics_optimized.java`: time reduction +50.54%; memory reduction +79.05%; base: `1142_combinatorics.java`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1142_combinatorics_optimized.py`: time place 25/26, memory place 2/26 in this comparable sample.

`1142_combinatorics_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB | 11279451 |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB | 11279453 |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB | 11279455 |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB | 11279454 |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB | 11279457 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics_optimized.java](1142_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(L²+Q) time; O(L+Q) space | AC | 0.046 s | 336 KB | 11326631 |
| [1142_combinatorics_optimized.py](1142_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(L²+I+O) time; O(L+I+O) space | AC | 0.125 s | 220 KB | 11325472 |
| [1142_combinatorics_optimized.rs](1142_combinatorics_optimized.rs) | Rust 1.75 x64 | combinatorics | O(L²+Q) time; O(L) space | AC | 0.001 s | 44 KB | 11325499 |
| [1142_combinatorics_optimized.go](1142_combinatorics_optimized.go) | Go 1.14 x64 | combinatorics | O(L²+Q) time; O(L²) space | AC | 0.015 s | 272 KB | 11325652 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
