# 1042. Toggling every switch an odd number of times

[Timus 1042](https://acm.timus.ru/problem.aspx?space=1&num=1042) · difficulty 810 · math

Original problem by Evgeny Shtykov, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` valves, all closed, and `N` technicians (`1 ≤ N ≤ 250`).
Each technician is responsible for a nonempty set of valves and, when
called, toggles every valve of the set (open ↔ closed). The sets are
independent: no technician's set is the symmetric difference of the sets
of some other technicians. Choose technicians so that afterwards every
valve is open. Print the numbers in increasing order, the shortest list if
there are several, or `No solution`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines: line `i` lists the valves of technician `i` and ends
with `-1`.

## Output

The numbers of the chosen technicians in increasing order, or
`No solution`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
1 2 -1
2 3 4 -1
2 -1
4 -1
```

Output:

```
1 2 3
```

### Example 2

Input:

```
3
2 3 -1
1 2 -1
3 -1
```

Output:

```
2 3
```

## Solution

Calling a technician twice changes nothing, so each technician is either
called once or not at all: an unknown `x_t` in GF(2). Valve `v` ends up
open when it is toggled an odd number of times:

```text
sum over technicians t with v in set(t) of x_t = 1   (mod 2),  for every v
```

That is `N` linear equations in `N` unknowns over GF(2). Independence of
the sets means the matrix is invertible: the system has exactly one
solution. So it is the only one and also the shortest, and `No solution`
never happens with valid input (the solutions still check for it).

Solve by Gauss–Jordan elimination with rows as bit sets: for each column
find a row with a 1, swap it up, and XOR it into every other row with a 1
in that column. With 64-bit words a row operation is about 4 XORs, so the
whole elimination is `O(N^3 / 64)`.

Pitfalls:

- all valves start closed, so the right-hand side is all ones;
- the equation of a valve collects the technicians who own it: the matrix
  is the transpose of the input lists;
- the list of a technician ends with `-1`, not with the end of the line.

## Language notes

- **C++**: `std::bitset`; **Go**, **Java**, **Rust**: arrays of 64-bit
  words.
- **Python**: every equation is one integer used as a bit mask, so a row
  operation is a single `^`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1042_math.cpp](1042_math.cpp) | G++ 13.2 x64 | math | O(N^3 / 64) | AC | 0.046 s | 204 KB |
| [1042_math.go](1042_math.go) | Go 1.14 x64 | math | O(N^3 / 64) | AC | 0.046 s | 2156 KB |
| [1042_math.java](1042_math.java) | Java 1.8 | math | O(N^3 / 64) | AC | 0.125 s | 516 KB |
| [1042_math.py](1042_math.py) | Python 3.12 x64 | math | O(N^3 / 64) | AC | 0.109 s | 5716 KB |
| [1042_math.rs](1042_math.rs) | Rust 1.75 x64 | math | O(N^3 / 64) | AC | 0.046 s | 764 KB |
