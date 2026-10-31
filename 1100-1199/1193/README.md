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

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1193_greedy.go](1193_greedy.go).
- [1193_greedy.rs](1193_greedy.rs).

- All languages sort the students by preparation time and run the same
  loop.

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
