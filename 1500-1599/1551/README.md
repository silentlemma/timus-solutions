# 1551. Sumo Tournament

[Timus 1551](https://acm.timus.ru/problem.aspx?space=1&num=1551) · difficulty 257 · math

Original problem by Sergey Pupyrev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A knockout tournament has 2ᴺ wrestlers (1 ≤ N ≤ 10) and N rounds; each
wrestler represents a prefecture. The organisers choose the starting
bracket. Find the largest K such that some bracket guarantees, whatever
the bouts' results, at least K rounds in which no two wrestlers of one
prefecture meet.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then 2ᴺ lines with a wrestler's name and prefecture.

## Output

K.

## Examples

### Example 1

Input:

```
3
Homasho Ishikawa
Tamakasuga Tokyo
Futeno Tochigi
Takekaze Tokyo
Kasugao Yamaguchi
Kotoshogiku Ishikawa
Kotomitsuki Tokyo
Miyabiyama Shizuoka
```

Output:

```
1
```

## Solution

In round r the bracket pairs up blocks of 2^(r−1) wrestlers, and since
any wrestler of a block may come out of it, round r is safe exactly when
the two halves of every block of 2^r share no prefecture.

Take a prefecture with c wrestlers. Two of them meet, at the earliest,
in the round where their blocks join; a set of wrestlers whose pairwise
meeting rounds all lie in m given rounds has at most 2ᵐ members, so at
least ⌈log₂ c⌉ rounds are unsafe and K ≤ N − ⌈log₂ c⌉ for the largest
prefecture.

That bound is reached: with k = ⌈log₂ c⌉ for the largest c, sort the
wrestlers by prefecture and deal them round-robin into the 2ᵏ blocks of
the top k levels. A prefecture has at most 2ᵏ wrestlers, so they land in
different blocks; inside a block everyone is from a different
prefecture, so the first N − k rounds are safe. The answer is therefore
N − ⌈log₂ c⌉, computed with integers. A search over all brackets for
N ≤ 3 agreed on 120 random cases. `O(2ᴺ log 2ᴺ)` for counting.

Pitfalls:

- a single prefecture leaves no safe round (tests 02, 04);
- c = 4 needs only two unsafe rounds, c = 5 three (tests 06, 07);
- prefectures are compared as written, so Tokyo and tokyo differ
  (test 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1551_math.cpp](1551_math.cpp) | G++ 13.2 x64 | math | O(2^N log 2^N) | AC | 0.015 s | 544 KB |
| [1551_math.go](1551_math.go) | Go 1.14 x64 | math | O(2^N log 2^N) | AC | 0.031 s | 1276 KB |
| [1551_math.java](1551_math.java) | Java 1.8 | math | O(2^N log 2^N) | AC | 0.156 s | 3280 KB |
| [1551_math.py](1551_math.py) | Python 3.12 x64 | math | O(2^N log 2^N) | AC | 0.062 s | 696 KB |
| [1551_math.rs](1551_math.rs) | Rust 1.75 x64 | math | O(2^N log 2^N) | AC | 0.046 s | 576 KB |
