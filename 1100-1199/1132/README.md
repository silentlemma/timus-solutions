# 1132. All square roots of a modulo a prime n, for up to 100000 queries

[Timus 1132](https://acm.timus.ru/problem.aspx?space=1&num=1132) · difficulty 548 · number_theory

Original problem by Mikhail Medvedev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For up to `K ≤ 100000` queries `a, n` with a prime `n ≤ 32767` and
`1 ≤ a ≤ 32767` not divisible by `n`, print all `x` from `1` to `n − 1`
with `x² ≡ a (mod n)` in increasing order, or `No root` if there are none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`, then `K` lines with `a` and `n`.

## Output

One line per query: the roots separated by spaces, or `No root`.

## Examples

### Example 1

Input:

```
5
4 17
3 7
2 7
14 31
10007 20011
```

Output:

```
2 15
No root
3 4
13 18
5382 14629
```

## Solution

Reduce `a` modulo `n`. For `n = 2` the only root is `1`. For an odd prime,
Euler's criterion decides whether a root exists: `a^((n−1)/2)` is `1` for a
quadratic residue and `n − 1` otherwise. If a root `r` exists, the other
one is `n − r`, and they differ because `n` is odd and `a` is not zero.

The root itself comes from the Tonelli–Shanks algorithm. Write
`n − 1 = q·2^s` with odd `q` and take any non-residue `z`. Start with
`r = a^((q+1)/2)`, `t = a^q` and `c = z^q`; then `r² = a·t` always holds.
While `t ≠ 1`, find the least `i` with `t^(2^i) = 1`, set
`b = c^(2^(s−i−1))`, and update `r ← r·b`, `t ← t·b²`, `c ← b²`, `s ← i`.
Each step lowers the order of `t`, so after at most `s` steps `t = 1` and
`r² = a`. The smallest non-residue of each prime is found once and kept.
For `n ≡ 3 (mod 4)` the loop does not run at all and `r = a^((n+1)/4)`.
`O(log² n)` per query.

Pitfalls:

- `a` can be larger than `n`, so reduce it first;
- `n = 2` has a single root, `1`, and Euler's criterion does not apply;
- the two roots are printed smaller first;
- with up to 100000 queries, input and output are buffered.

The answers were compared on every test with a table of all squares
modulo each prime that occurs.

## Language notes

- All languages run the same Tonelli–Shanks and cache the non-residue per
  prime.
- Go reads the 200000 numbers with a small byte reader, which is faster
  than `fmt.Fscan`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1132_number_theory.cpp](1132_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log² n) | AC | 0.203 s | 2196 KB |
| [1132_number_theory.go](1132_number_theory.go) | Go 1.14 x64 | number_theory | O(K log² n) | AC | 0.093 s | 1668 KB |
| [1132_number_theory.java](1132_number_theory.java) | Java 1.8 | number_theory | O(K log² n) | AC | 0.281 s | 5908 KB |
| [1132_number_theory.py](1132_number_theory.py) | Python 3.12 x64 | number_theory | O(K log² n) | AC | 0.468 s | 19404 KB |
| [1132_number_theory.rs](1132_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log² n) | AC | 0.015 s | 4068 KB |
