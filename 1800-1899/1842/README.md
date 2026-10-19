# 1842. Local Roots

[Timus 1842](https://acm.timus.ru/problem.aspx?space=1&num=1842) · difficulty 5538 · strings

Original problem by Ivan Burmistrov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Cut a word w of n letters at a point i (1 ≤ i ≤ n − 1) into a prefix p
and a suffix s. The local root at i is the shortest nonempty word r such
that p and r end alike (one is a suffix of the other) and s and r begin
alike (one is a prefix of the other). Find a point where the local root
is the longest, and its length.

## Input

One word of lowercase Latin letters, 2 to 300 000 letters long.

## Output

The point and the length of the local root there. Any point with the
longest root is accepted.

## Examples

### Example 1

Input:

```
aababaaa
```

Output:

```
5 6
```

## Solution

A length L fits at point i exactly when w[k] = w[k + L] for every k
with i − L ≤ k < i and both indices inside the word: r written twice, ending
and starting at the cut, agrees with w wherever the two copies lie
inside it. The period P of w always
fits, so no local root is longer than P. The critical factorization
theorem says that some point has a local root of exactly P, and the
Crochemore–Perrin construction finds one in linear time.

Take the lexicographically greatest suffix of w twice: once under the
usual order of letters and once under the reversed order, with a
shorter word that is a prefix of a longer one counting as smaller in
both. The later of the two starting points is a critical point. A word
of one repeated letter is the only case where both suffixes are the
whole word; then any point works, so take 1. The greatest suffix is
found by the comparison loop of the Two-Way string search: a candidate
start, a running offset and the period of the matched part, each
mismatch moving the candidate or the scan forward. The period itself is
n minus the longest border, from the prefix function. `O(n)`.

In the example the period is 6, since the longest border is "aa". Under
a < b the greatest suffix is "babaaa", after 2 letters; under b < a it is
"aaa", after 5 letters. The answer is the point 5, where the local root
is "aaabab".

Pitfalls:

- the root can overhang both ends of the word, so a short side does not
  bound it;
- the time limit is half a second, so use a linear algorithm; the
  Python solution runs on PyPy.

The answers pass a checker that recomputes the period and confirms that
no shorter root fits at the printed point. On all words of up to 8
letters over three letters and up to 12 letters over two, the points
are critical by direct search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1842_strings.cpp](1842_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 1652 KB |
| [1842_strings.go](1842_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 7380 KB |
| [1842_strings.java](1842_strings.java) | Java 1.8 | strings | O(n) | AC | 0.140 s | 4904 KB |
| [1842_strings.py](1842_strings.py) | PyPy 3.10 x64 | strings | O(n) | AC | 0.296 s | 4344 KB |
| [1842_strings.rs](1842_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 3444 KB |
