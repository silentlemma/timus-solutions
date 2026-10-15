# 1700. Awakening

[Timus 1700](https://acm.timus.ru/problem.aspx?space=1&num=1700) · difficulty 482 · implementation

Original problem by Pavel Atnashev, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every object has a set of associations. For each of several groups of
objects, print the associations common to all of them in alphabetical
order, or "No solution." when there are none.

## Input

n (2 ≤ n ≤ 1000) lines "name: association association …", then m
(1 ≤ m ≤ 1000) lines, each a group of at least two object names. Words
are lowercase Latin, and lines are at most 250 characters long.

## Output

One line per group.

## Examples

### Example 1

Input:

```
6
whale: big black water animal
penguin: black white ice beak
piano: keyboard black white wire
jackboot: leather heel black
train: rail wheel black
rose: red green thorn
3
whale penguin piano jackboot train
penguin piano
jackboot rose
```

Output:

```
black
black white
No solution.
```

## Solution

Store each object's associations as a set, keyed by its name. For a
group, intersect the sets of its members and print the result sorted,
or "No solution." if it is empty. Every line is short; a group uses
`O(L²)` set lookups. `O((n + m · L) · L log(n + L))` for lines of
length L.

Pitfalls:

- an association may be listed twice for one object, but must be
  printed once (test 02);
- a group may name the same object twice (test 03);
- an object may have no associations at all, so its line ends right
  after the colon.

The answers match an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.359 s | 7788 KB |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.765 s | 8908 KB |
| [1700_implementation.java](1700_implementation.java) | Java 1.8 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.437 s | 12376 KB |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.390 s | 13524 KB |
| [1700_implementation.rs](1700_implementation.rs) | Rust 1.75 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.593 s | 3584 KB |
