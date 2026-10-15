# 1661. Dodecahedron

[Timus 1661](https://acm.timus.ru/problem.aspx?space=1&num=1661) · difficulty 3657 · combinatorics

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Thirty rods of equal length, each of some colour, become the edges of a
dodecahedron. Count the different dodecahedra that can be built, where
two that differ only by a rotation count as one.

## Input

Thirty integers from 1 to 30, the colours of the rods.

## Output

The number of different dodecahedra.

## Examples

### Example 1

Input:

```
1 1 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2
```

Output:

```
11
```

## Solution

By Burnside's lemma, the number of colourings up to rotation is the
average, over the 60 rotations of the dodecahedron, of the number of
colourings each rotation leaves unchanged. A rotation splits the 30
edges into cycles, and a colouring stays put exactly when every cycle is
of one colour. The rotations fall into four kinds:

- the identity: 30 cycles of length 1;
- 24 turns about axes through the centres of opposite faces: 6 cycles
  of length 5;
- 20 turns about axes through opposite vertices: 10 cycles of length 3;
- 15 half-turns about axes through the midpoints of opposite edges:
  those 2 edges stay in place, the other 28 form 14 cycles of length 2.

With all cycles of length L, colour c must fill exactly count(c) / L
cycles, which is impossible unless L divides every count, and otherwise
gives the multinomial coefficient (30 / L)! / ∏ (count(c) / L)!. For a
half-turn the two kept edges get their colours first, in order, and the
rest is the same count for L = 2. The sum is divided by 60. `O(C³)` for
C = 30 colours.

Pitfalls:

- the answer reaches 30! / 60, about 4.4 · 10³⁰ (test 03), more than 64
  bits; every intermediate value stays below 30! < 2¹²⁸, so C++ and Rust
  use 128-bit integers and the others use big integers;
- a multinomial built as a product of binomials, one exact factor at a
  time, never needs a value larger than about 30 · 30!.

The cycle types above come from the actual rotation group built from
the coordinates of a dodecahedron, and the formula matches a brute-force
orbit count on small colourings. The answers also match an independent
accepted implementation on random inputs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1661_combinatorics.cpp](1661_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(C^3) | AC | 0.015 s | 192 KB |
| [1661_combinatorics.go](1661_combinatorics.go) | Go 1.14 x64 | combinatorics | O(C^3) | AC | 0.015 s | 1280 KB |
| [1661_combinatorics.java](1661_combinatorics.java) | Java 1.8 | combinatorics | O(C^3) | AC | 0.140 s | 932 KB |
| [1661_combinatorics.py](1661_combinatorics.py) | Python 3.12 x64 | combinatorics | O(C^3) | AC | 0.093 s | 548 KB |
| [1661_combinatorics.rs](1661_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(C^3) | AC | 0.031 s | 240 KB |
