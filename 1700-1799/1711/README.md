# 1711. Code Names

[Timus 1711](https://acm.timus.ru/problem.aspx?space=1&num=1711) · difficulty 135 · greedy

Original problem by Alex Samsonov, prepared by Igor Chevdar, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n problems has three candidate code names, and the problems
of a set go in the alphabetical order of their names. Pick one name
per problem so that the problems come in a given order, or report that
no choice works.

## Input

n (1 ≤ n ≤ 16), then n lines with the three names of each problem:
lowercase Latin letters, at most 20 per name, all names distinct. The
last line is the required order, a permutation of 1 … n.

## Output

The chosen names in the required order, one per line, or IMPOSSIBLE.
Any valid choice is accepted.

## Examples

### Example 1

Input:

```
11
cipher grille kamkohob
names codenames codes
newtests rejudge timus
size volume summit
watchmen braineater twosides
solution random yesorno
keywords subversion commands
bosses shooting shaitan
game strategy playgame
mnemonic palindromes bestname
eligibility rectangle rules
2 1 7 10 9 6 11 3 8 4 5
```

Output:

```
codenames
grille
keywords
mnemonic
playgame
random
rectangle
rejudge
shaitan
volume
watchmen
```

### Example 2

Input:

```
3
problems in the
first sample are
ordered not randomly
1 2 3
```

Output:

```
IMPOSSIBLE
```

## Solution

Go along the required order and give each problem the least of its
names that comes after the previous chosen name. If none does, the
answer is IMPOSSIBLE.

This greedy choice is safe. Suppose some valid choice exists, and
compare it with the greedy one problem by problem. By induction the
greedy name is never later than the valid one: the valid name for the
next problem comes after the valid previous name, so also after the
greedy previous name. It is therefore a candidate, and the greedy pick
is at most it. So the greedy run never gets stuck. `O(n)` comparisons
of short strings.

Pitfalls:

- the names are compared as strings, so a prefix comes first: "code"
  before "codenames";
- the order line lists problem numbers by their place in the set, not
  the place of each problem;
- any valid answer is accepted, so the tests use a checker.

The checker verifies that every name belongs to its problem and that
the names increase. The answers match an independent accepted
implementation on 600 random sets.

## Optimized solutions

The optimized C++ solution reads with `scanf` into a fixed array of
16 × 3 names of 21 bytes each, enough for n ≤ 16 and 20 letters plus the
terminating zero, instead of a vector of vectors of `std::string` read
through `iostream`. Instead of sorting the three names of a problem, it
scans them with `strcmp` for the least one after the previous choice,
remembers only pointers to the chosen names, and prints them with
`puts`: {1711_greedy_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1711_greedy_optimized.cpp`: time reduction +51.61%; memory reduction
  +74.75%; base: `1711_greedy.cpp`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1711_greedy.go](1711_greedy.go).
- [1711_greedy.java](1711_greedy.java).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy.cpp](1711_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 396 KB | 11304067 |
| [1711_greedy.go](1711_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1148 KB | 11289207 |
| [1711_greedy.java](1711_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 516 KB | 11289209 |
| [1711_greedy.py](1711_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.093 s | 492 KB | 11304068 |
| [1711_greedy.rs](1711_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 236 KB | 11289213 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy_optimized.cpp](1711_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 100 KB | 11304441 |
