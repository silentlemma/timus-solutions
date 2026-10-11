# 1213. Fewest partitions to drive the cockroaches into the airlock

[Timus 1213](https://acm.timus.ru/problem.aspx?space=1&num=1213) · difficulty 171 · graphs

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
names joined by `-`, then a line `#`. Names are up to 20 letters and
digits, and letter case matters.

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

## Language notes

- All languages collect the names in a set and print its size minus one.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1213_graphs.cpp](1213_graphs.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 392 KB |
| [1213_graphs.go](1213_graphs.go) | Go 1.14 x64 | graphs | O(P log P) | AC | 0.015 s | 1064 KB |
| [1213_graphs.java](1213_graphs.java) | Java 1.8 | graphs | O(P log P) | AC | 0.109 s | 1876 KB |
| [1213_graphs.py](1213_graphs.py) | Python 3.12 x64 | graphs | O(P log P) | AC | 0.078 s | 384 KB |
| [1213_graphs.rs](1213_graphs.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.062 s | 416 KB |
