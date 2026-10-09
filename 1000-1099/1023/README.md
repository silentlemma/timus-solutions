# 1023. Choosing the move limit that lets the second player win

[Timus 1023](https://acm.timus.ru/problem.aspx?space=1&num=1023) · difficulty 217 · games, number_theory

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players take turns removing from 1 to `L` buttons from a pile of `K`
buttons; whoever takes the last button wins. The first player has chosen
`K` (`3 ≤ K ≤ 10^8`); now the second player chooses `L` with `2 ≤ L < K`.
Find the smallest `L` with which the second player wins against any play of
the first, or print 0 if there is none.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`K`.

## Output

The smallest winning `L`, or 0.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
8
```

Output:

```
3
```

### Example 2

Input:

```
35
```

Output:

```
4
```

## Solution

**The game.** With moves of 1 to `L` buttons, the positions where the player
to move loses are exactly the multiples of `L + 1`: from such a pile every
move leaves a non-multiple, and from a non-multiple the move that removes
`n mod (L + 1)` buttons leaves a multiple. So the second player wins exactly
when `L + 1` divides `K`.

**The choice of L.** We need the smallest `L ≥ 2` with `L + 1 | K`, i.e. the
smallest divisor `d ≥ 3` of `K`, and `L = d - 1`; the condition `L < K` is
`d ≤ K`. Since `d = K` always works (`K ≥ 3`), the answer is never 0.

**Finding d quickly.** Try `d = 3, 4, ...` while `d^2 ≤ K`. If none divides
`K`, the smallest divisor above `sqrt(K)` is `K / j` for the largest divisor
`j ≤ sqrt(K)` — and the only divisors up to `sqrt(K)` left are 1 and 2. So
`d = K / 2` if `K` is even and `K / 2 ≥ 3`, otherwise `d = K`. At most
`sqrt(10^8) = 10^4` steps.

Pitfalls:

- `K = 4`: the divisor 2 is too small and `K / 2 = 2` too, so `d = 4`,
  `L = 3`;
- `K = 2p` for a prime `p`: the divisor `p` is above `sqrt(K)` and must not
  be missed;
- trying every `L` up to `K` is `10^8` steps — fine in C++, too slow in
  Python.

## Language notes

The same divisor search in every language.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1023_games_number_theory.cpp](1023_games_number_theory.cpp) | G++ 13.2 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 128 KB |
| [1023_games_number_theory.go](1023_games_number_theory.go) | Go 1.14 x64 | games, number_theory | O(sqrt(K)) | AC | 0.031 s | 1072 KB |
| [1023_games_number_theory.java](1023_games_number_theory.java) | Java 1.8 | games, number_theory | O(sqrt(K)) | AC | 0.109 s | 1576 KB |
| [1023_games_number_theory.py](1023_games_number_theory.py) | Python 3.12 x64 | games, number_theory | O(sqrt(K)) | AC | 0.078 s | 400 KB |
| [1023_games_number_theory.rs](1023_games_number_theory.rs) | Rust 1.75 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 220 KB |
