# 1724. Origin of Man Clarified

[Timus 1724](https://acm.timus.ru/problem.aspx?space=1&num=1724) · difficulty 666 · strings

Original problem by Alex Samsonov (prepared by Ivan Burmistrov), from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

DNA strings use the nucleotides `A`, `C`, `G`, `T` and their
antinucleotides `a`, `c`, `g`, `t`. A human string is empty, two human
strings one after the other, or a human string with a nucleotide added
in front and its antinucleotide at the end. Answer whether given
substrings of a string are human.

## Input

A string of length L (1 ≤ L ≤ 100 000) over `ACGTacgt`, then q
(1 ≤ q ≤ 50 000) and q pairs l and r (1 ≤ l ≤ r ≤ L), the first and
last positions of a substring.

## Output

A line of q characters: `1` if the substring is human and `0`
otherwise.

## Examples

### Example 1

Input:

```
caAgtGTtgAacCc
5
2 3
6 9
10 11
1 14
13 14
```

Output:

```
01101
```

## Solution

Human strings are bracket sequences with four kinds of brackets: a
nucleotide opens and its antinucleotide closes. A substring is human
exactly when a stack, fed its letters, never meets a close that does
not fit the top and ends empty.

Feed the whole string to one stack and give the stack after each prefix
a name, a node of a tree. A push makes a new child of the current node,
a close that fits goes back to the parent, and a close that does not
fit, or meets the bottom, starts a new lone node. A substring from l to
r is human exactly when the node after r is the node after l − 1: a
human piece pushes only what it pops again, and any piece that dips
below its start, or meets a wrong close, can never come back, since
every later node is new. So each query is one comparison.
`O(L + q)`.

In the example `GTtg` (6–9), `Aa` (10–11) and `Cc` (13–14) are human,
while `aA` (2–3) closes before it opens, and so does the whole string.

Pitfalls:

- `cC` and `GTgt` are not human: the order and the nesting both
  matter;
- a close that fits the global stack may belong to an opener before l,
  which is why equal stack contents are not enough and the nodes must
  be the same;
- with 50 000 queries and a limit of 0.5 s, each query must be answered
  without walking through its substring.

The answers match a search straight from the grammar for every
substring of 300 short random strings, and an independent accepted
implementation on long ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1724_strings.cpp](1724_strings.cpp) | G++ 13.2 x64 | strings | O(L + q) | AC | 0.031 s | 1604 KB |
| [1724_strings.go](1724_strings.go) | Go 1.14 x64 | strings | O(L + q) | AC | 0.093 s | 6976 KB |
| [1724_strings.java](1724_strings.java) | Java 1.8 | strings | O(L + q) | AC | 0.125 s | 5808 KB |
| [1724_strings.py](1724_strings.py) | Python 3.12 x64 | strings | O(L + q) | AC | 0.140 s | 13904 KB |
| [1724_strings.rs](1724_strings.rs) | Rust 1.75 x64 | strings | O(L + q) | AC | 0.031 s | 3420 KB |
