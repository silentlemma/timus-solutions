# 2103. Fastest memo with free air mail to multiples

[Timus 2103](https://acm.timus.ru/problem.aspx?space=1&num=2103) · difficulty 1199 · math, number_theory

Original problem by Alexey Danilyuk, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Employees are numbered 1, 2, 3, … and sit in rooms in that order.
Employee x can send a memo for free to any multiple of x larger than x,
or walk it to any other employee at a cost equal to the distance between
their numbers. Find the cheapest way for a board member s ≤ 7 to get a
memo to employee t, and print the route. Any optimal route is accepted.
The limits are 1 second and 64 MB.

## Input

s and t, 1 ≤ s ≤ 7, 1 ≤ t ≤ 10⁹.

## Output

The cost, the number of employees on the route, and the route.

## Checking

A checker compares the cost and replays the printed route.

## Examples

### Example 1

Input:

```
5 7
```

Output:

```
2
2
5 7
```

### Example 2

Input:

```
3 30
```

Output:

```
0
2
3 30
```

### Example 3

Input:

```
6 1000000
```

Output:

```
1
3
6 5 1000000
```

## Solution

Free mail only goes up, so reaching t ≤ s takes s − t steps of walking,
and walking down is the route. For t > s:

- Cost 0 exactly when t is a multiple of s: free mail reaches only
  multiples of the sender.
- Cost 1 means free mail to a multiple m of s, one step to m ± 1, and free
  mail on to t, so m ± 1 must divide t. All divisors r of t are tried in
  O(√t), looking for a multiple of s (at least s) next to r.
- Otherwise the cost is 2, and a route always exists. For s ≤ 5, go by
  mail to the multiple of s nearest to t, at most 2 away. For s = 6 or 7,
  write t = 2ᵃ 3ᵇ r with r coprime to 6. If r > 1, then r ± 1 is a
  multiple of 6: walk to 6 (at most one step), mail to r ± 1, step to r
  and mail to t. If t is a power of 2, it is a multiple of 8, two steps
  from 6 and one from 7; if t is a power of 3, it is a multiple of 9,
  reached as 7 → 9 or 6 → 5 → 10 → 9; and multiples of 6 were already
  cost 1 or 0.

In the third example 1 000 000 = 5 · 200 000 and 5 is one step below 6,
so the cost is 1: 6, 5, 1 000 000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2103_math_number_theory.cpp](2103_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(sqrt t) | AC | 0.015 s | 432 KB |
| [2103_math_number_theory.go](2103_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(sqrt t) | AC | 0.031 s | 1116 KB |
| [2103_math_number_theory.java](2103_math_number_theory.java) | Java 1.8 | math, number_theory | O(sqrt t) | AC | 0.140 s | 468 KB |
| [2103_math_number_theory.py](2103_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(sqrt t) | AC | 0.109 s | 756 KB |
| [2103_math_number_theory.rs](2103_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(sqrt t) | AC | 0.046 s | 232 KB |
