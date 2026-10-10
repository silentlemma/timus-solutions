# 1189. Pairs X + Y = N where Y is X with one digit struck out

[Timus 1189](https://acm.timus.ru/problem.aspx?space=1&num=1189) · difficulty 500 · math

Original problem by Vladimir Lelyukh and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `10 ≤ N ≤ 10⁹`, find all pairs `X + Y = N` where `X` has at least
two digits and no leading zero, and `Y` is `X` with one digit struck out,
written with one digit fewer than `X` (so it may start with zeros). Print
their number and the pairs in increasing order of `X`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of pairs, then lines `X + Y = N`.

## Examples

### Example 1

Input:

```
302
```

Output:

```
5
251 + 51 = 302
275 + 27 = 302
276 + 26 = 302
281 + 21 = 302
301 + 01 = 302
```

## Solution

Strike the digit `d` at place `k` (counted from the right, starting at 0)
out of `X`. Write `X = (10a + d)·10ᵏ + b` with `b < 10ᵏ`; then
`Y = a·10ᵏ + b`, and

`X + Y = (11a + d)·10ᵏ + 2b = N`.

So `2b` is congruent to `N` modulo `10ᵏ`. Since `2b < 2·10ᵏ`, it is
either `N mod 10ᵏ` or that plus `10ᵏ`, and it must be even with
`b < 10ᵏ`. The rest, `(N − 2b)/10ᵏ`, is `11a + d`, which gives `a` and
`d` by division by 11; the remainder must be a real digit, not 10. Keep
`X` if it has at least two digits and starts with a non-zero digit, that
is, `a > 0` or `d > 0`. At most two candidates per place, `O(log N)` in
all.

Pitfalls:

- the same pair can come from striking different equal digits, as in
  `11 + 1 = 12`, so candidates go into a set;
- `Y` is printed with exactly one digit fewer than `X`, with leading
  zeros, as in `301 + 01`;
- the remainder `d` from the division by 11 can be 10, which is not a
  digit.

The answers were compared with a direct search over all `X` for every `N`
up to 1199 and for 150 random `N` up to 200000, and with a separately
written solution on every test.

## Language notes

- All languages print `Y` with a width taken from the length of `X` and
  zero padding.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1189_math.cpp](1189_math.cpp) | G++ 13.2 x64 | math | O(log N) | AC | 0.015 s | 188 KB |
| [1189_math.go](1189_math.go) | Go 1.14 x64 | math | O(log N) | AC | 0.031 s | 1124 KB |
| [1189_math.java](1189_math.java) | Java 1.8 | math | O(log N) | AC | 0.109 s | 1872 KB |
| [1189_math.py](1189_math.py) | Python 3.12 x64 | math | O(log N) | AC | 0.093 s | 448 KB |
| [1189_math.rs](1189_math.rs) | Rust 1.75 x64 | math | O(log N) | AC | 0.015 s | 236 KB |
