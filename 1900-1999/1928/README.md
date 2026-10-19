# 1928. Alternating Grants with a Terminal Gift

[Timus 1928](https://acm.timus.ru/problem.aspx?space=1&num=1928) · difficulty 769 · games, dp

Original problem: folklore, prepared by Maria Zyryanova; from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players alternate requesting an integer amount from 1 to k, with the
first player starting and a shared initial budget n. If the budget is zero,
play ends before another request. An affordable request is paid from the
budget. Otherwise the current player receives only a separate gift m,
the budget is not spent, and the game ends.
Each player first maximizes their own total and, among equally good totals,
minimizes the other player's total. Find the final amounts under optimal play.
Limits: 1 second, 64 MB.

## Input

One line n m k: 0≤n≤10000, 0≤m≤1000, 1≤k≤100.

## Output

Two integers: the first player's total, then the second player's total.

## Checking

Compare the two integer tokens exactly.

## Examples

```
12 30 10
```

```
31 10
```

## Solution

For each remaining budget b, store F[b], the future earnings of the player
whose turn it is, and G[b], the future earnings of the other player.
Amounts already received are constants in all choices and do not affect
the preferences. For b=0 both values are zero: there is no next move.

For an affordable request x, 1≤x≤min(b,k), the next state has budget b−x
and swaps player roles. The candidate pair is (x+G[b−x], F[b−x]).
An unaffordable request exists exactly when 0<b<k; every such request
has the same terminal candidate (m,0). It does not pay x or the leftover b.
Choose the candidate with the largest first component, breaking ties by
the smallest second component. Fill b=1..n and print F[n],G[n].

Inductively, all smaller states already describe optimal future play.
Every legal move either ends with the gift or reaches one of those smaller
states with reversed roles. The candidate calculation therefore gives its
exact payoff pair. Selecting by the stated preferences is the optimal
decision at this state. The base and induction prove the whole algorithm.

O(nk) time and O(n) space: two arrays and at most 1,000,000 affordable
candidates at maximum bounds. No recursive game-tree search is submitted.

Do not confuse maximizing the difference with maximizing one's own money
first. The secondary preference matters: n=5,m=2,k=3 yields (3,2), and
ignoring ties can give a different outcome. A zero initial budget gives
(0,0), even if the gift is large. At b=k no unaffordable request is legal.
An unaffordable request pays only m and ends play immediately; do not
subtract a request or give away the remaining budget in that branch.
Swap both stored roles after every affordable request.

## Language notes

Every payout is nonnegative and the sum of both totals is at most n+m≤11000,
so signed 32-bit arithmetic suffices. Go uses int, Rust separates usize
indices from i32 payoffs, C++ and Java use int; Python uses ordinary lists.
An internal best value −1 marks absence of a candidate and is never printed.
CPython is sufficient for the bounded dynamic program.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1928_games_dp.cpp](1928_games_dp.cpp) | G++ 13.2 x64 | games, dp | O(nk) | AC | 0.015 s | 460 KB |
| [1928_games_dp.go](1928_games_dp.go) | Go 1.14 x64 | games, dp | O(nk) | AC | 0.031 s | 1240 KB |
| [1928_games_dp.java](1928_games_dp.java) | Java 1.8 | games, dp | O(nk) | AC | 0.125 s | 1672 KB |
| [1928_games_dp.py](1928_games_dp.py) | Python 3.12 x64 | games, dp | O(nk) | AC | 0.296 s | 960 KB |
| [1928_games_dp.rs](1928_games_dp.rs) | Rust 1.75 x64 | games, dp | O(nk) | AC | 0.015 s | 292 KB |
