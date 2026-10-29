# 1126. The maximum of every window of M consecutive readings

[Timus 1126](https://acm.timus.ru/problem.aspx?space=1&num=1126) · difficulty 92 · two_pointers

Original problem by Alexander Mironenko, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a window width `M` (`2 ≤ M ≤ 14000`) and `N` readings
(`M ≤ N ≤ 25000`, each from 0 to 100000) ending with `-1`, print the
maximum of readings `1..M`, then of `2..M+1`, and so on up to the last
full window.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`M`, then the readings one per line, then `-1`.

## Output

The `N − M + 1` window maxima, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
10
11
10
0
0
0
1
2
3
2
-1
```

Output:

```
11
11
10
0
1
2
3
3
```

## Solution

Keep a double-ended queue of indices whose values decrease from front to
back. A new reading first removes from the back every index whose value
is not larger than its own, since those can never increase the maximum
while the new one is in the window; then it joins the back. The front
leaves when it falls out of the window. The front of the queue is always
the maximum of the current window. Each index enters and leaves at most once, so
the whole pass is `O(N)`; recomputing every window would cost `O(N·M)`,
up to about 156 million steps.

Pitfalls:

- the readings end with `-1`, not with a count;
- equal readings may all be dropped from the back except the newest one,
  which leaves the window last;
- with `M = N` there is a single window.

The answers were checked against the maximum of every window slice
computed directly, on every test.

## Optimized solutions

The optimized solutions (C++, Java) do not store the readings: each one
joins the deque together with its index as soon as it is read, and the
maximum of a full window is printed at once. C++ reads with `getchar`;
Java parses a byte buffer by hand, keeps the deque in a ring buffer of
`M` cells, since the window never holds more, and writes the numbers
through a byte buffer. C++: 224 KB instead of 776 KB, with the same
time; Java: 0.109 s instead of 0.156 s and 624 KB instead of 2332 KB.

The optimized Python and Rust solutions do not store the readings
either: they keep only the window. Python keeps it in a circular buffer
of two `array`s instead of a deque and writes the answers in batches of
256 lines: 668 KB instead of 3448 KB, with the same time. Rust parses
the numbers by hand from a 4 KB buffer instead of reading the whole
input into a string, and writes each answer through a buffered writer as
soon as it is known: 332 KB instead of 1192 KB, with the same time.

## Language notes

- In the simple solutions, Go and Java keep the queue in an array with a
  moving head; C++, Rust and Python use their library deques.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB | 11279323 |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB | 11279328 |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB | 11279331 |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.140 s | 3448 KB | 11279329 |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB | 11279332 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1126_two_pointers_optimized.cpp](1126_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 224 KB | 11303561 |
| [1126_two_pointers_optimized.java](1126_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N) | AC | 0.109 s | 624 KB | 11303563 |
| [1126_two_pointers_optimized.py](1126_two_pointers_optimized.py) \* | Python 3.12 x64 | two_pointers | O(N) | AC | 0.125 s | 668 KB | 11303710 |
| [1126_two_pointers_optimized.rs](1126_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.031 s | 332 KB | 11303711 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
