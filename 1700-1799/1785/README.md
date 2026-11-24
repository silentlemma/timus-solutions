# 1785. Lost in Localization

[Timus 1785](https://acm.timus.ru/problem.aspx?space=1&num=1785) · difficulty 16 · implementation

Original problem: folklore, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A game names the size of an army by a word instead of a number: 1–4
is "few", 5–9 "several", 10–19 "pack", 20–49 "lots", 50–99 "horde",
100–249 "throng", 250–499 "swarm", 500–999 "zounds", and 1000 or more
"legion". Print the word for a given number of monsters.

## Input

n (1 ≤ n ≤ 2000).

## Output

The word for n.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
7
```

Output:

```
several
```

### Example 2

Input:

```
40
```

Output:

```
lots
```

## Solution

Keep the lower ends of the ranges from the largest down, 1000, 500,
250, 100, 50, 20, 10, 5, 1, next to their words. Skip the ends that are
above n; the first one that is not gives the word. `O(1)`.

In the examples 7 passes 1000 down to 10 and stops at 5, "several";
40 stops at 20, "lots".

Pitfalls:

- the ends belong to the larger word: 5 is "several", 1000 is
  "legion";
- every n from 1000 to 2000 is "legion".

The answers agree with an independent accepted implementation on every
n from 1 to 2000.

## Optimized solutions

`1785_implementation_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327034 measures 0.078 s / 704 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 18/582, memory rank 494/582. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11325075, 0.14 s / 196 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1785_implementation_optimized.go`. Keep the nine fixed army-name intervals with the same inclusive lower bounds. Use descending conditional branches instead of parallel threshold/name arrays and an index search; choose the first matching word, including exact boundaries 5,10,20,50,100,250,500,1000. No general sorting or search algorithm is introduced. The domain 1..2000 and fixed nine cases give O(1) time and state; output spelling is unchanged. Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `1785_implementation.go`: time 0.031 s → 0.015 s; memory 1080 KB → 820 KB.

`1785_implementation_optimized.py`. Keep the nine fixed army-name intervals with the same inclusive lower bounds. Use descending conditional branches instead of parallel threshold/name arrays and an index search; choose the first matching word, including exact boundaries 5,10,20,50,100,250,500,1000. No general sorting or search algorithm is introduced. The domain 1..2000 and fixed nine cases give O(1) time and state; output spelling is unchanged. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1785_implementation.py`: time 0.093 s → 0.14 s; memory 424 KB → 196 KB.

The optimized C++ solution looks the word up in the same table, but
reads with `scanf` and prints with `puts` instead of `iostream`: 116 KB
instead of 376 KB, with the same time.

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.125 s and
340 KB instead of 1600 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1785_implementation_optimized.go`: time place 1/21, memory place 1/21 in this comparable sample.

Earlier PyPy comparison: `1785_implementation_optimized.py`: time place 566/582, memory place 2/582 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1785_implementation.cpp](1785_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 376 KB | 11303506 |
| [1785_implementation.go](1785_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1080 KB | 11289797 |
| [1785_implementation.java](1785_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1600 KB | 11303507 |
| [1785_implementation.py](1785_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 424 KB | 11289798 |
| [1785_implementation.rs](1785_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 228 KB | 11289801 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1785_implementation_optimized.cpp](1785_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303636 |
| [1785_implementation_optimized.java](1785_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 340 KB | 11303777 |
| [1785_implementation_optimized.go](1785_implementation_optimized.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 820 KB | 11328304 |
| [1785_implementation_optimized.py](1785_implementation_optimized.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 704 KB | 11327034 |
