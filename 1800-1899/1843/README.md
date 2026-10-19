# 1843. Cutting a Parallelepiped

[Timus 1843](https://acm.timus.ru/problem.aspx?space=1&num=1843) · difficulty 3920 · constructive

Original problem by Mikhail Rubinchik, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A box whose six faces have six different colours was sawn by cuts
parallel to its faces, each going through the whole box. Each piece is
given in some unknown orientation, with its three extents and the
colours of its six faces, inner faces marked by a dot. Put every piece
back: name the faces of the piece that become its front and its bottom,
and give the coordinates of its front lower left corner in the box.

## Input

The box: its extents w, d and h (from front to back, from bottom to top
and from left to right, each from 1 to 1000) and six colours from
"ROYGBV" for the front, back, bottom, top, left and right faces. Then n
(1 ≤ n ≤ 1000) and the n pieces in the same format, with "." for faces
that were inside the box. A solution exists.

## Output

For every piece in input order, the letter of its face that becomes the
front and the letter of its face that becomes the bottom (F, B, D, U, L
or R for its own front, back, bottom, top, left and right), then its
front lower left corner. Any valid placement is accepted.

## Examples

### Example 1

Input:

```
2 2 2 ROYGBV
2
1 2 2 R.YGBV
2 2 1 YGVBO.
```

Output:

```
F D 0 0 0
R F 1 0 0
```

## Solution

Every cut goes through the whole box, so the pieces form a grid: the
cuts split each axis into sections, and every cell of the grid is one
piece. A piece touches a face of the box exactly when its cell is the
first or the last along the axis of that face.

The sections. Take the axis from left to right. The pieces with the
front colour and the bottom colour form the front lower edge along it,
one piece per section. In each of them the front and the bottom colour
mark two of its axes, and its extent along the third axis is a section
length. The piece also coloured left gives the first section and the
piece coloured right gives the last one (one piece may be both, when
there are no cuts). The middle sections may be put in any order, since
swapping two inner slices leaves the same set of pieces. The other two
axes work the same way.

The placement. Every cell now asks for a piece with given extents and
given colours: the box colour on the faces at the box surface, a dot
elsewhere. Write a piece in all its 24 turns and take the smallest
written form as its key; a cell gets the same key exactly when some
turn of the piece fits it. Group the pieces by key, give every cell any
piece of its group, then find the turn of that piece that fits the cell
exactly. The turns are generated from two quarter turns about crossing
axes, and a turn is named by the faces that land in front and below.
`O(24·n)` on average; C++ uses `std::map`: `O(24·n + n log n)`.

In the example the front lower edge holds only the first piece, so the
left-to-right axis has one section of length 2, and so has the vertical
axis. From front to back the pieces with the bottom and left colours
are both pieces, with extents 1 and 1, so the box is cut once in the
middle. The second piece fits the back cell after turning its right
face to the front and its front face down.

Pitfalls:

- several pieces may share a key, like unit cubes inside the box; any
  of them fits any such cell;
- a turn is a rotation, never a mirror image, so the 24 turns must come
  from rotations;
- an axis without cuts has a single section that touches both faces.

The placements pass a checker that turns every piece, confirms that
the pieces fill the box without overlaps and that the faces on the
surface carry the right colours, on random boxes of up to 1000 pieces.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1843_constructive.cpp](1843_constructive.cpp) | G++ 13.2 x64 | constructive | O(24 n + n log n) | AC | 0.015 s | 560 KB |
| [1843_constructive.go](1843_constructive.go) | Go 1.14 x64 | constructive | O(24 n) | AC | 0.046 s | 5864 KB |
| [1843_constructive.java](1843_constructive.java) | Java 1.8 | constructive | O(24 n) | AC | 0.171 s | 7512 KB |
| [1843_constructive.py](1843_constructive.py) | Python 3.12 x64 | constructive | O(24 n) | AC | 0.265 s | 1676 KB |
| [1843_constructive.rs](1843_constructive.rs) | Rust 1.75 x64 | constructive | O(24 n) | AC | 0.046 s | 652 KB |
