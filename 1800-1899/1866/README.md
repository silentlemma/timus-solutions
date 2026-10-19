# 1866. Poetic Foot

[Timus 1866](https://acm.timus.ru/problem.aspx?space=1&num=1866) · difficulty 751 · parsing

Original problem by Alex Samsonov, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A foot is a group of syllables with one of them stressed. Trochee and
iamb have feet of two syllables stressed on the first and the second;
dactyl, amphibrach and anapaest have feet of three syllables stressed
on the first, the second and the third. Every line of a poem is a run of
feet of one kind, and the last foot may be cut short. Syllables of a
word are joined by hyphens and stressed syllables are in square
brackets. Name the meter of the poem, or print "not a poem".

## Input

n (2 ≤ n ≤ 100), then n lines of at most 50 characters with at least
four syllables each, made of Latin letters, spaces, hyphens and square
brackets.

## Output

"trochee", "iamb", "dactyl", "amphibrach", "anapaest" or "not a poem".

## Examples

### Example 1

Input:

```
4
My [un]-cle [high] i-[deals] ins-[pire] him
But [when] past [jo]-king [he] fell [sick]
he [real]-ly [forced] one [to] ad-[mire] him
and [ne]-ver [played] a [shrew]-der [trick]
```

Output:

```
iamb
```

## Solution

Split each line at spaces and hyphens into syllables and mark the ones
holding a bracket. A meter with feet of k syllables stressed at place p
fits a line when syllable i (from 0) is stressed exactly when
i mod k = p − 1. A cut last foot changes nothing, since only places
inside a foot matter. The poem has the first meter that fits every
line; with at least four syllables in a line no two meters give the
same marks, so the order of the checks does not matter. `O(L)` for L
characters in all.

In the example every line stresses syllables 2, 4, 6, 8, which is iamb.

Pitfalls:

- every syllable must agree, unstressed ones too: an unstressed syllable
  at a stressed place breaks the meter;
- there may be several spaces between words, so empty pieces must be
  skipped;
- "not a poem" is three words, which the output must spell exactly.

The answers agree with an independent accepted implementation on 300
random poems, 120 of them broken in one syllable or in one line.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1866_parsing.cpp](1866_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 432 KB |
| [1866_parsing.go](1866_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1156 KB |
| [1866_parsing.java](1866_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.125 s | 1132 KB |
| [1866_parsing.py](1866_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 480 KB |
| [1866_parsing.rs](1866_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 240 KB |
