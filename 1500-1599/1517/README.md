# 1517. Freedom of Choice

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · difficulty 240 · suffix_structures

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two speeches of N capital Latin letters each (1 ≤ N ≤ 100000) are given.
Print their longest common piece: the longest string that occurs in
both as a contiguous part. Any longest one is accepted.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then the two speeches, one per line.

## Output

The longest common piece; an empty line if the speeches share no
letter.

## Examples

### Example 1

Input:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

Output:

```
THEGREATALBANIA
```

## Solution

Build the suffix automaton of the first speech: its states are the
classes of substrings that end at the same set of positions, with the
length of the longest string in each class and a suffix link to the
class of its shorter suffixes. It has at most 2N states and is built
letter by letter in `O(N)`. Then read the second speech through it,
keeping the state and the length run of the longest suffix of the read
part that occurs in the first speech. When the next letter has no
transition, follow suffix links, setting run to the length of each
state reached, until one has the transition or the start is reached;
then take the transition and add one. The largest run, and where it
ended in the second speech, give the answer. `O(N)` with an alphabet of
26.

Pitfalls:

- the speeches may share no letter, and then the answer is an empty
  line (test 03, gen5);
- the answer can be a whole speech (gen4);
- comparing every pair of positions takes 10¹⁰ steps;
- many pieces can tie, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB |
