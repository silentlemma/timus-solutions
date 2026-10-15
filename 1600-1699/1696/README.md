# 1696. Salary for Robots

[Timus 1696](https://acm.timus.ru/problem.aspx?space=1&num=1696) · difficulty 872 · dp

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n robots of ranks 1..n are paid salaries from 1 to k each month. A
payment is forbidden if there are robots a, b, c whose ranks decrease
from a to c while their salaries increase from a to c, and no payment
may repeat. Months are numbered 1..p within a year. In which month does
the accountant run out of payments?

## Input

n, k, p (1 ≤ n ≤ 1000; 1 ≤ k ≤ 200; 2 ≤ p ≤ 10⁹).

## Output

The number of that month within its year.

## Examples

### Example 1

Input:

```
3 3 20
```

Output:

```
7
```

## Solution

Write the salaries in order of rank. The forbidden pattern is then a
strictly decreasing subsequence of length three. If C payments are
allowed, the accountant rusts in month C + 1 counted from the start, so
the answer is (C mod p) + 1.

Count the sequences rank by rank. The state is a, the largest salary
so far, and b, the largest salary that comes after a larger one (0 if
there is none). A new salary z is allowed exactly when z ≥ b, since
z < b would end a decreasing triple. If z < a, the state becomes
(a, z); otherwise it becomes (z, b). Both moves are prefix sums: the
new (a, c) collects all old (a, b) with b ≤ c along a row, and the new
(z, b) collects all old (a, b) with a ≤ z down a column. That gives
`O(n · k²)` work modulo p.

Pitfalls:

- the month is (C mod p) + 1, so a count divisible by p gives month 1
  (test 10);
- equal salaries never form a forbidden triple, only strictly
  increasing ones do;
- the counts are kept modulo p from the start, since C itself is
  astronomically large.

The Python solution is submitted under PyPy: a local CPython run takes
about 3 s for n = 1000 and k = 200, beyond the 2 s limit.

The answers match a count over all salary sequences for n ≤ 6 and
k ≤ 5, and an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1696_dp.cpp](1696_dp.cpp) | G++ 13.2 x64 | dp | O(n · k²) | AC | 0.703 s | 452 KB |
| [1696_dp.go](1696_dp.go) | Go 1.14 x64 | dp | O(n · k²) | AC | 1.015 s | 7568 KB |
| [1696_dp.java](1696_dp.java) | Java 1.8 | dp | O(n · k²) | AC | 1.093 s | 2240 KB |
| [1696_dp.py](1696_dp.py) | PyPy 3.10 x64 | dp | O(n · k²) | AC | 1.203 s | 13612 KB |
| [1696_dp.rs](1696_dp.rs) | Rust 1.75 x64 | dp | O(n · k²) | AC | 0.359 s | 964 KB |
