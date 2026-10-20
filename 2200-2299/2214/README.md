# 2214. Best value from a sliding window that may move K times

[Timus 2214](https://acm.timus.ru/problem.aspx?space=1&num=2214) · difficulty 2005 · dp

Original problem by Vladimir Cherepanov, from the University Academic School Olympiad in Informatics 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An emitter covers L consecutive plants out of N, and on day i it adds
a_ij to every covered plant j. It starts anywhere, and at most once a
day, at most K times in total, it can be moved in the middle of the
day; then on that day both the old and the new positions count, each
plant once. Find the largest total over M days. The limits are 3.5
seconds and 256 MB.

## Input

N, M, L and K, 1 ≤ N ≤ 5000, 1 ≤ M ≤ 100, 1 ≤ L ≤ N, 0 ≤ K ≤ M, then the
M × N values from 0 to 10⁹.

## Output

The largest total.

## Examples

### Example 1

Input:

```
3 4 2 1
3 2 0
4 1 1
0 3 7
2 1 1
```

Output:

```
23
```

## Solution

A state is (day, moves used, position at the end of the day). Since a
move to the same position changes nothing, every plan can be padded to
use exactly K moves, so only move counts that can still reach K by the
last day are kept.

With prefix sums of the day's row, a day without a move adds the window
sum w(x). A day with a move from x to y adds the union of the two
windows:

- if |x − y| < L the union is one interval, worth
  prefix(max end) − prefix(min start), which splits into a term of x
  and a term of y; the best x for each y is a sliding window maximum
  over the last L positions, kept with a monotone deque, once for x
  left of y and once for x right of y;
- if the windows are disjoint, the value is w(x) + w(y), and the best
  dp(x) + w(x) over x at least L away is a running prefix maximum.

So each layer costs O(N), and there are M · (K + 1) layers.

In the example the emitter covers plants 1 and 2, moves to 2 and 3 in
the middle of the second day, and the plants end at 7, 7 and 9, which
is 23.

This takes O(N M K) time and O(N K) memory.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2214_dp.cpp](2214_dp.cpp) | G++ 13.2 x64 | dp | O(N M K) | AC | 0.250 s | 2244 KB |
| [2214_dp.go](2214_dp.go) | Go 1.14 x64 | dp | O(N M K) | AC | 0.265 s | 27244 KB |
| [2214_dp.java](2214_dp.java) | Java 1.8 | dp | O(N M K) | AC | 0.593 s | 16348 KB |
| [2214_dp.py](2214_dp.py) | PyPy 3.10 x64 | dp | O(N M K) | AC | 1.218 s | 63468 KB |
| [2214_dp.rs](2214_dp.rs) | Rust 1.75 x64 | dp | O(N M K) | AC | 0.250 s | 10548 KB |
