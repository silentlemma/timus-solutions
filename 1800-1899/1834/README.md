# 1834. Tennis Racket

[Timus 1834](https://acm.timus.ru/problem.aspx?space=1&num=1834) · difficulty 4432 · constructive

Original problem by Daniil Aizenshtein, from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A train of n cars is sorted in a racket-shaped siding. In one pass the
cars are uncoupled from the tail one by one, the first goes into the
siding and each next one is attached to the head or to the tail of the
train forming there; then the new train leaves head first. Find the
fewest passes that put the cars in the order 1, …, n, and the order
after each pass.

## Input

n (2 ≤ n ≤ 10000), then the cars from head to tail, a permutation of
1, …, n.

## Output

The least number of passes k, then k lines with the order after each
pass. Any optimal sequence is accepted.

## Examples

### Example 1

Input:

```
6
2 5 3 1 6 4
```

Output:

```
3
5 1 6 4 3 2
1 2 3 4 6 5
1 2 3 4 5 6
```

## Solution

Cars attached at the head come out in their old order before the
first car brought in, and cars attached at the tail come out after it
in reverse. So one pass picks any set of cars, keeps them in order and
appends the rest reversed.

Over k passes every car collects a k-bit code of its choices. Sorting
by the last pass first and unfolding, the cars end up ordered by their
codes in reflected Gray order, and cars sharing a code keep their
mutual order, reversed once for every one in the code. The parity of
those ones equals the parity of the code's Gray rank. So the sorted
train is cut into at most 2ᵏ runs of consecutive values in rank order,
and a run with an even rank must already rise in the original
positions, a run with an odd rank must fall.

Cut the values greedily into the longest alternating runs, once
starting with a rising run and once with a falling one. Giving ranks
0, 1, … to the first cutting needs 2ᵏ ≥ R runs; giving ranks 1, 2, …
to the second, leaving rank 0 empty, needs 2ᵏ ≥ F + 1. Empty ranks in
the middle never help, since a single car is both rising and falling.
The answer is the smaller k, and pass j moves exactly the runs whose
Gray code has bit j set. `O(n log n)` including the output.

In the example the cutting that starts rising is 1 | 2 | 3–4 | 5 | 6,
five runs, and the one that starts falling is 1–2 | 3–4 | 5 | 6, four
runs that with the empty rank 0 also take five ranks: three passes.

Pitfalls:

- the first car brought in is not special: it simply ends between the
  kept cars and the reversed ones;
- a train that starts falling may need one pass less with an empty
  rank 0 than with its rising cutting, as for a reversed train;
- a sorted train needs no passes and prints just 0.

The pass counts agree with a breadth-first search over all
permutations of up to 7 cars, and every printed sequence was checked
pass by pass for all permutations of 4 to 6 cars and for the large
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1834_constructive.cpp](1834_constructive.cpp) | G++ 13.2 x64 | constructive | O(n log n) | AC | 0.031 s | 1168 KB |
| [1834_constructive.go](1834_constructive.go) | Go 1.14 x64 | constructive | O(n log n) | AC | 0.031 s | 5308 KB |
| [1834_constructive.java](1834_constructive.java) | Java 1.8 | constructive | O(n log n) | AC | 0.109 s | 5944 KB |
| [1834_constructive.py](1834_constructive.py) | Python 3.12 x64 | constructive | O(n log n) | AC | 0.140 s | 7600 KB |
| [1834_constructive.rs](1834_constructive.rs) | Rust 1.75 x64 | constructive | O(n log n) | AC | 0.031 s | 2552 KB |
