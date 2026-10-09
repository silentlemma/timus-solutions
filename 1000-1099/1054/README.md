# 1054. The step number of a Tower of Hanoi position

[Timus 1054](https://acm.timus.ru/problem.aspx?space=1&num=1054) · difficulty 643 · math

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` disks (`1 ≤ N ≤ 31`, disk 1 the smallest) start on rod 1 and are moved
to rod 2 by the classic optimal recursion

```text
Hanoi(n, from, to, via):
    if n > 0:
        Hanoi(n − 1, from, via, to)
        move disk n from `from` to `to`
        Hanoi(n − 1, via, to, from)
```

called as `Hanoi(N, 1, 2, 3)`. A position lists the rod of every disk.
Find after how many moves the given position appears, or `-1` if it never
does.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the rods `D1 … DN` of disks `1 … N`, one per line.

## Output

The number of moves, or `-1`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
3
3
1
```

Output:

```
3
```

### Example 2

Input:

```
1
3
```

Output:

```
-1
```

## Solution

Follow the recursion from the largest disk down. While disks `1 … k` are
being moved from `a` to `b` over `c`, disk `k` moves exactly once, after
the first `2^(k−1) − 1` moves (those take disks `1 … k − 1` to `c`). So:

- disk `k` still on `a`: we are in the first half; continue with disks
  `1 … k − 1` moving from `a` to `c` over `b`;
- disk `k` on `b`: the first half and the move of disk `k` are done, that
  is `2^(k−1)` moves; continue with disks `1 … k − 1` moving from `c` to
  `b` over `a`;
- disk `k` on `c`: this never happens, the answer is `-1`.

Adding the `2^(k−1)` of every disk found on its target rod gives the
step. `O(N)`.

Pitfalls:

- the rods swap roles at every level; whether the smallest disk first
  goes to rod 2 or rod 3 depends on the parity of `N`;
- the final position of 31 disks is reached after `2^31 − 1` moves, so
  64-bit (or unsigned 32-bit) integers are needed;
- a single disk on the spare rod of its level makes the whole position
  unreachable, whatever the other disks do.

## Language notes

- All languages run the same loop over the disks, with three variables
  for the roles of the rods.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1054_math.cpp](1054_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.031 s | 196 KB |
| [1054_math.go](1054_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1084 KB |
| [1054_math.java](1054_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1620 KB |
| [1054_math.py](1054_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.093 s | 396 KB |
| [1054_math.rs](1054_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 216 KB |
