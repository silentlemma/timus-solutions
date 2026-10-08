# 1007. Correcting one error in checksum code words

[Timus 1007](https://acm.timus.ru/problem.aspx?space=1&num=1007) · difficulty 404 · math

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every sent word is a string of `N` characters `0`/`1` (`4 ≤ N ≤ 1000`) whose
**weight** — the sum of the positions, counted from 1, of its ones — is
divisible by `N + 1` (weight 0 counts too). Each word suffers at most one of
these changes on the way:

- one `0` is replaced by `1`;
- one character is deleted;
- one character (`0` or `1`) is inserted anywhere.

Given the received words, print the sent words. The sent word is always
determined uniquely.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then at most 2001 received words, one per line. The input may also
contain extra spaces and empty lines.

## Output

The sent words in the input order, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
00000
10101
1011
111000
```

Output:

```
00000
10001
11011
11100
```

### Example 2

Input:

```
6   

001100  
   10101


0100110 
110111

```

Output:

```
001100
101101
010010
110011
```

## Solution

Let `m = N + 1` and let `w` be the weight of the received word, `L` its
length.

- `L = N`: either the word is intact (`w ≡ 0`), or a `0` at position `p`
  became `1`, which added exactly `p`; then `p = w mod m` and the character
  at `p` is reset to `0`.
- `L = N - 1` (a deletion): inserting a digit `d` at position `i` adds `d·i`
  plus one for every `1` to the right of it, since those move one position
  further. Go over `i = L+1, L, ..., 1`, keeping the count of ones to the
  right, and take the first `i` and `d` with
  `w + ones_right + d·i ≡ 0 (mod m)`.
- `L = N + 1` (an insertion): deleting the character `d` at position `i`
  subtracts `d·i` and one for every `1` to the right. The same right-to-left
  pass finds `i` with `w - ones_right - d·i ≡ 0 (mod m)`.

These are Varshamov–Tenengolts codes, which correct one deletion or insertion
(and, here, one raised zero): different sent words can never become the same
received word, so any position that makes the weight right gives the sent
word. Each word is handled in `O(N)`, the whole input in `O(total length)`.

Pitfalls:

- words are separated by arbitrary whitespace, so read tokens, not lines;
- in a deletion the missing character may be the last one: try the position
  after the end too;
- a brute force that rebuilds and re-weighs every candidate word is
  `O(N^2)` per word, up to `4·10^9` steps in total.

## Language notes

The same linear pass everywhere. Python builds the answer with string slices;
the work per word is two `O(N)` passes, fast enough for CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1007_math.cpp](1007_math.cpp) | G++ 13.2 x64 | math | O(total length) | AC | 0.015 s | 2420 KB |
| [1007_math.go](1007_math.go) | Go 1.14 x64 | math | O(total length) | AC | 0.015 s | 3336 KB |
| [1007_math.java](1007_math.java) | Java 1.8 | math | O(total length) | AC | 0.109 s | 13200 KB |
| [1007_math.py](1007_math.py) | Python 3.12 x64 | math | O(total length) | AC | 0.281 s | 4516 KB |
| [1007_math.rs](1007_math.rs) | Rust 1.75 x64 | math | O(total length) | AC | 0.015 s | 3104 KB |
