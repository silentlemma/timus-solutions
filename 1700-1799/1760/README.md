# 1760. Infernal Work

[Timus 1760](https://acm.timus.ru/problem.aspx?space=1&num=1760) · difficulty 681 · math

Original problem by Alexander Ipatov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n items are written down in the same order in two notebooks, a per
page in the first and b per page in the second. Count the pairs of
items that are on one page of the first notebook but on different pages
of the second.

## Input

a, b and n (1 ≤ a, b ≤ n ≤ 25 000 000).

## Output

The number of such pairs.

## Examples

### Example 1

Input:

```
3 4 10
```

Output:

```
4
```

### Example 2

Input:

```
2 4 10
```

Output:

```
0
```

## Solution

The answer is the pairs on one page of the first notebook, n div a
full pages of C(a, 2) pairs plus C(n mod a, 2), minus the pairs on one
page of both. The page breaks of both notebooks cut the row into
pieces, and the pairs on one page of both are the sum of C(len, 2) over
the pieces.

That sum is taken page by page over the notebook with the larger pages:
each such page is cut by the smaller pages into a head, some whole
small pages and a tail, which costs O(1) per large page. Both page
breaks repeat every L = lcm(a, b) items, so when L ≤ n the sum over one
period is multiplied by n div L and the rest added. Either way at most
about √n large pages are walked: if L ≤ n there are L / max(a, b) =
min(a, b) / gcd(a, b) of them per period, at most √L, and if L > n then
max(a, b) > √n. So the work is `O(√n)`.

In the first example the pages of 3 hold 3 pairs each, 9 in all, and
the breaks at 3, 4, 6, 8 and 9 cut the row into pieces of 3, 1, 2, 2, 1
and 1 items with 5 pairs: 9 − 5 = 4.

Pitfalls:

- the answer reaches about 3·10¹⁴, beyond 32 bits;
- walking all n items is too slow in some languages, and walking every
  page of the smaller size is too slow when it is tiny;
- lcm(a, b) can reach 6·10¹⁴, so it is computed as a / gcd · b in 64
  bits.

The answers agree with a pair-by-pair count on 300 small cases, a
linear count on 60 larger ones and an independent accepted
implementation on 100 cases up to the limits.

## Optimized solutions

Count pairs on small pages first. A large-page cut within one of those pages removes the product of the lengths on its two sides. Sum that product by formula over complete periods and visit only the cuts in the remaining prefix.

Java submission 11318053 took 0.109 s and used 404 KB. The simple version took 0.156 s and used 1572 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321937 · Java 1.8 №11321939 · Python 3.12 x64 №11321885 · Rust 1.75 x64 №11321938 · Go 1.14 x64 №11322287.

Go sums the contributions of full periods by formula and scans the remaining cuts. Go 1.14 x64, submission 11321947. Time 0.031 → 0.015 s, memory 1132 → 288 KB.

Rust counts pairs using recursive sums of floor values, their squares, and their products with the indices. Rust 1.75 x64, submission 11323414. Time 0.046 → 0.046 s, memory 212 → 60 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1760_math.cpp](1760_math.cpp) | G++ 13.2 x64 | math | O(sqrt(n)) | AC | 0.015 s | 112 KB | 11321937 |
| [1760_math.go](1760_math.go) | Go 1.14 x64 | math | O(sqrt(n)) | AC | 0.031 s | 1132 KB | 11322287 |
| [1760_math.java](1760_math.java) | Java 1.8 | math | O(sqrt(n)) | AC | 0.156 s | 1572 KB | 11321939 |
| [1760_math.py](1760_math.py) | Python 3.12 x64 | math | O(sqrt(n)) | AC | 0.093 s | 552 KB | 11321885 |
| [1760_math.rs](1760_math.rs) | Rust 1.75 x64 | math | O(sqrt(n)) | AC | 0.046 s | 212 KB | 11321938 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1760_math_optimized.java](1760_math_optimized.java) | Java 1.8 | math | O(sqrt(n)) | AC | 0.109 s | 404 KB | 11318053 |
| [1760_math_optimized.go](1760_math_optimized.go) \* | Go 1.14 x64 | math | O(sqrt(n)) | AC | 0.015 s | 288 KB | 11321947 |
| [1760_number_theory_math.rs](1760_number_theory_math.rs) \* | Rust 1.75 x64 | number_theory, math | O(log n) | AC | 0.046 s | 60 KB | 11323414 |

\* The marked versions have room to improve in the ratings.
