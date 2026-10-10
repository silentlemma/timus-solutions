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
is not larger than its own, since those can never be a maximum again
while the new one is in the window; then it joins the back. The front
leaves when it falls out of the window. The front of the queue is always
the maximum of the current window. Each index enters and leaves once, so
the whole pass is `O(N)`; recomputing every window would cost `O(N·M)`,
up to 150 million steps.

Pitfalls:

- the readings end with `-1`, not with a count;
- equal readings may all be dropped from the back except the newest one,
  which leaves the window last;
- with `M = N` there is a single window.

The answers were checked against the maximum of every window slice
computed directly, on every test.

## Language notes

- Go and Java keep the queue in an array with a moving head; C++, Rust
  and Python use their library deques.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.140 s | 3448 KB |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB |
