# 1423. String Tale

[Timus 1423](https://acm.timus.ru/problem.aspx?space=1&num=1423) · difficulty 170 · strings

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Strings S and T have the same length N (1 ≤ N ≤ 250 000) and consist of
characters with codes from 33 to 255. One cyclic shift moves the last
character of a string to the front. Print a number X (0 ≤ X < N) such
that X shifts turn S into T, or −1 if there is none; any X will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then S, then T.

## Output

X or −1.

## Examples

### Example 1

Input:

```
11
abracadabra
racadabraab
```

Output:

```
9
```

In the example, 9 shifts turn "abracadabra" into "racadabraab".

## Solution

X shifts to the right equal N − X shifts to the left, and the left
shifts of S by k are exactly the substrings of length N of S + S that
start at k < N. So find T in S + S: if it starts at position k, the
answer is (N − k) mod N, and if it does not occur, −1. The search is
Knuth–Morris–Pratt with the prefix function of T, run over S + S
without its last character; Python's built-in search of bytes is also
linear here. `O(N)`.

Pitfalls:

- a periodic S has several answers, so the tests use a checker
  (test 04);
- characters above 127 must be read as raw bytes; some readers decode
  them or even take code 160 for a space (test 05, gen3);
- a naive substring search can take quadratic time on strings of one
  repeated letter (gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1423_strings.cpp](1423_strings.cpp) | G++ 13.2 x64 | strings | O(N) | AC | 0.015 s | 1940 KB |
| [1423_strings.go](1423_strings.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 4268 KB |
| [1423_strings.java](1423_strings.java) | Java 1.8 | strings | O(N) | AC | 0.125 s | 3492 KB |
| [1423_strings.py](1423_strings.py) | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1372 KB |
| [1423_strings.rs](1423_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.031 s | 3052 KB |
