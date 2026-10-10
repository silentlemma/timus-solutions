# 1158. Counting the sentences of length M that avoid every forbidden word

[Timus 1158](https://acm.timus.ru/problem.aspx?space=1&num=1158) · difficulty 506 · strings

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An alphabet has `N ≤ 50` letters, and a sentence is any string of exactly
`M ≤ 50` letters. `P ≤ 10` forbidden words of at most 10 letters are
given; a sentence is forbidden if it contains one of them as a substring.
Count the sentences that are not forbidden. Letters can be any characters
with codes above 32, including codes above 127.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, `M` and `P`, then the `N` letters on one line, then the `P` words.

## Output

The number of allowed sentences.

## Examples

### Example 1

Input:

```
3 3 3
QWE
QQ
WEE
Q
```

Output:

```
7
```

## Solution

Build the Aho–Corasick automaton of the forbidden words: a trie with
failure links, completed so that every state has a transition for every
letter. A state stands for the longest end of the text so far that is a
prefix of some word; it is bad if a word ends there, directly or through
its failure links. A sentence is allowed exactly when reading it never
enters a bad state.

So count paths: `ways[s]` is the number of allowed beginnings of the
current length that end in state `s`. Start with one empty beginning at
the root and apply `M` steps, each sending `ways[s]` along all `N`
transitions that do not enter a bad state. The answer is the sum over all
states. The automaton has at most 101 states, so one step is about 5000
additions.

Pitfalls:

- the count can reach `50⁵⁰ ≈ 8.9·10⁸⁴`, so big integers are needed;
- a word containing another word is bad already at the shorter one, which
  the failure links carry over;
- letters are arbitrary bytes, possibly above 127, so the input is read
  as bytes and not decoded as text;
- the same word may be given twice.

The answers were compared with listing every sentence on 200 small random
inputs; the tests store letters above 127 as Latin-1 characters in
UTF-8, and the runner hands them to the solutions as single bytes.

## Language notes

- Python, Go and Java use their big integers; C++ and Rust add numbers
  kept in limbs of nine decimal digits, which is all the counting needs.
- Java reads the whole input as bytes and masks each byte to `0..255`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1158_strings.cpp](1158_strings.cpp) | G++ 13.2 x64 | strings | O(M·S·N) | AC | 0.015 s | 472 KB |
| [1158_strings.go](1158_strings.go) | Go 1.14 x64 | strings | O(M·S·N) | AC | 0.031 s | 1684 KB |
| [1158_strings.java](1158_strings.java) | Java 1.8 | strings | O(M·S·N) | AC | 0.109 s | 5476 KB |
| [1158_strings.py](1158_strings.py) | Python 3.12 x64 | strings | O(M·S·N) | AC | 0.093 s | 768 KB |
| [1158_strings.rs](1158_strings.rs) | Rust 1.75 x64 | strings | O(M·S·N) | AC | 0.031 s | 340 KB |
