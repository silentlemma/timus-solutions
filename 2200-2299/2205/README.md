# 2205. The lowest common ancestor in the tree of largest proper divisors

[Timus 2205](https://acm.timus.ru/problem.aspx?space=1&num=2205) · difficulty 1462 · number_theory

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two different natural numbers are joined when one of them is the
largest proper divisor of the other. A path is a sequence of distinct
numbers with consecutive ones joined, and its price is its smallest
number. For each of N pairs (a, b), print the largest price of a path
from a to b, or −1 if there is none. The limits are 2 seconds and
256 MB.

## Input

N, 1 ≤ N ≤ 5 · 10⁵, then N pairs with 1 ≤ a, b ≤ 10⁷.

## Output

The answer for each pair.

## Examples

### Example 1

Input:

```
3
4 4
4 5
4 6
```

Output:

```
4
1
1
```

## Solution

The largest proper divisor of n > 1 is n / p for its smallest prime
factor p, so every number above 1 has exactly one smaller neighbor:
the joins form a tree rooted at 1, and every pair has exactly one path.
Values only shrink toward the root, so the smallest number on the path
is the lowest common ancestor, and −1 never happens.

Write the prime factors of a in decreasing order. Its ancestors drop the
smallest factors one by one, so they are exactly the products of the
first few factors of this list. The common ancestor is therefore the
product of the longest common beginning of the two decreasing lists.

That product comes from g = gcd(a, b). Let t be the largest prime
factor of a / g or b / g. Every prime above t has the same exponent in
a and b, and t itself appears in g with the smaller of its two
exponents, which is where the lists start to differ. Below t the lists
have already parted. So the answer is g with all prime factors smaller
than t removed; when a = b it is a itself, and when g = 1 it is 1.

A sieve of smallest odd prime factors up to 10⁷, stored for odd
numbers only, gives every factorization, and powers of 2 are removed
with a bit trick.

In the example 4 = 2 · 2 and 6 = 3 · 2 differ already in the largest
factor, so their common ancestor is 1.

The sieve takes O(V log log V) for V = 10⁷, and each query O(log V).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2205_number_theory.cpp](2205_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(V log log V + N log V) | AC | 0.343 s | 13416 KB |
| [2205_number_theory.go](2205_number_theory.go) | Go 1.14 x64 | number_theory | O(V log log V + N log V) | AC | 0.312 s | 54196 KB |
| [2205_number_theory.java](2205_number_theory.java) | Java 1.8 | number_theory | O(V log log V + N log V) | AC | 0.390 s | 19488 KB |
| [2205_number_theory.py](2205_number_theory.py) | PyPy 3.10 x64 | number_theory | O(V log log V + N log V) | AC | 1.921 s | 109108 KB |
| [2205_number_theory.rs](2205_number_theory.rs) | Rust 1.75 x64 | number_theory | O(V log log V + N log V) | AC | 0.234 s | 36432 KB |
