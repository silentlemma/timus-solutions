# 2193. Best rhyme score: suffix length halved for every mismatch

[Timus 2193](https://acm.timus.ru/problem.aspx?space=1&num=2193) · difficulty 1456 · strings

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two words rhyme on a suffix length L with the score L / 2ᵏ, where k is
the number of positions where their last L letters differ, and their
rhyme is the best score over all L. Given N words and Q queries
"u v c", find the rhyme of words u and v after cutting c letters from
the end of both. Answers within 10⁻⁶ are accepted. The limits are
3 seconds and 256 MB.

## Input

N and Q, 2 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁵, then N words of lowercase letters
with total length up to 10⁶, then the Q queries with
0 ≤ c < min(|s_u|, |s_v|).

## Output

The score for each query.

## Examples

### Example 1

Input:

```
5 7
fate
cmake
stake
cfake
cmate
1 2 0
2 3 0
1 4 0
2 5 0
1 5 0
1 4 1
2 5 2
```

Output:

```
1.5
3
2
2.5
3
1.5
3
```

## Solution

Align the two words at their ends. For a fixed number k of mismatches
the longest suffix is the best, so the candidates are the lengths just
before the (k + 1)-th mismatch counted from the cut, with score
L / 2ᵏ. The first mismatch may sit right at the cut, but then k = 1
already scores at least 1/2, while k ≥ 18 scores at most 10⁵ / 2¹⁸ < 1/2.
So each query looks at no more than 18 mismatches.

Queries are grouped by their pair of words, and each pair builds the
mismatch positions of its two aligned endings once: the compiled
languages compare the letters directly, and Python XORs the two words
read as big integers and finds the nonzero bytes. A query then jumps
from mismatch to mismatch, starting at its cut, and stops when even the
whole remaining length divided by the next power of two cannot beat the
best score. Equal word numbers or identical endings give the full
remaining length at once.

C++ and Python store multiples of 2⁻¹⁸; the other languages store exact
fractions. All print exact decimals.

In the example "fate" and "cmake" end in "fate" and "make"; with one
mismatch the suffix "ate" against "ake" gives 3/2 = 1.5, the best.

Pair preprocessing costs O(S sqrt Q), at most about 2 · 10⁸ letters,
where S is total word length. Queries cost O(18), or O(M) in Python for
maximum word length M; sorting adds O(Q log Q) in the compiled languages.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2193_strings.cpp](2193_strings.cpp) | G++ 13.2 x64 | strings | O(S sqrt Q + Q log Q + 18 Q) | AC | 0.531 s | 5344 KB |
| [2193_strings.go](2193_strings.go) | Go 1.14 x64 | strings | O(S sqrt Q + Q log Q + 18 Q) | AC | 0.625 s | 15792 KB |
| [2193_strings.java](2193_strings.java) | Java 1.8 | strings | O(S sqrt Q + Q log Q + 18 Q) | AC | 0.734 s | 17408 KB |
| [2193_strings.py](2193_strings.py) | Python 3.12 x64 | strings | O(S + M Q) | AC | 2.187 s | 61240 KB |
| [2193_strings.rs](2193_strings.rs) | Rust 1.75 x64 | strings | O(S sqrt Q + Q log Q + 18 Q) | AC | 0.390 s | 15092 KB |
