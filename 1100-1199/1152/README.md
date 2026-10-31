# 1152. The least damage from monsters on balconies around a hall

[Timus 1152](https://acm.timus.ru/problem.aspx?space=1&num=1152) · difficulty 155 · bitmask

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` balconies, `3 ≤ N ≤ 20`, stand in a circle, each with 1 to 100
monsters. One shot destroys three neighbouring balconies (balcony `N`
neighbours balcony 1). After every shot, every monster still alive deals
one unit of damage. Shots go on until no monsters remain. Find the least
total damage.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then the numbers of monsters on the balconies.

## Output

The least total damage.

## Examples

### Example 1

Input:

```
7
3 4 2 2 1 4 1
```

Output:

```
9
```

## Solution

The state is the set of balconies still occupied, a mask of `N` bits.
From a state, a shot at balcony `i` clears `i − 1`, `i` and `i + 1` and
leaves the set `rest`; it costs the number of monsters in `rest`, and then
the best play from `rest` follows. So with `damage(∅) = 0`

`damage(mask) = min over shots that hit something of alive(rest) + damage(rest)`.

Only states reachable from the full circle matter: their cleared parts are
unions of runs of three neighbours, and for `N = 20` there are just 15126
of them. Memoized recursion visits only those, with `N` shots each.
There are at most `N − 2` recursive transitions (`N − 1` active calls):
the first shot clears three balconies, and each later useful shot clears
at least one. Shots that hit no occupied balcony are skipped; they never
help. For `S` reachable states, computing `alive(rest)` in `O(N)` gives
`O(S·N²)` time for the recursion.

Pitfalls:

- the circle wraps around, so the shot at balcony 1 also clears balcony
  `N`;
- the damage after the last shot is zero, since nothing is left;
- the order of shots matters, because large groups should fall early;
- overlapping shots may clear only one new balcony. In test 07, shots
  centered at 1, 2 and 3 form a branch of three transitions, even though
  the optimal answer is 2; `⌈N / 3⌉` does not bound the recursion depth.

The answers were compared with a bottom-up table over all `2^N` subsets
on 120 random inputs with up to 13 balconies and on every test with 20.

## Optimized solutions

The optimized C++ solution caches for each state the damage still to
come plus the monsters alive in it, so the living sum is computed once
per state instead of once per transition, `O(S·N)` time in all; the
answer is the value of the full circle minus all monsters. The cache is
an `unordered_map` that holds only the reachable states instead of an
array of all `2^N` masks: {1152_bitmask_optimized.cpp}.

The optimized Go solution caches for each state the damage still to come
plus the monsters alive in it, so the living sum is computed once per
state instead of once per transition, `O(S·N)` time in all; the answer
is the value of the full circle minus all monsters. The cache is a `map`
that holds only the reachable states instead of a slice of all `2^N`
masks: {1152_bitmask_optimized.go}.

The optimized Java solution caches for each state the damage still to
come plus the monsters alive in it, so the living sum is computed once
per state instead of once per transition, `O(S·N)` time in all; the
answer is the value of the full circle minus all monsters. Instead of an
array of all `2^N` masks the cache is a hash table with open addressing
in two `int` arrays that doubles as it fills, so it holds only the
reachable states and boxes no keys; the input is read with
`StreamTokenizer` instead of `Scanner`: {1152_bitmask_optimized.java}.

The optimized Python solution keeps the reachable states in a plain
dictionary instead of `lru_cache` and caches for each state the damage
still to come plus the monsters alive in it, so the living sum is
computed once per state instead of once per transition, `O(S·N)` time in
all; the answer is the value of the full circle minus all monsters:
{1152_bitmask_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1152_bitmask_optimized.cpp`: time reduction +0.00%; memory reduction
  +87.18%; base: `1152_bitmask.cpp`.

- `1152_bitmask_optimized.go`: time reduction +51.61%; memory reduction
  +75.09%; base: `1152_bitmask.go`.

- `1152_bitmask_optimized.java`: time reduction +25.60%; memory
  reduction +81.78%; base: `1152_bitmask.java`.

- `1152_bitmask_optimized.py`: time reduction +67.52%; memory reduction
  +6.28%; base: `1152_bitmask.py`.

## Language notes

- All languages memoize the same recursion; Python keeps the memo in a
  cache keyed by the mask, the others in an array of `2^N` entries.
- Python uses `O(S + N)` space. The other languages initialize all
  `2^N` entries, giving `O(2^N + S·N²)` total time and `O(2^N + N)` space.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1152_bitmask.cpp](1152_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^N + S·N²) | AC | 0.015 s | 3868 KB | 11280481 |
| [1152_bitmask.go](1152_bitmask.go) | Go 1.14 x64 | bitmask | O(2^N + S·N²) | AC | 0.031 s | 10052 KB | 11280557 |
| [1152_bitmask.java](1152_bitmask.java) | Java 1.8 | bitmask | O(2^N + S·N²) | AC | 0.125 s | 5356 KB | 11280628 |
| [1152_bitmask.py](1152_bitmask.py) | Python 3.12 x64 | bitmask | O(S·N²) | AC | 0.625 s | 2420 KB | 11280596 |
| [1152_bitmask.rs](1152_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^N + S·N²) | AC | 0.001 s | 1592 KB | 11280672 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1152_bitmask_optimized.cpp](1152_bitmask_optimized.cpp) | G++ 13.2 x64 | bitmask | O(2^N + S·N) | AC | 0.015 s | 496 KB | 11305857 |
| [1152_bitmask_optimized.go](1152_bitmask_optimized.go) | Go 1.14 x64 | bitmask | O(S·N) | AC | 0.015 s | 2504 KB | 11305860 |
| [1152_bitmask_optimized.java](1152_bitmask_optimized.java) | Java 1.8 | bitmask | O(2^N + S·N) | AC | 0.093 s | 976 KB | 11305862 |
| [1152_bitmask_optimized.py](1152_bitmask_optimized.py) | Python 3.12 x64 | bitmask | O(S·N) | AC | 0.203 s | 2268 KB | 11305865 |
