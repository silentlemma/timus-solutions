# 1745. Yet Another Answer

[Timus 1745](https://acm.timus.ru/problem.aspx?space=1&num=1745) · difficulty 817 · dp

Original problem by Damir Akhmetzyanov, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n words of brackets, join some of them, each at most once and in
any order, into the longest correct bracket sequence.

## Input

n (1 ≤ n ≤ 1000), then the words; their total length is at most 10 000.

## Output

The length l and the number k of words used, then the k word numbers
in order. Any longest answer is accepted.

## Examples

### Example 1

Input:

```
4
(
(((
(
))
```

Output:

```
4 3
1 3 4
```

### Example 2

Input:

```
3
()
(()
)
```

Output:

```
6 3
2 3 1
```

## Solution

Describe a word by the change of depth it causes and the lowest depth it
reaches from its start. In a best answer, the words that do not lower
the depth can go first, those that dip least first: moving such a word
earlier only raises the depth for everyone after it. The words that
lower the depth go last; reversed with brackets swapped, they are the
same case, which puts first those whose end is highest above their lowest
point. So there is a best answer that takes the chosen words in this one
fixed order.

Then it is a knapsack over the fixed order: for every depth d, the
longest prefix built so far that ends at depth d. A word may follow
depth d if d plus its lowest depth is not below zero, and leads to
depth d plus its change. The answer is the value at depth 0, and a
table of which words were taken gives the order back. Depths never pass
the total length L. `O(n·L)`, about 10⁷ steps.

In the first example `(`, `(` and `))` give `(())` of length 4; the
`(((` would need three more closing brackets.

Pitfalls:

- the empty answer is allowed: `0 0` and an empty line;
- a word like `)(` needs a depth of 1 before it and keeps the depth;
- the order inside each half matters: a word that dips deep must come
  while the depth is still high.

The checker verifies the sequence, the distinct word numbers and the
length. The lengths match a search over every ordered choice of words
on 400 random sets of up to 6 words, and an independent accepted
implementation on the large tests. The Python solution runs on PyPy,
since its 10⁷ steps take about 0.5 s on CPython here.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1745_dp.cpp](1745_dp.cpp) | G++ 13.2 x64 | dp | O(n·L) | AC | 0.031 s | 10276 KB |
| [1745_dp.go](1745_dp.go) | Go 1.14 x64 | dp | O(n·L) | AC | 0.031 s | 8588 KB |
| [1745_dp.java](1745_dp.java) | Java 1.8 | dp | O(n·L) | AC | 0.140 s | 12788 KB |
| [1745_dp.py](1745_dp.py) | PyPy 3.10 x64 | dp | O(n·L) | AC | 0.250 s | 23664 KB |
| [1745_dp.rs](1745_dp.rs) | Rust 1.75 x64 | dp | O(n·L) | AC | 0.046 s | 10488 KB |
