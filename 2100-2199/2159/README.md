# 2159. Shortest and smallest essay that obeys word-order rules

[Timus 2159](https://acm.timus.ru/problem.aspx?space=1&num=2159) · difficulty 1303 · graphs, greedy

Original problem by Valentin Zuev, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An essay is a sequence of words separated by single spaces. It must
contain n keywords, and each of k rules (a, b) says that wherever a
occurs, b must occur somewhere later. Print the shortest essay that
satisfies everything, and among the shortest the lexicographically
smallest one, with the space smaller than every letter; print −1 if none
exists. The limits are 2 seconds and 256 MB.

## Input

n and k, 1 ≤ n, k ≤ 10⁵, the n distinct keywords, then the k distinct
rules; the total length of all words is at most 2 · 10⁶. Each word is a
nonempty sequence of lowercase Latin letters.

## Output

The essay, or −1.

## Examples

### Example 1

Input:

```
2 3
atan
tan
atan ate
atan tabular
zzz atan
```

Output:

```
atan ate tabular tan
```

### Example 2

Input:

```
1 3
a
a b
b c
c a
```

Output:

```
-1
```

## Solution

The words that must appear are the keywords and everything reachable
from them along the rules, found with one search. Writing each of them
once is enough when possible, so the shortest essay has a fixed set of
words and a fixed length. A word must come before all words its rules
point to among them; repeating a word does not help, since the rules of
its last copy still have to be met later. So an essay exists exactly
when these words form no cycle, and then it is a topological order of
them.

All such orders have the same length, so the smallest one is built
greedily: Kahn's algorithm with a priority queue always writes the
smallest word that is free. Comparing words directly is right, because
a word followed by a space is smaller than any longer word starting with
it, the space being the smallest character.

Let L be the total input word length, V the number of distinct input
words, and W the maximum word length. With expected hash-table costs,
the time is O(L + k + V W log(V + 1)) and the space is O(L + V + k).
Each heap operation can compare O(log(V + 1)) pairs of words, and each
comparison can scan O(W) characters.

Pitfall: n counts only keywords; rules can introduce more required
words (test gen6, `heap 6`). Long common prefixes (test gen10,
`prefix 10`) can be scanned repeatedly by heap comparisons, so their
cost cannot be charged just once to L. In particular, two long words
waiting beside a chain of short words can be compared at every chain
step, even with only three keywords.

In the first example "zzz" never has to appear, and the required words
atan, ate, tabular and tan come out in alphabetical order once atan is
written.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2159_graphs_greedy.cpp](2159_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.156 s | 19804 KB |
| [2159_graphs_greedy.go](2159_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.203 s | 28672 KB |
| [2159_graphs_greedy.java](2159_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.515 s | 31516 KB |
| [2159_graphs_greedy.py](2159_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.625 s | 53616 KB |
| [2159_graphs_greedy.rs](2159_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.140 s | 24824 KB |
