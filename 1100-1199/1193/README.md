# 1193. How much earlier must an oral exam start for everyone to finish in time?

[Timus 1193](https://acm.timus.ru/problem.aspx?space=1&num=1193) · difficulty 181 · greedy

Original problem by Anatoly Uglov, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 40` students get their questions when an oral exam starts. Student
`i` prepares for `T1` minutes (all different) and then answers for `T2`
minutes, one student at a time, in the order they finish preparing; a
student who finishes preparing while someone is answering waits in a
queue. Each student must be done by `T3` minutes after the planned start.
Find the least number of minutes to start the exam earlier so that
everyone is done in time.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` (`1 ≤ N ≤ 40`), then `T1 T2 T3` for each student, with
`0 ≤ T1 ≤ T3 ≤ 600` and `1 ≤ T2 ≤ 240`. All `T1` values are distinct.

## Output

The number of minutes, 0 if no shift is needed.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3
100 10 120
70 40 150
99 15 400
```

Output:

```
15
```

### Example 2

Input:

```
2
100 10 110
80 15 100
```

Output:

```
0
```

## Solution

Starting earlier by `s` minutes moves everything by `s`: the order of the
queue and every wait stay the same, and only the deadlines move `s`
minutes later relative to the start. So simulate the exam once, in order
of `T1`: each answer starts when the student is ready or when the
previous answer ends, whichever is later. The answer is the largest
lateness, the finish time minus `T3`, or 0 if nobody is late. `O(N log N)`
for the sort.

Pitfalls:

- the queue is ordered by the end of preparation, not by the input order;
- a student who is ready while nobody is answering starts at once, so the
  answering line can stand idle between students;
- the shift cannot be negative: if everyone is early, the answer is 0.

The answers were compared with a separately written solution, which
binary searches for the shift, on 300 random exams and on every test.

## Optimized solutions

`1193_greedy_sorting.java`. The same readiness-ordered exam simulation uses direct-address ordering instead of comparison sorting: all T1 are distinct integers in 0..600. Store (T2<<10)|T3 in the T1 slot; T2≥1 makes zero an unoccupied marker and T3≤600 fits ten bits. Scan occupied slots in increasing time, updating finish=max(finish,T1)+T2 and worst lateness. O(N+601) time and 601 integer slots, with a 256-byte decimal output buffer. This distinct ordering implementation is named greedy_sorting; the readable sort and prior optimized alternative remain.

Exact-source Java 1.8 Accepted #11327835: 0.078 s / 356 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 1/42; 1/42. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. Both metrics rank first; no asterisk. The preserved previous variant has its own paired receipt #11307308 (Java 1.8): 0.125 s / 376 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1193_greedy_sorting.java`: 0.078 s / 356 KB; retained teaching base `1193_greedy.java` (Java 1.8): 0.14 s / 3776 KB.

The optimized C++ solution keeps the students in a static array of
40 records, enough since `N ≤ 40`, instead of a vector of tuples
allocated on the heap; the sort and the simulation are the same:
{1193_greedy_optimized.cpp}.

The optimized Java solution reads the numbers byte by byte from 4 KB
blocks instead of with `Scanner`, and keeps the students in three `int`
arrays, putting each one in its place by insertion as it is read,
instead of sorting an array of triples with a lambda comparator. With at
most 40 students the quadratic insertion sort costs nothing:
{1193_greedy_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1193_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +39.58%; base: `1193_greedy.cpp`.

- `1193_greedy_optimized.java`: time reduction +10.71%; memory reduction
  +90.04%; base: `1193_greedy.java`.

`1193_greedy_optimized.rs`. Keep the same schedule sorted by distinct preparation times and the recurrence busy=max(busy,ready)+talk. The answer is the largest positive busy-deadline. Use an unstable in-place sort of the student vector, with no stable-sort temporary storage or full decoded input. Time O(N log N), storage O(N). The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1193_greedy.rs`: time 0.015 s → 0.046 s; memory 236 KB → 76 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1193_greedy_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1193_greedy.cpp](1193_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB | 11283459 |
| [1193_greedy.go](1193_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1116 KB | 11283460 |
| [1193_greedy.java](1193_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 3776 KB | 11283464 |
| [1193_greedy.py](1193_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 380 KB | 11283463 |
| [1193_greedy.rs](1193_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 236 KB | 11283465 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1193_greedy_optimized.cpp](1193_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 116 KB | 11307306 |
| [1193_greedy_optimized.java](1193_greedy_optimized.java) | Java 1.8 | greedy | O(N²) | AC | 0.125 s | 376 KB | 11307308 |
| [1193_greedy_sorting.java](1193_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(N+601) time; 601 integer slots | AC | 0.078 s | 356 KB | 11327835 |
| [1193_greedy_optimized.rs](1193_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 76 KB | 11325093 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
