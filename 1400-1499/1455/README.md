# 1455. Freedom of Speech

[Timus 1455](https://acm.timus.ru/problem.aspx?space=1&num=1455) · difficulty 2023 · shortest_paths

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dictionary has N different words (1 ≤ N ≤ 100) of 1 to 100 small
Latin letters. After a reform, texts are written without separators.
Find a text of at most 20000 letters that splits into dictionary words
in two different ways, or print "NO" if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N words.

## Output

"NO", or "YES" and the text. Any such text is accepted.

## Examples

### Example 1

Input:

```
5
ab
acb
bc
abac
babbc
```

Output:

```
YES
abacbabbc
```

The text "abacbabbc" is both "abac" + "babbc" and "ab" + "acb" + "ab" +
"bc".

## Solution

Read two different splits of one text side by side, in the spirit of
the Sardinas–Patterson test. At any moment one split runs ahead of the
other by some tail, and that tail is always a suffix of a dictionary
word, so there are at most 100 · 100 states. The search starts from
every pair of words u ≠ v where u is a prefix of v, with tail v minus u.
From a tail t, a word w added to the split behind either ends exactly at
t, which closes an ambiguous text; or is longer and starts with t, so the
other split falls behind by the rest of w; or is a prefix of t, which
leaves the rest of t.

The cost of a state is the length of the text written so far, which
grows only when the split behind overtakes. Dijkstra's algorithm on
these costs finds the shortest ambiguous text, so if any text within the
limit exists, the one found is within it too; the text is rebuilt by
following the pieces back to the starting pair. `O((N² + S · N) · L log(N + S + 2))`
for S reached tail states and maximum word length L.

Pitfalls:

- a single word, a prefix code or a suffix code has no ambiguous text
  (tests 02, 05, 09, gen4, gen5);
- one split may run ahead for many steps, so the search has to follow
  tails, not just pairs of words (test 13);
- a plain breadth-first search counts steps, not letters, and may return
  a longer text than needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1455_shortest_paths.cpp](1455_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.031 s | 3968 KB |
| [1455_shortest_paths.go](1455_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.031 s | 3668 KB |
| [1455_shortest_paths.java](1455_shortest_paths.java) | Java 1.8 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.156 s | 4448 KB |
| [1455_shortest_paths.py](1455_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.218 s | 2884 KB |
| [1455_shortest_paths.rs](1455_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.031 s | 2876 KB |
