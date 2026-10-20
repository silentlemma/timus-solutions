# 2208. Finding two numbers with a common factor in a range under updates

[Timus 2208](https://acm.timus.ru/problem.aspx?space=1&num=2208) · difficulty 1469 · number_theory, segment_tree

Original problem by Konstantin Rychkov, from the University Academic School Olympiad in Informatics 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array of N numbers from 2 to 10⁶ gets Q operations: replace one
element, or report two positions in a range [l, r] whose numbers are
not coprime, or −1 if there are none. Any valid pair is accepted. The
limits are 2 seconds and 256 MB.

## Input

N and Q, 2 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁵, then the array, then the operations
"1 l r" and "2 p x".

## Output

A pair of positions or −1 for each range query.

## Examples

### Example 1

Input:

```
5 4
2 3 4 5 6
1 1 5
1 2 4
2 3 6
1 2 4
```

Output:

```
1 3
-1
2 3
```

## Solution

Two numbers are not coprime exactly when they share a prime, and a
number up to 10⁶ has at most 7 distinct primes. For each position i let
prev(i) be the largest j < i whose number shares a prime with the number
at i, found as the latest earlier occurrence of each of its primes.

A range [l, r] has a valid pair exactly when some i in it has
prev(i) ≥ l, and then (prev(i), i) is such a pair. A segment tree of
prev values answers a query by descending to the first i ≥ l in the
range whose prev reaches l.

An update at p changes prev only at p itself and, for every prime that
p loses or gains, at the next occurrence of that prime after p. Each
prime keeps its occurrences in an ordered structure (a balanced set in
C++, a Fenwick tree over the positions it can ever take, collected in
advance, in the other languages), and the at most 15 affected positions
are recomputed.

The Python version saves time on the small primes: the 25 primes up to
100 become a bitmask that fits a machine word, and a tree node also
stores whether two of its elements already share a small prime. Since
101 · 103 · 107 > 10⁶, a number has at most two primes above 100, and
only those use the prev tree. Their occurrences, including those the
updates will create, are ranked in advance by one sort, and the present
ones are kept in a bitset with summary levels of 30-bit words, which
finds the previous occurrence in a few word operations. A query walks
the tree segments of the range from the left with the OR of the masks
passed so far and descends into the first segment that has a pair.

In the example 2 and 4 share the factor 2, the range 3, 4, 5 has no
pair, and after the update 3 and 6 share 3.

After a smallest-prime sieve up to 10⁶, each operation costs about
7 log N steps.

## Language notes

- Python runs under PyPy: under CPython 3.12 it exceeds the time limit on
  test 34 (2.046 s), while PyPy 3.10 is accepted in 1.64 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2208_number_theory_segment_tree.cpp](2208_number_theory_segment_tree.cpp) | G++ 13.2 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.937 s | 76668 KB |
| [2208_number_theory_segment_tree.go](2208_number_theory_segment_tree.go) | Go 1.14 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.578 s | 121460 KB |
| [2208_number_theory_segment_tree.java](2208_number_theory_segment_tree.java) | Java 1.8 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.906 s | 61776 KB |
| [2208_number_theory_segment_tree.py](2208_number_theory_segment_tree.py) | PyPy 3.10 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 1.640 s | 48276 KB |
| [2208_number_theory_segment_tree.rs](2208_number_theory_segment_tree.rs) | Rust 1.75 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.375 s | 61924 KB |
