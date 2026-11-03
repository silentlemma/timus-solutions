# 1244. Which cards are missing from a deck, by weight

[Timus 1244](https://acm.timus.ru/problem.aspx?space=1&num=1244) · difficulty 254 · dp

Original problem by Alexander Petrov, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A full deck has `N` indexed cards, `2 ≤ N ≤ 100`, with integer weights
`1 ≤ w_i ≤ 1000` milligrams. Let `T` be their total. The remaining cards
weigh an integer `W`, `0 < W < T`. Determine which indices are missing.
Print them in increasing order when the set is unique, `-1` for several
possible sets, and `0` when no set is possible. Equal weights still
belong to different cards. Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

W, then N, then the N card weights.

## Output

The missing cards, -1 or 0.

## Checking

Integers are compared as whitespace-separated tokens. A unique answer lists the missing indices in increasing order; otherwise the output is the single token `0` or `-1`.

## Examples

### Example 1

Input:

```
270
4
100
110
170
200
```

Output:

```
2 4
```

### Example 2

Input:

```
270
4
100
110
160
170
```

Output:

```
-1
```

### Example 3

Input:

```
270
4
100
120
160
180
```

Output:

```
0
```

## Solution

The cards left in the deck form a set of total weight W, and the missing
ones are the rest. So count the sets of cards that weigh W, but only up
to 2, since that is all that matters: `ways[i][s]` is the number of sets
of the first i cards weighing s, capped at 2, and
`ways[i][s] = min(2, ways[i−1][s] + ways[i−1][s − w_i])`. Then
`ways[N][W]` is 0, 2 (print -1) or exactly 1.

For the unique set, go back from the last card with s = W: card i is
missing exactly when the first i − 1 cards already make s on their own,
`ways[i−1][s] = 1`; otherwise it is in the deck and s drops by its
weight. Uniqueness means only one of the two can hold. `O(N·W)` with
W < 100 000.

Pitfalls:

- equal cards are different cards: with two cards of weight 1 and W = 1
  either one may be missing, so the answer is -1 (test 04);
- several cards can be missing, up to all but one (test 08).

The answers were compared with checking every subset on 1500 random small
decks.

## Optimized solutions

Complementing subsets gives a bijection between the remaining cards
of weight `W` and the missing cards of weight `T−W`. Count subsets for
`S = min(W,T−W)`, then complement the selected indices when necessary.
This preserves impossibility, uniqueness and ambiguity, and `S ≤ 50000`.

The four native versions update one capped-count row in descending sum
order. When a sum is reached for the first time, save the index of its
last card and never overwrite that predecessor. Its previous sum was
reachable before this card: descending updates and positive weights make
the saved card indices strictly decrease along a witness, so no card is
reused. For a unique final subset this witness is the required subset.
Counts need only `0,1,2`; predecessor indices are at most 100. Time is
`O(N·S)` and storage `O(S+N)`.

Python keeps a reachability bitset for each prefix, while only the current
bitset of sums having at least two representations is retained. For a
card, propagate old multiplicities both with and without it, and mark
the overlap of old reachability and shifted reachability as ambiguous.
Reconstruct a unique answer from the reachability prefixes. If ambiguity
at `S` is discovered early, excluding later cards preserves both witnesses,
so all versions may immediately print `-1`.

Let `C` be the largest card weight, `w` the number of bits per big-integer
limb, `B = ceil((S+C+1)/w)` and `B_W = ceil((W+C+1)/w)`. A conservative
word bound for optimized Python is `O(N·B)` time and space; the simple
Python version uses the corresponding `B_W` prefix bitsets. The `C` term
accounts for a shifted temporary before masking. The simple sources are
all retained unchanged.

Measured memory reductions against the unchanged Accepted simple sources: C++ 98.1%, Go 90.3%, Java 95.6%, Python 80.2%, Rust 97.7%. All five qualify by memory. A one-tick time difference is not treated as reliable acceleration. Ranking snapshot: 2 November 2026; starred rows still have room for optimization.

## Language notes

The simple C++/Go/Java/Rust files retain the full prefix count table; simple Python retains reachability and multiplicity bitsets per prefix. The optimized native files retain one count row and first-reach predecessors; optimized Python retains reachability prefixes and one multiplicity bitset. Python passed 40,770 input cases, using independent indexed-subset enumeration for small/random decks and exact large cases. Each of the five actual programs also passed 72 selected oracle inputs through Docker.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1244_dp.cpp](1244_dp.cpp) | G++ 13.2 x64 | dp | O(N W) | AC | 0.031 s | 9472 KB | 11283911 |
| [1244_dp.go](1244_dp.go) | Go 1.14 x64 | dp | O(N W) | AC | 0.031 s | 11676 KB | 11283913 |
| [1244_dp.java](1244_dp.java) | Java 1.8 | dp | O(N W) | AC | 0.109 s | 12768 KB | 11283918 |
| [1244_dp.py](1244_dp.py) | Python 3.12 x64 | dp | O(N B_W) | AC | 0.093 s | 2848 KB | 11283915 |
| [1244_dp.rs](1244_dp.rs) | Rust 1.75 x64 | dp | O(N W) | AC | 0.031 s | 9692 KB | 11283921 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1244_dp_optimized.cpp](1244_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N S) | AC | 0.015 s | 184 KB | 11308168 |
| [1244_dp_optimized.go](1244_dp_optimized.go) | Go 1.14 x64 | dp | O(N S) | AC | 0.031 s | 1128 KB | 11308170 |
| [1244_dp_optimized.java](1244_dp_optimized.java) | Java 1.8 | dp | O(N S) | AC | 0.109 s | 560 KB | 11308171 |
| [1244_dp_optimized.py](1244_dp_optimized.py) | Python 3.12 x64 | dp | O(N B) | AC | 0.078 s | 564 KB | 11308167 |
| [1244_dp_optimized.rs](1244_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N S) | AC | 0.015 s | 220 KB | 11308172 |
