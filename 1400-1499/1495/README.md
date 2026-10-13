# 1495. One-two, One-two 2

[Timus 1495](https://acm.timus.ru/problem.aspx?space=1&num=1495) · difficulty 340 · bfs

Original problem by Igor Chevdar, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the smallest number written only with the digits 1 and 2 that is
divisible by N (1 ≤ N ≤ 10⁶). Print "Impossible" if there is none or if
it is longer than 30 digits.

Time limit: 2 seconds. Memory limit: 256 MB.

## Input

N.

## Output

The number, or "Impossible".

## Examples

### Example 1

Input:

```
5
```

Output:

```
Impossible
```

### Example 2

Input:

```
8
```

Output:

```
112
```

## Solution

Only the remainder modulo N matters for what can follow a prefix, so
search over remainders breadth-first. Start from the numbers 1 and 2,
and from a number with remainder r go to r·10 + 1 and then r·10 + 2.
Shorter numbers are reached first, and within one length the queue
stays in numeric order, so the first number to reach a remainder is the
smallest one with that remainder; any later number with it, and all
its extensions, would be larger. Each of the N remainders is stored
once with its last digit and its parent, and the answer is read back
along the parents once remainder 0 appears. Numbers stop growing at 30
digits. `O(N)`.

Pitfalls:

- a number of 1s and 2s never ends in 0 or 5, so multiples of 5 are
  impossible (tests 01, 07, 09);
- the answer can be exactly 30 digits long, as for 999999, which is
  still allowed (test 05);
- r·10 + d stays below 10⁷, but the number itself does not fit any
  integer type (tests 05, 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1495_bfs.cpp](1495_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.046 s | 14636 KB |
| [1495_bfs.go](1495_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.093 s | 32440 KB |
| [1495_bfs.java](1495_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.156 s | 17324 KB |
| [1495_bfs.py](1495_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.906 s | 62744 KB |
| [1495_bfs.rs](1495_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.062 s | 26080 KB |
