# 1741. Communication Fiend

[Timus 1741](https://acm.timus.ru/problem.aspx?space=1&num=1741) · difficulty 287 · dp

Original problem by Alex Samsonov (prepared by Marina Mukhacheva), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A licensed client of version 1 has to reach version n. Each update
takes version x to version y > x and has a size. A pirated update
makes the client pirated for good; a cracked update installs on any
client; a licensed update installs only on a client that is still
licensed. Find the least total size of updates, or report that version
n cannot be reached.

## Input

n and m (2 ≤ n ≤ 10⁴, 1 ≤ m ≤ 10⁴), then m updates `x y d s`
(1 ≤ x < y ≤ n, 1 ≤ d ≤ 10⁶), where s is `Pirated`, `Cracked` or
`Licensed`.

## Output

`Online` and the least total size, or `Offline`.

## Examples

### Example 1

Input:

```
3 4
1 3 10 Licensed
1 2 2 Pirated
2 3 3 Licensed
2 3 6 Cracked
```

Output:

```
Online
8
```

### Example 2

Input:

```
3 1
1 2 10 Licensed
```

Output:

```
Offline
```

## Solution

Updates only raise the version, so the versions can be handled in
increasing order, each after everything that leads to it. The state is
the version together with whether the client is still licensed or
already pirated. From each reached state, a pirated update leads to the
pirated state of its target, a cracked one keeps the state, and a
licensed one is allowed only from the licensed state. The answer is
the smaller of the two values at version n. `O(n + m)`.

In the first example the pirated 1 → 2 for 2 and the cracked 2 → 3 for
6 give 8, cheaper than the licensed 1 → 3 for 10; the licensed 2 → 3
for 3 cannot follow the pirated update.

Pitfalls:

- the total can reach about 10¹⁰, more than 32 bits hold;
- a cracked update keeps a licensed client licensed;
- it does not matter whether version n ends up licensed.

The answers match an independent accepted implementation, a shortest
path search, on 200 random cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1741_dp.cpp](1741_dp.cpp) | G++ 13.2 x64 | dp | O(n + m) | AC | 0.015 s | 1092 KB |
| [1741_dp.go](1741_dp.go) | Go 1.14 x64 | dp | O(n + m) | AC | 0.046 s | 3284 KB |
| [1741_dp.java](1741_dp.java) | Java 1.8 | dp | O(n + m) | AC | 0.125 s | 5772 KB |
| [1741_dp.py](1741_dp.py) | Python 3.12 x64 | dp | O(n + m) | AC | 0.109 s | 6932 KB |
| [1741_dp.rs](1741_dp.rs) | Rust 1.75 x64 | dp | O(n + m) | AC | 0.015 s | 2164 KB |
