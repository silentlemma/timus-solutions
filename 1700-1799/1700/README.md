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

## Optimized solutions

C++/Go intern association spellings into shared integer IDs and keep each object’s IDs sorted and deduplicated. Start a query with a copy of its shortest list, intersect subsequent lists by two advancing indices, and sort surviving spellings only for output. No stored object list is modified by queries; repeated members and duplicate associations do not change an intersection. Python instead streams definitions into frozensets of interned strings and intersects a copy of the smallest set. All three stream answers. Let T be input characters, A the maximum association count, K group size and W word length; integer-list intersections cost O(KA), final spelling sorting O(A log A·W). Hash operations have their usual expected bounds. Storage shares distinct spellings instead of repeating them per object and retains neither all input nor all output. Ordinary set implementations remain; Java/Rust reuse admitted bases.

The accepted Go 1.14 x64 run takes 0.062 s versus 0.765 s for the base and uses 10 348 KB versus 8908 KB.

In the earlier comparison snapshot, the base implementations [1700_implementation.java](1700_implementation.java), [1700_implementation.rs](1700_implementation.rs) met the top-15% or top-ten admission rule on both metrics. Their measured results are kept in the Simple table.

Store each association set in a sorted array and intersect the arrays with two pointers. Stream the query answers. Accepted submission 11324225 took 0.250 s and used 8 536 KB. The simple version took 0.437 s and used 12376 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.359 s | 7788 KB | 11289069 |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.765 s | 8908 KB | 11289071 |
| [1700_implementation.java](1700_implementation.java) \* | Java 1.8 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.437 s | 12376 KB | 11289075 |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.390 s | 13524 KB | 11289073 |
| [1700_implementation.rs](1700_implementation.rs) \* | Rust 1.75 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.593 s | 3584 KB | 11289079 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1700_hashing_sorting.cpp](1700_hashing_sorting.cpp) | G++ 13.2 x64 | hashing, sorting | O(T + nA log A + m(KA + A log A·W)) expected | AC | 0.046 s | 6148 KB | 11315323 |
| [1700_hashing_sorting.go](1700_hashing_sorting.go) \* | Go 1.14 x64 | hashing, sorting | O(T + nA log A + m(KA + A log A·W)) expected | AC | 0.062 s | 10348 KB | 11315329 |
| [1700_implementation_optimized.py](1700_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(T + m(KA + A log A·W)) expected | AC | 0.343 s | 8920 KB | 11315330 |
| [1700_sorting.java](1700_sorting.java) | Java 1.8 | sorting | O((n + m · L) · L log(n + L)) | AC | 0.250 s | 8 536 KB | 11324225 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
