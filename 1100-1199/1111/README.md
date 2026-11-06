# 1111. Sorting squares by their distance to a point

[Timus 1111](https://acm.timus.ru/problem.aspx?space=1&num=1111) · difficulty 383 · geometry

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` filled squares (`1 ≤ n ≤ 50`), each given by two opposite
corners with integer coordinates in `(−9999, 9999)`; the squares may be
turned at any angle, and a square may shrink to a single point. The
distance from a point `P` to a square is the length of the shortest
segment from `P` to a point of the square, so it is 0 when `P` lies
inside. Print the square numbers sorted by distance, the smaller number
first on ties.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`n`, then `n` lines `x1 y1 x2 y2` with two opposite corners, then the
line `x y` of `P`.

## Output

The square numbers (1-based) in sorted order, separated by spaces.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2
0 0 1 1
0 3 1 4
0 0
```

Output:

```
1 2
```

## Solution

Look at each square from its centre `C`, with `D = (x2 − x1, y2 − y1)`
the diagonal. Its sides run along `D` turned by `±45°`, that is along
`D ± D⊥`, where `D⊥` is `D` turned by `90°`. With the doubled offset
`q = 2P − (x1 + x2, y1 + y2)`, all integer, the projections of `q` on the
two side directions are `s1 = |q · (D + D⊥)|` and `s2 = |q · (D − D⊥)|`,
and `P` is inside exactly when both are at most `h = |D|²`. Outside, the
excess `a = max(0, s1 − h)` and `b = max(0, s2 − h)` give the squared
distance `(a² + b²) / (8h)`, and a point square has `|q|² / 4`.

Every squared distance is thus an exact fraction of integers, and two of
them are compared by cross-multiplying, with the input index breaking
ties. Read `P` and compute every expression involving it with arbitrary-
precision integers; only the bounded corner coordinates and denominators
use fixed-width integers. There are `O(n log n)` comparisons. If `L` is
the maximum decimal length of a coordinate of `P` (at least 1), a
schoolbook-arithmetic upper bound is `O(n L² + n log n L)` time and
`O(n L)` working memory. The denominators have bounded size.

Pitfalls:

- ties are common, from symmetric squares and from `P` inside several of
  them, so the comparison must be exact: floating point can order two
  equal distances either way;
- the bounds on square corners do not bound `P`. Test `09` has two
  equal distances, but the square numerator is `2^64`: widening only
  the final comparison is too late. Even 128 bits cannot handle every
  allowed `P`, so parsing, projections, squares and comparisons must
  all support arbitrary precision;
- the given corners are opposite, not adjacent, and either diagonal in
  either direction describes the same square.

The answers were checked against a separate exact computation with
fractions: the four corners are built explicitly, containment is tested
by cross products, and the distance is the least distance to the four
sides as segments. Hundreds of random sets, many with ties, agreed.

## Optimized solutions

C++, Go and Rust preserve exact squared-distance fractions and sort by cross multiplication, breaking ties by input index. Comparison products reuse their backing buffers. C++ and Rust also parse the unrestricted query coordinates directly in groups of nine decimal digits, matching their base-10⁹ limbs. Go stores signed arbitrary-precision integers in 30-bit limbs, parses query coordinates directly from bytes and merges the sorted indices. Its arithmetic and comparison buffers are reused. Rust parses byte tokens, stores square coordinates and indices in fixed arrays and writes the result through one fixed byte buffer. Rust reads and writes through the C runtime.

The accepted Go 1.14 x64 run takes 0.031 s versus 0.015 s for the base and uses 800 KB versus 1288 KB.

The accepted base implementations [1111_geometry.java](1111_geometry.java), [1111_geometry.py](1111_geometry.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

- The simple C++ and Rust versions use their own signed limb arithmetic. The simple Go version uses `math/big.Int` and `sort.Slice` with an explicit index tie-break.
- The optimized Go version uses 30-bit limbs, reads coordinates directly from bytes and merges indices with reusable comparison products.
- Java uses `BigInteger`; Python uses its own integers with the decimal-input digit limit disabled. All versions compare exact squared-distance fractions and then input indices.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1111_geometry.cpp](1111_geometry.cpp) | G++ 13.2 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 444 KB | 11298020 |
| [1111_geometry.go](1111_geometry.go) | Go 1.14 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 1288 KB | 11298022 |
| [1111_geometry.java](1111_geometry.java) \* | Java 1.8 | geometry | O(n L² + n log n L) | AC | 0.156 s | 3956 KB | 11298023 |
| [1111_geometry.py](1111_geometry.py) \* | Python 3.12 x64 | geometry | O(n L² + n log n L) | AC | 0.078 s | 624 KB | 11298025 |
| [1111_geometry.rs](1111_geometry.rs) | Rust 1.75 x64 | geometry | O(n L² + n log n L) | AC | 0.031 s | 240 KB | 11298026 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1111_geometry_optimized.cpp](1111_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 208 KB | 11310910 |
| [1111_geometry_optimized.go](1111_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n L² + n log n L) | AC | 0.031 s | 800 KB | 11311126 |
| [1111_geometry_optimized.rs](1111_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 80 KB | 11311247 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
