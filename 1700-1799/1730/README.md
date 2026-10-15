# 1730. ManBearPig

[Timus 1730](https://acm.timus.ru/problem.aspx?space=1&num=1730) · difficulty 1146 · constructive

Original problem by Fedor Fominykh (prepared by Ivan Burmistrov), from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Crossing two creatures gives a creature that is, for every animal, the
average of the two shares. Given a creature's animals and their shares,
write a pedigree that produces it: a list of lines, each an animal or a
crossing of two earlier lines, ending with the creature, where every
line but the last takes part in some crossing. Print `No solution` if
there is none.

## Input

The creature's name: one to ten different animal names joined by
hyphens, 200 characters at most. Then the share of each animal as a
fraction a/b (1 ≤ a ≤ b ≤ 1500); the shares add up to 1.

## Output

The number of lines n (1 ≤ n ≤ 10 000) and the lines, or
`No solution`. Any fitting pedigree is accepted.

## Examples

### Example 1

Input:

```
man-bear-pig
1/2 1/4 1/4
```

Output:

```
7
man
pig
1 2
bear
man
4 5
3 6
```

### Example 2

Input:

```
man
1/1
```

Output:

```
1
man
```

### Example 3

Input:

```
man-bear-pig
1/3 1/3 1/3
```

Output:

```
No solution
```

## Solution

Every share in a crossing is the average of two shares, so by induction
every share in any pedigree has a power of two as its denominator. If
some reduced share does not, there is no solution.

Otherwise let L be the largest reduced denominator, at most 1024. Give
each animal its share of L equal leaves, in order, and build a balanced
binary tree over the leaves: each inner node crosses its two halves, so
each leaf ends up with exactly 1/L of the creature. A subtree whose
leaves are all one animal is that animal itself, so it becomes a single
line. At most 2L − 1 ≤ 2047 lines come out. `O(L)`.

In the first example L = 4 and the leaves are man, man, bear, pig. The
left half is pure man and the right half crosses bear with pig, so the
pedigree is man, bear, pig, 2 3, 1 4.

Pitfalls:

- the shares come unreduced, such as 750/1500, so they must be reduced
  before looking at the denominator;
- a pure animal is a one-line pedigree, with no crossing at all;
- the same animal may appear on several lines.

The checker replays the pedigree with exact fractions and checks the
shares, the line references and that every ancestor is used. The
pedigrees pass it on 200 random cases, with `No solution` exactly where
an independent accepted implementation gives it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1730_constructive.cpp](1730_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.015 s | 428 KB |
| [1730_constructive.go](1730_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.031 s | 1176 KB |
| [1730_constructive.java](1730_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.125 s | 1704 KB |
| [1730_constructive.py](1730_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.093 s | 504 KB |
| [1730_constructive.rs](1730_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.015 s | 244 KB |
