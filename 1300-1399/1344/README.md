# 1344. Gigantic Turnip

[Timus 1344](https://acm.timus.ru/problem.aspx?space=1&num=1344) · difficulty 4275 · dsu

Original problem by Pavel Egorov, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 32 weightless pulleys are joined by weightless ropes. Each pulley
has a rope thrown over it and another rope tied to its axle. In a pulley
of the first type the axle rope goes up and the two ends of the other
rope go down; in the second type it is the other way round. Every rope
end leads to another pulley, to the ceiling, to a turnip of 1 kg or,
for exactly one end, nowhere: a load is to be hung on it. All ropes are
vertical, and pulleys joined by a rope are at different heights. Find
the mass of the load that keeps the system in balance, with four digits
after the point, or print `No solution` if there is none and `Any` if
every mass works.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then for each pulley its type T, where the two ends of the rope over
it lead (X1 and X2) and where its axle rope leads (Y). 0 means the
ceiling, −1 the turnip and −2 the free end.

## Output

The mass, `No solution` or `Any`.

## Examples

### Example 1

Input:

```
2
1 -1 2 0
2 1 0 -2
```

Output:

```
2.0000
```

### Example 2

Input:

```
4
1 3 2 0
2 1 0 4
1 -1 4 1
2 3 2 -2
```

Output:

```
No solution
```

### Example 3

Input:

```
4
1 2 2 0
2 1 1 -2
1 4 4 0
2 3 3 -1
```

Output:

```
Any
```

## Solution

Measure forces in kilograms. A rope over a weightless pulley has the
same tension t at both ends, and the pulley is in balance when its axle
rope holds both ends: the axle tension is a = 2t. A rope between two
pulleys has one tension. The end at the turnip has tension 1, the free
end the unknown mass m, and the ceiling takes whatever is needed.

Which part of the other pulley a rope reaches follows from directions:
a rope that leaves pulley i downwards arrives at pulley j from below.
At j that is either its axle or the ends over it, whichever side faces
up. So every rope says "this tension equals that one", and every
pulley says "a = 2t".

All these relations multiply by powers of two. A union-find over the
tensions keeps, for every tension, the power of two that links it to
the root of its group. When a relation closes a cycle and the powers do
not agree, say t = 2t, every tension in that group must be 0. Then:

- if the turnip's group must be 0, the turnip cannot hang: `No solution`;
- if the turnip and the free end are in one group, m is the power of two
  between them;
- if the free end's group must be 0, m = 0;
- otherwise the free end does not depend on the turnip: `Any`.

`O(N α(N))`.

Pitfalls:

- a rope reaching a pulley meets either its axle or the rope over it,
  and only the directions tell which;
- the tensions can contradict each other, which leaves no balance
  (test 02);
- the free end can hang on a system that has nothing to do with the
  turnip (tests 03 and 06);
- a chain of 31 movable pulleys gives 2³¹, more than 32-bit integers
  hold.

The union-find was compared with exact Gaussian elimination on the same
equations for about 3000 random systems of up to 5 pulleys.

## Language notes

- All five solutions keep the powers of two as integers and only build
  the mass at the end.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1344_dsu.cpp](1344_dsu.cpp) | G++ 13.2 x64 | dsu | O(N·α(N)) | AC | 0.015 s | 224 KB |
| [1344_dsu.go](1344_dsu.go) | Go 1.14 x64 | dsu | O(N·α(N)) | AC | 0.031 s | 1104 KB |
| [1344_dsu.java](1344_dsu.java) | Java 1.8 | dsu | O(N·α(N)) | AC | 0.140 s | 1948 KB |
| [1344_dsu.py](1344_dsu.py) | Python 3.12 x64 | dsu | O(N·α(N)) | AC | 0.062 s | 784 KB |
| [1344_dsu.rs](1344_dsu.rs) | Rust 1.75 x64 | dsu | O(N·α(N)) | AC | 0.015 s | 260 KB |
