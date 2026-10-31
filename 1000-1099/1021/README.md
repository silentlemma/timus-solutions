# 1021. A pair from two sorted lists with a given sum

[Timus 1021](https://acm.timus.ru/problem.aspx?space=1&num=1021) · difficulty 148 · two_pointers, hashing

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two lists of integers are given: the first sorted in increasing order, the
second in decreasing order (`1 ≤ N_i ≤ 50 000` numbers each, every number
from -32768 to 32767). Decide whether one number from each list can be
chosen so that they sum to exactly 10000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first list: its size, then its numbers, one per line. Then the second
list in the same format.

## Output

`YES` if such a pair exists, `NO` otherwise.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
-5
3
9998
3
10
7
2
```

Output:

```
YES
```

### Example 2

Input:

```
3
1
2
3
3
9000
50
0
```

Output:

```
NO
```

## Solution

**Two pointers.** Put a pointer `i` at the start of the increasing list and
`j` at the start of the decreasing one, so `up[i]` is the smallest remaining
number of the first list and `down[j]` the largest of the second. Compare
`up[i] + down[j]` with 10000:

- equal — the pair is found;
- smaller — `up[i]` cannot be part of any pair, because even the largest
  remaining `down[j]` is not enough: move `i` forward;
- larger — `down[j]` cannot be part of any pair, because even the smallest
  remaining `up[i]` is too much: move `j` forward.

When a pointer runs off its list, there is no pair. Every step discards one
number: `O(N_1 + N_2)`.

**Hashing.** Put `10000 - b` for every `b` of the second list into a set and
check whether any number of the first list is in it — also linear on
average, and it does not need the sorting.

Pitfalls:

- the second list is sorted the other way: walk both lists from the
  beginning;
- the sum 10000 may need the extreme values, e.g. `32767 + (-22767)`.

## Optimized solutions

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
refilled with `fread` instead of `scanf`. It stores only the increasing
list, as `int16_t`, which holds every number from -32768 to 32767, and
moves its pointer while the decreasing list is being read, so the second
list is never stored: {1021_two_pointers_optimized.cpp}.

The optimized Go solution parses the numbers byte by byte from a
`bufio.Reader` instead of `fmt.Fscan`. It stores only the increasing
list, as `int16`, which holds every number from -32768 to 32767, and
moves its pointer while the decreasing list is being read, so the second
list is never stored: {1021_two_pointers_optimized.go}.

The optimized Java solution parses the numbers by hand from a 4 KB
buffer refilled from `System.in` instead of `StreamTokenizer`. It stores
only the increasing list, as `short`, which holds every number from
-32768 to 32767, and moves its pointer while the decreasing list is
being read, so the second list is never stored:
{1021_two_pointers_optimized.java}.

The optimized Python solution relies on one number per line and converts
each line as it comes instead of splitting the whole input into a list.
In place of a set it marks the numbers of the first list in a
`bytearray` of 65536 cells, one for every possible value from -32768 to
32767. For every `b` of the second list it checks that `10000 - b` lies
in this range and only then looks it up: {1021_hashing_optimized.py}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer refilled from standard input instead of reading the whole input
into a `String`. It stores only the increasing list, as `i16`, which
holds every number from -32768 to 32767, and moves its pointer while the
decreasing list is being read, so the second list is never stored:
{1021_two_pointers_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1021_two_pointers_optimized.cpp`: time reduction +80.77%; memory
  reduction +63.89%; base: `1021_two_pointers.cpp`.

- `1021_two_pointers_optimized.go`: time reduction +50.00%; memory
  reduction +57.25%; base: `1021_two_pointers.go`.

- `1021_two_pointers_optimized.java`: time reduction +37.60%; memory
  reduction +45.58%; base: `1021_two_pointers.java`.

- `1021_hashing_optimized.py`: time reduction -39.74%; memory reduction
  +95.36%; base: `1021_hashing.py`.

- `1021_two_pointers_optimized.rs`: time reduction +67.39%; memory
  reduction +86.55%; base: `1021_two_pointers.rs`.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: two pointers.
- **Python**: a set intersection, which runs at C speed.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1021_two_pointers.cpp](1021_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.078 s | 576 KB | 11278250 |
| [1021_two_pointers.go](1021_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 2620 KB | 11278252 |
| [1021_two_pointers.java](1021_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 904 KB | 11278257 |
| [1021_hashing.py](1021_hashing.py) | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.078 s | 10700 KB | 11278255 |
| [1021_two_pointers.rs](1021_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 2112 KB | 11278259 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1021_two_pointers_optimized.cpp](1021_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 208 KB | 11304533 |
| [1021_two_pointers_optimized.go](1021_two_pointers_optimized.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.031 s | 1120 KB | 11304534 |
| [1021_two_pointers_optimized.java](1021_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.078 s | 492 KB | 11304535 |
| [1021_hashing_optimized.py](1021_hashing_optimized.py) \* | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.109 s | 496 KB | 11304537 |
| [1021_two_pointers_optimized.rs](1021_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 284 KB | 11304536 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
