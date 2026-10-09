# 1110. All residues whose N-th power gives a remainder Y

[Timus 1110](https://acm.timus.ru/problem.aspx?space=1&num=1110) · difficulty 53 · bruteforce

Original problem from the Bulgarian National Olympiad in Informatics, Day 1.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N`, `M` and `Y` (`0 < N < 999`, `1 < M < 999`, `0 < Y < 999`),
find every integer `X` in `[0, M − 1]` with `X^N mod M = Y`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N M Y` on one line.

## Output

All such `X` in increasing order, separated by spaces, or `-1` if there
are none.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 6 4
```

Output:

```
2 4
```

## Solution

There are fewer than a thousand candidates, so try each `X` and compute
`X^N mod M` by repeated squaring, reducing modulo `M` after every
multiplication. `O(M log N)`.

Pitfalls:

- `Y` may be `M` or larger; a remainder never is, so the answer is then
  `-1`;
- `X^N` itself is astronomically large: reduce at every step, and keep
  the products below `M²`, which fits in 32 bits;
- with `N = 1` the answer is `Y` alone whenever `Y < M`.

The answers were checked against plain repeated multiplication, `N`
multiplications for every `X`.

## Language notes

- Python uses the built-in three-argument `pow`; the other languages
  carry a small power function.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1110_bruteforce.cpp](1110_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 196 KB |
| [1110_bruteforce.go](1110_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.015 s | 1104 KB |
| [1110_bruteforce.java](1110_bruteforce.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 1568 KB |
| [1110_bruteforce.py](1110_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.078 s | 352 KB |
| [1110_bruteforce.rs](1110_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M log N) | AC | 0.015 s | 212 KB |
