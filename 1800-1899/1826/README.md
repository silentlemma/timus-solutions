# 1826. Minefield

[Timus 1826](https://acm.timus.ru/problem.aspx?space=1&num=1826) · difficulty 309 · greedy

Original problem by Dmitry Teryaev, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A squad of n crosses a minefield with a single mine detector: two cross
together, then one brings the detector back, and so on. Each soldier
has a crossing time, and a pair moves at the speed of the slower one.
Find the least total time for the whole squad to cross.

## Input

n (2 ≤ n ≤ 100), then n crossing times, positive integers up to 600.

## Output

The least total time.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4
1
10
5
2
```

Output:

```
17
```

## Solution

This is the bridge-and-torch puzzle. Sort the times a ≤ b ≤ … ≤ y ≤ z.
While more than three soldiers wait, send the two slowest across in
one of two ways and keep the cheaper:

- the fastest escorts each of them: z + a + y + a = 2a + y + z;
- the two fastest cross, a returns, the two slowest cross together, b
  returns: b + a + z + b = a + 2b + z.

Either way the two fastest are back at the start and two fewer remain.
Three soldiers take a + b + c (a escorts both), two take the slower
time. An exchange argument shows that some optimal plan always moves
the two slowest this way. The algorithm takes `O(n log n)` time, but the
Python implementation takes `O(n^2)` because each `times[:-2]` copies the
remaining list. Peak space is `O(n)` in all five implementations.

In the example (1, 2, 5, 10) pairing costs 1 + 2·2 + 10 = 15 against
2 + 5 + 10 = 17 for escorting, and the last two take 2: 17.

Pitfalls:

- always escorting with the fastest is not optimal: 1, 2, 5, 10 would
  take 19;
- always pairing the slow ones is not optimal either when the second
  fastest is slow;
- the choice is made again in every round;
- Python list slicing copies elements: test 07 has n = 100 and copies
  98 + 96 + … + 2 = 2450 elements, so sorting does not dominate its runtime.

The answers agree with a Dijkstra search over all states for squads
of up to 7 and with an independent accepted implementation on random
squads.

## Optimized solutions

`1826_greedy_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1826_greedy.java`: time 0.109 s → 0.078 s; memory 1764 KB → 516 KB.

Go and Rust sort the crossing times in fixed-size arrays and remove the two slowest soldiers per step. With fastest times a, b and slowest remaining times y, z, add z + min(2a+y, a+2b). Finish with b for two soldiers or a+b+c for three. Both store input times in 16 bits. Go uses in-place heap sort; Rust accumulates the total in 32 bits. Both versions use fixed byte buffers for input and decimal output. Go accesses standard handles directly, and Rust uses the C runtime.

The accepted base implementations [1826_greedy.cpp](1826_greedy.cpp), [1826_greedy.java](1826_greedy.java), [1826_greedy.py](1826_greedy.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1826_greedy_optimized.java`: time place 1/28, memory place 5/28 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1826_greedy.cpp](1826_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 176 KB | 11325582 |
| [1826_greedy.go](1826_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1096 KB | 11290377 |
| [1826_greedy.java](1826_greedy.java) \* | Java 1.8 | greedy | O(n log n) | AC | 0.109 s | 1764 KB | 11290382 |
| [1826_greedy.py](1826_greedy.py) \* | Python 3.12 x64 | greedy | O(n^2) | AC | 0.078 s | 400 KB | 11325595 |
| [1826_greedy.rs](1826_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.015 s | 236 KB | 11325608 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1826_greedy_optimized.go](1826_greedy_optimized.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 284 KB | 11311235 |
| [1826_greedy_optimized.rs](1826_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 52 KB | 11311229 |
| [1826_greedy_optimized.java](1826_greedy_optimized.java) | Java 1.8 | greedy | O(n log n) | AC | 0.078 s | 516 KB | 11324789 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
