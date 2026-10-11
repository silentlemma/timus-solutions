# 1276. Train

[Timus 1276](https://acm.timus.ru/problem.aspx?space=1&num=1276) · difficulty 731 · combinatorics

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N ≤ 40 carriages, each with a coupling of kind A or B at its
left and right end (AA, AB, BA or BB), and a locomotive with such
couplings too. Nothing can be turned around. A train of K carriages
must have matching couplings between neighbours, and its two ends must
fit the locomotive: the train starts with the locomotive's right
coupling and ends with its left one, so the locomotive can be put at
either end. Count the different trains, compared as strings of
couplings; print NO if there is none.

Time limit: 1 second. Memory limit: 4 MB.

## Input

N and K, the locomotive, then the N carriages.

## Output

`NO`, or `YES` and the number of trains.

## Examples

### Example 1

Input:

```
4 4
AB
AA
AB
BA
BA
```

Output:

```
YES
2
```

### Example 2

Input:

```
4 4
BA
AA
AB
BA
BA
```

Output:

```
NO
```

## Solution

Read a train as a walk between two states, A and B. An AA carriage stays
in A, a BB carriage in B, an AB carriage switches from A to B and a BA
carriage back. So the switching carriages alternate, starting with the
one that leaves the starting state. Their number s fixes how many AB
and BA carriages are used and the final state. It also splits the walk
into s + 1 runs, alternately in A and B.

Carriages of one kind are identical, so a train is fixed by how many
AA carriages go into each A-run and how many BB into each B-run. For
every s whose final state is right and every split of the remaining
K − s carriages into a AA and b BB within stock, add

```text
C(a + rA − 1, rA − 1) · C(b + rB − 1, rB − 1)
```

where rA and rB are the numbers of A-runs and B-runs (with no runs of a
state, only zero carriages of its kind fit). Every binomial has at most
41 on top, and the total stays far below 2⁶³. `O(N + K²)`.

Pitfalls:

- the train's first coupling must fit the locomotive's right one and
  its last coupling the locomotive's left one; reversing these gives
  `YES` in the second example;
- carriages of one kind are interchangeable: forty AA carriages make a
  single train (test 05);
- a kind that cannot follow itself, like AB, gives no train longer
  than one carriage (test 08).

The counts were compared with listing every distinct train on 300
random cases of up to seven carriages.

## Language notes

- All sum over switches; Python uses `math.comb`, the others a
  binomial table.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1276_combinatorics.cpp](1276_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N + K²) | AC | 0.015 s | 164 KB |
| [1276_combinatorics.go](1276_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N + K²) | AC | 0.015 s | 1120 KB |
| [1276_combinatorics.java](1276_combinatorics.java) | Java 1.8 | combinatorics | O(N + K²) | AC | 0.125 s | 504 KB |
| [1276_combinatorics.py](1276_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N + K²) | AC | 0.109 s | 624 KB |
| [1276_combinatorics.rs](1276_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N + K²) | AC | 0.015 s | 268 KB |
