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
start positions in that order. The length is on the first line, the
values on the second and the two positions on the third.

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

## Optimized solutions

`2000_games_optimized.java`. Java keeps the same optimal ownership regions. With different starts, each cell belongs to the nearer starting point and equal-distance cells go to the first player; sum the corresponding prefix or suffix around the midpoint. With equal starts, the first player takes that cell and the larger outside side. Store values in char[N], two bytes per cell, because every value is at most 10000. The total is at most 10^9, so int sums are exact. Primitive integer input and buffered raw output avoid generic long parsing and text conversion. Time O(N), auxiliary storage O(N); starts follow the values, so the array is intentionally retained. Teaching versions remain.

Exact-source Java 1.8 Accepted #11327442: 0.109 s / 748 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/88, memory 3/88. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11325024 was 0.125 s / 948 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2000_games_optimized.java`: 0.109 s / 748 KB; retained teaching base `2000_games.java`: 0.14 s / 1300 KB.

`2000_prefix_sums.rs`. Build u32 prefix sums while reading the values, then evaluate the same two-start/equal-start score formulas in O(1). The total≤10⁹ bounds every prefix; no value vector or repeated slice sums are needed. Overall O(n) time and O(n) space. This prefix-sum algorithm has its own filename and the original direct-sum version is retained.

Compared with `2000_games.rs`: time 0.046 s → 0.046 s; memory 2916 KB → 456 KB.

`2000_prefix_sums.py`. Keep the same optimal midpoint/equal-start game result, but read integers in 4096-byte chunks and build only prefix sums. The two starting positions appear after all values; once known, a prefix lookup or two-prefix subtraction gives each score, including the midpoint tie favoring the first player. Equal starts take that cell plus the larger outside side. There is no values array or full input-token list. Time remains O(n), storage O(n) Python prefix integers plus bounded input chunks; this is not constant-space streaming. Values and totals use exact integers. The distinct prefix_sums filename describes the changed representation; the simple games source and existing Java optimization remain. Own Accepted memory 6152 KB versus 11780 KB admits the version despite unchanged 0.125 second time.

Compared with `2000_games.py`: time 0.125 s → 0.125 s; memory 11780 KB → 6 152 KB.

The optimized C++ solution keeps the values in a global array of 100 000
`uint16_t` instead of a `vector` of 64-bit integers, since a value is at
most 10000, and sums them in `int`, since the total is at most
100000 · 10000 = 10⁹. The numbers are parsed by hand from a 4 KB buffer
refilled with `fread` and the scores are printed with `printf` instead
of `iostream`: {2000_games_optimized.cpp}.

The optimized Go solution keeps the values in a slice of `uint16`
instead of `int64`, since a value is at most 10000, and widens each one
to `int64` when adding; the numbers are parsed by hand from a `bufio`
reader instead of `fmt.Fscan`: {2000_games_optimized.go}.

### Measured gains

Each optimized version has Accepted and meets a ranking or resource-improvement
admission criterion. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2000_games_optimized.cpp`: time reduction +51.61%; memory reduction
  +77.45%; base: `2000_games.cpp`.

- `2000_games_optimized.go`: time reduction +50.00%; memory reduction
  +50.40%; base: `2000_games.go`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2000_prefix_sums.py`: time place 2/19, memory place 1/19 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2000_games.cpp](2000_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.031 s | 1224 KB | 11292433 |
| [2000_games.go](2000_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.062 s | 2484 KB | 11292434 |
| [2000_games.java](2000_games.java) | Java 1.8 | games | O(n) | AC | 0.140 s | 1300 KB | 11307192 |
| [2000_games.py](2000_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.125 s | 11780 KB | 11292435 |
| [2000_games.rs](2000_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.046 s | 2916 KB | 11292437 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2000_games_optimized.cpp](2000_games_optimized.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 276 KB | 11307194 |
| [2000_games_optimized.go](2000_games_optimized.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1232 KB | 11307195 |
| [2000_games_optimized.java](2000_games_optimized.java) \* | Java 1.8 | games | O(N) time; O(N) auxiliary space | AC | 0.109 s | 748 KB | 11327442 |
| [2000_prefix_sums.py](2000_prefix_sums.py) \* | Python 3.12 x64 | prefix_sums | O(n) | AC | 0.125 s | 6152 KB | 11325460 |
| [2000_prefix_sums.rs](2000_prefix_sums.rs) \* | Rust 1.75 x64 | prefix_sums | O(n) time; O(n) space | AC | 0.046 s | 456 KB | 11325507 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
