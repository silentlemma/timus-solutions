# 1225. Rows of white, blue and red stripes

[Timus 1225](https://acm.timus.ru/problem.aspx?space=1&num=1225) · difficulty 35 · dp

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A row of `N ≤ 45` stripes is made of white, blue and red ones. No two
neighbouring stripes share a colour, and a blue stripe must stand between
a white and a red one. Count the possible rows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of rows.

## Examples

### Example 1

Input:

```
1
```

Output:

```
2
```

## Solution

A blue stripe needs neighbours on both sides, so a row never ends in
blue; it ends in white or red. Let `f(n)` count the valid rows of length
`n`. Before a last white stripe there is either red, which closes a valid
row of length `n − 1` ending in red, or blue preceded by red, which
closes a valid row of length `n − 2` ending in red; the same holds for
red with the colours swapped. By symmetry half of the rows of each length
end in red, so `f(n) = f(n − 1) + f(n − 2)` with `f(1) = f(2) = 2`:
twice the Fibonacci numbers. `O(N)`.

Pitfalls:

- a single stripe can be white or red but not blue, so `f(1) = 2`;
- for `N = 45` the count is 2,269,806,340, beyond 32-bit signed integers.

The formula was checked by brute force over all colourings up to 12
stripes, and every `N` from 1 to 45 was compared with a separately
written solution.

## Language notes

- All languages run the same loop with 64-bit integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1225_dp.cpp](1225_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB |
| [1225_dp.go](1225_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1072 KB |
| [1225_dp.java](1225_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB |
| [1225_dp.py](1225_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 372 KB |
| [1225_dp.rs](1225_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 216 KB |
