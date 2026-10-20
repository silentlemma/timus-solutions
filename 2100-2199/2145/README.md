# 2145. Counting assignments of problems that every student can solve

[Timus 2145](https://acm.timus.ru/problem.aspx?space=1&num=2145) · difficulty 376 · combinatorics, sorting

Original problem by Valentin Zuev, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n students have knowledge aᵢ and n problems have difficulty bⱼ; a student
can solve a problem when aᵢ ≥ bⱼ. Count, modulo p, the ways to give each
student exactly one problem, all different, so that every student can
solve theirs. The limits are 3 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, the values aᵢ, the values bⱼ, all between 0 and 10⁹,
and p, 1 ≤ p ≤ 10⁹.

## Output

The number of ways modulo p.

## Examples

### Example 1

Input:

```
3
1 2 3
1 2 3
100
```

Output:

```
1
```

### Example 2

Input:

```
3
3 3 3
1 1 1
100
```

Output:

```
6
```

## Solution

Sort the students by knowledge and hand out problems from the weakest
student up. Let cᵢ be the number of problems the i-th student (counting
from 0) can solve. Every problem that a weaker student can solve, the
i-th one can solve too, and the i weaker students have already taken i
different problems among the i-th student's cᵢ. Whatever they took, the
i-th student has exactly cᵢ − i choices, so the answer is the product of
cᵢ − i. Once a factor is 0 the product stays 0.

After sorting both arrays, cᵢ grows with i and a single pointer over the
problems gives all of them. The product is taken modulo p at every step,
and 1 % p covers p = 1. The work is O(n log n).

In the second example every student solves every problem, and the
product is 3 · 2 · 1 = 6.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2145_combinatorics_sorting.cpp](2145_combinatorics_sorting.cpp) | G++ 13.2 x64 | combinatorics, sorting | O(n log n) | AC | 0.171 s | 1768 KB |
| [2145_combinatorics_sorting.go](2145_combinatorics_sorting.go) | Go 1.14 x64 | combinatorics, sorting | O(n log n) | AC | 0.203 s | 5672 KB |
| [2145_combinatorics_sorting.java](2145_combinatorics_sorting.java) | Java 1.8 | combinatorics, sorting | O(n log n) | AC | 0.156 s | 2156 KB |
| [2145_combinatorics_sorting.py](2145_combinatorics_sorting.py) | Python 3.12 x64 | combinatorics, sorting | O(n log n) | AC | 0.187 s | 21384 KB |
| [2145_combinatorics_sorting.rs](2145_combinatorics_sorting.rs) | Rust 1.75 x64 | combinatorics, sorting | O(n log n) | AC | 0.031 s | 6320 KB |
