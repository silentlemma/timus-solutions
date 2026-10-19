# 1859. Last Season of Team.GOV

[Timus 1859](https://acm.timus.ru/problem.aspx?space=1&num=1859) · difficulty 3827 · greedy

Original problem by Mikhail Rubinchik (idea by Dmitry Kuznetsov), from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A delegation of 6n people travels in n blocks of a sleeping car; every
block has four compartment seats and two side seats. Each person wants
one kind of seat, and every person wants to travel in the same block as
all of their friends. Split the delegation into blocks so that nobody is
let down; a solution is known to exist.

## Input

n (1 ≤ n ≤ 1000), a string of 6n bits (1 for a compartment seat, 0 for
a side seat), then m (0 ≤ m ≤ 15n) and the m pairs of friends.

## Output

n lines with the six people of each block. Any valid split is accepted.

## Examples

### Example 1

Input:

```
2
001111001111
2
1 2
7 8
```

Output:

```
1 2 3 4 5 6
7 8 9 10 11 12
```

## Solution

Friendship joins people into groups that must share a block, and a group
matters only through (a, b): a people who want compartment seats and b
who want side seats. With only two side seats a block holds either one
group with b = 2, or two groups with b = 1 (call them halves), and the
compartment seats left over are filled by groups with b = 0, the
fillers.

Filling is a one-dimensional packing of fillers of sizes 1 … 4 into the
free compartment seats of the blocks. Fours need a block with 4 free
seats. A three goes to a block with 3 free first: swapping it with the
contents of a block with 4 free never makes things worse. Twos then
fit into what is left (a block with 2 or 3 free takes one, a block with
4 free takes two), and ones fill the rest. So for given numbers c₄, c₃,
c₂ of blocks with 4, 3 and 2 free seats the fillers fit exactly when
three inequalities hold.

What is left is how to pair the halves: a pair (a₁, a₂) leaves
4 − a₁ − a₂ free seats. Merging the free seats of two blocks into one
never hurts, which settles most choices. A three paired with a zero
next to a one paired elsewhere can be swapped into a pair (3, 1) and a
pair with a zero, so threes take as many ones as they can. Two pairs
(0, 2) become (2, 2) and (0, 0), so at most one (0, 2) remains. The
remaining choice is the number of pairs (1, 2) and of pairs (1, 1). For
each number of pairs (1, 2) the inequalities bound the pairs (1, 1) to
an interval. In that interval the room left for twos first grows and
then shrinks, so only the turning point and its neighbours need a
check. There are at most 2000 halves, so the search is linear, and the
blocks are then built and filled in the same order as the check
assumed. `O(n + m)`.

In the example the groups {1, 2} and {7, 8} each want both side seats
of a block, and every other person is a filler wanting a compartment
seat; any four of them complete each block.

Pitfalls:

- a three must not be pushed into a block with 4 free seats while a
  block with exactly 3 is still open;
- pairing halves greedily by size fails: (1, 1) with (0, 0) and two
  pairs (1, 0) leave different free seats, and which one is needed
  depends on the fillers;
- the answer is not unique, so the output is checked by a checker.

The splits pass a checker on 10 000 random delegations of up to 36
people, half of them built from groups with one side seat, and on the
largest tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1859_greedy.cpp](1859_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.031 s | 692 KB |
| [1859_greedy.go](1859_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.062 s | 1908 KB |
| [1859_greedy.java](1859_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.125 s | 3364 KB |
| [1859_greedy.py](1859_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.109 s | 2564 KB |
| [1859_greedy.rs](1859_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.046 s | 812 KB |
