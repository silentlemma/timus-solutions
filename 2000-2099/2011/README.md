# 2011. At Least Six Distinct Arrangements

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · difficulty 103 · combinatorics

Original problem by Alexey Kungurtsev, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

You have `n` symbols, each of one of three types. Rearrange all of them
into a word of length `n`; equal symbols are indistinguishable. Decide
whether at least six different words are possible. Every available
symbol must be used exactly once.

## Input

The first line contains `n`, `1 ≤ n ≤ 100`. The second contains `n`
integers from 1 to 3 specifying symbol types. Time limit 0.5 seconds,
memory 64 MB.

## Output

Print `Yes` if there are at least six different words, or `No`
otherwise. Capitalization matters. The unique answer is compared token
by token.

## Checking

Outputs are compared token by token.

## Examples

```
6
1 2 2 3 3 3
```

```
Yes
```

The multiplicities are 1, 2 and 3. There are `6!/(1!·2!·3!)=60`
different words, so the answer is `Yes`.

## Solution

Pieces of the same kind are equal, so k pieces with c₁, c₂, c₃ of each
kind make k!/(c₁!·c₂!·c₃!) different words. Read the pieces one by one
and keep this count for the pieces read so far: when the k-th piece
comes and its kind now occurs c times, the count is multiplied by k and
divided by c, exactly. As soon as the count reaches 6 the answer is
`Yes`: the remaining pieces, appended in a fixed order, keep the words
different. If it never reaches 6, the answer is `No`. `O(n)`.

The count is at most 5 before each step, so 5 · 100 fits any integer
type; multiply before dividing.

Pitfalls:

- exactly six words is already `Yes`;
- do not compute the full factorials: they overflow.

## Optimized solutions

`2011_combinatorics_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327046 measures 0.078 s / 732 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 1/52, memory rank 41/52. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11325480, 0.156 s / 264 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`2011_combinatorics_optimized.py`. Keep the exact multinomial recurrence ways=ways*length/count[value] and stop once it reaches six. Parse 4096-byte chunks directly into three frequencies instead of materializing all input integers before the early exit. The number of arrangements cannot decrease when appending an item, so the unread suffix cannot undo success. Worst-case O(n) time and O(B) storage for bounded tokens and chunk size B. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `2011_combinatorics.py`: time 0.109 s → 0.156 s; memory 516 KB → 264 KB.

`2011_combinatorics_optimized.java`. Keep the incremental multinomial count ways=ways*length/count[newType] and stop as soon as it reaches six. Adding a symbol cannot reduce this count, so ignoring the unread suffix after Yes is valid. Java retains the existing early-stop algorithm but replaces Scanner. Rust removes the complete input String and parsed value vector and consumes each type directly; both keep only three counters, taking O(n) worst-case time and O(1) auxiliary storage. Before each update ways<=5 and n<=100, so the product is at most 500 and fits ordinary integer types; no factorial or big integers are needed. The comparison remains >=6 and output capitalization stays Yes/No.

Compared with `2011_combinatorics.java`: time 0.125 s → 0.109 s; memory 1668 KB → 496 KB.

`2011_combinatorics_optimized.rs`. Keep the incremental multinomial count ways=ways*length/count[newType] and stop as soon as it reaches six. Adding a symbol cannot reduce this count, so ignoring the unread suffix after Yes is valid. Java retains the existing early-stop algorithm but replaces Scanner. Rust removes the complete input String and parsed value vector and consumes each type directly; both keep only three counters, taking O(n) worst-case time and O(1) auxiliary storage. Before each update ways<=5 and n<=100, so the product is at most 500 and fits ordinary integer types; no factorial or big integers are needed. The comparison remains >=6 and output capitalization stays Yes/No.

Compared with `2011_combinatorics.rs`: time 0.062 s → 0.046 s; memory 232 KB → 64 KB.

The optimized C++ solution counts the values as they are read with
`scanf` instead of `iostream` and a vector, and prints the answer as
soon as it is known: 116 KB instead of 380 KB, with the same time.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2011_combinatorics_optimized.java`: time place 8/127, memory place 10/127 in this comparable sample.

Earlier PyPy comparison: `2011_combinatorics_optimized.py`: time place 47/52, memory place 1/52 in this comparable sample.

`2011_combinatorics_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB | 11292493 |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB | 11292495 |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.125 s | 1668 KB | 11303363 |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB | 11292497 |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB | 11292499 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2011_combinatorics_optimized.cpp](2011_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 116 KB | 11303791 |
| [2011_combinatorics_optimized.java](2011_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(n) | AC | 0.109 s | 496 KB | 11324782 |
| [2011_combinatorics_optimized.rs](2011_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.046 s | 64 KB | 11324869 |
| [2011_combinatorics_optimized.py](2011_combinatorics_optimized.py) \* | Python 3.12 x64 | combinatorics | O(n) time; O(B) space | AC | 0.078 s | 732 KB | 11327046 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
