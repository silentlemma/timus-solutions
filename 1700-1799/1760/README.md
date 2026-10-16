# 1760. Infernal Work

[Timus 1760](https://acm.timus.ru/problem.aspx?space=1&num=1760) · difficulty 677 · math

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1760_math.cpp](1760_math.cpp) | G++ 13.2 x64 | math | O(sqrt(n)) | AC | 0.015 s | 128 KB |
| [1760_math.go](1760_math.go) | Go 1.14 x64 | math | O(sqrt(n)) | AC | 0.031 s | 1064 KB |
| [1760_math.java](1760_math.java) | Java 1.8 | math | O(sqrt(n)) | AC | 0.140 s | 1600 KB |
| [1760_math.py](1760_math.py) | Python 3.12 x64 | math | O(sqrt(n)) | AC | 0.078 s | 528 KB |
| [1760_math.rs](1760_math.rs) | Rust 1.75 x64 | math | O(sqrt(n)) | AC | 0.031 s | 236 KB |
