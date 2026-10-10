# 1174. The position of a permutation in the adjacent-swap order

[Timus 1174](https://acm.timus.ru/problem.aspx?space=1&num=1174) · difficulty 716 · math

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001; the generating program in the statement is based on programs by Frank Ruskey.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A given program lists all `N!` permutations of `1..N` (`N ≤ 100`),
starting with `1 2 … N` and each time swapping two neighbours. It does
this recursively: element `k` sweeps step by step across the arrangement
of the smaller elements, alternating its direction, and between its steps
the larger elements go through all their moves. Given a permutation, find
its line number in that list.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then the permutation.

## Output

The position, counted from 1; it can have over 150 digits.

## Examples

### Example 1

Input:

```
4 
2 3 1 4
```

Output:

```
17
```

## Solution

Look only at the elements `1..k` and ignore the larger ones. Their
relative order changes only when element `k` or a smaller one moves, so
the list of these orders is the same list for `k` elements. In it,
element `k` makes one sweep of `k` positions for each order of `1..k−1`,
and the sweeps alternate: the first one goes from the right end to the
left, the next from the left to the right, and so on.

So if `rank(k−1)` is the 0-based position of the order of `1..k−1`, the
order of `1..k` sits in sweep number `rank(k−1)`, at offset `s` within it,
where `s` is the number of smaller elements to the left of `k` when the
sweep goes rightwards (odd sweeps), and `k − 1` minus that when it goes
leftwards (even sweeps). Then `rank(k) = rank(k−1)·k + s`, and the answer
is `rank(N) + 1`. `O(N²)` for the counts plus big-number steps.

Pitfalls:

- the direction depends on the parity of `rank(k−1)`, a big number, but
  only its last digit is needed;
- the program starts with element `k` at the right end moving left,
  which makes the even sweeps the leftward ones;
- `100!` has 158 digits, so 64 bits are far from enough.

The answers were checked against a direct run of the listing program for
every permutation with `N ≤ 6`, and compared with a separately written
solution on random permutations of up to 100 elements.

## Language notes

- Python, Go and Java use their big integers; C++ and Rust keep the rank
  as base-10⁹ digits with one operation, multiply and add a small number.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1174_math.cpp](1174_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 196 KB |
| [1174_math.go](1174_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1176 KB |
| [1174_math.java](1174_math.java) | Java 1.8 | math | O(N²) | AC | 0.140 s | 1832 KB |
| [1174_math.py](1174_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.062 s | 408 KB |
| [1174_math.rs](1174_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.015 s | 236 KB |
