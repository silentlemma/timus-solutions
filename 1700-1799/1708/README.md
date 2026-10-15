# 1708. Sum of Digits 2

[Timus 1708](https://acm.timus.ru/problem.aspx?space=1&num=1708) · difficulty 9087 · math

Original problem by Vladimir Yakovlev, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Call a positive number in base b least if no smaller number has the
same sum of digits and the same sum of squares of digits. Describe all
least numbers by the shortest list of patterns. A pattern is made of
digits and stars, where a star lets the digit before it repeat any
number of times, zero included. Every number matching some pattern
must be least, and every least number must match some pattern.

## Input

The base b, 2 ≤ b ≤ 36.

## Output

The patterns sorted as strings, one per line, with the digits
1 … 9, A, B, … and no redundant parts: 12*3 rather than 12*2*3. A
pattern may also match the empty string.

## Examples

### Example 1

Input:

```
4
```

Output:

```
1*2*
112*3*
12*3*
2*3*
```

## Solution

Both sums ignore the order of the digits, so a least number has no
zeros and its digits never decrease: it is a multiset of the digits
1 … b − 1, a vector of counts. Of two vectors with equal sums, the one
with fewer digits is smaller. At equal length, look at the first digit
whose counts differ: the vector with more copies of it is smaller. The
comparison depends only on the difference of the two vectors, so
adding the same digits to both never changes it.

Removing digits from a least number leaves a least number, so the
least vectors are exactly those that lie above none of the minimal
non-least vectors, called forbidden below. To find them, compute for
every pair (sum, sum of squares) reachable with at most 15 digits its
least vector. Append the digits in increasing order and keep only the
best word per pair: by the remark above the best one stays best after
any extension. A forbidden vector without its largest digit is least,
so it comes from growing a least word by one digit at its end. The
grown word is forbidden when it is not the least of its pair, while
every one-digit deletion is. Base 36 has about 720000 pairs and
25000 forbidden vectors. None is longer than 15 digits, and raising the
cap to 17 finds no others.

The patterns come from a recursion on the last digit. For a set G of
forbidden vectors over the digits 1 … n, let t be the largest count of
the digit n in G. With k < t copies of it, a prefix must avoid the
vectors of G that have at most k copies, with the digit n removed and
only the minimal ones kept. With t copies or more, the prefix must
avoid them all, and that case becomes a star. So the patterns are those
for the star case with n* appended, and for every k < t the patterns
of its case with k copies appended. Prefix patterns that already avoid
everything are dropped there, as the star covers them. The forbidden regions grow
with k. Since G holds only minimal vectors, a newcomer never lies above
an older one, so each step only drops the older vectors above a
newcomer. The same sets recur often, so the results are memoized. The
patterns are kept as a trie of (parent, count) nodes, and the result
of one set is a few runs of consecutive nodes. Base 36 ends with about
2.1 million nodes and 47062 patterns. Expected time is
`O(P · b · L² + D · b + K · (b + L · log K))`, where P counts sum pairs,
D counts vector/support/prefix inspections during minimization and
recursion, K counts output patterns, and L = 15.

Pitfalls:

- the memory limit is 64 MB: the least words are kept compactly in an
  open-addressing table, which is freed before the patterns are
  built;
- whether a vector lies above one of many others is the hot test: the
  others are grouped by their sets of nonzero counts, and only groups
  inside the set of the tested vector are checked;
- base 2 has a single pattern, 1*, and base 36 prints about 325 KB;
- Java and Python build the same patterns another way, which fits the
  judge's limits: Java takes 0.27 s and Python, on PyPy, 1.75 s there,
  where earlier versions with the recursion above ran out of time on
  tests 30 and 22. They enumerate the least words breadth first in
  lexicographic order, so the first word to reach a pair of sums is its
  least one, in a table indexed directly by the pair: for each sum the
  sums of squares lie in an interval of one parity. A word is extended
  only by the digits that every one-digit deletion may take,
  which skips the forbidden words that are not minimal. Every pattern is
  a least word with at most two stars, on one digit or on two
  neighbouring digits: deleting all copies of a digit, or of two
  neighbouring digits, from a forbidden word gives a finite word that
  blocks such a star, and a blocked star passes from every word to its
  extensions. With P indexed sum-pair slots, F forbidden words and K
  patterns, the cost before sorting is `O((P + F) · (b + L) + K · b)`,
  L = 15. Sorting adds `O(K · L · log K)` in Python and `O(K² · L)`
  in the worst case in Java.

For every base from 2 to 36 the output is identical to that of an
independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1708_math.cpp](1708_math.cpp) | G++ 13.2 x64 | math | O(P · b · L² + D · b + K · (b + L · log K)) | AC | 2.375 s | 29376 KB |
| [1708_math.go](1708_math.go) | Go 1.14 x64 | math | O(P · b · L² + D · b + K · (b + L · log K)) | AC | 3.828 s | 39212 KB |
| [1708_math.java](1708_math.java) | Java 1.8 | math | O((P + F) · (b + L) + K · b + K² · L) | AC | 0.265 s | 25728 KB |
| [1708_math.py](1708_math.py) | PyPy 3.10 x64 | math | O((P + F) · (b + L) + K · (b + L · log K)) | AC | 1.750 s | 29456 KB |
| [1708_math.rs](1708_math.rs) | Rust 1.75 x64 | math | O(P · b · L² + D · b + K · (b + L · log K)) | AC | 2.671 s | 35628 KB |
