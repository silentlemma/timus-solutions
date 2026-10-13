# 1364. LaraKiller

[Timus 1364](https://acm.timus.ru/problem.aspx?space=1&num=1364) · difficulty 957 · simulation

Original problem by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cemetery has N rows of M graves, 2 ≤ N, M ≤ 100. Lara digs a tunnel
from grave (1, 1), heading east: the tunnel goes straight while the
next grave is untouched, and turns right in front of the wall or a
grave already dug. The tunnel reaches the treasure at (rT, cT). When
Lara is at grave (rL, cL) on the tunnel, an alarm leaves T ≤ 27 000
seconds, and Lara runs along the tunnel at one grave per second. Print
every dug grave Lara can reach in time, in the order they were dug.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then rT and cT, then rL and cL, then T.

## Output

The reachable graves, one `row column` pair per line, in digging order.

## Examples

### Example 1

Input:

```
5 4
4 3
2 2
5
```

Output:

```
5 2
5 1
4 1
3 1
2 1
2 2
2 3
3 3
4 3
```

## Solution

The digging rule draws a clockwise spiral, and the tunnel ends at the
treasure. Simulate it: keep a frame of "dug" cells around the cemetery
for the wall, and turn right whenever the next cell is dug. This lists
the graves in digging order, so the tunnel is a path where the distance
between two graves is the difference of their places in the list.

If Lara's grave is at place p and the treasure at place q, the answer is
places max(0, p − T) to min(q, p + T). `O(N · M)`.

Pitfalls:

- the tunnel ends at the treasure, so nothing past it can be reached
  (test 06);
- T can be 0, leaving only Lara's own grave (test 02);
- T can exceed the whole tunnel, which then is the answer (test 03 and
  generated test 1).

## Language notes

- All five solutions build the same spiral with a frame for the wall.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1364_simulation.cpp](1364_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.015 s | 300 KB |
| [1364_simulation.go](1364_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.015 s | 2096 KB |
| [1364_simulation.java](1364_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.093 s | 2068 KB |
| [1364_simulation.py](1364_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 1992 KB |
| [1364_simulation.rs](1364_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.015 s | 452 KB |
