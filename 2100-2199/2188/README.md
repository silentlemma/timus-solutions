# 2188. The earliest overtake that is never lost again

[Timus 2188](https://acm.timus.ru/problem.aspx?space=1&num=2188) · difficulty 2419 · prefix_sums, binary_search

Original problem by Artyom Kutuzov, from the Ural School Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pirate boat starts D feet ahead and moves bᵢ feet in second i; Jim's
boat may move any whole number of feet from 0 to aᵢ in that second.
Jim wants the first second t at whose end Jim's boat is strictly ahead
to be as small as possible, under the rule that it then stays strictly
ahead to the end of second n. For each of q guesses of D, find that t, or −1.
The limits are 1 second and 256 MB.

## Input

n and q, 1 ≤ n, q ≤ 10⁵, then a₁ … a_n and b₁ … b_n with values from 0
to 10⁹, then d₁ … d_q with 1 ≤ dⱼ ≤ 10⁹.

## Output

The answer for each guess.

## Examples

### Example 1

Input:

```
10 10
7 4 7 0 5 6 4 4 5 4
5 3 5 1 2 3 3 7 2 0
1 2 3 4 5 6 7 8 14 15
```

Output:

```
1
2
3
5
5
5
6
10
10
-1
```

### Example 2

Input:

```
1 4
4
1
1 2 3 4
```

Output:

```
1
1
-1
-1
```

## Solution

Let x(i) be the distance Jim has covered minus the distance the
pirates have covered, so Jim is ahead at the end of second i when
x(i) > D, and let G(i) be the prefix sum of aᵢ − bᵢ, which is x at full
speed. Both boats
move evenly within a second, so being ahead at both ends of a second
means being ahead during it.

Before t, Jim must not be ahead, so the best plan is to go full speed
but never above D. That clipped walk ends with x = G(i) − max(0, Mᵢ − D),
where Mᵢ is the largest of 0, G(1), …, G(i). From second t on Jim goes
full speed, so with M the maximum before t and S the smallest G(i) for
i ≥ t, Jim stays ahead exactly when

S − max(0, M − D) > D, that is, S > max(D, M).

So a second t can work only if S > M, and then it works for every
D < S. The suffix minima S grow with t, so the useful seconds have
increasing thresholds S, and each query is a binary search for the
first threshold above D.

In the second example G(1) = 3, so D = 1 and D = 2 overtake in the first
second, while D = 3 and D = 4 never get ahead.

Prefix sums and suffix minima take O(n), and the queries O(q log n).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2188_prefix_sums_binary_search.cpp](2188_prefix_sums_binary_search.cpp) | G++ 13.2 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.078 s | 2732 KB |
| [2188_prefix_sums_binary_search.go](2188_prefix_sums_binary_search.go) | Go 1.14 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.062 s | 12984 KB |
| [2188_prefix_sums_binary_search.java](2188_prefix_sums_binary_search.java) | Java 1.8 | prefix_sums, binary_search | O(n + q log n) | AC | 0.156 s | 5764 KB |
| [2188_prefix_sums_binary_search.py](2188_prefix_sums_binary_search.py) | Python 3.12 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.281 s | 32712 KB |
| [2188_prefix_sums_binary_search.rs](2188_prefix_sums_binary_search.rs) | Rust 1.75 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.046 s | 7212 KB |
