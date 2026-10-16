# 1778. Chinese Hockey 2

[Timus 1778](https://acm.timus.ru/problem.aspx?space=1&num=1778) · difficulty 3901 · greedy

Original problem by Alex Samsonov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n fans numbered 1 to n ride m buses numbered 1 to m, each bus taking
between a and b of them, and a bus with a larger number takes fans with
larger numbers. Some fans tell which bus they are in. Find every bus
that fan r can be in, or report that the answers contradict each other.

## Input

n, m, a and b (2 ≤ m ≤ n ≤ 10⁵, 1 ≤ a ≤ b ≤ n, m·a ≤ n ≤ m·b), then r,
then s (1 ≤ s ≤ n − 1) and s pairs of a fan rᵢ ≠ r and a bus fᵢ.

## Output

`IMPOSSIBLE`, or the number of possible buses and the buses in
increasing order.

## Examples

### Example 1

Input:

```
16 4 1 16
3
2
2 2
4 3
```

Output:

```
2
2 3
```

## Solution

Bus i takes the fans after the border P(i − 1) up to the border P(i),
where P(0) = 0, P(m) = n and a ≤ P(i) − P(i − 1) ≤ b. A fan x in bus f
means P(f) ≥ x and P(f − 1) ≤ x − 1, so every border starts with a
range of its own. Going left to right, each border must also lie a to b
past the range of the previous one, and going right to left, a to b
before the range of the next one; a chain of such constraints keeps
every set of possible values a range. After both passes each range
holds exactly the values that some whole seating gives that border, and
an empty range means the answers contradict each other.

Fan r is in bus k when P(k − 1) ≤ r − 1 and P(k) ≥ r for some seating.
Cutting the two ranges at r and checking that some pair of values in
them is a to b apart — the differences between the two ranges also form
a range — answers each bus at once. `O(n + m)`.

In the example fan 2 in bus 2 and fan 4 in bus 3 give P(1) ≤ 1,
P(2) = 2 or 3, P(3) ≥ 4. Fan 3 is in bus 2 when P(2) = 3, and in bus 3
when P(2) = 2.

Pitfalls:

- the two passes must both be done: the left pass alone misses limits
  that come from the far end;
- fan 1 is always in bus 1 and fan n in bus m;
- when every border range has one value, as with a = b, the whole seating is fixed.

The answers agree with a search over every seating on 500 random cases
of up to 5 buses, and with an independent accepted implementation on 80
cases of up to 10⁵ fans.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1778_greedy.cpp](1778_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.093 s | 976 KB |
| [1778_greedy.go](1778_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.140 s | 5860 KB |
| [1778_greedy.java](1778_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 3784 KB |
| [1778_greedy.py](1778_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.390 s | 27208 KB |
| [1778_greedy.rs](1778_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.031 s | 4736 KB |
