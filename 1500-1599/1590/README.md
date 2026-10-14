# 1590. Bacon's Cipher

[Timus 1590](https://acm.timus.ru/problem.aspx?space=1&num=1590) · difficulty 186 · strings

Original problem by Alexey Zhevak, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the distinct non-empty substrings of a string of at most 5000
lowercase Latin letters.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The string.

## Output

The number of distinct substrings.

## Examples

### Example 1

Input:

```
aaba
```

Output:

```
8
```

## Solution

Build the suffix automaton of the string. Each state stands for the
substrings that end at the same set of positions; they have lengths from
len(link) + 1 to len, so the state holds len − len(link) distinct
substrings, and no substring belongs to two states. The answer is the
sum of len − len(link) over all states except the start. The automaton
has at most 2n states and is built in `O(n·26)` time and memory.
The results were checked against putting every substring into a set
for short strings.

Pitfalls:

- a random string of 5000 letters has about 12.5 million distinct
  substrings, so storing them is out of the question in 64 MB;
- when a state is split, the clone takes over all of the old state's
  transitions and its suffix link;
- test 02 has one letter and two states including the start, so the
  state count can equal 2n.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1590_strings.cpp](1590_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1428 KB |
| [1590_strings.go](1590_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2328 KB |
| [1590_strings.java](1590_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 2412 KB |
| [1590_strings.py](1590_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 3132 KB |
| [1590_strings.rs](1590_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 2272 KB |
