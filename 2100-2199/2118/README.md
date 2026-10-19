# 2118. Cutting a prefix-code bit string into undecodable pieces

[Timus 2118](https://acm.timus.ru/problem.aspx?space=1&num=2118) · difficulty 1366 · greedy, strings

Original problem by Alexey Danilyuk, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A message over an alphabet of k letters is encoded with a binary prefix
code, giving a bit string T. Cut T into the largest number of pieces so
that no piece can be decoded with the same code, or report that it is
impossible. The limits are 1 second and 64 MB.

## Input

k, 1 ≤ k ≤ 52, the message of up to 10⁶ letters from the first k of
A–Z a–z, then the k code words, each of length at most k.

## Output

The largest number of pieces, or −1.

## Examples

### Example 1

Input:

```
3
CACB
011
1
001
```

Output:

```
2
```

### Example 2

Input:

```
3
ACBABCAACABCAACC
0
10
110
```

Output:

```
-1
```

## Solution

Decoding with a prefix code is deterministic: at each position at most
one code word fits. The answer depends on the one-bit code words.

- None: a single bit never decodes, so every bit is a piece and the
  answer is the length of T.
- Both 0 and 1: every string decodes, so the answer is −1.
- Exactly one, call it g, and call the other bit b. Then every other
  code word starts with b. A piece made only of g decodes, so every
  piece contains a b and there are at most as many pieces as b bits.

In the last case a piece g…g b never decodes: the g bits decode one by
one and the final b alone is not a code word. Let p be the last
position of T such that no code word is a prefix of the suffix starting
at p. Every later suffix starts with a code word, and by induction it
decodes, so the last piece cannot start after p; and the suffix from p
itself does not decode. Cutting right after every b before p and leaving
the rest as the last piece gives (number of b before p) + 1 pieces, which
is the most possible. If there is no such p, or T has no b at all, the
answer is −1.

T can have 5 · 10⁷ bits, so it is not built. The suffixes are scanned
from the end with an Aho–Corasick automaton of the reversed code words:
a state is accepting when some code word is a prefix of the suffix read
so far. The transition for a whole letter from a given state is computed
bit by bit once and cached, so the scan costs O(|s|) plus O(k²) per
state, with at most k² states.

In the first example T = 0010110011 and g = 1. The suffix 0011 starts
with the code word 001, but no code word starts the suffix 010110011, so
p is the second bit, one 0 lies before it, and the answer is 2.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2118_greedy_strings.cpp](2118_greedy_strings.cpp) | G++ 13.2 x64 | greedy, strings | O(L + k^4) | AC | 0.031 s | 2016 KB |
| [2118_greedy_strings.go](2118_greedy_strings.go) | Go 1.14 x64 | greedy, strings | O(L + k^4) | AC | 0.031 s | 3340 KB |
| [2118_greedy_strings.java](2118_greedy_strings.java) | Java 1.8 | greedy, strings | O(L + k^4) | AC | 0.125 s | 7440 KB |
| [2118_greedy_strings.py](2118_greedy_strings.py) | Python 3.12 x64 | greedy, strings | O(L + k^4) | AC | 0.265 s | 4020 KB |
| [2118_greedy_strings.rs](2118_greedy_strings.rs) | Rust 1.75 x64 | greedy, strings | O(L + k^4) | AC | 0.031 s | 2140 KB |
