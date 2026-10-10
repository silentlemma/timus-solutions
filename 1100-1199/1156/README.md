# 1156. Splitting 2N problems into two rounds with similar problems apart

[Timus 1156](https://acm.timus.ru/problem.aspx?space=1&num=1156) · difficulty 327 · graphs

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`2N` problems, `N ≤ 50`, must be split into two rounds of `N` problems
each. `M ≤ 100` pairs of problems are similar and must not be in the same
round. Print the two rounds, or `IMPOSSIBLE`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N` and `M`, then `M` pairs of similar problems.

## Output

Two lines with the `N` problems of each round, or `IMPOSSIBLE`.

## Checking

Any valid split is accepted. The checker verifies that the two lines hold
`N` problems each and together all problems from 1 to `2N`, that no
similar pair shares a round, and that `IMPOSSIBLE` is printed only when no
split exists.

## Examples

### Example 1

Input:

```
2 3
1 3
2 1
4 3
```

Output:

```
1 4
2 3
```

## Solution

Join similar problems by edges. Within a connected component, the round
of one problem decides the rounds of all the others: neighbours alternate.
So every component must be two-coloured, and an odd cycle makes the
split impossible. A component with colour classes of sizes `a` and `b`
then gives either `a` or `b` problems to the first round, and problems
without any similar partner are components of size `(1, 0)`.

It remains to pick, for every component, which class goes to the first
round so that the first round has exactly `N` problems. This is a
subset-sum over the components: `reach[k]` holds the sizes the first `k`
components can give, and a walk back from `N` recovers the choice. There
are at most `2N = 100` components and sizes up to `N`, so the table is
tiny.

Pitfalls:

- colouring alone is not enough: the class sizes must also add up to `N`;
- a problem similar to itself makes the split impossible;
- a pair can be given twice;
- the rounds may be printed in any order of problems; here they are
  increasing.

The answers were checked by the checker on every test, and the
feasibility was compared with trying every choice of `N` problems on 200
random inputs with up to 14 problems.

## Language notes

- All languages colour by depth-first search with an explicit stack and
  fill the same subset-sum table; Python keeps each row as a set.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1156_graphs.cpp](1156_graphs.cpp) | G++ 13.2 x64 | graphs | O(N·(N + M)) | AC | 0.001 s | 224 KB |
| [1156_graphs.go](1156_graphs.go) | Go 1.14 x64 | graphs | O(N·(N + M)) | AC | 0.015 s | 1136 KB |
| [1156_graphs.java](1156_graphs.java) | Java 1.8 | graphs | O(N·(N + M)) | AC | 0.093 s | 616 KB |
| [1156_graphs.py](1156_graphs.py) | Python 3.12 x64 | graphs | O(N·(N + M)) | AC | 0.078 s | 892 KB |
| [1156_graphs.rs](1156_graphs.rs) | Rust 1.75 x64 | graphs | O(N·(N + M)) | AC | 0.015 s | 244 KB |
