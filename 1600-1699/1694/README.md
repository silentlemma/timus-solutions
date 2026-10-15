# 1694. Killer Words

[Timus 1694](https://acm.timus.ru/problem.aspx?space=1&num=1694) · difficulty 2933 · backtracking

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A killer word uses only the first m Latin letters, is a k-repetition
(k copies of one word written one after another), and has no proper
substring that is a k-repetition. Count the killer words of length at
most n.

## Input

m, k, n (1 ≤ m ≤ 18; 2 ≤ k ≤ 5; 1 ≤ n ≤ 22).

## Output

The number of killer words.

## Examples

### Example 1

Input:

```
3 2 4
```

Output:

```
9
```

## Solution

A killer word is wᵏ for a word w of length L ≤ n / k, at most 11. Whether
wᵏ qualifies does not depend on which letters w uses, only on their
pattern. So enumerate w with its letters numbered in order of first
appearance (0, then 0 or 1, and so on). A pattern with d different
letters stands for m(m − 1)⋯(m − d + 1) words.

Every substring of w is a substring of wᵏ, so a prefix of w that already
ends in a k-repetition can be dropped together with all its extensions.
For every surviving w, check wᵏ itself. As w has no k-repetition and wᵏ
has period L, only windows that start in the first copy of w and reach
beyond it need a look. A w whose power fails is still extended, because
a longer w may work: (010)² contains 00, while (0102)² is fine.

The counts of patterns by length and number of letters are summed with
the falling factorials of m. The search visits about 10⁵ patterns for
k = 2 and n = 22, and far fewer for larger k. The largest answer,
3.5 · 10¹³, fits in 64 bits.

Pitfalls:

- the whole word is not a proper substring, so wᵏ itself is allowed;
- do not stop at a w whose power fails (test 06 with three letters
  needs this);
- n < k leaves no word at all (test 07).

The Python solution is submitted under PyPy: a local CPython run takes
about 0.6 s for k = 2 and n = 22, too close to the 1 s limit.

The answers match a count over all words for small m and n, and an
independent accepted implementation on 120 parameter sets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1694_backtracking.cpp](1694_backtracking.cpp) | G++ 13.2 x64 | backtracking | about 10^5 patterns | AC | 0.062 s | 192 KB |
| [1694_backtracking.go](1694_backtracking.go) | Go 1.14 x64 | backtracking | about 10^5 patterns | AC | 0.156 s | 1120 KB |
| [1694_backtracking.java](1694_backtracking.java) | Java 1.8 | backtracking | about 10^5 patterns | AC | 0.171 s | 1596 KB |
| [1694_backtracking.py](1694_backtracking.py) | PyPy 3.10 x64 | backtracking | about 10^5 patterns | AC | 0.546 s | 7688 KB |
| [1694_backtracking.rs](1694_backtracking.rs) | Rust 1.75 x64 | backtracking | about 10^5 patterns | AC | 0.078 s | 232 KB |
