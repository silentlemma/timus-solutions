# 1210. The cheapest climb through levels of planets

[Timus 1210](https://acm.timus.ru/problem.aspx?space=1&num=1210) · difficulty 169 · dp

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Planets are arranged in levels 0 to `N`, `0 < N < 30`, at most 30 per
level, and level 0 holds a single planet, the traveller's home. Links
lead only from a planet of one level to planets of the next, and each
costs an integer from `−32768` to `32767`; a negative cost means the
spirit guarding it pays the traveller. Find the cheapest route from home
to any planet of level `N`; it may be negative. A route is known to
exist.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` blocks separated by lines holding `*`. Block `i` starts
with the number `K_i` of planets on level `i`, numbered from 1 to `K_i`;
then, for each of them in that order, a line of pairs "planet of level
`i − 1`, cost" ended by `0`.

## Output

The least total cost.

## Examples

### Example 1

Input:

```
3
2
1 15 0
1 5 0
*
3
1 -5 2 10 0
1 3 0
2 40 0
*
2
1 1 2 5 3 -5 0
2 -19 3 -20 0
```

Output:

```
-1
```

## Solution

The map is layered and every link climbs one level, so there are no
cycles and negative costs do no harm: the cheapest way to a planet is the
cheapest way to one of the planets linking to it plus that link. Keep the
cheapest cost for every planet of the current level, starting with 0 for
home, and build the next level's costs from the incoming links listed in
its block. The answer is the smallest cost on level `N`. `O(L)` for `L`
links.

Pitfalls:

- a planet may have no incoming link at all, or only links from
  unreachable planets; such a planet must stay unreachable instead of
  passing on a generous link from it;
- the `*` lines are only separators and can be skipped when reading
  numbers;
- the total stays below `30 · 32768` in absolute value, so 32-bit integers
  are enough.

The answers were compared with a separately written solution on 300
random maps, half of them with unreachable planets.

## Optimized solutions

The optimized C++ solution parses the signed numbers by hand from a 4 KB
buffer refilled with `fread`, skipping the `*` separators along with the
other characters that are not part of a number, instead of reading every
token into a `std::string` and converting it with `std::stoi`; it prints
with `printf`, so `iostream` is not used at all. Its sentinel for an
unreachable planet is 1 000 000, which exceeds any route cost, since a
route has fewer than 30 links of at most 32 768 in absolute value:
{1210_dp_optimized.cpp}.

The optimized Java solution reads the input in 4 KB blocks and parses
the signed numbers by hand, skipping the `*` separators, instead of
splitting lines with `StringTokenizer` into strings, and finds the
minimum with a plain loop instead of `Arrays.stream`. Its sentinel for
an unreachable planet is 1 000 000, which exceeds any route cost, since
a route has fewer than 30 links of at most 32 768 in absolute value:
{1210_dp_optimized.java}.

The optimized Python solution reads the input in 4 KB chunks and splits
each chunk into tokens, carrying only an unfinished token over to the
next chunk, instead of reading and splitting the whole input at once,
so the input is never held in memory as a whole; the `*` tokens are
dropped as they come: {1210_dp_optimized.py}.

The optimized Rust solution parses the signed numbers by hand from a
4 KB buffer that is refilled from the standard input, skipping the `*`
separators, instead of reading the whole input into a `String`, so apart
from the costs of two levels only this buffer is held. Its sentinel for
an unreachable planet is 1 000 000, which exceeds any route cost, since
a route has fewer than 30 links of at most 32 768 in absolute value:
{1210_dp_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1210_dp_optimized.cpp`: time reduction +51.61%; memory reduction
  +65.62%; base: `1210_dp.cpp`.

- `1210_dp_optimized.java`: time reduction +22.14%; memory reduction
  +92.73%; base: `1210_dp.java`.

- `1210_dp_optimized.py`: time reduction +25.60%; memory reduction
  +83.15%; base: `1210_dp.py`.

- `1210_dp_optimized.rs`: time reduction +0.00%; memory reduction
  +74.86%; base: `1210_dp.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1210_dp.go](1210_dp.go).

- Python and Rust filter the `*` tokens out of the input stream; the
  other languages skip them in their number readers.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1210_dp.cpp](1210_dp.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.031 s | 384 KB | 11283629 |
| [1210_dp.go](1210_dp.go) | Go 1.14 x64 | dp | O(L) | AC | 0.031 s | 1220 KB | 11283633 |
| [1210_dp.java](1210_dp.java) | Java 1.8 | dp | O(L) | AC | 0.140 s | 5668 KB | 11283635 |
| [1210_dp.py](1210_dp.py) | Python 3.12 x64 | dp | O(L) | AC | 0.125 s | 3276 KB | 11283634 |
| [1210_dp.rs](1210_dp.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 732 KB | 11283636 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1210_dp_optimized.cpp](1210_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.001 s | 132 KB | 11307238 |
| [1210_dp_optimized.java](1210_dp_optimized.java) | Java 1.8 | dp | O(L) | AC | 0.109 s | 412 KB | 11307239 |
| [1210_dp_optimized.py](1210_dp_optimized.py) \* | Python 3.12 x64 | dp | O(L) | AC | 0.093 s | 552 KB | 11307241 |
| [1210_dp_optimized.rs](1210_dp_optimized.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 184 KB | 11307240 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
