# 1678. Space Poker 3

[Timus 1678](https://acm.timus.ru/problem.aspx?space=1&num=1678) · difficulty 4775 · combinatorics

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N players each get M private cards, and K common cards are dealt to the
table; a hand is a player's private cards plus the common ones. Cards
have only a rank (13 ranks, 2 to A), and every card from the infinite
deck takes each rank with probability 1/13. A combination
(v1, …, vL) asks for v1 cards of one rank, v2 of another, and so on,
with L different ranks; a hand holds it if it has at least that many.
The C combinations are listed from cheapest to most valuable, and the
round is won by the player whose hand holds the most valuable
combination of the table; if several players share it, it is a draw.

Knowing the first player's private cards and the common cards already
shown, find the chance that this player wins alone.

## Input

N, M and K (2 ≤ N, M ≤ 10; 1 ≤ K ≤ 5); the first player's M private
cards; the shown common cards, at most K of them (the line may be
empty); C (1 ≤ C ≤ 100) and the combinations from cheapest to most
valuable, each as L v1 … vL, with every vi positive and their sum at
most M + K.

## Output

The probability, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
2 5 2
23456

1
1 2
```

Output:

```
0.0883526857
```

### Example 2

Input:

```
2 5 2
23456
78
2
7 1 1 1 1 1 1 1
1 4
```

Output:

```
0.8407915043
```

## Solution

Only the number of cards of each rank matters. A hand holds
(v1, …, vL) exactly when, with both lists sorted in decreasing order,
the i-th largest rank count is at least the i-th largest vi: the
largest demand may always take the most frequent rank. So the best
combination of a hand depends only on its sorted counts, which a cache
remembers.

Enumerate the hidden common cards as counts over the 13 ranks; h hidden
cards give at most C(h + 12, 12) ≤ 6188 patterns, each with the
multinomial probability h! / (Π xᵢ! · 13ʰ). For each pattern take the
first player's best combination c; with no combination at all the
player cannot win. Given the common cards, the rivals' private cards
are independent, so the pattern adds its probability times q^(N − 1),
where q is the chance that one rival's best combination is cheaper than
c (holding nothing counts as cheapest).

That chance depends only on the sorted common counts, so there are at
most p(K) ≤ 7 different tables. To build one, group the ranks by their
common count: the g ranks of a group with common count v are
interchangeable, so a group receives a partition of its share s of the
rival's M cards into at most g parts, placed in
g! / ((g − parts)! · Π mult!) ways (mult counts equal parts), with
weight 1 / Π x!. The state after each group is the sorted list of the
rival's rank counts so far and the number of cards used; at the end,
each complete state times M! / 13ᴹ goes to its best combination, and
prefix sums give the chance of every "cheaper than c".

`O(C(K + 12, 12) · 13 + p(K) · S)`, where S is the work of one table,
a few thousand count shapes of at most M + K cards; everything runs in
well under a second.

Pitfalls:

- the third line may be empty, so read the input line by line;
- a tie is not a win: a rival must be strictly cheaper;
- a combination asks for at least vi cards, so "KQKQKQ" holds (2, 3).

The answers match a direct enumeration of every deal for tiny sizes and
an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1678_combinatorics.cpp](1678_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.015 s | 624 KB |
| [1678_combinatorics.go](1678_combinatorics.go) | Go 1.14 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.031 s | 5856 KB |
| [1678_combinatorics.java](1678_combinatorics.java) | Java 1.8 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.250 s | 7596 KB |
| [1678_combinatorics.py](1678_combinatorics.py) | Python 3.12 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.171 s | 1260 KB |
| [1678_combinatorics.rs](1678_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.046 s | 636 KB |
