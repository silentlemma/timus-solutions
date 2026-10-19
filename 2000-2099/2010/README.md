# 2010. Attacked Squares on an Empty Board

[Timus 2010](https://acm.timus.ru/problem.aspx?space=1&num=2010) · difficulty 133 · math

Folklore problem, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place one chess piece at square `(x,y)` of an otherwise empty `n×n`
board. Independently for a king, knight, bishop, rook and queen, count
the squares that the piece attacks in one move. Board coordinates run
from 1 to `n`. The starting square is never counted, and there are no
other pieces to block a ray. A knight jumps in the usual way.

## Input

The first line contains `n`, `1 ≤ n ≤ 100,000,000`. The next line
contains `x y`, with `1 ≤ x,y ≤ n`. Time limit 0.5 seconds, memory 64
MB.

## Output

Print exactly five lines in the order `King: count`, `Knight: count`,
`Bishop: count`, `Rook: count`, `Queen: count`. Labels are
case-sensitive. The unique labels and integers are compared token by
token.

## Checking

Outputs are compared token by token.

## Examples

```
8
5 2
```

```
King: 8
Knight: 6
Bishop: 9
Rook: 14
Queen: 23
```

All eight neighboring squares exist. Six knight destinations remain
inside the board. The bishop's four ray lengths are 1, 4, 1 and 3,
totaling 9. The rook attacks 7 squares in each of its row and column,
totaling 14, and the queen attacks `9+14=23` squares.

## Solution

Only distances to the borders matter; never allocate or scan the board.

For the king, the possible first coordinates are `x` and any existing
neighbors `x−1,x+1`. Their count is `a=1+[x>1]+[x<n]`, where brackets
mean 1 if true and 0 otherwise. Similarly define `b=1+[y>1]+[y<n]`.
Every pair is at most one step away, so the answer is `a·b−1`, removing
the starting square. This also gives zero for a one-square board.

For the knight, test each of the eight offsets `(±1,±2)` and `(±2,±1)`.
Count an offset exactly when both destination coordinates lie in `1..n`.
These offsets are distinct and none returns to the origin.

Each bishop ray stops when either coordinate reaches its border. The
four lengths are `min(x−1,y−1)`, `min(x−1,n−y)`, `min(n−x,y−1)` and
`min(n−x,n−y)`. Their sum counts every attacked diagonal square exactly
once: all such squares lie on one of these rays, and the rays meet only
at the excluded origin.

A rook attacks every other square in its row and column. There are `n−1`
in each, and their only intersection is the origin; the answer is
`2(n−1)`. The queen's diagonal and orthogonal attacks are disjoint away
from the origin, so its answer is the bishop's count plus the rook's
count. These arguments account for every legal destination and exclude
every illegal one, proving all five results.

The algorithm performs a fixed number of arithmetic operations and eight
knight checks: time `O(1)`, extra space `O(1)`. The largest possible
answer is at most `4(n−1) ≤ 399,999,996`; the ports use 64-bit integers
or Python integers. Signed destination coordinates make off-board
negative knight positions easy to reject. An alternative is to count the
complete two diagonal lines by intersection with the board and remove
the origin from each.

## Language notes

Do not count the origin, add an extra move, or assume that all eight
knight destinations exist near a border. The rook's answer does not
depend on `(x,y)`; the bishop's answer does. Queen attacks are a union,
with no extra subtraction after both component counts exclude the
origin. Handle `n=1` directly through the same formulas. Go 1.14 needs a
small minimum helper; Java 8 and Rust use signed wide coordinates.
Python uses constant memory and runs under CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2010_math.cpp](2010_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 400 KB |
| [2010_math.go](2010_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1120 KB |
| [2010_math.java](2010_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 412 KB |
| [2010_math.py](2010_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 552 KB |
| [2010_math.rs](2010_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB |
