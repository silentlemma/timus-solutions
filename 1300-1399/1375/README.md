# 1375. Bill Clevers

[Timus 1375](https://acm.timus.ru/problem.aspx?space=1&num=1375) · difficulty 541 · number_theory

Original problem by Den Raskovalov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a prime p ≤ 10⁶ and 0 ≤ k ≤ p − 1, print any x and y from 0 to
p − 1 with x² + y² ≡ k (mod p), or `NO SOLUTION` if there are none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k and p.

## Output

x and y, or `NO SOLUTION`.

## Examples

### Example 1

Input:

```
1 3
```

Output:

```
0 2
```

## Solution

For an odd prime p, the squares take (p + 1) / 2 different values
modulo p, and so do the values k − x². Two sets of (p + 1) / 2 values
among p must meet, so some x² and y² add up to k: there is always an
answer, and `NO SOLUTION` never comes. For p = 2 every k is 0² + 0² or
1² + 0².

To find it, list one square root for every square: for y from 0 to
p − 1, remember y as a root of y² mod p. Then try x = 0, 1, 2, … until
k − x² mod p has a root. About half of all values are squares, so this
ends almost at once. `O(p)`.

Pitfalls:

- k = 0 has the answer 0 0 (test 07);
- k − x² must be taken modulo p as a non-negative number;
- y² can approach 10¹², beyond 32-bit integers.

The answer was checked for every k and every prime below 300, and the
tests are judged by a checker that accepts any pair.

## Optimized solutions

The new C++, Go and Rust files replace the O(p) root table with constant-space prime-field arithmetic. For p=2 or k=0, (k,0) suffices. If p≡1 mod4, find a quadratic nonresidue z by Euler’s criterion and set i=z^((p−1)/4), so i²=−1. Choose the odd t congruent to k, either k or k+p. With a=(t+1)/2 and b=(t−1)/2, a²−b²=t; hence (a mod p, ib mod p) is the answer. If p≡3 mod4, enumerate x from 0 through (p−1)/2, one representative of each possible square. For r=k−x² mod p, compute y=r^((p+1)/4) and test y²=r. For a nonzero quadratic residue, y²=r·r^((p−1)/2)=r by Euler’s criterion. For r=0 the root is zero. The set of squares S and its reflection k−S each have (p+1)/2 elements, so the two sets intersect and the scan finds a pair. Modular powers use 64-bit products below 10^12. For T exponentiation trials, time O(1+T log p), worst O(p log p), extra space O(1); there is no assertion of a uniformly better asymptotic time than the lookup base. The memory improvement and judge timings determine admission. Rust uses C-entry character I/O. All simple table versions remain; Java/Python reuse bases.

The accepted base implementations [1375_number_theory.java](1375_number_theory.java), [1375_number_theory.py](1375_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The five original files use an array indexed by residue. The optimized C++, Go and Rust files use modular powers and a fixed number of integers. The judge checks the equation, so the two approaches can print different pairs.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1375_number_theory.cpp](1375_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p) | AC | 0.031 s | 3656 KB | 11285686 |
| [1375_number_theory.go](1375_number_theory.go) | Go 1.14 x64 | number_theory | O(p) | AC | 0.062 s | 9624 KB | 11285689 |
| [1375_number_theory.java](1375_number_theory.java) | Java 1.8 | number_theory | O(p) | AC | 0.156 s | 5172 KB | 11285695 |
| [1375_number_theory.py](1375_number_theory.py) \* | Python 3.12 x64 | number_theory | O(p) | AC | 0.359 s | 23992 KB | 11285693 |
| [1375_number_theory.rs](1375_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p) | AC | 0.046 s | 7892 KB | 11285697 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1375_math.cpp](1375_math.cpp) | G++ 13.2 x64 | math | O(1 + T log p) | AC | 0.015 s | 108 KB | 11315721 |
| [1375_math.go](1375_math.go) \* | Go 1.14 x64 | math | O(1 + T log p) | AC | 0.031 s | 916 KB | 11315726 |
| [1375_math.rs](1375_math.rs) \* | Rust 1.75 x64 | math | O(1 + T log p) | AC | 0.046 s | 64 KB | 11315729 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
