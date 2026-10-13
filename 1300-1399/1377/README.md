# 1377. Lara Croft

[Timus 1377](https://acm.timus.ru/problem.aspx?space=1&num=1377) · difficulty 295 · simulation

Original problem by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cemetery has N rows of M graves, 2 ≤ N, M ≤ 100. Every night Lara
digs under one grave, starting from (1, 1) heading east: the tunnel
goes straight while the next grave is untouched and turns right in
front of the wall or a grave already dug. Two given graves hold
treasures, and Lara has just found one of them. Print how many nights
later the other one is found.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then the two treasure graves (r₁, c₁) and (r₂, c₂).

## Output

The number of nights between the two finds.

## Examples

### Example 1

Input:

```
5 4
2 2
5 3
```

Output:

```
6
```

## Solution

The tunnel is the same clockwise spiral as in
[1364](../1364/README.md). Dig all of it, numbering every grave by the
night it is dug, with a frame of dug cells around the cemetery standing
for the wall. The answer is the difference of the two numbers, taken
without sign, since either treasure may come first. `O(N · M)`.

Pitfalls:

- the treasures may be listed in either order (test 03);
- the first and the last grave of a 100 × 100 cemetery are 9 999 nights
  apart (test 04);
- in a cemetery of two columns the spiral runs down one column and back
  up the other (test 07).

## Language notes

- All five solutions dig the same spiral.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1377_simulation.cpp](1377_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.001 s | 256 KB |
| [1377_simulation.go](1377_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.046 s | 1172 KB |
| [1377_simulation.java](1377_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.109 s | 1640 KB |
| [1377_simulation.py](1377_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 924 KB |
| [1377_simulation.rs](1377_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.031 s | 272 KB |
