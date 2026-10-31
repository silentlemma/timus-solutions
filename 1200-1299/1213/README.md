# 1213. Fewest partitions to drive the cockroaches into the airlock

[Timus 1213](https://acm.timus.ru/problem.aspx?space=1&num=1213) · difficulty 170 · graphs

Original problem by Evgeny Krokhalev, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cargo module has up to 30 compartments joined by partitions, and every
compartment is full of cockroaches. Filling a compartment with gas and
opening one of its partitions drives all its cockroaches into the
neighbouring compartment. Every compartment is connected to the airlock.
Find the fewest partition openings that gather all the cockroaches in the
airlock.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The name of the airlock, then one partition per line as two compartment
names joined by `-`, then a line `#`. Names are up to 20 Latin letters
and digits, and letter case matters.

## Output

The fewest openings.

## Examples

### Example 1

Input:

```
Gateway
Machinery-Gateway
Machinery-Control
Control-Central
Control-Engine
Central-Engine
Storage-Gateway
Storage-Waste
Central-Waste
#
```

Output:

```
6
```

## Solution

Every compartment other than the airlock starts with cockroaches and must
end empty, and a compartment only empties when one of its own partitions
is opened, so at least one opening per compartment is needed. That many
is also enough: take a tree of partitions that reaches the airlock from
every compartment and empty the compartments from the farthest towards
the airlock, each through its partition on the way. The answer is the
number of different compartment names minus one. `O(P log P)` for `P`
partitions.

Pitfalls:

- `Engine` and `engine` are different compartments;
- the airlock may have no partitions listed at all, and then the answer
  is 0;
- the layout of the partitions does not matter, only how many
  compartments there are.

The answers were compared with a separately written solution on 100
random modules.

## Optimized solutions

The optimized C++ solution reads the partitions with `scanf` into a
buffer of 42 bytes, enough for two names of at most 20 characters and
the dash, and keeps the different names in a static table of 30 names of
21 bytes, searched with `strcmp`: there are at most 30 compartments, so
the linear search is cheap. This replaces `iostream`, `std::string` and
the nodes of `std::set`: {1213_graphs_optimized.cpp}.

The optimized Java solution reads the tokens with `BufferedReader` and
`StringTokenizer` instead of `Scanner`, whose regular expressions are
costly to set up. It finds the dash with `indexOf` and adds the two
names directly, without the temporary array and list wrapper made by
`split` and `Arrays.asList`: {1213_graphs_optimized.java}.

The optimized Rust solution reads the input line by line instead of
reading all of it into one string, and keeps the different names in a
small vector searched linearly instead of a hash set: there are at most
30 compartments, so at most 30 names are kept, whatever the number of
partitions: {1213_graphs_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1213_graphs_optimized.cpp`: time reduction +0.00%; memory reduction
  +74.49%; base: `1213_graphs.cpp`.

- `1213_graphs_optimized.java`: time reduction +28.44%; memory reduction
  +72.07%; base: `1213_graphs.java`.

- `1213_graphs_optimized.rs`: time reduction +50.00%; memory reduction
  +50.96%; base: `1213_graphs.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1213_graphs.go](1213_graphs.go).

- All languages collect the names in a set and print its size minus one.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1213_graphs.cpp](1213_graphs.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 392 KB | 11283651 |
| [1213_graphs.go](1213_graphs.go) | Go 1.14 x64 | graphs | O(P log P) | AC | 0.015 s | 1064 KB | 11283652 |
| [1213_graphs.java](1213_graphs.java) | Java 1.8 | graphs | O(P log P) | AC | 0.109 s | 1876 KB | 11283654 |
| [1213_graphs.py](1213_graphs.py) | Python 3.12 x64 | graphs | O(P log P) | AC | 0.078 s | 384 KB | 11283653 |
| [1213_graphs.rs](1213_graphs.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.062 s | 416 KB | 11283655 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1213_graphs_optimized.cpp](1213_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 100 KB | 11307251 |
| [1213_graphs_optimized.java](1213_graphs_optimized.java) | Java 1.8 | graphs | O(P log P) | AC | 0.078 s | 524 KB | 11307254 |
| [1213_graphs_optimized.rs](1213_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.031 s | 204 KB | 11307256 |
