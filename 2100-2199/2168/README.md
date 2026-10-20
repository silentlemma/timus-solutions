# 2168. Covering a string with disjoint pieces that have a border

[Timus 2168](https://acm.timus.ru/problem.aspx?space=1&num=2168) · difficulty 3630 · dp, strings

Original problem by Vadim Barinov, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A row of N runes is a string of lowercase letters. One move lifts a
contiguous block of runes that are all still in place, provided some
proper prefix of the block equals its suffix of the same length (the
block has a border, like abcdab or aa, but not abc or a). Find the most
runes that can be lifted. The limits are 2 seconds and 256 MB.

## Input

N, 1 ≤ N ≤ 10⁵, then the string.

## Output

The largest number of lifted runes.

## Examples

### Example 1

Input:

```
6
abcdab
```

Output:

```
6
```

### Example 2

Input:

```
7
abcdabd
```

Output:

```
6
```

### Example 3

Input:

```
6
abacdc
```

Output:

```
6
```

## Solution

The lifted blocks are disjoint intervals of the original string, so let
f(i) be the fewest runes left behind among the first i, and the answer
is N − f(N). A block [l, e] has a border of length L exactly when the
text at l reappears at some p > l with LCP(l, p) ≥ L and e = p + L − 1.
So a start l and a later match p let every end in
p … p + LCP(l, p) − 1 inherit f(l), and otherwise f(i + 1) = f(i) + 1.

Two facts keep this small.

- **At most 26 runes are left.** Walk left to right: a rune whose letter
  appears again starts a block up to that letter's last occurrence, and
  a rune whose letter never appears again is skipped. Each letter is
  skipped at most once, so f only takes values 0 … 26.
- **For one letter, only starts with falling costs matter.** Take starts
  l₁ < l₂ with the same letter c and f(l₁) ≤ f(l₂), and a block
  [l₂, e] with border length L found at p. If L = 1, then s[p] = c and
  [l₁, p] is a block with border c, already reaching e with cost f(l₁).
  If L ≥ 2, the block [l₁, l₂] gives f(l₂ + 1) ≤ f(l₁), and [l₂ + 1, e]
  has the border of length L − 1 found at p + 1. Repeating the argument
  on the shorter border ends at L = 1, so l₂ is never needed.

So each letter keeps a stack of starts whose costs strictly fall, at
most 27 of them. At position p the solution scans the stack of s[p]
from the newest start, asks the suffix array for LCP(l, p) with a range
minimum over the LCP array (a sparse table in Python, a segment tree in
the other languages), and records, for each cost k, the farthest end any block of cost
k can reach. An older start only helps if its LCP is longer, since its
cost is higher. Then f(p + 1) is the smallest cost whose recorded end
covers p, or f(p) + 1.

In the third example the blocks aba and cdc lift all six runes.

The suffix array and the range-minimum structure take O(N log N), with counting
sort on rank pairs (the Python version sorts them, O(N log² N)), and the
scan adds O(27 N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2168_dp_strings.cpp](2168_dp_strings.cpp) | G++ 13.2 x64 | dp, strings | O(N log N) | AC | 0.062 s | 4128 KB |
| [2168_dp_strings.go](2168_dp_strings.go) | Go 1.14 x64 | dp, strings | O(N log N) | AC | 0.109 s | 10720 KB |
| [2168_dp_strings.java](2168_dp_strings.java) | Java 1.8 | dp, strings | O(N log N) | AC | 0.218 s | 4992 KB |
| [2168_dp_strings.py](2168_dp_strings.py) | PyPy 3.10 x64 | dp, strings | O(N log N) | AC | 0.968 s | 34932 KB |
| [2168_dp_strings.rs](2168_dp_strings.rs) | Rust 1.75 x64 | dp, strings | O(N log N) | AC | 0.093 s | 5604 KB |
