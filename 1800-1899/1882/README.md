# 1882. Old Nokia

[Timus 1882](https://acm.timus.ru/problem.aspx?space=1&num=1882) · difficulty 2585 · shortest_paths

Original problem by Mikhail Rubinchik, from the Ural Regional Team Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A phone book holds n distinct names in alphabetical order; at first
all of them are shown and the first one is current. "Up" and "down"
move through the shown names in a circle. Typing a letter shows only
the names starting with the typed letters and makes the first of them
current; a letter that no name continues with is not accepted. Erasing
the last letter keeps the current name and shows all names with the
shorter beginning. A button press takes a second; a letter costs as
many presses as its place on the key of a standard phone keypad (abc,
def, ghi, jkl, mno, pqrs, tuv, wxyz). For every name, find the least
time to make it current.

## Input

n (1 ≤ n ≤ 10⁵), then the names in alphabetical order, lowercase, with
total length at most 10⁵.

## Output

The least time for each name.

## Examples

### Example 1

Input:

```
5
a
aaa
aab
b
d
```

Output:

```
0 1 2 2 1
```

## Solution

A situation is a pair: the typed letters, which must begin the current
name, and the current name x. The typed letters are then the first d
letters of x, so the pair is (x, d), and there are Σ (|x| + 1) ≤ 2·10⁵
of them. In sorted order the names with a given beginning form a range,
the subtree of a trie node. "Down" and "up" move to the next or
previous name in that range, wrapping around, for one second. Erasing
goes to (x, d − 1) for one second. Typing letter c leads to the first
name of the child node, whatever x is. So every node gets a hub vertex:
each pair reaches the hub of its node for free, and the hub leads to the
first name of each child at the cost of the letter. Edge weights are 0
to 4, so Dijkstra runs with five buckets in a circle. The answer for x
is the smallest distance over its pairs. `O(n + L)` for total length
L.

In the example "d" is one "up" from "a", and "b" two; "aab" takes two
"down" presses from "a", and typing "a" first would not help.

Pitfalls:

- erasing keeps the current name, so a route may type letters, step
  through the short list, erase and step again;
- "up" from the first shown name wraps to the last one, which makes
  the last names cheap;
- typing a letter costs its place on the key, up to 4 for s and z,
  so stepping can beat typing;
- the edges of a typed letter do not depend on the current name, which
  the hubs exploit to stay linear.

The times match a search over (typed letters, current name) states on
1500 small random books, and an independent accepted implementation on
large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1882_shortest_paths.cpp](1882_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n + L) | AC | 0.031 s | 7060 KB |
| [1882_shortest_paths.go](1882_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n + L) | AC | 0.046 s | 20636 KB |
| [1882_shortest_paths.java](1882_shortest_paths.java) | Java 1.8 | shortest_paths | O(n + L) | AC | 0.203 s | 19012 KB |
| [1882_shortest_paths.py](1882_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n + L) | AC | 0.500 s | 35004 KB |
| [1882_shortest_paths.rs](1882_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n + L) | AC | 0.031 s | 16020 KB |
