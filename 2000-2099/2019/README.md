# 2019. Matching Typed Endpoints Without Crossing

[Timus 2019](https://acm.timus.ru/problem.aspx?space=1&num=2019) · difficulty 297 · greedy

Original problem by Denis Dublennykh, prepared by Oleg Merkurev, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `2n` ordered distinct endpoints on a semicircle, described by Latin
letters. Exactly `n` letters are uppercase and `n` are lowercase. Match each
uppercase endpoint to a lowercase endpoint of the same letter, ignoring case,
using each endpoint once. The straight connecting segments must not cross.
Find any such matching or report that none exists.

Here `1 ≤ n ≤ 5,000`; all 26 letter types may occur repeatedly.
Uppercase endpoints and lowercase endpoints are numbered **separately**
from 1 to `n` in their order along the word. Time limit: 1 second.
Memory limit: 64 MB.

## Input

The first line contains `n`. The second contains the word of exactly `2n`
uppercase and lowercase Latin letters.

## Output

If possible, print `n` distinct indices: the lowercase endpoint matched to
uppercase endpoint 1, then to uppercase endpoint 2, and so on. Any valid
matching is allowed. Otherwise print exactly `Impossible`.

## Checking

A checker verifies that the pairs match letters of the same type, use
every endpoint once and do not cross; `Impossible` is accepted only when
no matching exists. Any valid matching is accepted.

## Examples

```
2
AbBa
```

```
2 1
```

```
2
AbaB
```

```
Impossible
```

```
1
Ab
```

```
Impossible
```

## Solution

Two chords between points on a semicircle cross exactly when their
endpoints alternate in order. Nested and disjoint pairs are safe. Every
complete noncrossing matching has an innermost pair whose endpoints are
adjacent among the remaining positions. Removing such pairs reduces the
word to empty. Conversely, cancelling adjacent equal letters of opposite
case constructs a noncrossing matching: the endpoints inside each
recorded pair were already paired.

Scan left to right with a stack of unmatched endpoints. Give each endpoint
its next uppercase or lowercase ID. If the current letter and the stack top
are the same type with opposite case, pop and record their pair. Otherwise
push the current endpoint. Uppercase-first and lowercase-first pairs are both
allowed. Store the lowercase ID in the answer slot belonging to the uppercase
ID, whichever endpoint arrived first. A leftover stack means `Impossible`.

Why can a greedy cancellation never lose a solution? Consider any two choices
of an adjacent opposite-case pair. Disjoint cancellations commute: deleting
both leaves the same word. Overlapping choices must have the form `xXx` or
`XxX`; deleting either pair leaves the same letter. Every cancellation
shortens the word. Induction on word length now proves that all complete
cancellation orders have the same irreducible result: after two different
first choices, either the words already agree or another deletion makes
them agree, and the shorter words satisfy the induction hypothesis.

The stack always holds an irreducible form of the processed prefix.
Appending one letter either cancels its top or keeps the prefix
irreducible. Thus the stack computes this common reduced result. If a
full noncrossing matching exists, its innermost-pair deletions end at
empty, so the greedy stack also ends empty. If the stack is nonempty, no
deletion order, hence no such matching, can succeed. When it is empty,
the recorded pairs are nested or disjoint, are type-compatible and cover
every endpoint once, proving correctness.

For `AbBa`, first cancel `bB`, then `Aa`; the uppercase IDs match lowercase
IDs `2 1`. For `AbaB`, the only type-compatible pairs alternate their
endpoints and must cross. For `Ab`, the types already differ.
Even equal totals for each letter type are insufficient, as `ABab` shows.

Every endpoint is pushed at most once and popped at most once, giving
`O(n)` time and `O(n)` memory. The stack has at most `2n ≤ 10,000` entries.

Pitfalls:

- Count uppercase and lowercase IDs independently; word positions are
  different indices.
- Match opposite cases of the same letter, never two equal-case letters.
- Allow lowercase endpoints to appear before their uppercase partners.
- Equal per-type counts do not guarantee a noncrossing matching.
- Output partners in uppercase order and preserve the exact spelling
  `Impossible`.

## Language notes

The implementations use ASCII bytes or characters; opposite cases of the
same Latin letter differ by bit 32. C++ and Go use endpoint structs, Rust
and Python use pairs, and Java uses parallel arrays with a stack size.
All traversals are iterative and all indices fit ordinary integer types.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2019_greedy.cpp](2019_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 468 KB |
| [2019_greedy.go](2019_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 1412 KB |
| [2019_greedy.java](2019_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 912 KB |
| [2019_greedy.py](2019_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 1200 KB |
| [2019_greedy.rs](2019_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 396 KB |
