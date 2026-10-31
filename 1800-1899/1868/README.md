# 1868. Prediction Contest

[Timus 1868](https://acm.timus.ru/problem.aspx?space=1&num=1868) · difficulty 158 · implementation

Original problem by Denis Dublennykh, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

At the world finals the first four teams win gold medals, the next four
silver and the next four bronze. Several veterans made forecasts of the
form "team X wins a medal of kind Y", and Vadik pays five dollars to
each veteran with the most right guesses. Given the twelve medallists
in order of their places and all the forecasts, how much does Vadik
pay?

## Input

Twelve team names from the first place to the twelfth, then n
(1 ≤ n ≤ 100) and n forecasts. A forecast starts with its number of
guesses kᵢ, followed by kᵢ lines "team : medal" with the medal "gold",
"silver" or "bronze". No forecast gives a team two medals or a medal to
more than four teams. Names are 1 to 30 Latin letters, underscores, dots
and commas. Every name, number and guess is on a line of its own.

## Output

The amount Vadik pays, in dollars.

## Examples

### Example 1

Input:

```
Zhejiang_U
U_of_Michigan_at_Ann_Arbor
Tsinghua_U
St._Petersburg_SU
Nizhny_Novgorod_SU
Saratov_SU
Friedrich_Alexander_U
Donetsk_National_U
Jagiellonian_U_in_Krakow
Moscow_SU
Ural_SU
U_of_Waterloo
3
6
Moscow_SU : gold
St._Petersburg_SU_of_ITMO : gold
Warsaw_U : gold
Tsinghua_U : gold
Nizhny_Novgorod_SU : silver
Saratov_SU : silver
6
Warsaw_U : gold
Saratov_SU : gold
Tsinghua_U : gold
Donetsk_National_U : silver
St._Petersburg_SU_of_ITMO : silver
Ural_SU : bronze
6
Zhejiang_U : gold
Tsinghua_U : gold
Shanghai_Jiao_Tong_U : gold
Fudan_U : gold
Moscow_SU : silver
Nizhny_Novgorod_SU : silver
```

Output:

```
15
```

## Solution

Names contain no spaces, so the input is a stream of words: twelve
names, then for each guess a name, a colon and a medal. A dictionary
from the twelve names to their medals (place 1–4 gold, 5–8 silver,
9–12 bronze) tells whether a guess is right; a team missing from it
won nothing. Count the right guesses of every veteran, and pay five
dollars for each veteran with the largest count. `O(n·k)` dictionary
lookups.

In the example each veteran has three right guesses, so all three win
and Vadik pays 15 dollars.

Pitfalls:

- the medal comes from the place: the names are in order, so the
  first four are gold, and so on;
- a forecast may name teams that won no medal at all;
- names are case-sensitive and may consist of dots and commas only;
- when nobody guessed anything right, every veteran ties with zero and
  is paid.

The amounts agree with an independent accepted implementation on 150
random contests.

## Optimized solutions

The optimized C++ solution keeps the twelve names in fixed `char` arrays
of 31 bytes, since a name has at most 30 characters, reads each guess
with `scanf` into buffers of 31 and 7 bytes (a medal word has at most 6
letters) and compares it with the twelve names by `strcmp` instead of a
`map` of `string`s. It keeps the best count and the number of veterans
with it as it goes instead of a `vector` of all counts, and uses `stdio`
instead of `iostream`: {1868_implementation_optimized.cpp}.

The optimized Python solution reads the input line by line, since every
name, number and guess is on a line of its own, instead of splitting the
whole input into a list of words; it keeps the best count and the number
of veterans with it as it goes instead of a list of all counts:
{1868_implementation_optimized.py}.

The optimized Rust solution reads the input line by line into one reused
`String`, since every name, number and guess is on a line of its own,
instead of reading the whole input; it compares each guess with the
twelve stored names directly instead of a `HashMap` and keeps the best
count and the number of veterans with it as it goes instead of a vector
of all counts: {1868_implementation_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1868_implementation_optimized.cpp`: time reduction +0.00%; memory
  reduction +75.45%; base: `1868_implementation.cpp`.

- `1868_implementation_optimized.py`: time reduction -19.23%; memory
  reduction +42.20%; base: `1868_implementation.py`.

- `1868_implementation_optimized.rs`: time reduction +0.00%; memory
  reduction +60.45%; base: `1868_implementation.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1868_implementation.go](1868_implementation.go).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1868_implementation.cpp](1868_implementation.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 440 KB | 11304080 |
| [1868_implementation.go](1868_implementation.go) | Go 1.14 x64 | implementation | O(n k) | AC | 0.015 s | 1220 KB | 11290927 |
| [1868_implementation.java](1868_implementation.java) | Java 1.8 | implementation | O(n k) | AC | 0.093 s | 1196 KB | 11290930 |
| [1868_implementation.py](1868_implementation.py) | Python 3.12 x64 | implementation | O(n k) | AC | 0.078 s | 692 KB | 11290928 |
| [1868_implementation.rs](1868_implementation.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 536 KB | 11290931 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1868_implementation_optimized.cpp](1868_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 108 KB | 11305924 |
| [1868_implementation_optimized.py](1868_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(n k) | AC | 0.093 s | 400 KB | 11305927 |
| [1868_implementation_optimized.rs](1868_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 212 KB | 11305928 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
