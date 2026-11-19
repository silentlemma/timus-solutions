# 2104. Folding a two-sided strip until it shows one colour

[Timus 2104](https://acm.timus.ru/problem.aspx?space=1&num=2104) · difficulty 375 · games

Original problem by Nikita Sivukhin, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 1 × n strip has colours A and B on its squares, on both sides. Alice
and Bob take turns, Alice first; a turn folds the strip in half (only
when its length is even), inwards or outwards. If after a turn the strip
shows a single colour on both sides, A means Alice wins and B means Bob
wins, whoever made the fold. If the player to move cannot fold and
nobody has won, it is a draw. Who wins with best play? The limits are
2 seconds and 64 MB.

## Input

n ≤ 5·10⁵, then the two sides as strings of A and B.

## Output

`Alice`, `Bob` or `Draw`.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
4
BBAA
BABB
```

Output:

```
Bob
```

### Example 2

Input:

```
3
AAA
BBB
```

Output:

```
Draw
```

### Example 3

Input:

```
2
AA
BB
```

Output:

```
Alice
```

## Solution

A fold puts the right half on top of or below the left half. One way the
outside faces are the left half of the top side and the reversed right
half of the top side; the other way they are the reversed right half of
the bottom side and the left half of the bottom side. The faces that end
up inside are never seen again. So every position has at most two moves,
each halving the length, and the game has at most log₂ n ≈ 19 levels.

A plain minimax over this tree is enough: after each fold check whether
the new strip shows one colour; otherwise recurse with the other player
to move, and an odd length is a draw. Each player takes the result that
is best for their own side, stopping as soon as a move wins. Level k has
at most 2ᵏ strips of length n / 2ᵏ, so the work is O(n log n).

In the first example both folds of Alice leave strips that Bob folds
into B/B, so Bob wins.

## Optimized solutions

`2104_games_optimized.java`. Keep the same fold minimax and outcomes Alice/Draw/Bob, but represent each exposed face by an original-side ID, start, direction±1 and length. Two original-side prefix-count arrays answer whether both newly exposed faces are allA or allB in O(1), without substring, reversal or repeated scans. Each recursive branch halves the length, so the search has O(n) nodes in the worst case and O(log n) stack depth; prefix construction also takes O(n). Total storage O(n). An odd current length still draws before a new fold; uniform colors win only after a fold, preserving the original game semantics and early minimax cutoffs.

Compared with `2104_games.java`: time 0.125 s → 0.125 s; memory 14 904 KB → 5 032 KB.

The C++, Go and Rust variants represent a face by a slice of the original strip and a reversal flag. A fold takes two subslices and flips the orientation of one. The exposed halves together contain exactly the cells of the chosen face, so a single scan of that face detects a uniform color. The minimax still takes O(n log n) time and uses only O(log n) stack space beyond the input.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.015 s for the base and uses 1 152 KB versus 2132 KB.

The accepted base implementations [2104_games.java](2104_games.java), [2104_games.py](2104_games.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`2104_games_optimized.java`: time place 5/27, memory place 1/27 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2104_games.cpp](2104_games.cpp) | G++ 13.2 x64 | games | O(n log n) | AC | 0.046 s | 3812 KB | 11325592 |
| [2104_games.go](2104_games.go) | Go 1.14 x64 | games | O(n log n) | AC | 0.046 s | 8076 KB | 11294757 |
| [2104_games.java](2104_games.java) \* | Java 1.8 | games | O(n log n) | AC | 0.125 s | 14904 KB | 11325571 |
| [2104_games.py](2104_games.py) \* | Python 3.12 x64 | games | O(n log n) | AC | 0.265 s | 3968 KB | 11294760 |
| [2104_games.rs](2104_games.rs) | Rust 1.75 x64 | games | O(n log n) | AC | 0.015 s | 2132 KB | 11294764 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2104_games_optimized.cpp](2104_games_optimized.cpp) | G++ 13.2 x64 | games | O(n log n) | AC | 0.015 s | 1424 KB | 11310425 |
| [2104_games_optimized.go](2104_games_optimized.go) \* | Go 1.14 x64 | games | O(n log n) | AC | 0.015 s | 1896 KB | 11310428 |
| [2104_games_optimized.rs](2104_games_optimized.rs) \* | Rust 1.75 x64 | games | O(n log n) | AC | 0.046 s | 1152 KB | 11310427 |
| [2104_games_optimized.java](2104_games_optimized.java) \* | Java 1.8 | games | O(n) | AC | 0.125 s | 5032 KB | 11325036 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
