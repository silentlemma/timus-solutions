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

`N`, then `T1 T2 T3` for each student.

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

## Language notes

- All languages sort the students by preparation time and run the same
  loop.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1193_greedy.cpp](1193_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB |
| [1193_greedy.go](1193_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1116 KB |
| [1193_greedy.java](1193_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 3776 KB |
| [1193_greedy.py](1193_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 380 KB |
| [1193_greedy.rs](1193_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 236 KB |
