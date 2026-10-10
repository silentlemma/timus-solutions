# 1147. The visible area of each colour after stacking rectangles on a sheet

[Timus 1147](https://acm.timus.ru/problem.aspx?space=1&num=1147) · difficulty 736 · dsu

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 1000` coloured rectangles with sides parallel to the axes are laid
one after another on a white sheet `A × B`, `A, B ≤ 10000`; the sheet has
colour 1 and the colours go up to 2500. Seen from above, list every
visible colour with its total visible area, in increasing order of
colour.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`A`, `B` and `N`, then `N` lines with the lower left corner, the upper
right corner and the colour of a rectangle, from the bottom one up.

## Output

The visible colours with their areas, one per line, by colour.

## Examples

### Example 1

Input:

```
20 20 3
2 2 18 18 2
0 8 19 19 3
8 0 10 19 4
```

Output:

```
1 91
2 84
3 187
4 38
```

## Solution

All corners split the sheet into at most `2001` vertical strips and `2001`
horizontal bands; inside one strip and one band the colour seen from
above is constant. Take the strips one at a time. In a strip, go through
the rectangles that cross it from the top one down: each paints the bands
it covers that no higher rectangle has painted yet, and adds their height
times the strip width to its colour. Whatever stays unpainted is white.

To find the unpainted bands quickly, `skip[j]` points from band `j` to
the next band that may still be unpainted, as in a disjoint-set union
with path halving; painting band `j` sets `skip[j] = j + 1`. Every band
is painted once per strip, so a strip costs `O(N + Y)` and the whole
sweep `O(X·(N + Y))` with `X, Y ≤ 2001`. A strip stops early once it is
fully painted.

Pitfalls:

- a white rectangle on top shows white, so it adds to colour 1 like the
  uncovered sheet;
- colours with zero visible area are not printed;
- areas reach `10⁸`, still within 32 bits, but 64-bit sums are used.

The answers were compared with painting every unit square of the sheet
on 150 small random inputs.

## Language notes

- C++, Go, Java and Rust check every rectangle for every strip.
- Python builds the list of rectangles over each strip first and skips
  the check; it is still the slowest of the five here. On the largest
  tests it takes about 0.8 s under CPython in our runs, beyond the 0.5 s
  limit, so the Python solution is submitted under PyPy 3.10, where Timus
  accepts it in 0.484 s, close to the limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1147_dsu.cpp](1147_dsu.cpp) | G++ 13.2 x64 | dsu | O(X·(N + Y)) | AC | 0.078 s | 228 KB |
| [1147_dsu.go](1147_dsu.go) | Go 1.14 x64 | dsu | O(X·(N + Y)) | AC | 0.218 s | 1356 KB |
| [1147_dsu.java](1147_dsu.java) | Java 1.8 | dsu | O(X·(N + Y)) | AC | 0.281 s | 3796 KB |
| [1147_dsu.py](1147_dsu.py) | PyPy 3.10 x64 | dsu | O(X·(N + Y)) | AC | 0.484 s | 30596 KB |
| [1147_dsu.rs](1147_dsu.rs) | Rust 1.75 x64 | dsu | O(X·(N + Y)) | AC | 0.109 s | 264 KB |
