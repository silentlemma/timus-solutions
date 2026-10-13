# 1386. Maze

[Timus 1386](https://acm.timus.ru/problem.aspx?space=1&num=1386) · difficulty 1157 · simulation

Original problem by Andrew Khalyavin, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A maze is an N × M field, 1 ≤ N, M ≤ 100, with four commands. For every
cell and command the map gives the cell the player moves to. The
player's start is unknown, but all S ≤ 4000 commands of the game are
known. Print every cell where the player may stand now.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N and M, then four blocks, one per command, of N lines with M pairs:
the pair in column i of line j of block k is the cell reached from
cell (j, i) by command k. Then S and the S commands.

## Output

The number of cells, then the cells sorted by row and then by column.

## Examples

### Example 1

Input:

```
2 3
1 2  1 3  1 3
2 2  2 3  2 3
2 1  2 2  2 3
2 1  2 2  2 3
1 1  1 1  1 2
2 1  2 1  2 2
1 1  1 2  1 3
1 1  1 2  1 3
4
1 2 3 4
```

Output:

```
2
1 1
1 2
```

## Solution

Keep the set of cells where the player may be, starting with the whole
field, and send it through each command. Several cells may lead to the
same one, so the new set keeps each cell once: a cell is added only if
its mark does not hold the current step yet. The set never grows, so a
step costs at most N·M lookups. `O(S·N·M)`, which is 4·10⁷ simple steps
at worst.

Pitfalls:

- the maps may be permutations, as on a torus, and then nothing ever
  merges: every step touches all 10 000 cells (generated tests 1 and 3);
- the time limit is half a second, so the cells are numbered as one
  index and each step is one tight loop;
- the output is sorted by row first, then by column.

The answers were compared on 400 small random fields with a simulation
from every start cell.

## Language notes

- Python runs under PyPy and applies the commands four at a time: 16
  tables for pairs of commands, and a table for a block of four built
  from two pairs when the block first occurs, so the cells go through a
  quarter of the steps. One command at a time it exceeded the 0.5 s limit
  on the judge's test 46; now it takes 0.33 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1386_simulation.cpp](1386_simulation.cpp) | G++ 13.2 x64 | simulation | O(S·N·M) | AC | 0.078 s | 280 KB |
| [1386_simulation.go](1386_simulation.go) | Go 1.14 x64 | simulation | O(S·N·M) | AC | 0.093 s | 1584 KB |
| [1386_simulation.java](1386_simulation.java) | Java 1.8 | simulation | O(S·N·M) | AC | 0.203 s | 1152 KB |
| [1386_simulation.py](1386_simulation.py) | PyPy 3.10 x64 | simulation | O(S·N·M) | AC | 0.328 s | 45076 KB |
| [1386_simulation.rs](1386_simulation.rs) | Rust 1.75 x64 | simulation | O(S·N·M) | AC | 0.093 s | 924 KB |
