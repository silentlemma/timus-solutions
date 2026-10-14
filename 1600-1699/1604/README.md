# 1604. In the Country of Fools

[Timus 1604](https://acm.timus.ru/problem.aspx?space=1&num=1604) · difficulty 143 · greedy

Original problem by Alexander Ipatov (idea by Alexander Toropov), from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are k kinds of speed limit signs, nᵢ signs of kind i, at most
10000 signs in all. Place them all along a road so that drivers change
speed as often as possible: a change happens at the first sign and at
every sign that differs from the one before. Any best order is
accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k, then n₁, …, nₖ.

## Output

The kinds of the signs in road order.

## Examples

### Example 1

Input:

```
2
2 2
```

Output:

```
1 2 1 2
```

## Solution

Changing speed as often as possible means having as few equal
neighbours as possible. Let m be the largest count and n the total. The
other n − m signs split the m signs of the commonest kind into at most
n − m + 1 groups, so at least max(0, 2m − n − 1) neighbours are equal.

A greedy order reaches this bound: always place the kind with the most
signs left, unless it was the previous sign, in which case place the
kind with the second most. A heap gives both in `O(log k)`, so the whole
order takes `O(n log k)`.

The tests use a checker that counts the equal neighbours and compares
them with the bound. The bound itself was checked against an exhaustive
search over all orders of small sets of signs.

Pitfalls:

- when one kind has more than half of the signs, equal neighbours cannot
  be avoided, and the greedy puts them together at the end (test 05);
- taking the commonest kind every time without looking at the previous
  sign repeats it; taking kinds in turn ignores the counts and can run
  out of other kinds too early (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1604_greedy.cpp](1604_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 292 KB |
| [1604_greedy.go](1604_greedy.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.031 s | 2184 KB |
| [1604_greedy.java](1604_greedy.java) | Java 1.8 | greedy | O(n log k) | AC | 0.156 s | 3456 KB |
| [1604_greedy.py](1604_greedy.py) | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1776 KB |
| [1604_greedy.rs](1604_greedy.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.015 s | 1044 KB |
