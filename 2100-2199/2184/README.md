# 2184. The largest pile size when one pile was split between two chests

[Timus 2184](https://acm.timus.ru/problem.aspx?space=1&num=2184) · difficulty 1412 · number_theory

Original problem by Artyom Stepanov, from the Ural School Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Coins were dealt in piles of d into n chests, each pile whole into one
chest, except the last pile, which was split in any way between two
chests. Given the chest contents aᵢ, find the largest possible d. The
limits are 1 second and 256 MB.

## Input

n, 2 ≤ n ≤ 10⁵, then a₁ … a_n with 0 ≤ aᵢ ≤ 10¹², not all zero.

## Output

The largest d.

## Examples

### Example 1

Input:

```
4
5 8 7 100
```

Output:

```
5
```

### Example 2

Input:

```
5
9 4 6 5 12
```

Output:

```
3
```

### Example 3

Input:

```
6
4 8 16 24 12 40
```

Output:

```
8
```

## Solution

The chests hold a whole number of piles in total, so d divides the sum
S, and every chest except the two that shared the last pile holds a
multiple of d. Conversely, if d divides S and all but two aᵢ, the two
remainders add up to 0 or d, which is a split pile. So the answer is the
largest gcd of S with all values except at most two of them.

Removing a value only helps where it changes a running gcd. Let i < j be
the removed pair. If the gcd of S and the values before i already
divides aᵢ, keeping aᵢ changes nothing, and likewise for j with the
values after it. So i can be taken among the positions where the prefix
gcd (started from S) changes, and j among those where the suffix gcd
changes. Each change at least halves a number up to 10¹⁷, so there are
fewer than 60 of each.

The solution marks those positions, folds all other values into one gcd
with S, and tries every pair of marked values with suffix gcds over the
marked list. Removing nothing is covered by the gcd of everything.

In the first example S = 120 and d = 5 keeps 5 and 100, while 8 and 7
leave remainders 3 and 2 that form one pile of 5.

The scan takes O(n log S), and the pairs about 120² gcd steps.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2184_number_theory.cpp](2184_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log S) | AC | 0.046 s | 1032 KB |
| [2184_number_theory.go](2184_number_theory.go) | Go 1.14 x64 | number_theory | O(n log S) | AC | 0.062 s | 5676 KB |
| [2184_number_theory.java](2184_number_theory.java) | Java 1.8 | number_theory | O(n log S) | AC | 0.125 s | 1244 KB |
| [2184_number_theory.py](2184_number_theory.py) | Python 3.12 x64 | number_theory | O(n log S) | AC | 0.187 s | 10604 KB |
| [2184_number_theory.rs](2184_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log S) | AC | 0.031 s | 3736 KB |
