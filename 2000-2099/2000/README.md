# 2000. Grand Theft Array V

[Timus 2000](https://acm.timus.ru/problem.aspx?space=1&num=2000) · difficulty 160 · games

Original problem by Ilya Kuchumov. (Prepared by Kirill Devyatkin), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players start at specified cells of a line of nonnegative values.
Player one acts first, then turns alternate. A turn collects the current
cell's value, replaces it by zero, and moves one cell left or right
without leaving the array. Sharing a cell is allowed. Play ends when all
values are zero. Each player maximizes their own final score, breaking a
tie by minimizing the opponent's score. Find both optimal scores.

Bounds: `10≤n≤100000`, values from 0 to 10000, and one-based start
positions `p,q` in 1..n. Time 0.5 seconds; memory 64 MB.

## Input

The length `n`, then `n` values, then the first and second player's
start positions in that order.

## Output

Two integers: player one's score and player two's score.

## Checking

Outputs are compared token by token.

## Examples

```
10
1 2 3 4 5 6 7 8 9 0
4 8
```

```
21 24
```

The starts are 4 and 8. Their midpoint is cell 6, whose equal-distance
race belongs to player one. Thus player one receives cells 1–6, totaling
21; cells 7–10 total 24 for player two.

## Solution

At completion the total score is the sum of the original array, so
maximizing one's own score already minimizes the other's. Nonnegative
values make it possible to guarantee the weight of a whole region
without wanting to avoid any cell.

### Different starts

The earliest global turn on which a player could collect cell `i` is

`T1(i)=2·|i−p|+1`, `T2(i)=2·|i−q|+2`.

Equal distances favor player one. These comparisons divide the line into
two contiguous territories. If `p<q`, let `c=floor((p+q)/2)`: player
one's score is the sum of cells 1..c. If `p>q`, let `c=ceil((p+q)/2)`:
player one receives c..n. Player two receives the complement.

The arrival comparison alone is not a proof, since a player cannot
travel toward both endpoints at once. To guarantee a territory, first
walk toward the opponent as far as the territory's boundary cell.
Collect that boundary before the opponent could collect it, then
immediately reverse and walk toward the outer endpoint. To enter this
outer region the opponent must pass through that boundary. The opponent
may share cells and can follow, but now has later collection priority
and the same speed, so cannot overtake the outward walk. Every cell of
the territory is therefore collected by its owner, regardless of the
opponent's moves.

Both players have such a strategy. Each guarantees the stated territory
sum, and the two sums add to the total. Consequently neither player can
force more against the other's guard strategy, proving both optimal
scores. This is a temporal collection argument, not a rule that occupied
cells block movement.

### The same start

Player one takes the starting value. Let `L` and `R` be the sums
strictly to its left and right. Player one can choose the heavier side
and walk straight to its endpoint, guaranteeing `a[p]+max(L,R)`: a
follower stays behind. Player two can observe the first move, choose the
opposite side and guard it. If player one reverses, the second player's
moving front still has priority on that side. Thus player one can get no
more than the starting value plus the side initially chosen, which is at
most `a[p]+max(L,R)`. At an endpoint the opposite side is empty and
player two follows, obtaining zero.

The answer is therefore `a[p]+max(L,R)` for player one and `min(L,R)`
for player two. If all values are initially zero, both answers are zero
immediately.

### Complexity and verification horizon

Summation takes `O(n)` time. The input array uses `O(n)` memory; only
`O(1)` additional arithmetic storage is needed. The maximum total is
`10^9`; native programs use 64-bit scores.

The guard strategies collect their entire guaranteed regions within `2n`
personal turns, so `4n` alternating turns suffice to bound the optimal
score from both sides. In a truncated literal minimax, player one's
guard gives the same lower bound and player two's guard gives the
complementary upper bound; uncollected weight is nonnegative. Hence this
finite horizon already gives the full-game value, so a minimax over
`4n` turns checks small cases exactly.

Collect before moving. For different starts, the midpoint tie belongs to
the first player in either left/right order. Identical starts require
the heavier-side formula, not a midpoint split. A zero-valued cell still
takes a move to cross; sharing a cell does not stop either player. Keep
the original player labels when the first start is to the right.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2000_games.cpp](2000_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.031 s | 1224 KB |
| [2000_games.go](2000_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.062 s | 2484 KB |
| [2000_games.java](2000_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 1252 KB |
| [2000_games.py](2000_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.125 s | 11780 KB |
| [2000_games.rs](2000_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.046 s | 2916 KB |
