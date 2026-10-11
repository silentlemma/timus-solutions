# 1238. Folding a string with repeat counts

[Timus 1238](https://acm.timus.ru/problem.aspx?space=1&num=1238) · difficulty 415 · dp

Original problem by Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A folded sequence is a letter, two folded sequences written one after the
other, or `X(S)` for a folded sequence S and an integer X > 1, which
stands for S repeated X times. Given a string of 1 to 100 capital
letters, print a shortest folded sequence that unfolds to it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The string.

## Output

A shortest folded sequence; any of them will do.

## Checking

Several foldings can be equally short, so the checker unfolds the
answer, compares it with the input and compares its length with the
minimum length.

## Examples

### Example 1

Input:

```
AAAAAAAAAABABABCCD
```

Output:

```
9(A)3(AB)CCD
```

### Example 2

Input:

```
NEERCYESYESYESNEERCYESYESYES
```

Output:

```
2(NEERC3(YES))
```

## Solution

Let `best[i][j]` be the length of the shortest folding of `s[i..j]`. Its
top level is either a concatenation, so it splits into two shorter
foldings at some k, or a single `X(S)`, so the segment is S's unfolding
repeated X times. That gives the interval DP, by growing length:

- `best[i][j] = min(best[i][k−1] + best[k][j])` over the split points;
- for each divisor p < length of the segment's length such that the
  segment has period p, also `digits(length/p) + 2 + best[i][i+p−1]`.

The segment has period p exactly when it equals itself shifted by p,
`s[i..j−p] = s[i+p..j]`. Each interval remembers its choice, and the
folding is rebuilt from the top. `O(n³)` with n ≤ 100.

Pitfalls:

- counts can have two or three digits, and their length counts:
  `100(A)` and `A99(A)` are equally short (test 04);
- the inner part of a repeat is itself folded, as in `2(NEERC3(YES))`.

## Language notes

- All languages compare the shifted substrings with one library call.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1238_dp.cpp](1238_dp.cpp) | G++ 13.2 x64 | dp | O(n³) | AC | 0.031 s | 460 KB |
| [1238_dp.go](1238_dp.go) | Go 1.14 x64 | dp | O(n³) | AC | 0.031 s | 1264 KB |
| [1238_dp.java](1238_dp.java) | Java 1.8 | dp | O(n³) | AC | 0.125 s | 1108 KB |
| [1238_dp.py](1238_dp.py) | Python 3.12 x64 | dp | O(n³) | AC | 0.125 s | 696 KB |
| [1238_dp.rs](1238_dp.rs) | Rust 1.75 x64 | dp | O(n³) | AC | 0.046 s | 316 KB |
